row_list = []
columns = ('Index', 'DrugsName', 'NumberWasted', 'MoneyWasted', 'Date')

for child in treeview.get_children():
    row_list.append(treeview.item(child)["values"])

"""
The line below should also be removed from the for loop 
because you are re initializing the data frame 
on every iteration of the loop. """

treeview_df = pd.DataFrame(row_list, columns=columns)

print(treeview_df)  # Notice here the difference in indention level of this print statement