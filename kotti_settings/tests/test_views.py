import pytest
from kotti.resources import get_root

from kotti_settings.views import SettingsView
from kotti_settings.util import add_settings

from kotti_settings.testing import get_view
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

    view = get_view(rendered['settings_form_views'],
                    name='test_settings_dict')
    assert view['view'].title == "Testsettings Dict"
    assert view['form'].startswith('<form')
    assert 'name="test_views-testsetting_1"'\
        in view['form']
    assert 'value="my first string"' in view['form']
    assert 'name="test_views-testsetting_2"'\
        in view['form']
    assert 'value="23"' in view['form']


def test_settingtab_with_schema(db_session, dummy_request):
    add_settings(TestSettingsSchema)
    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    view = get_view(rendered['settings_form_views'],
                    name='test_settings_schema')
    assert view['view'].title == "Testsettings Schema"
    assert view['form'].startswith('<form')
    se = 'name="test_views-teststringsetting" value="hello world"'
    assert se in view['form']
    se = 'name="test_views-testrageintsetting" value="5"'
    assert se in view['form']


def test_settingtab_multiple(db_session, dummy_request):
    add_settings(TestSettingsDict)
    add_settings(TestSettingsSchema)
    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    rendered = view.view()
    assert 'settings_form_views' in rendered

    import pdb;pdb.set_trace()



def test_wrong_settings(db_session, dummy_request):
    add_settings(TestWrongSettingsDict)

    root = get_root()
    view = SettingsView(root, dummy_request)
    assert type(view) == SettingsView

    with pytest.raises(NameError):
        view.view()
