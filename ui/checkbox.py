import tkinter as tk


class SelectTargetDatabaseApp:
    select_all_boolean_list = []
    select_all_checkbutton_list = []

    database_boolean_list = []
    database_checkbutton_list = []
    checked_list = []

    change_button_usage = False
    mark_only_one_flag = False

    def __init__(self, root, config_list, mark_only_one_flag=False,
                 change_button_usage=False):  # config_list 는 DR/운영1/운영2/재연 db list가 들어가 있으니 2d list임
        root.title("Select Target DB")
        self.change_button_usage = change_button_usage
        self.mark_only_one_flag = mark_only_one_flag

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
                    tk.Checkbutton(frame, text=f"Database {j + 1}", variable=self.database_boolean_list[i][j],
                                   command=lambda a=i, b=j: self.__toggle(a, b)))
                self.database_checkbutton_list[i][j].grid(row=j + 1, column=0, sticky=tk.W, padx=10)

        button = tk.Button(root, text='Go!', command=self.__select_database)
        button.grid(row=1, column=0, sticky='nesw', columnspan=3)

        if mark_only_one_flag:
            for i, k in enumerate(self.select_all_checkbutton_list):
                self.select_all_checkbutton_list[i].config(state=tk.DISABLED)

    def __toggle(self, i, j):
        # mark_only_one flag 가 있으면 checkbox는 1개만 선택됨.
        if self.mark_only_one_flag:
            for a, k in enumerate(self.database_checkbutton_list):
                for b, v in enumerate(self.database_checkbutton_list[a]):
                    if a != i or b != j:
                        self.database_checkbutton_list[a][b].deselect()

    def __select_database(self):
        # 선택된 checkbox list를 전달함
        ret = []
        for i, k in enumerate(self.database_checkbutton_list):
            for j, v in enumerate(self.database_checkbutton_list[i]):
                checked_state = self.database_boolean_list[i][j].get()
                checkbutton = self.database_checkbutton_list[i][j]
                if checked_state:
                    ret.append(checkbutton)
                    print(checkbutton['text'])

        if self.change_button_usage:
            self.mark_only_one_flag = True

            for i, k in enumerate(self.select_all_checkbutton_list):
                self.select_all_checkbutton_list[i].config(state=tk.DISABLED)

        return ret

    def __toggle_all(self, i):
        if self.select_all_boolean_list[i].get():
            for checkbox in self.database_checkbutton_list[i]:
                checkbox.select()
        else:
            for checkbox in self.database_checkbutton_list[i]:
                checkbox.deselect()


if __name__ == '__main__':
    temp_list = ['A', 'sdf']
    root = tk.Tk()
    SelectTargetDatabaseApp(root, temp_list, mark_only_one_flag=True)
    root.mainloop()
