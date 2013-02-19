from kotti_settings.tests.util import TestSettingsDict
from kotti_settings.tests.util import TestSettingsSchema
from kotti_settings.util import add_settings


def _populator():
    from kotti.populate import populate as kotti_p
    from kotti_settings.populate import populate as kotti_settings_p
    kotti_p()
    kotti_settings_p()


def _add_schema_settings():
    add_settings(TestSettingsSchema)


def _add_dict_settings():
    add_settings(TestSettingsDict)
