from platform import system
from tkinter import Frame, Tk, Label, Button, TOP, RIGHT, LEFT, Y, Toplevel, W

from _plc_data.plc_ip_select import SelectIP
from _threading.thread_loop import ThreadLoop
from _view.indicator_view import IndicatorSquare
from tartaly_data.tartaly2_data import Tartaly2_Address, Tartaly2_data
from tartaly_data.tartaly2_draw import Tartaly2_View


class Indicators(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.start = IndicatorSquare(self, text='Start [%s]' % Tartaly2_Address.START)
        self.stop = IndicatorSquare(self, text='Stop [%s]' % Tartaly2_Address.STOP)

        self.start.grid(row=1, column=1, sticky=W)
        self.stop.grid(row=2, column=1, sticky=W)


class App(Tk):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        if system() == 'Windows':
            self.resizable(False, False)
            self.geometry("800x480")
        else:
            # noinspection SpellCheckingInspection
            self.attributes("-fullscreen", True)

        self.title('Tartaly data 2')

        self.name_frame = Frame(self)
        self.indicator_frame = Frame(self)
        self.tanks_frame = Frame(self)
        self.connect_frame = Frame(self)

        # noinspection SpellCheckingInspection
        self.name_label = Label(self.name_frame, text='Tartály-1', font=("Arial", 25), wraplength=1)
        # noinspection SpellCheckingInspection
        self.close_button = Button(self.name_frame, text='Bezárás', command=self.close)
        self.indicators = Indicators(self.tanks_frame)
        self.tanks = Tartaly2_View(self.tanks_frame)
        self.connect_label = Label(self.connect_frame, text='--', wraplength=1)

        self.ip_select = SelectIP(self.connect_frame,
                                  default_ip=Tartaly2_Address.DEFAULT_IP,
                                  ip_list=Tartaly2_Address.IP_LIST,
                                  change_process=self.ip_selected)

        self.close_button.pack(side=TOP)
        self.name_label.pack()
        self.indicators.pack(side=RIGHT)
        self.tanks.pack()
        self.ip_select.pack(side=TOP)
        self.connect_label.pack()

        self.name_frame.pack(side=RIGHT, fill=Y)
        self.connect_frame.pack(side=LEFT, fill=Y)
        self.tanks_frame.pack()

        self.plc_data = Tartaly2_data(self.ip_select.ip_address.get())

        self.data_transfer = ThreadLoop(loop=self.data_transfer)
        self.data_transfer.start()

        self.protocol('WM_DELETE_WINDOW', self.close)

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
            self.connect_label.configure(text='PLC-connected', fg='black')
        else:
            self.connect_label.configure(text='PLC-not-connected', fg='red')

        if self.__closed and not self.data_transfer.is_alive():
            self.destroy()

        self.after(100, self.loop)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
