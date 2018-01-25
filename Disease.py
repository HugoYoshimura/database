from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from capivaraprojects.greeneyes.database.Image import Image
from capivaraprojects.greeneyes.database.Plant import Plant
from capivaraprojects.greeneyes.models.Disease import Disease as DiseaseModel
from capivaraprojects.greeneyes.repository.base import Base


class Disease(Base.Base):
    __tablename__ = 'diseases'

    id = Column(Integer, primary_key=True)
    scientificName = Column('scientific_name', String(2000))
    commonName = Column('common_name', String(2000))
    idPlant = Column('id_plant', Integer, ForeignKey('plants.id'))
    plant = relationship('Plant', back_populates='diseases')
    images = relationship('Image', back_populates='disease')

    def __init__(self,
                 id=0,
                 scientificName="",
                 commonName="",
                 plant=Plant(),
                 images=[],
                 disease=DiseaseModel()):
        if (not disease.id or not disease.scientificName):
            self.id = disease.id
            self.scientificName = disease.scientificName
            self.commonName = disease.commonName
            self.plant = Plant(disease.plant)
            self.images = []
            for image in disease.images:
                self.images.append(Image(image))
        else:
            self.id = id
            self.scientificName = scientificName
            self.commonName = commonName
            self.plant = plant
            self.images = images
