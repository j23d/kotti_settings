

def test_settings(db_session):
    from kotti.resources import get_root
    from kotti_settings.util import get_settings
    assert get_settings() == {}

    data = {'foo': u'bar', 'bar': u'foo'}
    root = get_root()
    root.annotations['kotti_settings'] = data
    assert get_settings() == {'foo': u'bar', 'bar': u'foo'}
