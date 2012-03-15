Run directly with main.py
or
configure apache with mod_wsgi:

WSGIScriptAlias /translate /path/to/SOT/main.py/
Alias /translate/static /path/to/SOT/static

Rename settings.sample.py to settings.py for sample settings