import tkinter as tk

# e = 元件(父元件)
# e.排版() pack(上下左右) grid(表格) absolute(絕對)

window = tk.Tk()
window.geometry("500x500+100+100")
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
# 標籤: Label
l1 = tk.Label(f1, text="請輸入文章")
l1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
# 多行輸入: Text 單行輸入: Entry
t1 = tk.Text(f1)
t1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
b1 = tk.Button(f1, text="分析")
# tk.X/tk.Y
b1.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
result = tk.Label(f1, text="點按鈕分析...")
result.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)

window.mainloop()
