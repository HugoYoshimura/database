from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.Image import Image as ImageModel
import database.Disease
from repository.base import Base


class Image(Base.Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    url = Column(String(2000))
    description = Column(String(2000))
    source = Column(String(2000))
    size = Column(Integer, ForeignKey('types.id'))
    idDisease = Column('id_disease', Integer, ForeignKey('diseases.id'))
    disease = relationship('Disease', back_populates='images')

    def __init__(self,
                 id=0,
                 url='',
                 description='',
                 source='',
                 size=0,
                 disease=object, # =Disease(),
                 image=ImageModel()):
        if (not image.id or not image.url):
            self.id = image.id
            self.url = image.url
            self.description = image.description
            self.source = image.source
            self.size = image.size
            self.disease = Disease(image.disease)
        else:
            self.id = id
            self.url = url
            self.description = description
            self.source = source
            self.size = size
            self.disease = disease
