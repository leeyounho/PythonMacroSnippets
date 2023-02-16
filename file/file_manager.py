import os


class FileManager:
    def __init__(self):
        print(os.getcwd())

    def get_file_list(self, path):
        return os.listdir(path)

    def change_directory(self, path):
        os.chdir(path)


if __name__ == '__main__':
    file_manager = FileManager()
    print(file_manager.get_file_list('.'))
