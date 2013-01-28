import inspect

from pyramid.i18n import TranslationStringFactory
from kotti.util import ViewLink
from kotti.views.site_setup import CONTROL_PANEL_LINKS
from kotti_settings.settings import ModuleSettings
from kotti_settings.settings import SettingObj

_ = TranslationStringFactory('kotti_settings')


SETTINGS = []


def add_settings(module_settings):
    """Get a dictionary and translate this into an object structure.
    """
    module_settings = ModuleSettings(**module_settings)
    if module_settings.module is None:
        # If the module name is omitted get it.
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        module_settings.module = module.__name__
    for setting in module_settings.settings:
        setting_obj = SettingObj(**setting)
        # name and title of a setting is required
        if setting_obj.name is None:
            raise ValueError('A setting has to have a name.')
        if setting_obj.title is None:
            raise ValueError('A setting has to have a title.')
        setting_obj.module = module_settings.module
        module_settings.settings_objs.append(setting_obj)
    SETTINGS.append(module_settings)


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_settings'
    settings['kotti.populators'] += ' kotti_settings.populate.populate'

    settings = ViewLink('settings', title=_(u'Settings'))
    CONTROL_PANEL_LINKS.append(settings)

    TestSettings1 = {
        'name': 'test_settings',
        'title': "Testsettings",
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'name': 'testsetting_1',
             'title': 'Test 1',
             'description': 'a test setting',
             'default': '', },
            {'type': 'Integer',
             'name': 'testsetting_2',
             'title': 'Test 2',
             'description': 'again a test setting',
             'default': 23, }
        ]
    }
    add_settings(TestSettings1)
    TestSettings2 = {
        'name': 'test_settings',
        'title': "Testsettings2",
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'name': 'testsetting_3',
             'title': 'Test 1',
             'description': 'a test setting',
             'default': '', },
            {'type': 'Integer',
             'name': 'testsetting_4',
             'title': 'Test 2',
             'description': 'again a test setting',
             'default': 23, }
        ]
    }
    add_settings(TestSettings2)


def includeme(config):

    config.add_translation_dirs('kotti_settings:locale')
    config.scan(__name__)
