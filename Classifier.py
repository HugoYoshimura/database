from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Plant
import database.Analysis
from models.Classifier import Classifier as ClassifierModel
from repository.base import Base



class Classifier(Base.Base):
    __tablename__ = 'classifiers'

    id = Column(Integer, primary_key=True)
    idPlant = Column('id_plant', Integer, ForeignKey('plants.id'))
    tag = Column('tag', String(2000))
    path = Column('path', String(2000))
    plant = relationship('Plant', back_populates='classifiers')
    analysis = relationship('database.Analysis.Analysis', lazy='subquery',
                            back_populates='classifier')

    def __init__(self, 
                    id=0, 
                    idPlant=0, 
                    tag="", 
                    path="", 
                    plant=object(), 
                    analyses=[], 
                    classifier=ClassifierModel()):
        if (classifier.id or classifier.tag or classifier.path):
            self.id = classifier.id
            self.idPlant = classifier.plant.id
            self.tag = classifier.tag
            self.path = classifier.path
            self.analyses = []
            for analysis in classifier.analyses:
                self.analyses.append(database.Analysis.Analysis(analysis))
        else:
            self.id = id
            self.idPlant = idPlant
            self.tag = tag
            self.path = path
            self.analyses = analyses
