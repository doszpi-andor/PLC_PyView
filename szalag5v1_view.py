from _view.plc_view import PLC_ViewA
from szalag_data.szalag5v1_data import Szalag5v1_data
from szalag_data.szalag5v1_draw import Szalag5v1_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 5v1')

        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 5v1')

        self.conveyors = Szalag5v1_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag5v1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        super().loop()

        if self.plc_data.start1_is_changed() or self.plc_data.start2_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed() or self.plc_data.hiba_is_changed():
            self.indicator_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.silo1_refresh()

        if self.plc_data.m2_is_changed() or self.plc_data.s2_is_changed():
            self.silo2_refresh()

        if self.plc_data.m3_is_changed() or self.plc_data.s3_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m4_is_changed() or self.plc_data.s4_is_changed():
            self.conveyor2_refresh()

    def button_refresh(self):
        # 1 1 1
        if self.plc_data.start1 and self.plc_data.start2 and self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='green', start2_color='green', stop_color='red')
        # 0 1 1
        elif not self.plc_data.start1 and self.plc_data.start2 and self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='gray', start2_color='green', stop_color='red')
        # 1 0 1
        elif self.plc_data.start1 and not self.plc_data.start2 and self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='green', start2_color='gray', stop_color='red')
        # 0 0 1
        elif not self.plc_data.start1 and not self.plc_data.start2 and self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='gray', start2_color='gray', stop_color='red')
        # 1 1 0
        elif self.plc_data.start1 and self.plc_data.start2 and not self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='green', start2_color='green', stop_color='gray')
        # 0 1 0
        elif not self.plc_data.start1 and self.plc_data.start2 and not self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='gray', start2_color='green', stop_color='gray')
        # 1 0 0
        elif self.plc_data.start1 and not self.plc_data.start2 and not self.plc_data.stop:
            self.conveyors.button_change_color(start1_color='green', start2_color='gray', stop_color='gray')
        # 0 0 0
        else:
            self.conveyors.button_change_color(start1_color='gray', start2_color='gray', stop_color='gray')

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


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
