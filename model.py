from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Person(Base):

    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

    def __repr__(self):
        return str(self)

class Phone(Base):

    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    person_id = Column(Integer, ForeignKey("people.id"))

    def __str__(self):
        return "{}:{}".format(self.id, self.number)

    def __repr__(self):
        return str(self)