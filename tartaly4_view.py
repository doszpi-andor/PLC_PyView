from tkinter import Frame, W, TOP, RIGHT, LEFT, Y

from _view.indicator_view import IndicatorSquare
from _view.plc_view import PLC_View
from tartaly_data.tartaly4_data import Tartaly4_Address, Tartaly4_data
from tartaly_data.tartaly4_draw import Tartaly4_View


class Indicators(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.start = IndicatorSquare(self, text='Start [%s]' % Tartaly4_Address.START)
        self.stop = IndicatorSquare(self, text='Stop [%s]' % Tartaly4_Address.STOP)
        self.start_urit = IndicatorSquare(self, text='Start ürít [%s]' % Tartaly4_Address.START_URIT)

        self.start.grid(row=1, column=1, sticky=W)
        self.stop.grid(row=2, column=1, sticky=W)
        self.start_urit.grid(row=3, column=1, sticky=W)


class App(PLC_View):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('Tartaly 4')
        self.name_label.config(text='Tartály-4', wraplength=1)
        self.connect_label.config(wraplength=1)

        self.indicators = Indicators(self.process_frame)
        self.tanks = Tartaly4_View(self.process_frame)

        self.close_button.pack(side=TOP)
        self.indicators.pack(side=RIGHT)
        self.tanks.pack()

        self.name_frame.pack(side=RIGHT, fill=Y)
        self.connect_frame.pack(side=LEFT, fill=Y)

        self.plc_data = Tartaly4_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.start_is_changed():
            self.start_refresh()

        if self.plc_data.stop_is_changed():
            self.stop_refresh()

        if self.plc_data.start_urit_is_changed():
            self.start_urit_refresh()

        if self.plc_data.t1_teli_is_changed() or self.plc_data.t1_fut_is_changed():
            self.tank1_refresh()

        if self.plc_data.t1_tolt_is_changed() or self.plc_data.t1_urit_is_changed():
            self.tank1_valve_refresh()

        if self.plc_data.t2_teli_is_changed() or self.plc_data.t2_fut_is_changed():
            self.tank2_refresh()

        if self.plc_data.t2_tolt_is_changed() or self.plc_data.t2_urit_is_changed():
            self.tank2_valve_refresh()

        if self.plc_data.t3_kever_is_changed() or self.plc_data.t3_urit_is_changed():
            self.tank3_refresh()

        super().loop()

    def start_refresh(self):
        pass

    def stop_refresh(self):
        pass

    def start_urit_refresh(self):
        pass

    def tank1_refresh(self):
        pass

    def tank1_valve_refresh(self):
        pass

    def tank2_refresh(self):
        pass

    def tank2_valve_refresh(self):
        pass

    def tank3_refresh(self):
        pass


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
