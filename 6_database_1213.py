import os
import model_1213 as model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tkinter as tk

class MyFrame(tk.Frame):

    def __init__(self, parent, session):
        tk.Frame.__init__(self, parent)
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.result = tk.Label(self, text="電話")
        self.result.pack()
        self.session = session

    def query(self):
        name = self.e1.get()
        print(name)
        student = self.session.query(model.Student).filter_by(name=name).first()
        print(student)


# create_engine("sqlite:///")
dn = os.path.dirname(__file__)
fn = os.path.join(dn, "data.sqlite")
sqlpath = "sqlite:///{}".format(fn)
# echo=True
engine = create_engine(sqlpath)
Session = sessionmaker(bind=engine)
session1 = Session()

# gui
window = tk.Tk()
f1 = MyFrame(window, session1)
f1.pack()
window.mainloop()