import tkinter as tk

class MyFrame(tk.Frame):

    def __init__(self, root, session):
        tk.Frame.__init__(self, root)
        self.l1 = tk.Label(self, text="輸入姓名")
        self.l1.pack()
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.result = tk.Label(self, text="按上面查詢")
        self.result.pack()
        self.session = session

    def query(self):
        name = self.e1.get()
        print(name)


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
dn = os.path.dirname(__file__)
fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
# echo=True
engine = create_engine(fn, echo=False)
Session = sessionmaker(bind=engine)
session1 = Session()

window = tk.Tk()
f1 = MyFrame(window, session1)
f1.pack()
window.mainloop()