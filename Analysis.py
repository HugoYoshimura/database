from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Image
from models.Analysis import Analysis as AnalysisModel
from repository.base import Base

class Analysis(Base.Base):
    __tablename__ = 'analysis'

    id = Column(Integer, primary_key=True)
    idImage = Column('id_image', Integer, ForeignKey('images.id'))

    def __init__(self,
                 id=0,
                 idImage=0,
                 analysis=AnalysisModel()):
        if (analysis.id or analysis.idImage):
            self.id = analysis.id
            self.idImage = analysis.idImage
        else:
            self.id = id
            self.idImage = idImage
