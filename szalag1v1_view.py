
from tkinter import Frame, W, RIGHT, LEFT, X

from _view.conveyor_view import ConveyorView
from _view.indicator_view import IndicatorSquare, IndicatorOval
from _view.plc_view import PLC_View
from szalag_data.szalag1v1_data import Szalag1v1_data, Szalag1v1_Address


class Conveyors(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.conveyor1 = ConveyorView(self, conv_number=1, motor_number=1, length=340)
        self.conveyor2 = ConveyorView(self, conv_number=2, motor_number=2, length=340, mirror='yes', shift_x=100)
        self.conveyor3 = ConveyorView(self, conv_number=3, motor_number=3, shift_x=150)
        self.conveyor1.grid(row=1, column=1, sticky='W')
        self.conveyor2.grid(row=1, column=2)
        self.conveyor3.grid(row=2, column=1, columnspan=2)


class IndicatorsButton(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.start1 = IndicatorSquare(self, text='Start 1 [%s]' % Szalag1v1_Address.START1)
        self.stop1 = IndicatorSquare(self, text='Stop 1 [%s]' % Szalag1v1_Address.STOP1)
        self.start2 = IndicatorSquare(self, text='Start 2 [%s]' % Szalag1v1_Address.START2)
        self.stop2 = IndicatorSquare(self, text='Stop 2 [%s]' % Szalag1v1_Address.STOP2)
        self.start1.grid(row=1, column=1, sticky=W)
        self.stop1.grid(row=2, column=1, sticky=W)
        self.start2.grid(row=1, column=2, sticky=W)
        self.stop2.grid(row=2, column=2, sticky=W)


class IndicatorsLamp(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        # noinspection SpellCheckingInspection
        self.uzem = IndicatorOval(self, text='Üzem [%s]' % Szalag1v1_Address.UZEM)
        self.hiba1 = IndicatorOval(self, text='Hiba 1 [%s]' % Szalag1v1_Address.HIBA1)
        self.hiba2 = IndicatorOval(self, text='Hiba 2 [%s]' % Szalag1v1_Address.HIBA2)
        self.hiba3 = IndicatorOval(self, text='Hiba 3 [%s]' % Szalag1v1_Address.HIBA3)
        self.uzem.grid(row=1, column=1, sticky=W)
        self.hiba1.grid(row=1, column=2, sticky=W)
        self.hiba2.grid(row=2, column=2, sticky=W)
        self.hiba3.grid(row=3, column=2, sticky=W)


class App(PLC_View):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 1v1')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 1v1')

        self.indicator_frame = Frame(self.process_frame)
        self.conveyor_frame = Frame(self.process_frame)

        self.indicators_button = IndicatorsButton(self.indicator_frame)
        self.indicators_lamp = IndicatorsLamp(self.indicator_frame)
        self.conveyors = Conveyors(self.conveyor_frame)

        self.indicators_button.pack(side=LEFT)
        self.indicators_lamp.pack(side=RIGHT)
        self.conveyors.pack()

        self.indicator_frame.pack(fill=X)
        self.conveyor_frame.pack()

        self.plc_data = Szalag1v1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.s1_is_changed():
            self.s1_refresh()

        if self.plc_data.s2_is_changed():
            self.s2_refresh()

        if self.plc_data.s3_is_changed():
            self.s3_refresh()

        if self.plc_data.start1_is_changed():
            self.start1_refresh()

        if self.plc_data.stop1_is_changed():
            self.stop1_refresh()

        if self.plc_data.start2_is_changed():
            self.start2_refresh()

        if self.plc_data.stop2_is_changed():
            self.stop2_refresh()

        if self.plc_data.m1_is_change():
            self.m1_refresh()
            self.s1_refresh()

        if self.plc_data.m2_is_change():
            self.m2_refresh()
            self.s2_refresh()

        if self.plc_data.m3_is_change():
            self.m3_refresh()
            self.s3_refresh()

        if self.plc_data.uzem_is_change():
            self.uzem_refresh()

        if self.plc_data.hiba1_is_change():
            self.hiba1_refresh()

        if self.plc_data.hiba2_is_change():
            self.hiba2_refresh()

        if self.plc_data.hiba3_is_change():
            self.hiba3_refresh()

        super().loop()

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

    def s3_refresh(self):
        if self.plc_data.s3 and self.plc_data.m3:
            self.conveyors.conveyor3.change_indicator_color('green')
        elif self.plc_data.s3 and not self.plc_data.m3:
            self.conveyors.conveyor3.change_indicator_color('yellow')
        elif not self.plc_data.s3 and self.plc_data.m3:
            self.conveyors.conveyor3.change_indicator_color('red')
        else:
            self.conveyors.conveyor3.change_indicator_color('gray')

    def start1_refresh(self):
        if self.plc_data.start1:
            self.indicators_button.start1.change_color('green')
        else:
            self.indicators_button.start1.change_color('gray')

    def stop1_refresh(self):
        if self.plc_data.stop1:
            self.indicators_button.stop1.change_color('red')
        else:
            self.indicators_button.stop1.change_color('gray')

    def start2_refresh(self):
        if self.plc_data.start2:
            self.indicators_button.start2.change_color('green')
        else:
            self.indicators_button.start2.change_color('gray')

    def stop2_refresh(self):
        if self.plc_data.stop2:
            self.indicators_button.stop2.change_color('red')
        else:
            self.indicators_button.stop2.change_color('gray')

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

    def m3_refresh(self):
        if self.plc_data.m3:
            self.conveyors.conveyor3.change_motor_color('green')
        else:
            self.conveyors.conveyor3.change_motor_color('gray')

    # noinspection SpellCheckingInspection
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

    def hiba3_refresh(self):
        if self.plc_data.hiba3:
            self.indicators_lamp.hiba3.change_color('red')
        else:
            self.indicators_lamp.hiba3.change_color('gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
