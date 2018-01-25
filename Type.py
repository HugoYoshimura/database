from sqlalchemy import Column, String, Integer
from capivaraprojects.greeneyes.models.Type import Type as TypeModel
from capivaraprojects.greeneyes.repository.base import Base


class Type(Base.Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    value = Column(String(2000))
    description = Column(String(2000))

    def __init__(self, id, value, description, type=TypeModel()):
        if(not type.value or not type.id):
            self.id = type.id
            self.value = type.value
            self.description = type.description
        else:
            self.id = id
            self.value = value
            self.description = description
