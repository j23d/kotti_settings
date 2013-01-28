from kotti.resources import get_root

from kotti_settings.views import SettingsView
from kotti_settings import add_settings


TestSettings = {
    'name': 'test_settings',
    'title': "Testsettings",
    'success_message': u"Successfully saved test settings.",
    'settings': [
        {'type': 'String',
         'name': 'testsetting_1',
         'title': 'Test 1',
         'description': 'a test setting',
         'default': '', },
        {'type': 'Integer',
         'name': 'testsetting_2',
         'title': 'Test 2',
         'description': 'again a test setting',
         'default': 23, }
    ]
}


def test_views(db_session, populate_kotti_settings, dummy_request):
    add_settings(TestSettings)
    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    form = rendered['settings_form_views'][0]
    assert form['title'] == "Testsettings"
    assert form['form'].startswith('<form')
    assert 'name="kotti_settings-testsetting_1"' in form['form']
