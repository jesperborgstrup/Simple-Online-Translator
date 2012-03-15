from user import User

# Rename this file to settings.py to use these sample settings

users = [ User( username="admin", password="password", name="Administrator", languages=["es"], admin=True ),
          User( username="user", password="user", name="Regular user", languages=["fr"], admin=False) ]

all_languages = ( ( 'es', 'Spanish' ),
                  ( 'fr', 'French'),
                  ( 'en', 'English' ), )

