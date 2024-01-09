import tkinter as tk
import main
from functools import partial
import pandas as pd


def on_button_click(func, *args):
    func(*args)


if __name__ == "__main__":
    # 假设你已经有了 df1 和 merged_df
    file_path = '日化.xlsx'
    df1 = pd.read_excel(file_path, sheet_name=0)
    df2 = pd.read_excel(file_path, sheet_name=1)
    merged_df = pd.merge(df1, df2, on='商品编号', how='inner')
    root = tk.Tk()
    root.title("绘图函数选择界面")
    functions = [main.draw1, main.draw2, main.draw3, main.draw4, main.draw5, main.draw6, main.draw7, main.draw8]
    for i, func in enumerate(functions, start=1):
        button = tk.Button(root, text=f"绘图函数{i}", command=partial(on_button_click, func, merged_df))
        button.pack(pady=10)

    # 运行主循环
    root.mainloop()
