from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import database.Disease
import database.Analysis
from models.AnalysisResult import AnalysisResult as AnalysisResultModel
from repository.base import Base

class AnalysisResult(Base.Base):
    __tablename__ = 'analysis_result'

    id = Column(Integer, primary_key=True)
    idAnalysis = Column('id_analysis', Integer, ForeignKey('analysis.id'))
    idDisease = Column('id_disease', Integer, ForeignKey('diseases.id'))
    score = Column(Float)
    disease = relationship('database.Disease.Disease', back_populates='analysis_result')
    analysis = relationship('database.Analysis.Analysis', back_populates='analysis_result')

    def __init__(self,
                 id=0,
                 idAnalysis=0,
                 analysis=object(),
                 idDisease=0,
                 disease=object(),
                 score=0,
                 analysisResult=AnalysisResultModel()):
        if (analysisResult.id or 
                analysisResult.analysis.id or 
                analysisResult.disease.id or 
                analysisResult.score):
            self.id = analysisResult.id
            self.idAnalysis = analysisResult.analysis.id
            self.idDisease = analysisResult.disease.id
            self.score = analysisResult.score
        else:
            self.id = id
            self.idAnalysis = idAnalysis
            self.idDisease = idDisease
            self.score = score
