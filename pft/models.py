from dictalchemy import make_class_dictable
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()
make_class_dictable(ModelBase)


class Note(ModelBase):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=True)
