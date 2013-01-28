from kotti.resources import DBSession
from kotti_settings.resources import Settings


def populate():
    """
    add values for settings table
    """
    if DBSession.query(Settings).count() == 0:
        settings = Settings(data={})
        DBSession.add(settings)
        DBSession.flush()
