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
    size = Column(Integer)
    idDisease = Column('id_disease', Integer, ForeignKey('diseases.id'))
    disease = relationship('Disease', back_populates='images')

    def __init__(self,
                 url='',
                 description='',
                 source='',
                 size=0,
                 idDisease=0,
                 disease=object,  # =Disease(),
                 image=ImageModel()):
        if (image.id or image.url):
            self.url = image.url
            self.description = image.description
            self.source = image.source
            self.size = image.size
            self.idDisease = image.disease.id
            # self.disease = database.Disease.Disease(image.disease)
        else:
            self.url = url
            self.description = description
            self.source = source
            self.size = size
            self.idDisease = idDisease
            # self.disease = disease
