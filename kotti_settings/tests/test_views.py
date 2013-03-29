import pytest
from kotti.resources import get_root

from kotti_settings.views import SettingsView
from kotti_settings.util import add_settings

from kotti_settings.testing import TestSettingsDict
from kotti_settings.testing import TestSettingsSchema
from kotti_settings.testing import TestWrongSettingsDict


def test_settingtab_with_dict(db_session, dummy_request):
    add_settings(TestSettingsDict)

    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    name = 'test_settings_dict'
    for ren in rendered['settings_form_views']:
        if name is not None and name == ren['view'].name:
            view = ren

    assert view['view'].title == "Testsettings Dict"
    assert view['form'].startswith('<form')
    assert 'name="kotti_settings-testsetting_1"'\
        in view['form']
    assert 'value="my first string"' in view['form']
    assert 'name="kotti_settings-testsetting_2"'\
        in view['form']
    assert 'value="23"' in view['form']


def test_settingtab_with_schema(db_session, dummy_request):
    add_settings(TestSettingsSchema)
    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    name = 'test_settings_schema'
    for ren in rendered['settings_form_views']:
        if name is not None and name == ren['view'].name:
            view = ren

    assert view['view'].title == "Testsettings Schema"
    assert view['form'].startswith('<form')
    se = 'name="kotti_settings-teststringsetting" value="hello world"'
    assert se in view['form']
    se = 'name="kotti_settings-testrageintsetting" value="5"'
    assert se in view['form']


def test_wrong_settings(db_session, dummy_request):
    add_settings(TestWrongSettingsDict)

    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    with pytest.raises(NameError):
        view.view()
