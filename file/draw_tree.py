import os.path
import sys
from bigtree import Node, print_tree
# bigtree docs : https://bigtree.readthedocs.io/en/latest/index.html

from file_manager import *


def dict_to_text(d1, path):
    root = Node("Root")

    # dict to node (only 1 depth)
    for key, values in d1.items():
        key_node = Node(key, parent=root)
        # key_node = Node(key, parent=root, eventId=key)
        for value in values:
            Node(value, parent=key_node)
            # Node(value, parent=key_node, vId=value)

    # open sydout to write file
    sys.stdout = open(path, 'w', encoding='utf-8')

    # print_tree(root)
    print_tree(root, attr_list=["eventId", "vId"])

    # recover stdout
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    d1 = {'101': ['1', '2'], '200': ['100', '200', '300'], '1000': ['1', '50', '66']}
    save_path = os.path.join(FileManager.project_home_path, 'test.txt')

    # convert dict to tree & write text file
    dict_to_text(d1, save_path)

    # open text file
    file_manager = FileManager()
    file_manager.open_text_file(save_path)
