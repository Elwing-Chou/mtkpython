import tkinter as tk
import jieba.analyse

class MyFrame(tk.LabelFrame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="分析")
        self.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.e1 = tk.Text(self, height=10)
        self.e1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.b1 = tk.Button(self, text="請點我", command=self.analyze)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.l1 = tk.Label(self, text="分析結果!!!")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def analyze(self):
        news = self.e1.get("1.0", "end")
        keywords = jieba.analyse.extract_tags(news)
        self.l1["text"] = str(keywords)

window = tk.Tk()
window.geometry("500x500+200+200")

# Step1. 創造元件(老爸) Step2. 排版(grid[表格], pack[上下左右])
# 元件在創立前, 先創立tk.mainloop()Frame
MyFrame(window)

tk.mainloop()