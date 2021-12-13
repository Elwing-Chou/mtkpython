import tkinter as tk

# 變數名稱 = 創造元件(父親)
# 變數.排版 (pack/grid/...)
window = tk.Tk()
window.geometry("500x500+250+250")
f1 = tk.Frame(window, padx=20, pady=20)
f1.pack(expand=True, fill=tk.BOTH)
l1 = tk.Label(f1, text="輸入文章")
l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# single:Entry multi:Text
t1 = tk.Text(f1)
t1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
b1 = tk.Button(f1, text="分析")
b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
result = tk.Label(f1, text="結果")
result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
window.mainloop()