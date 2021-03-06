
from _view.plc_view import PLC_ViewB
from tartaly_data.tartaly2_data import Tartaly2_data
from tartaly_data.tartaly2_draw import Tartaly2_View


class App(PLC_ViewB):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartály 2')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály-2')

        self.tanks = Tartaly2_View(self.process_frame)
        self.tanks.pack()

        self.plc_data = Tartaly2_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

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
