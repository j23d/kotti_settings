# -*- coding: utf-8 -*-
import sys
import colander
from deform import Button
from types import ClassType
from pyramid_deform import CSRFSchema
from pyramid_deform import FormView
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti import DBSession
from kotti.views.util import is_root

from kotti_settings.resources import Settings
from kotti_settings import SETTINGS
from kotti_settings import _


class SettingsSchema(colander.MappingSchema):
    pass


class SettingsFormView(FormView):
    """The form template class for one setting tab.
    """
    name = 'settings'
    title = u"Settings"
    buttons = (
        Button('save', _(u'Save')),
        Button('cancel', _(u'Cancel')))
    success_message = _(u"Your changes have been saved.")
    success_url = None
    schema_factory = SettingsSchema
    use_csrf_token = True

    def tab_title(self):
        return self.title

    def __init__(self, context, request, **kwargs):
        self.context = context
        self.request = request
        self.__dict__.update(kwargs)

    def __call__(self):
        # get the settings - this should be done with some failure proof util method
        [settings] = DBSession.query(Settings).all()
        # build the schema and append csrf token if needed
        if self.schema_factory is not None:
            self.schema = self.schema_factory()
        if self.use_csrf_token and 'csrf_token' not in self.schema:
            self.schema.children.append(CSRFSchema()['csrf_token'])
        # enhance the schema with the given definitions
        for setting_obj in self.settings:
            node = colander.SchemaNode(
                self.colander_type(setting_obj.type)(),
                name=setting_obj.field_name,
                title=setting_obj.title,
                description=setting_obj.description,
                missing=setting_obj.default  # did this actually work?
            )
            self.schema.children.append(node)
        result = super(SettingsFormView, self).__call__()
        return result

    def before(self, form):
        [settings] = DBSession.query(Settings).all()
        for key in form.cstruct:
            if key in settings.data:
                form.cstruct[key] = settings.data[key]

    def colander_type(self, name):
        # http://docs.pylonsproject.org/projects/colander/en/latest/api.html#types
        try:
            klass = getattr(sys.modules['colander'], name)
        except AttributeError:
            raise NameError("%s is not an sqlalchemy data type." % name)
        if isinstance(klass, (ClassType, type)):
            return klass
        raise TypeError("%s is not a class." % name)

    def save_success(self, appstruct):
        [settings] = DBSession.query(Settings).all()
        # https://github.com/Kotti/Kotti/commit/ca7db42711c9e29cb797dad95de0898eb598b72e
        appstruct.pop('csrf_token', None)
        for item in appstruct:
            if appstruct[item]:
                settings.data[item] = appstruct[item]
        # new_settings = settings.copy(data)
        # DBSession.add(new_settings)
        DBSession.add(settings)  # needed?
        DBSession.flush()  # needed?

    def cancel_success(self, appstruct):
        self.request.session.flash(_(u'No changes made.'), 'info')
        location = "%s/@@settings" % self.request.application_url
        raise HTTPFound(location=location)
    cancel_failure = cancel_success


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
                'settings': settings.settings_objs,
                'success_message': settings.success_message,
            })
            view = View(self.context, self.request)
            dikt = view()
            dikt['title'] = view.tab_title()  # aehm - no
            settings_form_views.append(dikt)
        return {'settings_form_views': settings_form_views, }
