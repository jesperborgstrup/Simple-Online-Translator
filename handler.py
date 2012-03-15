import web
import os.path
import auth
from translator import Translator
import settings


template_globals = { 'web': web }

def get_template( name, *args, **kwargs ):
    return web.template.frender( os.path.join( settings.template_dir, '%s.html' % name ), globals=template_globals )( *args, **kwargs )

_render = web.template.frender( os.path.join( settings.template_dir, 'base.html' ), globals=template_globals )

def render( *args, **kwargs ):
    return _render( auth, *args, **kwargs )

trans = Translator( os.path.join( settings.root_dir, 'data' ), settings.all_languages )



# if you are going to use FileHandler
#web.config.session_parameters.handler = 'file'
# set the file prefix
#web.config.handler_parameters.file_prefix = 'sess'
# and directory
#web.config.handler_parameters.file_dir = os.path.join( root_dir, 'sessions' )

class Root:
    def GET(self):
        if not auth.logged_in():
            return web.seeother( '/login' )
        return web.seeother('/edit/%s/en/' % auth.logged_in_user().languages[0] )
        #return render( get_template( "translate", trans, auth.logged_in_user() ) )
    
class Edit:
    def authorized(self, langcode):
        return langcode in auth.logged_in_user().languages
    
    def GET(self, langcode=None, *compare_languages):
        if not auth.logged_in():
            return web.seeother( '/login' )
        
        if not self.authorized(langcode):
            return web.seeother('/edit/')
        
        return render( get_template( "edit", trans, langcode, compare_languages, settings.all_languages, auth.logged_in_user() ) )
    
    def POST(self, *args):
        i = web.input( "langcode" )
        if not self.authorized(i.langcode):
            return web.seeother('/edit/')
        
        for (k,v) in i.items():
            if k == "langcode":
                continue
             
            trans.set_string(i.langcode, k, v.strip() )
        trans.languages[i.langcode][1].save()
            
        return self.GET( *args )

class Login:
    def GET(self, error=None):
        if auth.logged_in():
            return render( "Logged in" )
        else:
            return render( get_template( "login", error ) )
    
    def POST(self):
        i = web.input( "username", "password" )
        return self.GET( auth.session )
        if auth.authenticate( i.username, i.password ):
            return web.seeother( '/' )
        
        return self.GET( "Invalid login" )

class Logout:
    def GET(self):
        auth.logout()
        return web.seeother( '/' )

