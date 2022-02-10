from platform import system
from tkinter import Frame, Tk, Label, W, Button, RIGHT, X, LEFT, BOTTOM, Y, Toplevel, StringVar, OptionMenu

from _plc_data.plc_ip_select import SelectIP
from _threading.thread_loop import ThreadLoop
from _view.conveyor_view import ConveyorView
from _view.indicator_view import IndicatorSquare, IndicatorOval
from szalag_data.szalag1v0_data import Szalag1v0_Address, Szalag1v0_data


class Conveyors(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.conveyor1 = ConveyorView(self, conv_number=1, motor_number=1)
        self.conveyor2 = ConveyorView(self, conv_number=2, motor_number=2, shift_x=200)
        self.conveyor1.grid(row=1, column=1, sticky='W')
        self.conveyor2.grid(row=2, column=1, columnspan=2)


class IndicatorsButton(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.start = IndicatorSquare(self, text='Start [%s]' % Szalag1v0_Address.START)
        self.stop = IndicatorSquare(self, text='Stop [%s]' % Szalag1v0_Address.STOP)
        # noinspection SpellCheckingInspection
        self.nyugta = IndicatorSquare(self, text='Nyugta [%s]' % Szalag1v0_Address.NYUGTA)
        self.start.grid(row=1, column=1, sticky=W)
        self.stop.grid(row=2, column=1, sticky=W)
        self.nyugta.grid(row=1, column=2, rowspan=2, sticky=W)


class IndicatorsLamp(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        # noinspection SpellCheckingInspection
        self.uzem = IndicatorOval(self, text='Üzem [%s]' % Szalag1v0_Address.UZEM)
        self.hiba1 = IndicatorOval(self, text='Hiba 1 [%s]' % Szalag1v0_Address.HIBA1)
        self.hiba2 = IndicatorOval(self, text='Hiba 2 [%s]' % Szalag1v0_Address.HIBA2)
        self.uzem.grid(row=1, column=1, sticky=W)
        self.hiba1.grid(row=1, column=2, sticky=W)
        self.hiba2.grid(row=2, column=2, sticky=W)


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

        # noinspection SpellCheckingInspection
        self.title('Szalag 1v0')

        self.name_frame = Frame()
        self.indicator_frame = Frame()
        self.conveyor_frame = Frame()
        self.connect_frame = Frame()

        # noinspection SpellCheckingInspection
        self.name_label = Label(self.name_frame, text='Szalag 1v0', font=("Arial", 25))
        # noinspection SpellCheckingInspection
        self.close_button = Button(self.name_frame, text='Bezárás', command=self.close)
        self.indicators_button = IndicatorsButton(self.indicator_frame)
        self.indicators_lamp = IndicatorsLamp(self.indicator_frame)
        self.conveyors = Conveyors(self.conveyor_frame)
        self.connect_label = Label(self.connect_frame, text='--')

        self.ip_select = SelectIP(self.connect_frame)

        self.close_button.pack(side=RIGHT)
        self.name_label.pack()
        self.indicators_button.pack(side=LEFT)
        self.indicators_lamp.pack(side=RIGHT)
        self.conveyors.pack()
        self.ip_select.pack()
        self.connect_label.pack()

        self.name_frame.pack(fill=X)
        self.indicator_frame.pack(fill=X)
        self.conveyor_frame.pack(pady=50)
        self.connect_frame.pack(side=BOTTOM, fill=Y)

        self.plc_data = Szalag1v0_data(self.ip_select.ip_address.get())

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
            self.connect_label.configure(text='PLC connected', fg='black')
        else:
            self.connect_label.configure(text='PLC not connected', fg='red')

        if self.plc_data.s1_is_changed():
            self.s1_refresh()

        if self.plc_data.s2_is_changed():
            self.s2_refresh()

        if self.plc_data.start_is_changed():
            self.start_refresh()

        if self.plc_data.stop_is_changed():
            self.stop_refresh()

        if self.plc_data.nyugta_is_changed():
            self.nyugta_refresh()

        if self.plc_data.m1_is_change():
            self.m1_refresh()
            self.s1_refresh()

        if self.plc_data.m2_is_change():
            self.m2_refresh()
            self.s2_refresh()

        if self.plc_data.uzem_is_change():
            self.uzem_refresh()

        if self.plc_data.hiba1_is_change():
            self.hiba1_refresh()

        if self.plc_data.hiba2_is_change():
            self.hiba2_refresh()

        if self.__closed and not self.data_transfer.is_alive():
            self.destroy()

        self.after(100, self.loop)

    def s1_refresh(self):
        if self.plc_data.s1 and self.plc_data.m1:
            self.conveyors.conveyor1.change_indicator_color('green')
        elif self.plc_data.s1 and not self.plc_data.m1:
            self.conveyors.conveyor1.change_indicator_color('yellow')
        elif not self.plc_data.s1 and self.plc_data.m1:
            self.conveyors.conveyor1.change_indicator_color('red')
        else:
            self.conveyors.conveyor1.change_indicator_color('gray')

    def s2_refresh(self):
        if self.plc_data.s2 and self.plc_data.m2:
            self.conveyors.conveyor2.change_indicator_color('green')
        elif self.plc_data.s2 and not self.plc_data.m2:
            self.conveyors.conveyor2.change_indicator_color('yellow')
        elif not self.plc_data.s2 and self.plc_data.m2:
            self.conveyors.conveyor2.change_indicator_color('red')
        else:
            self.conveyors.conveyor2.change_indicator_color('gray')

    def start_refresh(self):
        if self.plc_data.start:
            self.indicators_button.start.change_color('green')
        else:
            self.indicators_button.start.change_color('gray')

    def stop_refresh(self):
        if self.plc_data.stop:
            self.indicators_button.stop.change_color('red')
        else:
            self.indicators_button.stop.change_color('gray')

    # noinspection SpellCheckingInspection
    def nyugta_refresh(self):
        if self.plc_data.nyugta:
            self.indicators_button.nyugta.change_color('yellow')
        else:
            self.indicators_button.nyugta.change_color('gray')

    def m1_refresh(self):
        if self.plc_data.m1:
            self.conveyors.conveyor1.change_motor_color('green')
        else:
            self.conveyors.conveyor1.change_motor_color('gray')

    def m2_refresh(self):
        if self.plc_data.m2:
            self.conveyors.conveyor2.change_motor_color('green')
        else:
            self.conveyors.conveyor2.change_motor_color('gray')

    def uzem_refresh(self):
        if self.plc_data.uzem:
            self.indicators_lamp.uzem.change_color('green')
        else:
            self.indicators_lamp.uzem.change_color('gray')

    def hiba1_refresh(self):
        if self.plc_data.hiba1:
            self.indicators_lamp.hiba1.change_color('red')
        else:
            self.indicators_lamp.hiba1.change_color('gray')

    def hiba2_refresh(self):
        if self.plc_data.hiba2:
            self.indicators_lamp.hiba2.change_color('red')
        else:
            self.indicators_lamp.hiba2.change_color('gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
