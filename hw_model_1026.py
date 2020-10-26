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

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    dn = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
    engine = create_engine(fn, echo=True)
    session = sessionmaker(bind=engine)()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    s = Student(name="Elwing")
    s.phones = [Phone(number="0912345678"),
                Phone(number="0938236123")]
    session.add(s)
    session.commit()

    # .first() .all()
    p = (session.query(Phone)
                .filter_by(number="0912345678")
                .first())
    print(p)
    print(p.student)
    print(p.student.phones)