import tkinter as tk
import jieba.analyse

class MyFrame(tk.LabelFrame):
    def __init__(self, parent, text):
        tk.LabelFrame.__init__(self, parent, text=text)
        # single:Entry multi:Text
        self.t1 = tk.Text(self, height=10)
        self.t1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.b1 = tk.Button(self, text="分析", command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.result = tk.Label(self, text="結果")
        self.result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

    def analyse(self):
        t = self.t1.get("1.0", "end")
        tags = jieba.analyse.extract_tags(t, topK=5)
        self.result["text"] = str(tags)

# 變數名稱 = 創造元件(父親)
# 變數.排版 (pack/grid/...)
window = tk.Tk()
window.geometry("500x500+250+250")
f1 = MyFrame(window, "文章分析")
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20, side=tk.LEFT)
# f2 = MyFrame(window, "文章分析2")
# f2.pack(expand=True, fill=tk.BOTH, padx=20, pady=20, side=tk.LEFT)
window.mainloop()