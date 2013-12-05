from pyramid.interfaces import ITranslationDirectories

from kotti_settings import includeme
from kotti_settings import kotti_configure


def test_kotti_configure():

    settings = {
        'pyramid.includes': '',
        'kotti.populators': '',
    }

    kotti_configure(settings)

    assert settings['pyramid.includes'] == ' kotti_settings kotti_settings.views'


def test_includeme(config):

    includeme(config)

    utils = config.registry.__dict__['_utility_registrations']
    k = (ITranslationDirectories, u'')

    # test if the translation dir is registered
    assert k in utils
    assert utils[k][0][0].find('kotti_settings/locale') > 0
