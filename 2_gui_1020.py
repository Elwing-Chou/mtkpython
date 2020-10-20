import tkinter as tk
import jieba.analyse

def analyse():
    global t1, l1
    news = t1.get("1.0", "end")
    l1["text"] = str(jieba.analyse.extract_tags(news, 5))

window = tk.Tk()
window.geometry("500x500+250+300")
# 創造元件(老爸) -> 元件.排版(pack)
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
t1 = tk.Text(f1)
t1.pack(expand=True, fill=tk.BOTH)
b1 = tk.Button(f1, text="產生關鍵詞", command=analyse)
b1.pack(expand=True, fill=tk.BOTH)
l1 = tk.Label(f1, text="點擊上方按鈕")
l1.pack(expand=True, fill=tk.BOTH)
window.mainloop()