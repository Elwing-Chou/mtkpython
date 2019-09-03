from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __str__(self):
        return self.name