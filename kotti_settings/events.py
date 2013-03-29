

class SettingsEvent(object):
    """ """
    def __init__(self, module=None):
        self.module = module


class SettingsBeforeSave(SettingsEvent):
    pass


class SettingsAfterSave(SettingsEvent):
    pass
