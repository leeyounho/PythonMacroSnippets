from tkinter import *


class SplunkDownload(object):
    # reader file information
    config_file_name = 'config/config.ini'
    splunk_section_name = 'splunk_section'

    # reader file keys & values
    splunk_id = 'splunk_id'
    splunk_password = 'splunk_password'
    eqp_id = 'EQP_ID'
    query = 'query'
    headless = 'headless'

    def __init__(self):
        # UI
        window = Tk()
        window.title("get_eqp_log_from_splunk")

        # row1 splunk_id
        self.lbl1 = Label(window, text="Splunk ID")
        self.lbl1.grid(column=0, row=0)

        self.txt1 = Entry(window, width=15)
        self.txt1.insert(END, config_read(self.config_file_name, self.splunk_section_name, self.splunk_id))
        self.txt1.grid(column=1, row=0)

        # row2 splunk_password
        self.lbl2 = Label(window, text="Splunk Password")
        self.lbl2.grid(column=0, row=1)

        self.txt2 = Entry(window, show="*", width=15)
        self.txt2.insert(END, config_read(self.config_file_name, self.splunk_section_name, self.splunk_password))
        self.txt2.grid(column=1, row=1)

        # row3 eqp_id
        self.lbl3 = Label(window, text="Equipment ID")
        self.lbl3.grid(column=0, row=2)

        self.txt3 = Entry(window, width=15)
        self.txt3.insert(END, config_read(self.config_file_name, self.splunk_section_name, self.eqp_id))
        self.txt3.grid(column=1, row=2)

        # row4 headless option
        self.lbl3 = Label(window, text="headless")
        self.lbl3.grid(column=0, row=4)

        self.cb1_var = IntVar()
        headless_string = config_read(self.config_file_name, self.splunk_section_name, self.headless)
        self.cb1_var.set(0 if (headless_string == "" or headless_string == '0') else 1)
        self.cb1 = Checkbutton(window, variable=self.cb1_var, onvalue=1, offvalue=0)
        self.cb1.grid(column=1, row=4)

        # row5 query
        self.lbl4 = Label(window, text="query")
        self.lbl4.grid(column=0, row=5)

        self.txt4 = Text(window, width=50, height=3)
        self.txt4.insert(END, config_read(self.config_file_name, self.splunk_section_name, self.query))
        self.txt4.bind('<Return>', self.parse)
        self.txt4.grid(column=1, row=5)

        # last row buttons
        self.btn1 = Button(window, text="Get Eqp Log From Splunk", command=self.button_clicked, bg='#54FA9B',
                           activebackground='#54FA9B')
        self.btn1.grid(column=0, row=6, columnspan=2, sticky=W + E)

        window.mainloop()

    def button_clicked(self):
        config_write(self.config_file_name, self.splunk_section_name, self.splunk_id, self.txt1.get())
        config_write(self.config_file_name, self.splunk_section_name, self.splunk_password, self.txt2.get())
        config_write(self.config_file_name, self.splunk_section_name, self.eqp_id, self.txt3.get())
        config_write(self.config_file_name, self.splunk_section_name, self.headless, str(self.cb1_var.get()))
        config_write(self.config_file_name, self.splunk_section_name, self.query,
                     self.txt4.get(1.0, END).strip())  # text widget always has new line. so need to strip it.

        print('button clicked')

    def parse(self, event):
        print("prevent inserting line break in text widget")
        return 'break'


if __name__ == '__main__':
    SplunkDownload()
