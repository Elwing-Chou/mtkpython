import tkinter as tk

class MyFrame(tk.Frame):

    def __init__(self, parent, session):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.e1 = tk.Entry(self)
        self.e1.pack()
        self.b1 = tk.Button(self, text="按我查詢", command=self.query)
        self.b1.pack()
        self.l1 = tk.Label(self, text="點擊上方")
        self.l1.pack()
        self.session = session

    def query(self):
        number = self.e1.get()
        print(number)
        self.l1["text"] = str(student)

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    dir = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dir, "data.sqlite")
    engine = create_engine(fn, echo=True)
    session = sessionmaker(bind=engine)()
    window = tk.Tk()
    MyFrame(window, session)
    window.mainloop()