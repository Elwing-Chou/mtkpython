import os
import tkinter as tk
from model import Student, Phone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class MyFrame(tk.Frame):
    def __init__(self, parent, session):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.l1 = tk.Label(self)
        self.l1.pack()
        self.session = session

    def query(self):
        n = self.e1.get()
        print(n)
        # self.session.query


window = tk.Tk()

dn = os.path.dirname(__file__)
fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
engine = create_engine(fn, echo=True)
session = sessionmaker(bind=engine)()

MyFrame(window, session)
window.mainloop()