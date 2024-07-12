from _view.plc_view import PLC_ViewB
from tartaly_data.tartaly6v1_data import Tartaly6v1_data
from tartaly_data.tartaly6v1_draw import Tartaly6v1_View


class App(PLC_ViewB):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartaly 6')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály-6')

        self.tanks = Tartaly6v1_View(self.process_frame)
        self.tanks.pack()

        self.plc_data = Tartaly6v1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed() or self.plc_data.uzem_is_changed():
            self.operator_interface_refresh()

        if self.plc_data.t1_tolt_is_changed() or self.plc_data.t1_teli_is_changed():
            self.tank1_change_refresh()

        if self.plc_data.t2_tolt_is_changed() or\
                self.plc_data.t2_adalek_is_changed() or\
                self.plc_data.t2_urit_is_changed():
            self.tank2_change_refresh()

        if self.plc_data.t3_tolt_is_changed() or\
                self.plc_data.t3_adalek_is_changed() or\
                self.plc_data.t3_urit_is_changed():
            self.tank3_change_refresh()

        if self.plc_data.t2_szint_is_changed(threshold=1000):
            self.tank2_level_refresh()

        if self.plc_data.t3_szint_is_changed(threshold=1000):
            self.tank3_level_refresh()

        super().loop()

    def operator_interface_refresh(self):
        # 1 1 1
        if self.plc_data.start and self.plc_data.stop and self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='green', stop_color='red', factory_color='green')
        # 0 1 1
        elif not self.plc_data.start and self.plc_data.stop and self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='gray', stop_color='red', factory_color='green')
        # 1 0 1
        elif self.plc_data.start and not self.plc_data.stop and self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='green', stop_color='gray', factory_color='green')
        # 0 0 1
        elif not self.plc_data.start and not self.plc_data.stop and self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='gray', stop_color='gray', factory_color='green')
        # 1 1 0
        elif self.plc_data.start and self.plc_data.stop and not self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='green', stop_color='red', factory_color='gray')
        # 0 1 0
        elif not self.plc_data.start and self.plc_data.stop and not self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='gray', stop_color='red', factory_color='gray')
        # 1 0 0
        elif self.plc_data.start and not self.plc_data.stop and not self.plc_data.uzem:
            self.tanks.operator_interface_change_color(start_color='green', stop_color='gray', factory_color='gray')
        # 0 0 0
        else:
            self.tanks.operator_interface_change_color(start_color='gray', stop_color='gray', factory_color='gray')

    def tank1_change_refresh(self):
        # 1 1
        if self.plc_data.t1_tolt and self.plc_data.t1_teli:
            self.tanks.tank1_change_color(valve_color='blue', sensor_color='red')
        # 0 1
        elif not self.plc_data.t1_tolt and self.plc_data.t1_teli:
            self.tanks.tank1_change_color(valve_color='gray', sensor_color='red')
        # 1 0
        elif self.plc_data.t1_tolt and not self.plc_data.t1_teli:
            self.tanks.tank1_change_color(valve_color='blue', sensor_color='gray')
        # 0 0
        else:
            self.tanks.tank1_change_color(valve_color='gray', sensor_color='gray')

    def tank2_change_refresh(self):
        # 1 1 1
        if self.plc_data.t2_tolt and self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='blue', add_valve_color='blue', bottom_valve_color='blue')
        # 0 1 1
        elif not self.plc_data.t2_tolt and self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='gray', add_valve_color='blue', bottom_valve_color='blue')
        # 1 0 1
        elif self.plc_data.t2_tolt and not self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='blue', add_valve_color='gray', bottom_valve_color='blue')
        # 0 0 1
        elif not self.plc_data.t2_tolt and not self.plc_data.t2_adalek and self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='gray', add_valve_color='gray', bottom_valve_color='blue')
        # 1 1 0
        elif self.plc_data.t2_tolt and self.plc_data.t2_adalek and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='blue', add_valve_color='blue', bottom_valve_color='gray')
        # 0 1 0
        elif not self.plc_data.t2_tolt and self.plc_data.t2_adalek and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='gray', add_valve_color='blue', bottom_valve_color='gray')
        # 1 0 0
        elif self.plc_data.t2_tolt and not self.plc_data.t2_adalek and not self.plc_data.t2_urit:
            self.tanks.tank2_change_color(top_valve_color='blue', add_valve_color='gray', bottom_valve_color='gray')
        # 0 0 0
        else:
            self.tanks.tank2_change_color(top_valve_color='gray', add_valve_color='gray', bottom_valve_color='gray')

    def tank2_level_refresh(self):
        self.tanks.tank2_change_level(level_percent=self.plc_data.t2_szint_percent)

    def tank3_change_refresh(self):
        # 1 1 1
        if self.plc_data.t3_tolt and self.plc_data.t3_adalek and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='blue', add_valve_color='blue', bottom_valve_color='blue')
        # 0 1 1
        elif not self.plc_data.t3_tolt and self.plc_data.t3_adalek and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='gray', add_valve_color='blue', bottom_valve_color='blue')
        # 1 0 1
        elif self.plc_data.t3_tolt and not self.plc_data.t3_adalek and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='blue', add_valve_color='gray', bottom_valve_color='blue')
        # 0 0 1
        elif not self.plc_data.t3_tolt and not self.plc_data.t3_adalek and self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='gray', add_valve_color='gray', bottom_valve_color='blue')
        # 1 1 0
        elif self.plc_data.t3_tolt and self.plc_data.t3_adalek and not self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='blue', add_valve_color='blue', bottom_valve_color='gray')
        # 0 1 0
        elif not self.plc_data.t3_tolt and self.plc_data.t3_adalek and not self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='gray', add_valve_color='blue', bottom_valve_color='gray')
        # 1 0 0
        elif self.plc_data.t3_tolt and not self.plc_data.t3_adalek and not self.plc_data.t3_urit:
            self.tanks.tank3_change_color(top_valve_color='blue', add_valve_color='gray', bottom_valve_color='gray')
        # 0 0 0
        else:
            self.tanks.tank3_change_color(top_valve_color='gray', add_valve_color='gray', bottom_valve_color='gray')

    def tank3_level_refresh(self):
        self.tanks.tank3_change_level(level_percent=self.plc_data.t3_szint_percent)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
