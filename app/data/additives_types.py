import sqlalchemy

from .db_session import SqlAlchemyBase


class AdditivesTypes(SqlAlchemyBase):
    __tablename__ = 'additives_types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
