from pyramid.i18n import TranslationStringFactory
from kotti.util import ViewLink
from kotti.views.site_setup import CONTROL_PANEL_LINKS

_ = TranslationStringFactory('kotti_settings')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_settings'

    settings = ViewLink('settings', title=_(u'Settings'))
    CONTROL_PANEL_LINKS.append(settings)


def includeme(config):

    from kotti_settings.testing import TestSettingsDict
    from kotti_settings.testing import TestSettingsSchema
    from kotti_settings.testing import TestSettingsSchemaBrowser
    # add_settings(TestSettingsSchema)
    # add_settings(TestSettingsDict)
    # add_settings(TestSettingsSchemaBrowser)

    config.add_translation_dirs('kotti_settings:locale')
    config.scan(__name__)
