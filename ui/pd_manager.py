import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd


root = tk.Tk()
root.geometry('1600x900+10+10')
root.title('Workshop Manager')

class TestApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                           'num_wings': [2, 'dfgfdghdfhsdfhsdfgsdfgsdfgksjldfhgslkjer5hgljekrgjlsergsergsregsreg', 0,
                                         0],
                           'num_specimen_seen': ['788\njkgukg\nhhjhjjh\n', 2, 1, 8]},
                          index=['falcon', 'dog', 'spider', 'fish'])
        self.table = Table(self, dataframe=df, showtoolbar=True, showstatusbar=True)
        self.table.autoresizecols=False
        self.table.show()


app = TestApp(root)
app.pack(fill=tk.BOTH, expand=1)

root.mainloop()