

class ModuleSettings(object):
    """Object to hold informations about the settings of
       the calling module.
    """

    def __init__(self, **kwargs):
        self.module = None
        self.name = None
        self.title = None
        self.description = None
        self.success_message = u''
        self.settings = []
        self.schema_factory = None
        self.settings_objs = []
        self.__dict__.update(kwargs)


class SettingObj(object):
    """One setting in a module. Here we are also set the defaults
       for one setting.
    """

    def __init__(self, **kwargs):
        self.module = None
        self.type = 'String'
        self.name = None
        self.title = None
        self.description = u''
        self.default = ''
        self.__dict__.update(kwargs)

    @property
    def field_name(self):
        """Return a name that is somewhat unique.
        """
        return "%s-%s" % (self.module, self.name)
