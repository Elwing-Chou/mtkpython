
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    phones = relationship("Phone", backref="student")

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

class Phone(Base):

    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return "{}:{}".format(self.id, self.number)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    dn = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
    # echo=True
    engine = create_engine(fn, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session1 = Session()

    p1 = Phone(number="0912345678")
    p2 = Phone(number="0932123456")
    s1 = Student(name="Elwing", phones=[p1, p2])

    session1.add(s1)
    session1.commit()

    result = session1.query(Student).filter_by(name="Elwing").first()
    # .first()/.all() -> for in
    print(result.phones)
    for p in result.phones:
        print("!", p.student)