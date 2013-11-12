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

        for i, settings in enumerate(SETTINGS):
            # create settings forms
            view_name = "%s-%s" % (settings.module, settings.name)
            View = type(view_name, (SettingsFormView,), {
                'title': settings.title,
                'description': settings.description,
                'name': settings.name,
                'schema_factory': settings.schema_factory,
                'settings': settings,
                'success_message': settings.success_message,
                'active': i == 0,
            })
            view = View(self.context, self.request)
            dikt = view()
            dikt['view'] = view
            settings_form_views.append(dikt)
            # disable active on the first form if there is another active one
            if view.active and i != 0:
                settings_form_views[0]['view'].active = False
        return {'settings_form_views': settings_form_views, }


def includeme(config):
    config.scan(__name__)
