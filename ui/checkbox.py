import tkinter as tk


class SelectTargetDatabaseApp:
    select_all_boolean_list = []
    select_all_checkbutton_list = []

    database_boolean_list = []
    database_checkbutton_list = []
    checked_list = []

    def __init__(self, root, config_list):  # config_list 는 DR/운영1/운영2/재연 db list가 들어가 있으니 2d list임
        root.title("Select Target DB")

        for i in range(len(config_list)):
            self.database_boolean_list.append([])
            # create
            frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
            frame.grid(row=0, column=i)

            self.select_all_boolean_list.append(tk.BooleanVar())
            self.select_all_checkbutton_list.append(
                tk.Checkbutton(frame, text=f"Select All {i}", variable=self.select_all_boolean_list[i],
                               command=lambda a=i: self.__toggle_all(a)))
            self.select_all_checkbutton_list[i].grid(row=0, column=0, sticky=tk.W)

            self.database_boolean_list.append([])
            self.database_checkbutton_list.append([])
            for j in range(3):
                self.database_boolean_list[i].append(tk.BooleanVar())
                self.database_checkbutton_list[i].append(
                    tk.Checkbutton(frame, text=f"Database {j + 1}", variable=self.database_boolean_list[i][j]))
                self.database_checkbutton_list[i][j].grid(row=j + 1, column=0, sticky=tk.W, padx=10)

        button = tk.Button(root, text='Go!', command=self.__select_database)
        button.grid(row=1, column=0, sticky='nesw', columnspan=3)

    def __select_database(self):
        print('selected')

    def __toggle_all(self, i):
        if self.select_all_boolean_list[i].get():
            for checkbox in self.database_checkbutton_list[i]:
                checkbox.select()
        else:
            for checkbox in self.database_checkbutton_list[i]:
                checkbox.deselect()

    # def get_selected(self):
    #     selected = []
    #     for i, var in enumerate(self.checkbox_vars1):
    #         if var.get():
    #             selected.append(f"Checkbox {i + 1}")
    #     return selected


if __name__ == '__main__':
    temp_list = ['A', 'sdf']
    root = tk.Tk()
    SelectTargetDatabaseApp(root, temp_list)
    root.mainloop()
