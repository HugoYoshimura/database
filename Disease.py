from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Image
import database.Plant
import database.AnalysisResult
from models.Disease import Disease as DiseaseModel
from repository.base import Base


class Disease(Base.Base):
    __tablename__ = 'diseases'

    id = Column(Integer, primary_key=True)
    scientificName = Column('scientific_name', String(2000))
    commonName = Column('common_name', String(2000))
    idPlant = Column('id_plant', Integer, ForeignKey('plants.id'))
    plant = relationship('Plant', back_populates='diseases')
    images = relationship('Image', lazy='subquery', 
                          back_populates='disease')
    analysis_result = relationship('database.AnalysisResult.AnalysisResult',
                                    lazy='subquery',
                                    back_populates='disease')
    def __init__(self,
                 id=0,
                 scientificName="",
                 commonName="",
                 idPlant=0,
                 plant=object(),  # database.Plant.Plant(),
                 images=[],
                 disease=DiseaseModel()):
        if (disease.id or disease.scientificName):
            self.id = disease.id
            self.scientificName = disease.scientificName
            self.commonName = disease.commonName
            self.idPlant = disease.plant.id
            #self.plant = database.Plant.Plant(disease.plant)
            self.images = []
            for image in disease.images:
                self.images.append(database.Image.Image(image))
        else:
            self.id = id
            self.scientificName = scientificName
            self.commonName = commonName
            self.idPlant = idPlant
            #self.plant = plant
            self.images = images
