from sqlalchemy.sql.expression import desc

from kotti import DBSession

from kotti_settings.resources import Settings


# @property
def get_settings():
    settings = DBSession.query(Settings).order_by(desc(Settings.id)).first()
    data = {}
    if settings is not None:
        data = settings.data
    return data
