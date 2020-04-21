import sqlalchemy
from .db_session import SqlAlchemyBase


class UsersFriends(SqlAlchemyBase):
    __tablename__ = 'users_friends'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    # id пользователя, который добавляет в друзья
    inviter_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'))
    # id пользователя, которого добавляют в друзья
    invitee_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'))
    is_accepted = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
