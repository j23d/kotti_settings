import colander
from kotti_settings.util import add_settings


def get_form(rens, name=None, title=None):
    """Get us the right form dictionary."""
    for ren in rens:
        if name is not None and name == ren['name']:
            return ren
        if title is not None and title == ren['title']:
            return ren
    return rens[0]


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


class StringSchemaNode(colander.SchemaNode):
    name = 'teststringsetting'
    title = 'hello'
    default = 'hello world'


class RangedIntSchemaNode(colander.SchemaNode):
    name = 'testrageintsetting'
    validator = colander.Range(0, 10)
    default = 5
    title = 'Ranged Int'


class TestSchema(colander.MappingSchema):
    string = StringSchemaNode(colander.String())
    ranged_int = RangedIntSchemaNode(colander.Int())


TestSettingsSchema = {
    'name': 'test_settings_schema',
    'title': "Testsettings Schema",
    'success_message': u"Successfully saved test settings.",
    'schema_factory': TestSchema
}


class TestSchemaBrowser(colander.MappingSchema):
    string = StringSchemaNode(colander.String())
    ranged_int = RangedIntSchemaNode(colander.Int())

TestSettingsSchemaBrowser = {
    'name': 'test_settings_schema_browser',
    'title': "Testsettings Schema",
    'success_message': u"Successfully saved test settings.",
    'schema_factory': TestSchemaBrowser
}


def _populator():
    from kotti.populate import populate as kotti_p
    from kotti_settings.populate import populate as kotti_settings_p
    kotti_p()
    kotti_settings_p()


def _add_schema_settings():
    add_settings(TestSettingsSchema)


def _add_dict_settings():
    add_settings(TestSettingsDict)


def _add_browser_settings():
    add_settings(TestSettingsSchemaBrowser)
