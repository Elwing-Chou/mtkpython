import os
import model_1213 as model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create_engine("sqlite:///")
dn = os.path.dirname(__file__)
fn =os.path.join(dn, "data.sqlite")
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