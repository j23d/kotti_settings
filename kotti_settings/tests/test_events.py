from pyramid.events import subscriber

from kotti_settings.events import SettingsAfterSave
from kotti_settings.views import SettingsFormView


VALUE = 'foo'


@subscriber(SettingsAfterSave)
def change_after(event):
    global VALUE
    VALUE = 'bar'


def test_events_subscriber(db_session, settings_events, root, dummy_request):
    global VALUE
    from kotti_settings.util import add_settings
    test_settings = {
        'name': 'test-event-setting',
        'title': "Some settings.",
        'settings': [
            {'type': 'String',
             'name': 'evt_test_setting',
             'title': 'evt test setting', },
        ]
    }
    add_settings(test_settings)

    view = SettingsFormView(root, dummy_request)
    view.save_success({})
    assert VALUE == 'bar'
