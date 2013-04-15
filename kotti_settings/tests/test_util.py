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


def test_get_setting(db_session, root):
    from kotti_settings.util import add_settings
    from kotti_settings.util import get_setting
    test_settings = {
        'name': 'test-get-setting',
        'title': "Some test settings.",
        'settings': [
            {'type': 'String',
             'name': 'first_test_setting',
             'title': 'first test setting',
             'default': 'first test string', },
            {'type': 'Integer',
             'name': 'second_test_setting',
             'title': 'second test setting',
             'default': 5, },
        ]
    }
    add_settings(test_settings)

    first = get_setting('first_test_setting')
    assert first == 'first test string'
    second = get_setting('kotti_settings-second_test_setting')
    assert second == 5


def test_get_setting_not_found(db_session, root):
    from kotti_settings.util import get_setting

    setting = get_setting('not_exiting_setting')
    assert setting == None
    setting = get_setting('not_exiting_setting', 'default')
    assert setting == 'default'


def test_remove_widget_from_slot(config, db_session, events,
                                 dummy_request, root):
    from pyramid.response import Response
    from kotti.views.slots import assign_slot
    from kotti.views.util import TemplateAPI
    from kotti_settings.util import remove_from_slots

    def a_widget(request):
        return Response(u"The widget speaks")
    config.add_view(a_widget, name='a-widget')
    assign_slot('a-widget', 'right')

    api = TemplateAPI(root, dummy_request)
    assert api.slots.right == [u"The widget speaks"]

    remove_from_slots('a-widget')
    api = TemplateAPI(root, dummy_request)
    assert api.slots.right == []
