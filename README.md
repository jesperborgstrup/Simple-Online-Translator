Run directly with ```main.py```
or
configure apache with ```mod_wsgi```:

<pre>
WSGIScriptAlias /translate /path/to/SOT/main.py/
Alias /translate/static /path/to/SOT/static
</pre>

Rename ```settings.sample.py``` to ```settings.py``` for sample settings.

Rename ```data/values/strings.sample.xml``` to ```data/values/strings.xml``` for a sample base translation file.
