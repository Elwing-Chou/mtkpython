from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phones = relationship("Mobile", backref="student")

    def __str__(self):
        return "{} {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

class Mobile(Base):

    __tablename__ = "mobiles"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return "{} {}".format(self.id, self.number)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    import os
    import model_1213 as model
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # create_engine("sqlite:///")
    dn = os.path.dirname(__file__)
    fn = os.path.join(dn, "data.sqlite")
    sqlpath = "sqlite:///{}".format(fn)
    # echo=True
    engine = create_engine(sqlpath)
    model.Base.metadata.drop_all(engine)
    model.Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session1 = Session()

    p1 = model.Mobile(number="0912345678")
    p2 = model.Mobile(number="0923123421")
    s1 = model.Student(name="Elwing", phones=[p1, p2])
    session1.add(s1)
    session1.commit()

    # 1: first()
    result = session1.query(model.Student).filter_by(name="Elwing")
    for s in result:
        print(s)
        print(s.phones)