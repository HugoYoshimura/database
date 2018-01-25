from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import database.Disease
import models.Plant
from repository.base import Base


class Plant(Base.Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    scientificName = Column('scientific_name', String(2000))
    commonName = Column('common_name', String(2000))
    diseases = relationship('database.Disease.Disease', lazy='subquery',
                            back_populates='plant')

    def __init__(self,
                 id=0,
                 scientificName="",
                 commonName="",
                 diseases=[],
                 plant=models.Plant.Plant()):
        if(not plant.commonName or not plant.id):
            self.id = plant.id
            self.scientificName = plant.scientificName
            self.commonName = plant.commonName
            self.diseases = []
            for disease in plant.diseases:
                self.diseases.append(database.Disease.Disease(disease))
        else:
            self.id = id
            self.scientificName = scientificName
            self.commonName = commonName
            self.diseases = diseases
