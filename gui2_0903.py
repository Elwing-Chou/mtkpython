from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.l1 = Label(self, text="輸入新聞")
        self.l1.pack()
        self.t1 = Text(self, height=10)
        self.t1.pack()
        self.b1 = Button(self,
                         text="分析",
                         command=self.analyse)
        self.b1.pack()
        self.result = Label(self, text="按上面得到關鍵詞")
        self.result.pack()

    def analyse(self):
        self.result["text"] = "!!!!"

# 1. 元件(父元件) 2. 元件.排版(pack grid)
window = Tk()
window.geometry("500x500+200+200")

f1 = MyFrame(window)
f1.pack()

window.mainloop()