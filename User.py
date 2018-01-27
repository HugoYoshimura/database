from sqlalchemy import Column, String, Integer, ForeignKey
import models.User
from repository.base import Base


class User(Base.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    idType = Column('id_type', Integer, ForeignKey('types.id'))
    email = Column(String(200))
    username = Column(String(20))
    password = Column(String(128))
    salt = Column(String(32))
    dateInsertion = Column('date_insertion', String(100))
    dateUpdate = Column('date_last_update', String(100))

    def __init__(self,
                 id=0,
                 idType=0,
                 email="",
                 username="",
                 password="",
                 salt="",
                 dateInsertion="",
                 dateUpdate="",
                 user=models.User.User()):
        if (user.id or user.username):
            self.id = user.id
            self.idType = user.type.id
            self.email = user.email
            self.username = user.username
            self.password = user.password
            self.salt = user.salt
            self.dateInsertion = user.date_insertion
            self.dateUpdate = user.date_update
        else:
            self.id = id
            self.idType = idType
            self.email = email
            self.username = username
            self.password = password
            self.salt = salt
            self.dateInsertion = dateInsertion
            self.dateUpdate = dateUpdate
