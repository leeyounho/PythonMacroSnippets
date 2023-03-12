import tkinter as tk


class UserInput:
    def __init__(self, parent, title="User Input", label_text="Enter input:", button_text="Submit"):
        self.parent = parent
        self.parent.title(title)

        self.label = tk.Label(self.parent, text=label_text)
        self.label.pack()

        self.entry = tk.Entry(self.parent)
        self.entry.pack()

        self.button = tk.Button(self.parent, text=button_text, command=self.submit)
        self.button.pack()

        self.user_input = None

    def submit(self):
        self.user_input = self.entry.get()
        self.parent.destroy()

    def get_input(self):
        self.parent.mainloop()
        return self.user_input

    def show(self):
        self.parent.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    user_input_window = UserInput(root)
    user_input_window.show()

    print(user_input_window.user_input)
