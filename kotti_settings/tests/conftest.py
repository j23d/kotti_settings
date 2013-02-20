# See http://kotti.readthedocs.org/en/latest/developing/testing.html
from pytest import fixture
from kotti.tests import settings

pytest_plugins = "kotti"


@fixture
def populate_kotti_settings():
    from transaction import commit
    from kotti import _resolve_dotted
    kotti_settings = settings()
    kotti_settings['kotti.populators'] = 'kotti_settings.populate.populate'
    _resolve_dotted(kotti_settings)
    for populate in kotti_settings['kotti.populators']:
        populate()
    commit()
