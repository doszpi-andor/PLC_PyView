from _view.plc_view import PLC_ViewA
from szalag_data.szalag2v1_data import Szalag2v1_data
from szalag_data.szalag2v1_draw import Szalag2v1_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 2v1')

        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 2v1')

        self.conveyors = Szalag2v1_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag2v1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):
        super().loop()

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed() or self.plc_data.hiba_is_changed():
            self.indicator_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.silo_refresh()

        if self.plc_data.m2_is_changed() or self.plc_data.s2_is_changed():
            self.conveyor_refresh()

        if self.plc_data.kp1_is_changed() or self.plc_data.kp2_is_changed() or self.plc_data.ks_is_changed():
            self.wagon_refresh()

    def button_refresh(self):
        # 1 1
        if self.plc_data.start and self.plc_data.stop:
            self.conveyors.button_change_color(start_color='green', stop_color='red')
        # 0 1
        elif not self.plc_data.start and self.plc_data.stop:
            self.conveyors.button_change_color(start_color='gray', stop_color='red')
        # 1 0
        elif self.plc_data.start and not self.plc_data.stop:
            self.conveyors.button_change_color(start_color='green', stop_color='gray')
        # 0 0
        else:
            self.conveyors.button_change_color(start_color='gray', stop_color='gray')

    def indicator_refresh(self):
        # 1 1
        if self.plc_data.uzem and self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='green', error_color='red')
        # 0 1
        elif not self.plc_data.uzem and self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='gray', error_color='red')
        # 1 0
        elif self.plc_data.uzem and not self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='green', error_color='gray')
        # 0 0
        else:
            self.conveyors.indicator_change_color(factory_color='gray', error_color='gray')

    def silo_refresh(self):
        # 1 1
        if self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.silo_change_color(motor_color='green', sensor_color='red')
        # 0 1
        elif not self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.silo_change_color(motor_color='gray', sensor_color='red')
        # 1 0
        elif self.plc_data.m1 and not self.plc_data.s1:
            self.conveyors.silo_change_color(motor_color='green', sensor_color='gray')
        else:
            self.conveyors.silo_change_color(motor_color='gray', sensor_color='gray')

    def conveyor_refresh(self):
        # 1 1
        if self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m2 and not self.plc_data.s2:
            self.conveyors.conveyor_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor_change_color(motor_color='grey', sensor_color='grey')

    def wagon_refresh(self):
        # 1 1 1
        if self.plc_data.kp1 and self.plc_data.kp2 and self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='red', sensor2_color='red', wight_color='red')
        # 0 1 1
        elif not self.plc_data.kp1 and self.plc_data.kp2 and self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='gray', sensor2_color='red', wight_color='red')
        # 1 0 1
        elif self.plc_data.kp1 and not self.plc_data.kp2 and self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='red', sensor2_color='gray', wight_color='red')
        # 0 0 1
        elif not self.plc_data.kp1 and not self.plc_data.kp2 and self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='gray', sensor2_color='gray', wight_color='red')
        # 1 1 0
        elif self.plc_data.kp1 and self.plc_data.kp2 and not self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='red', sensor2_color='red', wight_color='gray')
        # 0 1 0
        elif not self.plc_data.kp1 and self.plc_data.kp2 and not self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='gray', sensor2_color='red', wight_color='gray')
        # 1 0 0
        elif self.plc_data.kp1 and not self.plc_data.kp2 and not self.plc_data.ks:
            self.conveyors.wagon_change_color(sensor1_color='red', sensor2_color='gray', wight_color='gray')
        # 0 0 0
        else:
            self.conveyors.wagon_change_color(sensor1_color='gray', sensor2_color='gray', wight_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
