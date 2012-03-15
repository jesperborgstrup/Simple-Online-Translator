from user import User
import os.path
import sys

users = [ User( username="jesper", password="eskimo", name="Jesper Borgstrup", languages=["es", "da"], admin=True ),
          User( username="jesperbonde", password="prutsavl", name="Jesper Bonde Laursen", languages=["de"], admin=False ),
          User( username="kasperorn", password="hulken", name="Kasper Orn Andersen", languages=["is"], admin=False ),
          User( username="frantxu", password="gomez", name="Francisco Gomez-Fonseca", languages=["es", "fr"], admin=False) ]

all_languages = ( ( 'da', 'Danish'  ),
                  ( 'es', 'Spanish' ),
                  ( 'fr', 'French' ),
                  ( 'en', 'English' ),
                  ( 'de', 'German' ),
                  ( 'is', 'Icelandic' ) )

root_dir = os.path.abspath( os.path.dirname( __file__ ) )
sys.path.insert(0, root_dir)

template_dir = os.path.join( root_dir, "templates" )

