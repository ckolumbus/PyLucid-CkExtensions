PyLucid-CkExtensions
====================

My extensions for the PyLucid CMS: plugins, tags, ..

PyLucid-ProtectedGallery-plugin
-------------------------------

This is a gallery component copied from the original gallery plugin of PyLucid
but it can serve data/images from outside the media root tree. Access is regulated
through the plugin access rights mechanism. With this you can host non-public
galleries. 

### Todo

 * no testing is available yet


PyLucid-CkGeneric-plugin
------------------------

Provides additional `generic` tags that I use.


### `filelist`

  `filelist(request, dir, prefix, expr=".*", template_name="generic/filelist.html", **kwargs)`

provides a file list from the local directory `dir` with all files matching `expr`. The returned
file list is prefixed with `prefix` which should containt the url-prefix under which the files
are reachable via the webserver.


