import os
from os.path import dirname
import subprocess
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

import numpy as np


class FileManager:
    project_home_path = dirname(dirname(__file__))  # file package 위치가 변경되면 같이 변경되야 하는 code

    def get_file_list(self, path):
        return os.listdir(path)

    def change_directory(self, path):
        os.chdir(path)

    def save_dataframe_to_file(self, df, filename, extension):
        if df.empty:
            print('Dataframe is empty')
            return
        save_file_name = asksaveasfilename(initialfile=filename + extension, defaultextension=extension,
                                           filetypes=[("All Files", "*.*"), ("SQL Files", "*" + extension)])
        np.savetxt(save_file_name, df.dropna().values, fmt="%s", newline='\n\n')

    def save_dataframe_to_file_column_by_column(self, df, filename, extension):
        if df.empty:
            print('Dataframe is empty')
            return
        save_file_path = asksaveasfilename(initialfile=filename + extension, defaultextension=extension,
                                           filetypes=[("All Files", "*.*"), ("SQL Files", "*" + extension)])
        save_file_name = save_file_path.split('/')[-1]
        for idx, column in enumerate(df, 1):
            np.savetxt(f'{idx:02d}' + '_' + save_file_name + extension, df[column].dropna().values, fmt="%s",
                       newline='\n\n')

    def open_text_file(self, path):
        subprocess.Popen(path, shell=True)


    def ask_open_file_name(self):
        return filedialog.askopenfilename(initialdir="/", filetypes=(("xlsx files", "*.xlsx"),
                                          ("all files", "*.*")), defaultextension="*.*")

    def ask_save_file_name(self):
        # initialdir = 바탕화면
        return filedialog.asksaveasfilename(initialdir=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') , filetypes=(("xlsx files", "*.xlsx"),
                                          ("all files", "*.*")), defaultextension="*.*")

    def ask_directory(self):
        return filedialog.askdirectory()


if __name__ == '__main__':
    file_manager = FileManager()
    # print(file_manager.get_file_list('.'))
    print(file_manager.ask_save_file_name())
