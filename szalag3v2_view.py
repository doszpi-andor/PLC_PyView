from _view.plc_view import PLC_ViewA
from szalag_data.szalag3_data import Szalag3_data
from szalag_data.szalag3v2_draw import Szalag3v2_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 3v2')

        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 3v2')

        self.conveyors = Szalag3v2_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag3_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):
        super().loop()

        if self.plc_data.uzem_is_changed() or self.plc_data.szalag_hiba_is_changed() or self.plc_data.kocsi_hiba_is_changed():
            self.indicator_refresh()

        if self.plc_data.silo1_ures_is_changed() or self.plc_data.silo2_ures_is_changed():
            self.silo_indicator_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.silo1_refresh()

        if self.plc_data.m2_is_changed() or self.plc_data.s2_is_changed():
            self.silo2_refresh()

        if self.plc_data.m3_is_changed() or self.plc_data.s3_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m4_is_changed() or self.plc_data.s4_is_changed():
            self.conveyor2_refresh()

        if self.plc_data.m5_is_changed() or self.plc_data.s5_is_changed():
            self.conveyor3_refresh()

        if self.plc_data.kp_is_changed() or self.plc_data.kp_is_changed():
            self.wagon_refresh()

        if self.plc_data.ks_is_changed(threshold=1000):
            self.wagon_wight_refresh()

    def indicator_refresh(self):

        # 1 1 1
        if self.plc_data.uzem and self.plc_data.szalag_hiba and self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='green',
                                                  conveyor_error_color='red',
                                                  wagon_error_color='red')
        # 0 1 1
        elif not self.plc_data.uzem and self.plc_data.szalag_hiba and self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='gray',
                                                  conveyor_error_color='red',
                                                  wagon_error_color='red')
        # 1 0 1
        elif self.plc_data.uzem and not self.plc_data.szalag_hiba and self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='green',
                                                  conveyor_error_color='gray',
                                                  wagon_error_color='red')
        # 0 0 1
        elif not self.plc_data.uzem and not self.plc_data.szalag_hiba and self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='gray',
                                                  conveyor_error_color='gray',
                                                  wagon_error_color='red')
        # 1 1 0
        elif self.plc_data.uzem and self.plc_data.szalag_hiba and not self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='green',
                                                  conveyor_error_color='red',
                                                  wagon_error_color='gray')
        # 0 1 0
        elif not self.plc_data.uzem and self.plc_data.szalag_hiba and not self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='gray',
                                                  conveyor_error_color='red',
                                                  wagon_error_color='gray')
        # 1 0 0
        elif self.plc_data.uzem and not self.plc_data.szalag_hiba and not self.plc_data.kocsi_hiba:
            self.conveyors.indicator_change_color(factory_color='green',
                                                  conveyor_error_color='gray',
                                                  wagon_error_color='gray')
        # 0 0 0
        else:
            self.conveyors.indicator_change_color(factory_color='gray',
                                                  conveyor_error_color='gray',
                                                  wagon_error_color='gray')

    def silo_indicator_refresh(self):
        # 1 1
        if self.plc_data.silo1_ures and self.plc_data.silo2_ures:
            self.conveyors.silo_indicator_change_color(silo1_empty_color='red', silo2_empty_color='red')
        # 0 1
        elif not self.plc_data.silo1_ures and self.plc_data.silo2_ures:
            self.conveyors.silo_indicator_change_color(silo1_empty_color='gray', silo2_empty_color='red')
        # 1 0
        elif self.plc_data.silo1_ures and not self.plc_data.silo2_ures:
            self.conveyors.silo_indicator_change_color(silo1_empty_color='red', silo2_empty_color='gray')
        # 0 0
        else:
            self.conveyors.silo_indicator_change_color(silo1_empty_color='gray', silo2_empty_color='gray')

    def silo1_refresh(self):
        # 1 1
        if self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.silo1_change_color(motor_color='green', sensor_color='red')
        # 0 1
        elif not self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.silo1_change_color(motor_color='gray', sensor_color='red')
        # 1 0
        elif self.plc_data.m1 and not self.plc_data.s1:
            self.conveyors.silo1_change_color(motor_color='green', sensor_color='gray')
        else:
            self.conveyors.silo1_change_color(motor_color='gray', sensor_color='gray')

    def silo2_refresh(self):
        # 1 1
        if self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.silo2_change_color(motor_color='green', sensor_color='red')
        # 0 1
        elif not self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.silo2_change_color(motor_color='gray', sensor_color='red')
        # 1 0
        elif self.plc_data.m2 and not self.plc_data.s2:
            self.conveyors.silo2_change_color(motor_color='green', sensor_color='gray')
        else:
            self.conveyors.silo2_change_color(motor_color='gray', sensor_color='gray')

    def conveyor1_refresh(self):
        # 1 1
        if self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor1_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m3 and not self.plc_data.s3:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor1_change_color(motor_color='grey', sensor_color='grey')

    def conveyor2_refresh(self):
        # 1 1
        if self.plc_data.m4 and self.plc_data.s4:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m4 and self.plc_data.s4:
            self.conveyors.conveyor2_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m4 and not self.plc_data.s4:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor2_change_color(motor_color='grey', sensor_color='grey')

    def conveyor3_refresh(self):
        # 1 1
        if self.plc_data.m5 and self.plc_data.s5:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m5 and self.plc_data.s5:
            self.conveyors.conveyor3_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m5 and not self.plc_data.s5:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor3_change_color(motor_color='grey', sensor_color='grey')

    def wagon_refresh(self):
        # 1
        if self.plc_data.kp:
            self.conveyors.wagon_change_color(sensor_color='red')
        # 0
        else:
            self.conveyors.wagon_change_color(sensor_color='gray')

    def wagon_wight_refresh(self):
        self.conveyors.wagon_wight_change(wight_percent=self.plc_data.ks_percent)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
