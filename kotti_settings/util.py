import inspect

from kotti import DBSession
from kotti.resources import get_root
from kotti.views.slots import objectevent_listeners
from kotti.views.slots import slot_events

from kotti_settings.config import SETTINGS
from kotti_settings.settings import ModuleSettings
from kotti_settings.settings import SettingObj


def get_setting(name, not_found=None):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    modname = module.__name__
    if '.' in modname:
        modname = modname[:modname.find('.')]  # pragma: no cover
    if not name.startswith(modname):
        name = '{0}-{1}'.format(modname, name)
    settings = get_settings()
    if name in settings:
        return settings[name]
    return not_found


def get_settings():
    root = get_root()
    if "kotti_settings" not in root.annotations:
        root.annotations['kotti_settings'] = {}
    return root.annotations['kotti_settings']


def add_settings(module_settings):
    """Get a dictionary and translate this into an object structure.
    """
    settings = get_settings()
    module_settings = ModuleSettings(**module_settings)
    if module_settings.module is None:
        # If the module name is omitted: get it
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        modname = module.__name__
        if '.' in modname:
            modname = modname[:modname.find('.')]
        module_settings.module = modname
    for setting in module_settings.settings:
        setting_obj = SettingObj(**setting)
        # name and title of a setting is required
        if setting_obj.name is None:
            raise ValueError('A setting has to have a name.')
        if setting_obj.title is None:
            raise ValueError('A setting has to have a title.')
        setting_obj.module = module_settings.module
        default = None
        if 'default' in setting:
            default = setting['default']
        settings[setting_obj.field_name] = default
        module_settings.settings_objs.append(setting_obj)
    SETTINGS.append(module_settings)


def remove_from_slots(widget):
    """Check all slots if a widget is already set and remove it
       from the listener.
    """
    for slot_event in slot_events:
        try:
            listener = objectevent_listeners[(slot_event, None)]
        except TypeError:  # pragma: no cover
            listener = None
        if listener is not None:
            for func in listener:
                if func.func_closure[1].cell_contents == widget:
                    listener.remove(func)
    DBSession.flush()
