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
            self.dump_refresh()

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

        if self.plc_data.t3_felso_is_changed() or\
                self.plc_data.t3_kozep_is_changed() or\
                self.plc_data.t3_also_is_changed():
            self.tank3_sensor_refresh()

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

    def dump_refresh(self):
        if self.plc_data.stert_urit:
            self.indicators.start_urit.change_color('green')
        else:
            self.indicators.start_urit.change_color('gray')

    def tank1_refresh(self):
        # 1 1
        if self.plc_data.t1_teli and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(sensor_color='red', heating_color='red')
        # 0 1
        elif not self.plc_data.t1_teli and self.plc_data.t1_fut:
            self.tanks.tank1_change_color(sensor_color='gray', heating_color='red')
        # 1 0
        elif self.plc_data.t1_teli and not self.plc_data.t1_fut:
            self.tanks.tank1_change_color(sensor_color='red', heating_color='black')
        # 0 0
        else:
            self.tanks.tank1_change_color(sensor_color='gray', heating_color='black')

    def tank1_valve_refresh(self):
        # 1 1
        if self.plc_data.t1_tolt and self.plc_data.t1_urit:
            self.tanks.tank1_change_valve_color(top_valve_color='blue', bottom_valve_color='blue')
        # 0 1
        elif not self.plc_data.t1_tolt and self.plc_data.t1_urit:
            self.tanks.tank1_change_valve_color(top_valve_color='gray', bottom_valve_color='blue')
        # 1 0
        elif self.plc_data.t1_tolt and not self.plc_data.t1_urit:
            self.tanks.tank1_change_valve_color(top_valve_color='blue', bottom_valve_color='gray')
        # 0 0
        else:
            self.tanks.tank1_change_valve_color(top_valve_color='gray', bottom_valve_color='gray')

    def tank2_refresh(self):
        # 1 1
        if self.plc_data.t2_teli and self.plc_data.t2_fut:
            self.tanks.tank2_change_color(sensor_color='red', heating_color='red')
        # 0 1
        elif not self.plc_data.t2_teli and self.plc_data.t2_fut:
            self.tanks.tank2_change_color(sensor_color='gray', heating_color='red')
        # 1 0
        elif self.plc_data.t2_teli and not self.plc_data.t2_fut:
            self.tanks.tank2_change_color(sensor_color='red', heating_color='black')
        # 0 0
        else:
            self.tanks.tank2_change_color(sensor_color='gray', heating_color='black')

    def tank2_valve_refresh(self):
        # 1 1
        if self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank2_change_valve_color(top_valve_color='blue', bottom_valve_color='blue')
        # 0 1
        elif not self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank1_change_valve_color(top_valve_color='gray', bottom_valve_color='blue')
        # 1 0
        elif self.plc_data.t2_tolt and not self.plc_data.t2_urit:
            self.tanks.tank2_change_valve_color(top_valve_color='blue', bottom_valve_color='gray')
        # 0 0
        else:
            self.tanks.tank2_change_valve_color(top_valve_color='gray', bottom_valve_color='gray')

    def tank3_refresh(self):
        # 1 1
        if self.plc_data.t3_kever and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(rotor_color='green', bottom_valve_color='blue')
        # 0 1
        elif not self.plc_data.t3_kever and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(rotor_color='yellow', bottom_valve_color='blue')
        # 1 0
        elif self.plc_data.t3_kever and not self.plc_data.t3_urit:
            self.tanks.tank3_change_color(rotor_color='green', bottom_valve_color='gray')
        # 0 0
        else:
            self.tanks.tank3_change_color(rotor_color='yellow', bottom_valve_color='gray')

    def tank3_sensor_refresh(self):
        # 1 1 1
        if self.plc_data.t3_felso and self.plc_data.t3_kozep and self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='red', half_sensor_color='red', bottom_sensor_color='red')
        # 0 1 1
        elif not self.plc_data.t3_felso and self.plc_data.t3_kozep and self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='gray', half_sensor_color='red', bottom_sensor_color='red')
        # 1 0 1
        elif self.plc_data.t3_felso and not self.plc_data.t3_kozep and self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='red', half_sensor_color='gray', bottom_sensor_color='red')
        # 0 0 1
        elif not self.plc_data.t3_felso and not self.plc_data.t3_kozep and self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='gray', half_sensor_color='gray', bottom_sensor_color='red')
        # 1 1 0
        elif self.plc_data.t3_felso and self.plc_data.t3_kozep and not self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='red', half_sensor_color='red', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t3_felso and self.plc_data.t3_kozep and not self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='gray', half_sensor_color='red', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t3_felso and not self.plc_data.t3_kozep and not self.plc_data.t3_also:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='red', half_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank3_change_sensor_color(
                top_sensor_color='gray', half_sensor_color='gray', bottom_sensor_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
