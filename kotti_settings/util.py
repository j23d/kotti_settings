import inspect

from sqlalchemy.sql.expression import desc

from kotti import DBSession

from kotti_settings.config import SETTINGS
from kotti_settings.resources import Settings
from kotti_settings.settings import ModuleSettings
from kotti_settings.settings import SettingObj


# @property
def get_settings():
    settings = DBSession.query(Settings).order_by(desc(Settings.id)).first()
    data = {}
    if settings is not None:
        data = settings.data
    return data


def add_settings(module_settings):
    """Get a dictionary and translate this into an object structure.
    """
    module_settings = ModuleSettings(**module_settings)
    if module_settings.module is None:
        # If the module name is omitted: get it
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        module_settings.module = module.__name__
    for setting in module_settings.settings:
        setting_obj = SettingObj(**setting)
        # name and title of a setting is required
        if setting_obj.name is None:
            raise ValueError('A setting has to have a name.')
        if setting_obj.title is None:
            raise ValueError('A setting has to have a title.')
        setting_obj.module = module_settings.module
        module_settings.settings_objs.append(setting_obj)
    SETTINGS.append(module_settings)
