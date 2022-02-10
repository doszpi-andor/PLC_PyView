from tkinter import Frame, StringVar, OptionMenu


class SelectIP(Frame):

    def __init__(self, master=None, default_ip='172.0.0.1', ip_list=None, change_process=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if ip_list is None:
            ip_list = [default_ip]

        self.ip_address = StringVar()
        self.ip_address.set(default_ip)
        self.ip_list = ip_list
        self.ip_menu = OptionMenu(self, self.ip_address, *self.ip_list, command=change_process)
        self.ip_menu.pack()
