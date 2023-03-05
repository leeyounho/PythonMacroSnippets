import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd

from util.dataframe_manager import DataFrameManager

dfm = DataFrameManager()
df1 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": ["apple\nfggffg\nfgfgdzdsf\n", "berry", "grapes"],
    "C": ["red", "blue", "green"]
},
    columns=["A", "B", "C"])

df2 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": ["apple", "berry", "banana"],
    "C": ["green", "blue", "green"]
},
    columns=["A", "B", "C"])

print(df1)
print()

print(df2)
print()

df_diff = dfm.df_compare_to_diff_df(df1, df2, None)
print(df_diff)
print()
print(df_diff.style.highlight_null())
print(df_diff)


root = tk.Tk()
root.geometry('1600x900+10+10')
root.title('Workshop Manager')

class TestApp(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent)
        self.table = Table(self, dataframe=df, showtoolbar=True, showstatusbar=True)
        self.table.autoresizecols=False
        self.table.show()


app = TestApp(root, df_diff)
app.pack(fill=tk.BOTH, expand=1)



root.mainloop()

print()
