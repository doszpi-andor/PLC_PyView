
from _view.plc_view import PLC_ViewA
from tartaly_data.tartaly3_data import Tartaly3_data
from tartaly_data.tartaly3_draw import Tartaly3_View


class App(PLC_ViewA):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartály 3')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály 3')

        self.tanks = Tartaly3_View(self.process_frame)
        self.tanks.pack()

        self.plc_data = Tartaly3_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.start_is_change() or self.plc_data.stop_is_change():
            self.button_refresh()

        if self.plc_data.bekapcsolva_is_changed() or self.plc_data.kikapcsolva_is_changed():
            self.indicator_refresh()

        if self.plc_data.t1_felso_is_changed() or self.plc_data.t1_also_is_changed() \
                or self.plc_data.t1_tolt_is_changed():
            self.tank1_refresh()

        if self.plc_data.t2_felso_is_changed() or self.plc_data.t2_also_is_changed() \
                or self.plc_data.t2_tolt_is_changed():
            self.tank2_refresh()

        if self.plc_data.t3_felso_is_changed() or self.plc_data.t3_also_is_changed() \
                or self.plc_data.t3_tolt_is_changed():
            self.tank3_refresh()

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

    def indicator_refresh(self):
        # 1 1
        if self.plc_data.bekapcsolva and self.plc_data.kikapcsolva:
            self.tanks.indicators_change_color(on_color='green', off_color='red')
        # 0 1
        elif not self.plc_data.bekapcsolva and self.plc_data.kikapcsolva:
            self.tanks.indicators_change_color(on_color='gray', off_color='red')
        # 1 0
        elif self.plc_data.bekapcsolva and not self.plc_data.kikapcsolva:
            self.tanks.indicators_change_color(on_color='green', off_color='gray')
        # 0 0
        else:
            self.tanks.indicators_change_color(on_color='gray', off_color='gray')

    def tank1_refresh(self):
        # 1 1 1
        if self.plc_data.t1_tolt and self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t1_tolt and self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t1_tolt and not self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t1_tolt and not self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t1_tolt and self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t1_tolt and self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t1_tolt and not self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank1_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')

    def tank2_refresh(self):
        # 1 1 1
        if self.plc_data.t2_tolt and self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t2_tolt and self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t2_tolt and not self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t2_tolt and not self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t2_tolt and self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t2_tolt and self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t2_tolt and not self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank2_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')

    def tank3_refresh(self):
        # 1 1 1
        if self.plc_data.t3_tolt and self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t3_tolt and self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t3_tolt and not self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t3_tolt and not self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t3_tolt and self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t3_tolt and self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t3_tolt and not self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_color(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank3_change_color(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
