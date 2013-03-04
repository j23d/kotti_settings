import colander
from kotti_settings.util import add_settings


def get_view(rens, name=None, title=None):
    """Get us the right view dictionary."""
    for ren in rens:
        if name is not None and name == ren['view'].name:
            return ren
        if title is not None and title == ren['view'].title:
            return ren
    return rens[0]


TestSettingsDict = {
    'name': 'test_settings_dict',
    'title': "Testsettings Dict",
    'description': "Some settings in a dict.",
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

TestWrongSettingsDict = {
    'name': 'test_settings_dict',
    'title': "Testsettings Dict",
    'description': "Some wrong settings.",
    'success_message': u"Successfully saved test settings.",
    'settings': [
        {'type': 'Something',
         'name': 'something',
         'title': 'Something', },
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
    'description': "Some settings in a schema.",
    'success_message': u"Successfully saved test settings.",
    'schema_factory': TestSchema
}


class TestSchemaBrowser(colander.MappingSchema):
    string = StringSchemaNode(colander.String())
    ranged_int = RangedIntSchemaNode(colander.Int())

TestSettingsSchemaBrowser = {
    'name': 'test_settings_schema_browser',
    'title': "Testsettings Schema",
    'description': "Some settings in a schema.",
    'success_message': u"Successfully saved test settings.",
    'schema_factory': TestSchemaBrowser
}


def _add_schema_settings():
    add_settings(TestSettingsSchema)


def _add_dict_settings():
    add_settings(TestSettingsDict)


def _add_browser_settings():
    add_settings(TestSettingsSchemaBrowser)
