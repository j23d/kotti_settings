from pyramid.i18n import TranslationStringFactory
from kotti.util import ViewLink
from kotti.views.site_setup import CONTROL_PANEL_LINKS

from kotti_settings.util import add_settings

_ = TranslationStringFactory('kotti_settings')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_settings'
    settings['kotti.populators'] += ' kotti_settings.populate.populate'

    settings = ViewLink('settings', title=_(u'Settings'))
    CONTROL_PANEL_LINKS.append(settings)

    # TestSettings1 = {
    #     'name': 'test_settings',
    #     'title': "Testsettings",
    #     'success_message': u"Successfully saved test settings.",
    #     'settings': [
    #         {'type': 'String',
    #          'name': 'testsetting_1',
    #          'title': 'Test 1',
    #          'description': 'a test setting',
    #          'default': '', },
    #         {'type': 'Integer',
    #          'name': 'testsetting_2',
    #          'title': 'Test 2',
    #          'description': 'again a test setting',
    #          'default': 23, }
    #     ]
    # }
    # add_settings(TestSettings1)
    # TestSettings2 = {
    #     'name': 'test_settings',
    #     'title': "Testsettings2",
    #     'success_message': u"Successfully saved test settings.",
    #     'settings': [
    #         {'type': 'String',
    #          'name': 'testsetting_3',
    #          'title': 'Test 1',
    #          'description': 'a test setting',
    #          'default': '', },
    #         {'type': 'Integer',
    #          'name': 'testsetting_4',
    #          'title': 'Test 2',
    #          'description': 'again a test setting',
    #          'default': 23, }
    #     ]
    # }
    # add_settings(TestSettings2)


def includeme(config):

    config.add_translation_dirs('kotti_settings:locale')
    config.scan(__name__)
