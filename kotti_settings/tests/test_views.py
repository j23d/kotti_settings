from kotti.resources import get_root

from kotti_settings.views import SettingsView
from kotti_settings.util import add_settings

from kotti_settings.testing import get_form
from kotti_settings.testing import TestSettingsDict
from kotti_settings.testing import TestSettingsSchema


def test_settingtab_with_dict(db_session, dummy_request):
    add_settings(TestSettingsDict)

    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    form = get_form(rendered['settings_form_views'],
                    name='test_settings_dict')
    assert form['title'] == "Testsettings Dict"
    assert form['form'].startswith('<form')
    assert 'name="test_views-testsetting_1"'\
        in form['form']
    assert 'value="my first string"' in form['form']
    assert 'name="test_views-testsetting_2"'\
        in form['form']
    assert 'value="23"' in form['form']


def test_settingtab_with_schema(db_session, dummy_request):
    add_settings(TestSettingsSchema)
    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    form = get_form(rendered['settings_form_views'],
                    name='test_settings_schema')
    assert form['title'] == "Testsettings Schema"
    assert form['form'].startswith('<form')
    se = 'name="test_views-teststringsetting" value="hello world"'
    assert se in form['form']
    se = 'name="test_views-testrageintsetting" value="5"'
    assert se in form['form']
