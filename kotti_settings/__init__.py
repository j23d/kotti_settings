from pyramid.i18n import TranslationStringFactory
from kotti.util import ViewLink
from kotti.views.site_setup import CONTROL_PANEL_LINKS

_ = TranslationStringFactory('kotti_settings')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_settings kotti_settings.views'

    settings = ViewLink('settings', title=_(u'Settings'))
    CONTROL_PANEL_LINKS.append(settings)


def includeme(config):
    config.add_translation_dirs('kotti_settings:locale')
