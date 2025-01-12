from sqlalchemy import Column, Integer, String
from db import Base, engine

class Students(Base):
   __tablename__ = 'student'
   id = Column(Integer, primary_key=True, nullable=False)
   name = Column(String(63), unique=True)
   marks = Column(Integer)

Base.metadata.create_all(bind=engine)