import tkinter as tk
import jieba.analyse

def analyze():
    global e1, l1
    news = e1.get("1.0", "end")
    keywords = jieba.analyse.extract_tags(news)
    l1["text"] = str(keywords)

window = tk.Tk()
window.geometry("500x500+200+200")

# Step1. 創造元件(老爸) Step2. 排版(grid[表格], pack[上下左右])
# 元件在創立前, 先創立tk.mainloop()Frame
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

e1 = tk.Text(f1, height=10)
e1.pack(expand=True, fill=tk.BOTH)

b1 = tk.Button(f1, text="請點我", command=analyze)
b1.pack(expand=True, fill=tk.BOTH)

l1 = tk.Label(f1, text="分析結果!!!")
l1.pack(expand=True, fill=tk.BOTH)

tk.mainloop()