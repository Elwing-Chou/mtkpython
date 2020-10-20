import tkinter as tk
import jieba.analyse
import time
import threading

class MyFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="新聞分析")
        self.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.t1 = tk.Text(self)
        self.t1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.b1 = tk.Button(self, text="產生關鍵詞", command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.l1 = tk.Label(self, text="點擊上方按鈕")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def analyse(self):
        def work():
            self.b1["state"] = tk.DISABLED
            time.sleep(5)
            news = self.t1.get("1.0", "end")
            self.l1["text"] = str(jieba.analyse.extract_tags(news, 5))
            self.b1["state"] = tk.ACTIVE
        th = threading.Thread(target=work)
        th.start()

window = tk.Tk()
window.geometry("700x700+250+300")
# 創造元件(老爸) -> 元件.排版(pack)
MyFrame(window)
window.mainloop()