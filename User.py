from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.User import User as UserModel
from repository.base import Base
import database.Analysis


class User(Base.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(200))
    username = Column(String(20))
    password = Column(String(2000))
    salt = Column(String(32))
    dateInsertion = Column('date_insertion', String(100))
    dateUpdate = Column('date_last_update', String(100))
    idType = Column('id_type', Integer)
    analysis = relationship('database.Analysis.Analysis', lazy='subquery',
                            back_populates='user')

    def __init__(self,
                 id=0,
                 email="",
                 username="",
                 password="",
                 salt="",
                 dateInsertion="",
                 dateUpdate="",
                 idType=0,
                 user=UserModel,
                 analysis=[]):
        if (user.id or user.username):
            self.id = user.id
            self.email = user.email
            self.username = user.username
            self.password = user.password
            self.salt = user.salt
            self.dateInsertion = user.dateInsertion
            self.dateUpdate = user.dateUpdate
            self.idType = user.idType
            self.analysis = []
            for an in analysis:
                self.analysis.append(database.Analysis.Analysis())
        else:
            self.id = id
            self.email = email
            self.username = username
            self.password = password
            self.salt = salt
            self.dateInsertion = dateInsertion
            self.dateUpdate = dateUpdate
            self.idType = idType
            self.analysis = []
            for an in analysis:
                self.analysis.append(database.Analysis.Analysis())
