import tkinter as tk

window = tk.Tk()
window.geometry("500x500+200+200")
# 創造元件(老爸)
# 元件.排版(pack/grid/absolute)
# 容器(Frame)
f1 = tk.Frame(window)
# tk.BOTH, tk.X, tk.Y
f1.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)
l1 = tk.Label(f1, text="給我一篇文章")
l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# Entry:single line Text: multi line
t1 = tk.Text(f1, height=10)
t1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
b1 = tk.Button(f1, text="分析")
b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
result = tk.Label(f1, text="點擊按鈕分析")
result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
window.mainloop()