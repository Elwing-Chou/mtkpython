from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):

    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phones = relationship("Phone", backref="person")

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

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    nowdir = os.path.dirname(__file__)
    sqlpath = "sqlite:///" + os.path.join(nowdir, "data.sqlite")

    engine = create_engine(sqlpath, echo=True)
    Session = sessionmaker(bind=engine)
    sess = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    p1 = Person(name="Elwing")
    sess.add(p1)
    p1.phones = [Phone(number="0912345678"),
                 Phone(number="0934671213")]
    sess.commit()
    result = sess.query(Phone).filter_by(number="0912345678")
    p = result.first()
    print("!", p)
    print("!!", p.person)
    print("!!!", p.person.phones)