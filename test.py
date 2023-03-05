import tkinter as tk

class SelectDatabaseApp:
    def __init__(self, root):
        root.title("Select Database to Query")

        # Create two checkbox lists with a for loop
        for i in range(3):
            frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
            frame.grid(row=0, column=i)

            select_all_var = tk.BooleanVar()
            select_all_var.set(False)

            checkboxes = []
            for j in range(3):
                checkbox_var = tk.BooleanVar()
                checkbox = tk.Checkbutton(frame, text=f"Checkbox {j + 1}", variable=checkbox_var,
                                          command=self.toggle_select_all)
                checkbox.grid(row=j + 1, column=0, sticky=tk.W)
                checkboxes.append(checkbox_var)

            select_all_checkbox = tk.Checkbutton(frame, text="Select All", variable=select_all_var,
                                                 command=lambda checkboxes=checkboxes: self.toggle_all(checkboxes,
                                                                                                       select_all_var))
            select_all_checkbox.grid(row=0, column=0, sticky=tk.W)

            # Save references to the select all checkbox and checkbox variables for each checkbox list
            if i == 0:
                self.select_all_checkbox1 = select_all_checkbox
                self.checkbox_vars1 = checkboxes
            else:
                self.select_all_checkbox2 = select_all_checkbox
                self.checkbox_vars2 = checkboxes

        button = tk.Button(root, text='Go!', command=self.__select_database)
        button.grid(row=1, column=0, sticky='nesw', columnspan=3)

    def __select_database(self):
        print('selected')

    def toggle_all(self, checkboxes, select_all_var):
        all_checked = select_all_var.get()
        for var in checkboxes:
            var.set(all_checked)

    def toggle_select_all(self):
        if all(var.get() for var in self.checkbox_vars1):
            self.select_all_checkbox1.select()
        else:
            self.select_all_checkbox1.deselect()
        if all(var.get() for var in self.checkbox_vars2):
            self.select_all_checkbox2.select()
        else:
            self.select_all_checkbox2.deselect()

    def get_selected1(self):
        selected = []
        for i, var in enumerate(self.checkbox_vars1):
            if var.get():
                selected.append(f"Checkbox {i + 1}")
        return selected

    def get_selected2(self):
        selected = []
        for i, var in enumerate(self.checkbox_vars2):
            if var.get():
                selected.append(f"Checkbox {i + 4}")
        return selected


root = tk.Tk()
SelectDatabaseApp(root)
root.mainloop()
