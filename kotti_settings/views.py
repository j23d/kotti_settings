# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti.views.util import is_root

from kotti_settings.config import SETTINGS
from kotti_settings.form import SettingsFormView


@view_defaults(permission='manage')
class SettingsView(object):
    """View(s) for settings"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='settings',
                 custom_predicates=(is_root, ),
                 permission='manage',
                 renderer='kotti_settings:templates/settings.pt')
    def view(self):
        settings_form_views = []

        for settings in SETTINGS:
            # create settings forms
            view_name = "%s-%s" % (settings.module, settings.name)
            View = type(view_name, (SettingsFormView,), {
                'title': settings.title,
                'description': settings.description,
                'name': settings.name,
                'schema_factory': settings.schema_factory,
                'settings': settings,
                'success_message': settings.success_message,
            })
            view = View(self.context, self.request)
            dikt = view()
            dikt['view'] = view
            settings_form_views.append(dikt)
        return {'settings_form_views': settings_form_views, }
