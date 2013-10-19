# -*- coding: utf-8 -*-
import sys
import colander
import deform
from types import ClassType
from pyramid.decorator import reify
from pyramid_deform import CSRFSchema
from pyramid_deform import FormView
from pyramid.httpexceptions import HTTPFound

from kotti_settings.events import SettingsAfterSave
from kotti_settings.events import SettingsBeforeSave
from kotti_settings.util import get_settings
from kotti_settings import _

import itertools
counter = itertools.count()


class SettingsSchema(colander.MappingSchema):
    """An empty schema to have a named one if needed.
    """
    pass


class SettingsFormView(FormView):
    """The form template class for one setting tab.
    """
    form_class = deform.form.Form
    name = 'settings'
    title = _(u"Settings")
    description = u""
    success_message = _(u"Your changes have been saved.")
    success_url = None
    settings = None
    schema_factory = None
    use_csrf_token = True
    use_ajax = True
    active = False
    form_options = {'counter': counter}

    def __init__(self, context, request, **kwargs):
        self.context = context
        self.request = request
        self.__dict__.update(kwargs)

    def __call__(self):
        """Build up the schema and return the form view.
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
        # Build up the buttons dynamically, so we can check what setting form
        # was saved.
        save = 'save_' + self.form_id
        self.buttons = (
            deform.Button(save, _(u'Save')),
            deform.Button('cancel', _(u'Cancel')))
        setattr(self, save + '_success', self.save_success)
        return super(SettingsFormView, self).__call__()

    @reify
    def form_id(self):
        form_id = "{0}-{1}".format(self.settings.module, self.name)
        return form_id

    def before(self, form):
        settings = get_settings()
        for key in form.cstruct:
            if key in settings:
                # Convert boolean to 'true' or 'false' to meet the
                # requirements of deform's checkbox widget.
                if isinstance(settings[key], bool):
                    value = settings[key] and 'true' or 'false'
                else:
                    value = settings[key]
                form.cstruct[key] = value
        form.formid = self.form_id

    def colander_type(self, name):
        # http://docs.pylonsproject.org/projects/colander/en/latest/api.html#types
        try:
            klass = getattr(sys.modules['colander'], name)
        except AttributeError:
            raise NameError("%s is not an sqlalchemy data type." % name)
        if isinstance(klass, (ClassType, type)):
            return klass
        raise TypeError("%s is not a class." % name)  # pragma: no cover

    def save_success(self, appstruct):
        from kotti_settings.util import set_setting
        formid = self.request.POST.get('__formid__', None)
        self.active = False
        if formid is not None and formid == self.form_id:
            self.active = True
            appstruct.pop('csrf_token', None)
            module = None
            if appstruct:
                key = appstruct.keys()[0]
                module = key[:key.find('-')]
            self.request.registry.notify(SettingsBeforeSave(module))
            for item in appstruct:
                if appstruct[item] is not None:
                    set_setting(item, appstruct[item])
            ses = self.request.session
            if not '_f_success' in ses or\
                not self.success_message in ses['_f_success']:
                    self.request.session.flash(self.success_message, 'success')
            self.request.registry.notify(SettingsAfterSave(module))

    def cancel_success(self, appstruct):
        self.request.session.flash(_(u'No changes made.'), 'info')
        location = "%s@@settings" % self.request.resource_url(self.context)
        raise HTTPFound(location=location)
