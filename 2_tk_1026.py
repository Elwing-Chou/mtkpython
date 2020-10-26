import tkinter as tk

window = tk.Tk()
window.geometry("500x500+300+300")
# 元件(parent) 元件.排版(pack)
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
t1 = tk.Text(f1)
t1.pack(expand=True, fill=tk.BOTH)
b1 = tk.Button(f1, text="請按我")
b1.pack(expand=True, fill=tk.BOTH)
l1 = tk.Label(f1, text="按上面顯示結果")
l1.pack(expand=True, fill=tk.BOTH)
window.mainloop()