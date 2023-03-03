import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd


root = tk.Tk()
root.geometry('1600x900+10+10')
root.title('Workshop Manager')

class TestApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        df = pd.DataFrame({'target_database': ['S3', '17', 'P1', 'U1'],
                           'value1': ['fdgdfg', 'dfgfdghdfhsdfhsdfgsdfgsdfgksjldfhgslkjer5hgljekrgjlsergsergsregsreg', 0, 0],
                           'value2': ['788\njkgukg\nhhjhjjh\n', 'fdgdfg', 1, 0]},
                          index=['falcon', 'dog', 'spider', 'fish'])
        self.table = Table(self, dataframe=df, showtoolbar=True, showstatusbar=True)
        self.table.autoresizecols=False
        self.table.show()


app = TestApp(root)
app.pack(fill=tk.BOTH, expand=1)

root.mainloop()