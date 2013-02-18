from kotti.resources import DBSession
from kotti_settings.resources import Settings


def populate():
    """Add container in the settings table for the data.
    """
    if DBSession.query(Settings).count() == 0:
        settings = Settings(data={})
        DBSession.add(settings)
        DBSession.flush()
