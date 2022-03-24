import tkinter as tk
import jieba.analyse
import time
import threading

class MyFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # 標籤: Label
        self.l1 = tk.Label(self, text="請輸入文章")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        # 多行輸入: Text 單行輸入: Entry
        self.t1 = tk.Text(self)
        self.t1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.b1 = tk.Button(self, text="分析", command=self.analyse)
        # tk.X/tk.Y
        self.b1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        self.result = tk.Label(self, text="點按鈕分析...")
        self.result.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)

    # e = 元件(父元件)
    # e.排版() pack(上下左右) grid(表格) absolute(絕對)
    def analyse(self):
        def work():
            self.b1["state"] = tk.DISABLED
            self.result["text"] = "分析中..."
            time.sleep(5)
            news = self.t1.get("1.0", "end")
            keywords = jieba.analyse.extract_tags(news)
            # 第二時間設置text
            self.result["text"] = str(keywords)
            self.b1["state"] = tk.ACTIVE
        t1 = threading.Thread(target=work)
        t1.start()


# main thread: UI事件
window = tk.Tk()
window.geometry("500x500+100+100")

f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

# f2 = MyFrame(window)
# f2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

window.mainloop()
