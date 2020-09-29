import tkinter as tk
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

nowdir = os.path.dirname(__file__)
sqlpath = "sqlite:///" + os.path.join(nowdir, "data.sqlite")

engine = create_engine(sqlpath, echo=True)
Session = sessionmaker(bind=engine)
sess = Session()

class MyFrame(tk.LabelFrame):

    def __init__(self, parent, sess):
        tk.LabelFrame.__init__(self, parent, text="電話簿")
        self.pack()
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.l1 = tk.Label(self, text="查詢結果")
        self.l1.pack()
        self.session = sess

    def query(self):
        number = self.e1.get()
        print(number)


window = tk.Tk()
window.geometry("500x500+200+200")
MyFrame(window, sess)
tk.mainloop()