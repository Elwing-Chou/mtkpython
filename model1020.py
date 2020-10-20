from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    mobiles = relationship("Mobile", backref="student")

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

class Mobile(Base):

    __tablename__ = "mobiles"
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
    dir = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dir, "data.sqlite")
    engine = create_engine(fn, echo=True)
    session = sessionmaker(bind=engine)()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    s = Student(name="Elwing")
    s.mobiles = [
        Mobile(number="0912345678"),
        Mobile(number="0932144244")
    ]
    session.add(s)
    session.commit()

    mobile = (session.query(Mobile)
                     .filter_by(number="0912345678")
                     .first())
    # 當你需要
    # first, all
    print(mobile)
    print(mobile.student)
    print(mobile.student.mobiles)
