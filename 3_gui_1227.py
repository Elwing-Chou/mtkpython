import tkinter as tk
import jieba.analyse

class MyFrame(tk.LabelFrame):
    def __init__(self, root):
        tk.LabelFrame.__init__(self, root, text="文章分析器")
        self.l1 = tk.Label(self, text="給我一篇文章")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        # Entry:single line Text: multi line
        self.t1 = tk.Text(self, height=10)
        self.t1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.b1 = tk.Button(self, text="分析", command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.result = tk.Label(self, text="點擊按鈕分析")
        self.result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

    def analyse(self):
        s = self.t1.get("1.0", "end")
        keywords = jieba.analyse.extract_tags(s)
        self.result["text"] = str(keywords)

window = tk.Tk()
window.geometry("500x500+200+200")
# 創造元件(老爸)
# 元件.排版(pack/grid/absolute)
# 容器(Frame)
f1 = MyFrame(window)
# tk.BOTH, tk.X, tk.Y
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=15, pady=15)
f2 = MyFrame(window)
# tk.BOTH, tk.X, tk.Y
f2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=15, pady=15)
window.mainloop()
