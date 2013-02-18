import pytest
from kotti.resources import get_root

from kotti_settings.views import SettingsView
from kotti_settings.util import add_settings


def get_form(rens, name=None, title=None):
    """Get us the right form dictionary."""
    for ren in rens:
        if name is not None and name == ren['name']:
            return ren
        if title is not None and title == ren['title']:
            return ren
    return rens[0]


def test_settingtab_with_dict(db_session,
                              populate_kotti_settings,
                              dummy_request):
    TestSettingsDict = {
        'name': 'test_settings_dict',
        'title': "Testsettings Dict",
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'name': 'testsetting_1',
             'title': 'Test 1',
             'description': 'a test setting',
             'default': 'my first string', },
            {'type': 'Integer',
             'name': 'testsetting_2',
             'title': 'Test 2',
             'description': 'again a test setting',
             'default': 23, }
        ]
    }
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
    assert 'name="test_views-testsetting_1"' in form['form']
    pytest.xfail("missing the default to be transformed into the form")
    assert 'value="my first string"' in form['form']
    assert 'name="kotti_settings-testsetting_2"' in form['form']
    assert 'value="23"' in form['form']


def test_settingtab_with_schema(db_session,
                                populate_kotti_settings,
                                dummy_request):
    from kotti_settings.form import SettingsSchema
    import colander

    class StringSchemaNode(colander.SchemaNode):
        name = 'teststringsetting'
        title = 'hello'
        default = 'hello world'

    class RangedIntSchemaNode(colander.SchemaNode):
        name = 'testrageintsetting'
        validator = colander.Range(0, 10)
        default = 5
        title = 'Ranged Int'

    class TestSchema(SettingsSchema):
        string = StringSchemaNode(colander.String())
        ranged_int = RangedIntSchemaNode(colander.Int())

    TestSettingsSchema = {
        'name': 'test_settings_schema',
        'title': "Testsettings Schema",
        'success_message': u"Successfully saved test settings.",
        'schema': TestSchema()
    }

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
    assert 'name="teststringsetting"' in form['form']
    assert 'value="hello world"' in form['form']
    assert 'name="testrageintsetting"' in form['form']
    assert 'value="5"' in form['form']
