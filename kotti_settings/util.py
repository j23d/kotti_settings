import inspect

from kotti.resources import get_root

from kotti_settings.config import SETTINGS
from kotti_settings.settings import ModuleSettings
from kotti_settings.settings import SettingObj


def get_settings():
    root = get_root()
    if "kotti_settings" not in root.annotations:
        root.annotations['kotti_settings'] = {}
    return root.annotations['kotti_settings']


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
