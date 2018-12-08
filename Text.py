from sqlalchemy import Column, String, Integer
import models.Text
from repository.base import Base


class Text(Base.Base):
    __tablename__ = 'texts'

    id = Column(Integer, primary_key=True)
    language = Column(String(5))
    plant = Column(String(200))
    status = Column(String(200))
    attribute = Column(String(2000))
    value = Column(String(100000))
    reference = Column(String(2000))

    def __init__(self,
                 id=0,
                 language="",
                 plant="",
                 status="",
                 attribute="",
                 value="",
                 reference="",
                 text=models.Text.Text()):
        if (text.id or text.value):
            self.id = text.id
            self.language = text.language
            self.plant = text.plant
            self.status = text.status
            self.attribute = text.attribute
            self.value = text.value
            self.reference = text.reference
        else:
            self.id = id
            self.language = language
            self.plant = plant
            self.status = status
            self.attribute = attribute
            self.value = value
            self.reference = reference
