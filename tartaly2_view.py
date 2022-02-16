from platform import system
from tkinter import Frame, Tk, Label, Button, TOP, RIGHT, LEFT, Y, Toplevel, W

from _plc_data.plc_ip_select import SelectIP
from _threading.thread_loop import ThreadLoop
from _view.indicator_view import IndicatorSquare
from _view.plc_view import PLC_View
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


class App(PLC_View):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartály 2')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály-2', wraplength=1)
        self.connect_label.config(wraplength=1)

        self.indicators = Indicators(self.process_frame)
        self.tanks = Tartaly2_View(self.process_frame)

        self.close_button.pack(side=TOP)
        self.indicators.pack(side=RIGHT)
        self.tanks.pack()

        self.name_frame.pack(side=RIGHT, fill=Y)
        self.connect_frame.pack(side=LEFT, fill=Y)

        self.plc_data = Tartaly2_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.start_is_changed():
            self.start_refresh()

        if self.plc_data.stop_is_changed():
            self.stop_refresh()

        if self.plc_data.t1_tolt_is_changed() or\
                self.plc_data.t1_urit_is_changed() or\
                self.plc_data.t1_fut_is_changed():
            self.tank1_refresh()

        if self.plc_data.t1_teli_is_changed() or\
                self.plc_data.t1_meleg_is_changed() or\
                self.plc_data.t1_hideg_is_changed():
            self.tank1_sensor_refresh()

        if self.plc_data.t2_adalek_is_changed() or self.plc_data.t2_urit_is_changed():
            self.tank2_refresh()

        if self.plc_data.t2_szint_is_changed(threshold=1000):
            self.tank2_level_refresh()

        if self.plc_data.t3_tolt_is_changed() or \
                self.plc_data.t3_urit_is_changed() or \
                self.plc_data.t3_fut_is_changed():
            self.tank3_refresh()

        if self.plc_data.t3_teli_is_changed() or \
                self.plc_data.t3_meleg_is_changed() or \
                self.plc_data.t3_hideg_is_changed():
            self.tank3_sensor_refresh()

        if self.plc_data.t4_adalek_is_changed() or self.plc_data.t4_urit_is_changed():
            self.tank4_refresh()

        if self.plc_data.t4_szint_is_changed(threshold=1000):
            self.tank4_level_refresh()

        super().loop()

    def start_refresh(self):
        if self.plc_data.start:
            self.indicators.start.change_color('green')
        else:
            self.indicators.start.change_color('gray')

    def stop_refresh(self):
        if self.plc_data.stop:
            self.indicators.stop.change_color('red')
        else:
            self.indicators.stop.change_color('gray')

    def tank1_refresh(self):

        # 1 1 1
        if self.plc_data.t1_tolt and self.plc_data.t1_urit and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='blue', bottom_valve_color='blue', heating_color='red')
        # 0 1 1
        elif not self.plc_data.t1_tolt and self.plc_data.t1_urit and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='gray', bottom_valve_color='blue', heating_color='red')
        # 1 0 1
        elif self.plc_data.t1_tolt and not self.plc_data.t1_urit and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='blue', bottom_valve_color='gray', heating_color='red')
        # 0 0 1
        elif not self.plc_data.t1_tolt and not self.plc_data.t1_urit and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='gray', bottom_valve_color='gray', heating_color='red')
        # 1 1 0
        elif self.plc_data.t1_tolt and self.plc_data.t1_urit and not self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='blue', bottom_valve_color='blue', heating_color='black')
        # 0 1 0
        elif not self.plc_data.t1_tolt and self.plc_data.t1_urit and not self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='gray', bottom_valve_color='blue', heating_color='black')
        # 1 0 0
        elif self.plc_data.t1_tolt and not self.plc_data.t1_urit and not self.plc_data.t1_fut:
            self.tanks.tank1_change_color(top_valve_color='blue', bottom_valve_color='gray', heating_color='black')
        # 0 0 0
        else:
            self.tanks.tank1_change_color(top_valve_color='gray', bottom_valve_color='gray', heating_color='black')

    def tank1_sensor_refresh(self):

        # 1 1 1
        if self.plc_data.t1_teli and self.plc_data.t1_meleg and self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='red', hot_sensor_color='red', clod_sensor_color='red')
        # 0 1 1
        elif not self.plc_data.t1_teli and self.plc_data.t1_meleg and self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='gray', hot_sensor_color='red', clod_sensor_color='red')
        # 1 0 1
        elif self.plc_data.t1_teli and not self.plc_data.t1_meleg and self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='red', hot_sensor_color='gray', clod_sensor_color='red')
        # 0 0 1
        elif not self.plc_data.t1_teli and not self.plc_data.t1_meleg and self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='gray', hot_sensor_color='gray', clod_sensor_color='red')
        # 1 1 0
        elif self.plc_data.t1_teli and self.plc_data.t1_meleg and not self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='red', hot_sensor_color='red', clod_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t1_teli and self.plc_data.t1_meleg and not self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='gray', hot_sensor_color='red', clod_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t1_teli and not self.plc_data.t1_meleg and not self.plc_data.t1_hideg:
            self.tanks.tank1_change_sensor_color(sensor_color='red', hot_sensor_color='gray', clod_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank1_change_sensor_color(sensor_color='gray', hot_sensor_color='gray', clod_sensor_color='gray')

    def tank2_refresh(self):

        # 1 1
        if self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(add_valve_color='blue', bottom_valve_color='blue')
        # 0 1
        elif not self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(add_valve_color='gray', bottom_valve_color='blue')
        # 1 0
        elif self.plc_data.t2_adalek and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(add_valve_color='blue', bottom_valve_color='gray')
        # 0 0
        else:
            self.tanks.tank2_change_color(add_valve_color='gray', bottom_valve_color='gray')

    def tank2_level_refresh(self):
        self.tanks.tank2_change_level(level_percent=self.plc_data.t2_szint_percent)

    def tank3_refresh(self):

        # 1 1 1
        if self.plc_data.t3_tolt and self.plc_data.t3_urit and self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='blue', bottom_valve_color='blue', heating_color='red')
        # 0 1 1
        elif not self.plc_data.t3_tolt and self.plc_data.t3_urit and self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='gray', bottom_valve_color='blue', heating_color='red')
        # 1 0 1
        elif self.plc_data.t3_tolt and not self.plc_data.t3_urit and self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='blue', bottom_valve_color='gray', heating_color='red')
        # 0 0 1
        elif not self.plc_data.t3_tolt and not self.plc_data.t3_urit and self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='gray', bottom_valve_color='gray', heating_color='red')
        # 1 1 0
        elif self.plc_data.t3_tolt and self.plc_data.t3_urit and not self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='blue', bottom_valve_color='blue', heating_color='black')
        # 0 1 0
        elif not self.plc_data.t3_tolt and self.plc_data.t3_urit and not self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='gray', bottom_valve_color='blue', heating_color='black')
        # 1 0 0
        elif self.plc_data.t3_tolt and not self.plc_data.t3_urit and not self.plc_data.t3_fut:
            self.tanks.tank3_change_color(top_valve_color='blue', bottom_valve_color='gray', heating_color='black')
        # 0 0 0
        else:
            self.tanks.tank3_change_color(top_valve_color='gray', bottom_valve_color='gray', heating_color='black')

    def tank3_sensor_refresh(self):

        # 1 1 1
        if self.plc_data.t3_teli and self.plc_data.t3_meleg and self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='red', hot_sensor_color='red', clod_sensor_color='red')
        # 0 1 1
        elif not self.plc_data.t3_teli and self.plc_data.t3_meleg and self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='gray', hot_sensor_color='red', clod_sensor_color='red')
        # 1 0 1
        elif self.plc_data.t3_teli and not self.plc_data.t3_meleg and self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='red', hot_sensor_color='gray', clod_sensor_color='red')
        # 0 0 1
        elif not self.plc_data.t3_teli and not self.plc_data.t3_meleg and self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='gray', hot_sensor_color='gray', clod_sensor_color='red')
        # 1 1 0
        elif self.plc_data.t3_teli and self.plc_data.t3_meleg and not self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='red', hot_sensor_color='red', clod_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t3_teli and self.plc_data.t3_meleg and not self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='gray', hot_sensor_color='red', clod_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t3_teli and not self.plc_data.t3_meleg and not self.plc_data.t3_hideg:
            self.tanks.tank3_change_sensor_color(sensor_color='red', hot_sensor_color='gray', clod_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank3_change_sensor_color(sensor_color='gray', hot_sensor_color='gray', clod_sensor_color='gray')

    def tank4_refresh(self):
        
        # 1 1
        if self.plc_data.t4_adalek and self.plc_data.t4_urit:
            self.tanks.tank4_change_color(add_valve_color='blue', bottom_valve_color='blue')
        # 0 1
        elif not self.plc_data.t4_adalek and self.plc_data.t4_urit:
            self.tanks.tank4_change_color(add_valve_color='gray', bottom_valve_color='blue')
        # 1 0
        elif self.plc_data.t4_adalek and not self.plc_data.t4_urit:
            self.tanks.tank4_change_color(add_valve_color='blue', bottom_valve_color='grey')
        # 0 0
        else:
            self.tanks.tank4_change_color(add_valve_color='gray', bottom_valve_color='gray')

    def tank4_level_refresh(self):
        self.tanks.tank4_change_level(level_percent=self.plc_data.t4_szint_percent)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
