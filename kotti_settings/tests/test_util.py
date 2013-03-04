import pytest


def test_add_settings_with_missing_attributes(db_session):
    from kotti_settings.util import add_settings

    TestSettings = {
        'description': "Some settings in a dict.",
        'name': 'a name',
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'description': 'a test setting',
             'default': 'my first string', },
        ]
    }
    with pytest.raises(ValueError) as excinfo:
        add_settings(TestSettings)
    assert str(excinfo.value) == 'A setting has to have a name.'

    TestSettings['settings'][0]['name'] = 'testsetting'
    with pytest.raises(ValueError) as excinfo:
        add_settings(TestSettings)
    assert str(excinfo.value) == 'A setting has to have a title.'

    TestSettings['settings'][0]['title'] = 'test title'
    assert add_settings(TestSettings) == None
