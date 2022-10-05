import tkinter as tk

window = tk.Tk()
window.geometry("500x500+200+200")

# e = 創造元件(父親) -> e.排版()
# 1. 先畫Frame, 再放元件
# 2. 排版(pack[左右上下]/grid[表格]/absolute[絕對])
# 建議pack
f1 = tk.Frame(window)
f1.pack()

l1 = tk.Label(f1, text="輸入文章:")
l1.pack()

window.mainloop()