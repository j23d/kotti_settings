# -*- coding: utf-8 -*-
import sys
import colander
from deform import Button
from types import ClassType
from pyramid_deform import CSRFSchema
from pyramid_deform import FormView
from pyramid.httpexceptions import HTTPFound

from kotti_settings.util import get_settings
from kotti_settings import _


class SettingsSchema(colander.MappingSchema):
    pass


class SettingsFormView(FormView):
    """The form template class for one setting tab.
    """
    name = 'settings'
    title = _(u"Settings")
    buttons = (
        Button('save', _(u'Save')),
        Button('cancel', _(u'Cancel')))
    success_message = _(u"Your changes have been saved.")
    # success_url = None
    settings = None
    schema_factory = None
    use_csrf_token = True

    def tab_title(self):
        return self.title

    def __init__(self, context, request, **kwargs):
        self.context = context
        self.request = request
        self.__dict__.update(kwargs)

    def __call__(self):
        """get the settings - this should be done with some
           failure proof util method
        """
        # build the schema if it not exist
        if self.schema is None:
            if self.schema_factory is None:
                self.schema_factory = SettingsSchema
            self.schema = self.schema_factory()
        # append csrf token if needed
        if self.use_csrf_token and 'csrf_token' not in self.schema:
            self.schema.children.append(CSRFSchema()['csrf_token'])
        # enhance the schema with the given definitions
        for setting_obj in self.settings.settings_objs:
            node = colander.SchemaNode(
                self.colander_type(setting_obj.type)(),
                name=setting_obj.field_name,
                title=setting_obj.title,
                description=setting_obj.description,
                #missing=setting_obj.default,
                default=setting_obj.default
            )
            self.schema.children.append(node)
        # the names of the children should begin with the module name
        for child in self.schema.children:
            if child.name == 'csrf_token':
                continue
            if not child.name.startswith(self.settings.module):
                child.name = "%s-%s" % (self.settings.module, child.name)
        result = super(SettingsFormView, self).__call__()
        return result

    def before(self, form):
        settings = get_settings()
        for key in form.cstruct:
            if key in settings:
                form.cstruct[key] = settings[key]

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
        settings = get_settings()
        # https://github.com/Kotti/Kotti/commit/ca7db42711c9e29cb797dad95de0898eb598b72e
        appstruct.pop('csrf_token', None)
        for item in appstruct:
            if appstruct[item]:
                settings[item] = appstruct[item]

    def cancel_success(self, appstruct):
        self.request.session.flash(_(u'No changes made.'), 'info')
        location = "%s/@@settings" % self.request.application_url
        raise HTTPFound(location=location)

    cancel_failure = cancel_success
