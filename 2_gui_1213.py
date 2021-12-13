import tkinter as tk
import jieba.analyse

def analyse():
    global t1, result
    t = t1.get("1.0", "end")
    tags = jieba.analyse.extract_tags(t, topK=5)
    result["text"] = str(tags)

# 變數名稱 = 創造元件(父親)
# 變數.排版 (pack/grid/...)
window = tk.Tk()
window.geometry("500x500+250+250")
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
l1 = tk.Label(f1, text="輸入文章")
l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# single:Entry multi:Text
t1 = tk.Text(f1, height=10)
t1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
b1 = tk.Button(f1, text="分析", command=analyse)
b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
result = tk.Label(f1, text="結果")
result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
window.mainloop()