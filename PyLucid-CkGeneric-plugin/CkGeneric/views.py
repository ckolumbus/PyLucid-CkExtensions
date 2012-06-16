# coding: utf-8

"""
    CkGeneric plugin
    ~~~~~~~~~~~~~~~~
    
    Simple rendering templates with some variables.

    :copyleft: 2012 by the CKolumbus
    :license: GNU GPL v3 or above, see LICENSE for more details
"""

from django.conf import settings
from django.contrib import messages

from pylucid_project.apps.pylucid.decorators import render_to

import os, re


@render_to()
def filelist(request, dir, prefix, expr=".*", template_name="CkGeneric/filelist.html", **kwargs): 
    re_expr =  re.compile(expr)
    f = [x for x in os.listdir(dir) if re_expr.match(x) and os.path.isfile(os.path.join(dir,x)) ]
    f.sort()

    context = {
        "files": f,
	"dir" : dir,
	"expr" : expr,
	"prefix" : prefix,
        "template_name":template_name,
    }
    context.update(kwargs)
    return context

