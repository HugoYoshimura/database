from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Image
import database.Classifier
import database.AnalysisResult
import database.User
from models.Analysis import Analysis as AnalysisModel
from repository.base import Base


class Analysis(Base.Base):
    __tablename__ = 'analysis'

    id = Column(Integer, primary_key=True)
    idImage = Column('id_image', Integer, ForeignKey('images.id'))
    idClassifier = Column(
        'id_classifier',
        Integer,
        ForeignKey('classifiers.id'))
    idUser = Column(
        'id_user',
        Integer,
        ForeignKey('users.id'))
    image = relationship('Image', back_populates='analysis')
    classifier = relationship('Classifier', back_populates='analysis')
    analysis_results = relationship('database.AnalysisResult.AnalysisResult',
                                    lazy='subquery',
                                    cascade='delete',
                                    back_populates='analysis')
    user = relationship('database.User.User', back_populates='analysis')

    def __init__(self,
                 id=0,
                 idImage=0,
                 image=object(),
                 idClassifier=0,
                 classifier=object(),
                 analysis=AnalysisModel(),
                 analysis_results=[],
                 user=object(),
                 idUser=0):
        if (analysis.id or analysis.image.id or analysis.classifier.id):
            self.id = analysis.id
            self.idImage = analysis.image.id
            self.idClassifier = analysis.classifier.id
            self.idUser = analysis.user.id
            self.analysis_results = []
            for result in analysis_results:
                self.analysis_results.append(
                    database.AnalysisResult.AnalysisResult(result))
        else:
            self.id = id
            self.idImage = idImage
            self.idClassifier = idClassifier
            self.idUser = idUser
            self.analysis_results = analysis_results
