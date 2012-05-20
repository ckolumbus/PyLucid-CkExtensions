# coding: utf-8

"""
    ProtectedGallery PyLucid Plugin - admin 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Register model in django admin interface.

    Last commit info:
    ~~~~~~~~~~~~~~~~~
    $LastChangedDate$
    $Rev$
    $Author$

    :copyleft: 2009 by the PyLucid team, see AUTHORS for more details.
               Adapted by CKolumbus for protected file serving
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from django.http import HttpResponseRedirect
from django.contrib import admin
from django import forms

from pylucid_project.apps.pylucid.models import PageTree, PluginPage
from pylucid_project.apps.pylucid.base_admin import BaseAdmin, RedirectToPageAdmin

from ProtectedGallery.models import ProtectedGalleryModel



class ProtectedGalleryAdminForm(forms.ModelForm):
    """
    Filter pagetree selection.
    Add only pagetree items witch are a gallery plugin page.
    """
    class Meta:
        model = ProtectedGalleryModel

    def __init__(self, *args, **kwargs):
        super(ProtectedGalleryAdminForm, self).__init__(*args, **kwargs)

        plugin_pages = PluginPage.objects.filter(app_label="pylucid_project.external_plugins.ProtectedGallery")
        # TODO: Filter pagetree's witch has already a Gallery PluginPage
        choices = [
            (page.pagetree.id, page.pagetree.get_absolute_url())
            for page in plugin_pages
        ]
        self.fields["pagetree"].choices = choices


class ProtectedGalleryModelAdmin(RedirectToPageAdmin, BaseAdmin):
    form = ProtectedGalleryAdminForm
    list_display = (
        "view_on_site_link", "path", "template",
        "lastupdatetime", "lastupdateby"
    )
    list_display_links = ("path",)
    list_filter = ("template", "createby", "lastupdateby",)
    date_hierarchy = 'lastupdatetime'
    #search_fields = ("path", "template",)

admin.site.register(ProtectedGalleryModel, ProtectedGalleryModelAdmin)
