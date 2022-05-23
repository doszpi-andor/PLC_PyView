
from _view.plc_view import PLC_ViewB
from tartaly_data.tartaly1_data import Tartaly1_data
from tartaly_data.tartaly1_draw import Tartaly1_View


class App(PLC_ViewB):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartaly 1')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály-1')

        self.tanks = Tartaly1_View(self.process_frame)
        self.tanks.pack()

        self.plc_data = Tartaly1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

        if self.plc_data.t1_teli_is_changed() or self.plc_data.t1_fut_is_changed():
            self.tank1_refresh()

        if self.plc_data.t1_tolt_is_changed() or self.plc_data.t1_urit_is_changed():
            self.tank1_valve_refresh()

        if self.plc_data.t2_teli_is_changed() or self.plc_data.t2_tolt_is_changed() or \
                self.plc_data.t2_urit_is_changed():
            self.tank2_refresh()

        if self.plc_data.t3_kever_is_changed() or self.plc_data.t3_urit_is_changed():
            self.tank3_refresh()

        if self.plc_data.t1_homerseklet_is_changed(threshold=1000):
            self.tank1_heating_refresh()

        if self.plc_data.t3_szint_is_changed(threshold=1000):
            self.tank3_level_refresh()

        super().loop()

    def button_refresh(self):
        # 1 1
        if self.plc_data.start and self.plc_data.stop:
            self.tanks.button_change_color(start_color='green', stop_color='red')
        # 0 1
        elif not self.plc_data.start and self.plc_data.stop:
            self.tanks.button_change_color(start_color='gray', stop_color='red')
        # 1 0
        elif self.plc_data.start and not self.plc_data.stop:
            self.tanks.button_change_color(start_color='green', stop_color='gray')
        # 0 0
        else:
            self.tanks.button_change_color(start_color='gray', stop_color='gray')

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
        # 1 1 1
        if self.plc_data.t2_teli and self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='red', top_valve_color='blue', bottom_valve_color='blue')
        # 0 1 1
        elif not self.plc_data.t2_teli and self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='gray', top_valve_color='blue', bottom_valve_color='blue')
        # 1 0 1
        elif self.plc_data.t2_teli and not self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='red', top_valve_color='gray', bottom_valve_color='blue')
        # 0 0 1
        elif not self.plc_data.t2_teli and not self.plc_data.t2_tolt and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='gray', top_valve_color='gray', bottom_valve_color='blue')
        # 1 1 0
        elif self.plc_data.t2_teli and self.plc_data.t2_tolt and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='red', top_valve_color='blue', bottom_valve_color='gray')
        # 0 1 0
        elif not self.plc_data.t2_teli and self.plc_data.t2_tolt and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='gray', top_valve_color='blue', bottom_valve_color='gray')
        # 1 0 0
        elif self.plc_data.t2_teli and not self.plc_data.t2_tolt and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(sensor_color='red', top_valve_color='gray', bottom_valve_color='gray')
        # 0 0 0
        else:
            self.tanks.tank2_change_color(sensor_color='gray', top_valve_color='gray', bottom_valve_color='gray')

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

    def tank1_heating_refresh(self):
        self.tanks.tank1_change_heating_level(temperature_percent=self.plc_data.t1_homerseklet_percent)

    def tank3_level_refresh(self):
        self.tanks.tank3_change_level(level_percent=self.plc_data.t3_szint_percent)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
