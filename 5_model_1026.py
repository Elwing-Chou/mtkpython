from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phones = relationship("Phone", backref="student")

    def __str__(self):
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

class Phone(Base):

    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return "{}: {}".format(self.id, self.number)

    def __repr__(self):
        return self.__str__()
