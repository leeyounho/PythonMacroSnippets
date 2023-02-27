# TODO
# ui package 에는 tkinter sample 만들고
# dataframe_manager는 dataframe wrapper 만들고
# disc package에는 discord bot 만들고
# oracle_manager 에는 oracle 접속 wrapper 만들고

import tkinter as tk
from tkinter import ttk

# Create a new instance of Tkinter
root = tk.Tk()

# Set the window title
root.title("My Tkinter App")

# Set the window size
root.geometry("400x300")

# Set the style to a modern theme
style = ttk.Style()
style.theme_use("clam")

# Create a label widget and add it to the window
label = ttk.Label(root, text="Hello, Tkinter!", font=("Segoe UI", 16))
label.pack(pady=20)

# Create a button widget and add it to the window
button = ttk.Button(root, text="Click me!", style=style)
button.pack()

# Define a function to handle button click events
def on_button_click():
    label.config(text="Button clicked!", foreground="green")

# Bind the button click event to the function
button.config(command=on_button_click)

# Run the Tkinter event loop
root.mainloop()