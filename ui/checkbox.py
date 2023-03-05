import tkinter.ttk as Tix
import tkinter as tk


class View(object):
    def __init__(self, root):
        self.root = root
        self.makeCheckList()

    def makeCheckList(self):
        # self.cl = Tix.CheckList(self.root, command=self.select_child, browsecmd=self.select_child)
        self.cl = tk.CheckList(self.root, command=self.select_children, browsecmd=self.select_children)
        self.cl.pack(expand=1, fill='both')
        self.cl.hlist.add("C", text="Top")
        # self.cl.hlist.bind("<Button-1>", self.select)

        self.cl.hlist.add("C.CL1", text="Computer Science")
        self.cl.hlist.add("C.CL1.Item1", text="Algorithm")
        self.cl.hlist.add("C.CL1.Item2", text="Data Structures")
        self.cl.hlist.add("C.CL1.Item2.Item3", text="python")

        self.cl.hlist.add("C.CL2", text="Gate Paper")
        self.cl.hlist.add("C.CL2.Item1", text="2018 paper")
        self.cl.hlist.add("C.CL2.Item2", text="2019 paper")

        self.cl.hlist.add("C.CL3", text="Programming language")
        self.cl.hlist.add("C.CL3.Item1", text="Python")
        self.cl.hlist.add("C.CL3.Item2", text="java")

        self.cl.setstatus("C", "off")
        self.cl.setstatus("C.CL1", "off")
        self.cl.setstatus("C.CL1.Item1", "off")
        self.cl.setstatus("C.CL1.Item2", "off")
        self.cl.setstatus("C.CL1.Item2.Item3", "off")

        self.cl.setstatus("C.CL2", "off")
        self.cl.setstatus("C.CL2.Item1", "off")
        self.cl.setstatus("C.CL2.Item2", "off")

        self.cl.setstatus("C.CL3", "off")
        self.cl.setstatus("C.CL3.Item1", "off")
        self.cl.setstatus("C.CL3.Item2", "off")
        self.cl.autosetmode()

    def select_children(self, item):  # selects all the children

        children = self.cl.hlist.info_children(item)
        status = self.cl.getstatus(item)

        for child in children:
            self.cl.setstatus(child, status)
            grand_child = self.cl.hlist.info_children(child)
            while grand_child:
                for x in grand_child:
                    self.cl.setstatus(x, status)
                    grand_child = self.cl.hlist.info_children(x)

    def select_child(self, item):  # selects only the first level children
        children = self.cl.hlist.info_children(item)
        status = self.cl.getstatus(item)

        for child in children:
            self.cl.setstatus(child, status)


def main():
    root = tk.Tk()
    view = View(root)
    root.update()
    root.mainloop()


if __name__ == '__main__':
    main()
