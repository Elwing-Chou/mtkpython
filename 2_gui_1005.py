import tkinter as tk

def analyse():
    text = t1.get("1.0", "end")
    import jieba.analyse
    keywords = jieba.analyse.extract_tags(text)
    result["text"] = str(keywords)

window = tk.Tk()
window.geometry("500x500+200+200")

# e = 創造元件(父親) -> e.排版()
# 1. 先畫Frame, 再放元件
# 2. 排版(pack[左右上下]/grid[表格]/absolute[絕對])
# 建議pack
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

l1 = tk.Label(f1, text="輸入文章:")
l1.pack(expand=True, fill=tk.BOTH)

t1 = tk.Text(f1)
t1.pack(expand=True, fill=tk.BOTH)

b1 = tk.Button(f1, text="關鍵詞分析", command=analyse)
b1.pack(expand=True, fill=tk.BOTH, pady=10)

result = tk.Label(f1, text="點擊上面分析")
result.pack(expand=True, fill=tk.BOTH)

window.mainloop()