import codecs
import os.path
import xml.dom.minidom

class Translator:
    languages = {}
    language_codes = []
    all_languages = []
    default_langcode = "en"
    
    def __init__(self, data_dir, all_languages):
#        self.languages[''] = ( 'Default', TranslatorLanguage( '', os.path.join( data_dir, "values", "strings.xml" ) ) )
#        self.language_codes.append( ('', 'Default' ) )
        self.all_languages = all_languages
        
        for lang in all_languages:
            langcode = lang[0]
            langname = lang[1]
            filename = os.path.join( data_dir, "values-%s" % langcode, "strings.xml" )
            if langcode == self.default_langcode:
                filename = os.path.join( data_dir, "values", "strings.xml" )
            
            self.languages[ langcode ] = ( langname, TranslatorLanguage( langcode, filename ) )
            self.language_codes.append( ( langcode, langname ) )
            
    def get_string(self, langcode, name):
        lang = self.languages[ langcode ][1]
        if not lang.strings.has_key( name ):
            return ""
            #lang = self.languages[''][1]

        return lang.strings[ name ]
    
    def get_default_string(self, name):
        return self.get_string( self.default_langcode, name )
    
    def set_string(self, langcode, name, value):
        self.languages[ langcode ][1].set_string( name, value )
        
    def get_all_strings(self):
        return sorted( self.languages[ self.default_langcode ][1].strings.keys() )
    
    def get_language_name(self, langcode):
        if ( self.languages.has_key( langcode ) ):
            return self.languages[ langcode ][0]
        else:
            return "Unknown (%s)" % (langcode,)
            
      
      
class TranslatorLanguage:  
    
    def __init__(self, language, filename):
        self.language = language
        self.filename = filename
        
        self.strings = {}
        self.plurals = {}
        self.elements = {}
#        print self.strings
        
        if not os.path.exists( filename ):
            if not os.path.exists( os.path.dirname( filename ) ):
                os.mkdir( os.path.dirname( filename ) )
                
            f = codecs.open( filename, 'w', 'utf8' )
            f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n</resources>")
            f.close()
            
            
        f = codecs.open( filename, 'r', 'utf8' )
        data = f.read()
        f.close()
        
        self.doc = xml.dom.minidom.parseString( data.encode( 'utf-8' ) )
        self.root = self.doc.getElementsByTagName( "resources" )[0]
        
        for child in self.root.childNodes:
            if child.nodeName == "string":
                element = child
                name = element.attributes[ 'name' ].value
                self.elements[ name ] = element
                if element.hasChildNodes():
                    self.strings[ name ] = self.read_in_string( element.firstChild.wholeText )
                    
                    if len ( element.childNodes ) == 3 and self.is_cdata_element( element.childNodes[1] ):
                        element.removeChild( element.firstChild )
                        element.removeChild( element.lastChild )

                else:
                    element.appendChild( self.doc.createTextNode( "" ) )
                
                
    def read_in_string(self, string):
        return string.replace( r"\n", "\n" ).replace( r"\'" , "'" )
    
    def set_string(self, name, value):
        self.strings[ name ] = value
        if self.elements.has_key( name ):
            element = self.elements[ name ]
            if self.is_cdata_element( element.firstChild ):
                element.removeChild( element.firstChild )
                element.appendChild( self.doc.createCDATASection( self.write_out_string( value ) ) )
            else:
                element.removeChild( element.firstChild )
                element.appendChild( self.doc.createTextNode( self.write_out_string( value ) ) )
        else:
            element = self.doc.createElement("string")
            element.setAttribute("name", name)
            element.appendChild( self.doc.createTextNode( self.write_out_string( value ) ) )
            self.root.appendChild( element )
            self.elements[ name ] = element
                
    def is_cdata_element(self, element):
        return element.__class__.__name__.find( 'CDATA' ) != -1
    
    def save(self):
        f = codecs.open( self.filename, 'w', 'utf8' )
        f.write( self.doc.toxml() )
        f.close();

    def write_out_string(self, string):
        return string.replace( "'", r"\'" ).replace( "\n", r"\n" )
    
    def count_words(self):
        count = 0
        for string in self.strings.values():
            count += len( string.split(None) )
        return count
        
        
        
if __name__ == '__main__':
    from settings import all_languages
    trans = Translator( "data", all_languages )
    for lang in trans.languages.values():
        print "Count (%s): %d" % ( lang[0], lang[1].count_words() ) 
        
