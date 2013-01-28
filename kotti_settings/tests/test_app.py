from kotti import DBSession
from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_settings.resources import Settings


def test_settings(db_session, populate_kotti_settings):
    from kotti_settings.util import get_settings
    assert get_settings() == {}

    data = {'foo': u'bar', 'bar': u'foo'}
    [settings] = DBSession.query(Settings).all()
    settings.data.update(data)
    DBSession.add(settings)
    assert get_settings() == {'foo': u'bar', 'bar': u'foo'}




# def test_persistent_settings(self):
#     from kotti import get_settings
#     from kotti import get_version
#     from kotti import DBSession
#     from kotti.resources import Settings
#     session = DBSession()
#     [settings] = session.query(Settings).all()
#     self.assertEqual(settings.data, {'kotti.db_version': get_version()})
#     self.assertEqual(get_settings()['kotti.db_version'], get_version())
#     settings.data['foo.bar'] = u'baz'
#     self.assertEqual(get_settings()['foo.bar'], u'baz')


# def test_persistent_settings_add_new(self):
#     from kotti import DBSession
#     from kotti import get_settings
#     from kotti.resources import Settings


#     self.assertEqual(get_settings()['foo.bar'], u'spam')
#     self.assertEqual(get_settings()['kotti.db_version'], u'next')
