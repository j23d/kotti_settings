from sqlalchemy.ext.mutable import Mutable


class MutableDict(Mutable, dict):
    """http://docs.sqlalchemy.org/en/rel_0_8/orm/extensions/
       mutable.html#sqlalchemy.ext.mutable.MutableDict
    """
    @classmethod
    def coerce(cls, key, value):
        """Convert plain dictionaries to MutableDict.
        """
        if not isinstance(value, MutableDict):
            if isinstance(value, dict):
                return MutableDict(value)

            # this call will raise ValueError
            return Mutable.coerce(key, value)
        else:
            return value

    def __setitem__(self, key, value):
        """Detect dictionary set events and emit change events.
        """
        dict.__setitem__(self, key, value)
        self.changed()

    def __delitem__(self, key):
        """Detect dictionary del events and emit change events.
        """
        dict.__delitem__(self, key)
        self.changed()
