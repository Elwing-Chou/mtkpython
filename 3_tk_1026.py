import tkinter as tk
import time
import threading
import jieba.analyse

class MyFrame(tk.LabelFrame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="分析")
        self.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.t1 = tk.Text(self)
        self.t1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.b1 = tk.Button(self, text="請按我", command=self.analyse)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.l1 = tk.Label(self, text="按上面顯示結果")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def analyse(self):
        def work():
            self.b1["state"] = tk.DISABLED
            time.sleep(5)
            news = self.t1.get("1.0", "end")
            keys = jieba.analyse.extract_tags(news, 5)
            self.l1["text"] = str(keys)
            self.b1["state"] = tk.ACTIVE
        thread = threading.Thread(target=work)
        thread.start()

window = tk.Tk()
window.geometry("700x700+300+300")
# 元件(parent) 元件.排版(pack)
MyFrame(window)
window.mainloop()