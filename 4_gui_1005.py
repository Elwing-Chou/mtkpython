import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.l1 = tk.Label(self, text="輸入文章:")
        self.l1.pack(expand=True, fill=tk.BOTH)

        self.t1 = tk.Text(self)
        self.t1.pack(expand=True, fill=tk.BOTH)

        self.b1 = tk.Button(self, text="關鍵詞分析", command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH, pady=10)

        self.result = tk.Label(self, text="點擊上面分析")
        self.result.pack(expand=True, fill=tk.BOTH)

    def analyse(self):
        text = self.t1.get("1.0", "end")
        import jieba.analyse
        keywords = jieba.analyse.extract_tags(text)
        self.result["text"] = str(keywords)

window = tk.Tk()
window.geometry("500x500+200+200")

# e = 創造元件(父親) -> e.排版()
# 1. 先畫Frame, 再放元件
# 2. 排版(pack[左右上下]/grid[表格]/absolute[絕對])
# 建議pack
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)

f2 = MyFrame(window)
f2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)

window.mainloop()