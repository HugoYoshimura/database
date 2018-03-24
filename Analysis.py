from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Image
import database.Classifier
from models.Analysis import Analysis as AnalysisModel
from repository.base import Base

class Analysis(Base.Base):
    __tablename__ = 'analysis'

    id = Column(Integer, primary_key=True)
    idImage = Column('id_image', Integer, ForeignKey('images.id'))
    idClassifier = Column('id_classifier', Integer, ForeignKey('classifiers.id'))
    image = relationship('Image', back_populates='analysis')
    classifier = relationship('Classifier', back_populates='analysis')


    def __init__(self,
                 id=0,
                 idImage=0,
		 image=object(),
		 idClassifier=0,
		 classifier=object(),
                 analysis=AnalysisModel()):
        if (analysis.id or analysis.image.id or analysis.classifier.id):
            self.id = analysis.id
            self.idImage = analysis.image.id
	    self.idClassifier = analysis.classifier.id
        else:
            self.id = id
            self.idImage = idImage
	    self.idClassifier = idClassifier
