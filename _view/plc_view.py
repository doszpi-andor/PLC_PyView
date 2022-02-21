from platform import system
from tkinter import Tk, Frame, Label, Button, RIGHT, Y, Toplevel, BOTTOM, X

from _config.plc_config_read import PLC_Config
from _plc_data.plc_data import PLC_data, PLC_Address
from _plc_data.plc_ip_select import SelectIP
from _threading.thread_loop import ThreadLoop


# noinspection PyPep8Naming
class PLC_View(Tk):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        try:
            self.plc_ip_list, self.plc_rack, self.plc_slot = PLC_Config.read_plc_config('_config/config.xml')
            self.plc_default_ip = PLC_Config.read_plc_default_ip('_config/default.xml')
        except FileNotFoundError:
            self.plc_ip_list = ['']
            self.plc_rack = 0
            self.plc_slot = 0
            self.plc_default_ip = ''

        if system() == 'Windows':
            self.resizable(False, False)
            self.geometry("800x480")
        else:
            # noinspection SpellCheckingInspection
            self.attributes("-fullscreen", True)

        self.title('PLC View')

        self.name_frame = Frame(self)
        self.process_frame = Frame(self)
        self.connect_frame = Frame(self)

        # noinspection SpellCheckingInspection
        self.name_label = Label(self.name_frame, text='PLC View', font=("Arial", 16))
        # noinspection SpellCheckingInspection
        self.close_button = Button(self.name_frame, text='Bezárás', command=self.close)

        self.close_button.pack(side=RIGHT)
        self.name_label.pack()

        self.connect_label = Label(self.connect_frame, text='--')
        self.ip_select = SelectIP(self.connect_frame,
                                  default_ip=self.plc_default_ip,
                                  ip_list=self.plc_ip_list,
                                  change_process=self.ip_selected)

        self.ip_select.pack()
        self.connect_label.pack()

        self.name_frame.pack(fill=X)
        # self.process_frame.pack()
        self.connect_frame.pack(side=BOTTOM, fill=Y)
        self.process_frame.pack()

        self.plc_data = PLC_data(PLC_Address(), self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.data_transfer = ThreadLoop(loop=self.data_transfer)
        self.data_transfer.start()

        self.protocol('WM_DELETE_WINDOW', self.close)

    # noinspection PyUnusedLocal
    def ip_selected(self, *args):
        self.plc_data.reconnect(self.ip_select.ip_address.get())

    def close(self):
        toplevel = Toplevel(self, bg='red')
        Label(toplevel, text='Close connection!').pack(padx=10, pady=10)
        toplevel.overrideredirect(True)
        toplevel_width = 140
        toplevel_height = 40
        toplevel.geometry('%sx%s+%s+%s' % (toplevel_width,
                                           toplevel_height,
                                           (self.winfo_rootx() + self.winfo_width() // 2) - toplevel_width // 2,
                                           (self.winfo_y() + self.winfo_height() // 2) - toplevel_height // 2))
        toplevel.grab_set()
        self.data_transfer.stop()
        self.__closed = True

    def destroy(self):
        self.data_transfer.stop()
        self.data_transfer.join()
        super().destroy()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        if self.plc_data.connected:
            self.connect_label.configure(text='PLC connected', fg='black')
        else:
            self.connect_label.configure(text='PLC not connected', fg='red')

        if self.__closed and not self.data_transfer.is_alive():
            self.destroy()

        self.after(100, self.loop)


if __name__ == '__main__':
    app = PLC_View()

    app.after(100, app.loop)

    app.mainloop()
