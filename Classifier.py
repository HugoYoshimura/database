from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import database.Plant
from models.Classifier import Classifier as ClassifierModel
from repository.base import Base

class ClassifierDB(Base.Base):
	__tablename__ = 'classifiers'

	id = Column(Integer, primary_key=True)
	idPlant = Column('id_plant', Integer, ForeignKey('plants.id')
	tag = Column('tag', String(2000))
	path = Column('path', String(2000))

	def __init__(self, id=0, idPlant=0, tag="", path="", classifier=ClassifierModel()):
		if (classifier.id):
			self.id = classifier.id
			self.idPlant = classifier.idPlant
			self.tag = classifier.tag
			self.path = classifier.path
		else:
			self.id = id
                        self.idPlant = idPlant
                        self.tag = tag
                        self.path = path
