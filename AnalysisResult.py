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

    def __init__(self,
                 id=0,
                 idAnalysis=0,
                 idDisease=0,
                 score=0,
                 analysisResult=AnalysisResultModel()):
        if if (analysisResult.id or analysisResult.idAnalysis or analysisResult.idDisease or analysisResult.score):
            self.id = analysisResult.id
            self.idAnalysis = analysisResult.idAnalysis
            self.idDisease = analysisResult.idDisease
            self.score = analysisResult.score
        else:
            self.id = id
            self.idAnalysis = idAnalysis
            self.idDisease = idDisease
            self.score = score
