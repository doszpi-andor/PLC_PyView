from tkinter import Frame, StringVar, OptionMenu


class SelectIP(Frame):

    def __init__(self, master=None, change_process=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.ip_address = StringVar()
        self.ip_address.set('172.17.1.1')
        self.ip_list = ['172.17.1.1', '172.17.1.2', '172.17.1.3',
                        '172.17.1.4', '172.17.1.5', '172.17.1.6', '172.17.1.6']
        self.ip_menu = OptionMenu(self, self.ip_address, *self.ip_list, command=change_process)
        self.ip_menu.pack()
