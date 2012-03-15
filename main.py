import web
import sys
import os.path
"""
We need to insert the path into the syspath here,
because it isn't added automatically when running through mod_wsgi.
If it wasn't here, local imports would fail
"""
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

urls = (
      '/?', 'handler.Root',
      '/edit/?', 'handler.Root',
      r'/edit/(\w\w)/?', 'handler.Edit',
      r'/edit/(\w\w)/(\w\w)/?', 'handler.Edit',
      r'/edit/(\w\w)/(\w\w)/(\w\w)/?', 'handler.Edit',
      r'/edit/(\w\w)/(\w\w)/(\w\w)/(\w\w)/?', 'handler.Edit',
      r'/edit/(\w\w)/(\w\w)/(\w\w)/(\w\w)/(\w\w)/?', 'handler.Edit',
      r'/edit/(\w\w)/(\w\w)/(\w\w)/(\w\w)/(\w\w)/(\w\w)/?', 'handler.Edit',
      r'/login', 'handler.Login',
      r'/logout', 'handler.Logout',
      )

app = web.application(urls, globals())
application = app.wsgifunc()

root_dir = os.path.abspath( os.path.dirname( __file__ ) )
template_dir = os.path.join( root_dir, "templates" )

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore( os.path.join( root_dir, 'sessions' ) ), {})
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    app.run()
