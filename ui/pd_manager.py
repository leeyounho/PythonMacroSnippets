import tkinter as tk
import tkinter.ttk
from pandastable import Table, TableModel
import pandas as pd

# pandas table
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

window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

notebook = tkinter.ttk.Notebook(window, width=300, height=300)
notebook.pack()

frame1 = tk.Frame(window)
temp = notebook.add(frame1, text="페이지1")

label1 = tk.Label(frame1, text="페이지1의 내용")
label1.pack()
#
frame2 = tk.Frame(window)
notebook.add(frame2, text="페이지2")
#
label2 = tkinter.Label(frame2, text="페이지2의 내용")
label2.pack()
#
frame3 = tk.Frame(window)
notebook.add(frame3, text="페이지3")


table = Table(frame3, dataframe=df1, showtoolbar=True, showstatusbar=True)
table.autoresizecols = False
table.show()

def on_tab_change(event):
  tab = event.widget.tab('current')['text']
  if tab == '페이지3':
      print('show 페이지3')
      # table.show()
      # table.close()
  else:
      print('close 페이지3')



notebook.bind('<<NotebookTabChanged>>', on_tab_change)


window.mainloop()
