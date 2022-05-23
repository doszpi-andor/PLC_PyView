from _view.plc_view import PLC_ViewA
from szalag_data.szalag1v2_data import Szalag1v2_data
from szalag_data.szalag1v2_draw import Szalag1v2_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 1v2')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 1v2')

        self.conveyors = Szalag1v2_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag1v2_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):
        super().loop()

        if self.plc_data.start1_is_changed() or self.plc_data.stop1_is_changed():
            self.button1_refresh()

        if self.plc_data.start2_is_changed() or self.plc_data.stop2_is_changed():
            self.button2_refresh()

        if self.plc_data.uzem1_is_changed() or self.plc_data.uzem2_is_changed():
            self.factory_refresh()

        if self.plc_data.hiba1_is_changed() or self.plc_data.hiba2_is_changed() or self.plc_data.hiba3_is_changed():
            self.error_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m2_is_changed() or self.plc_data.s2_is_changed():
            self.conveyor2_refresh()

        if self.plc_data.m3_is_changed() or self.plc_data.s3_is_changed():
            self.conveyor3_refresh()

    def button1_refresh(self):
        # 1 1
        if self.plc_data.start1 and self.plc_data.stop1:
            self.conveyors.button1_change_color(start_color='green', stop_color='red')
        # 0 1
        elif not self.plc_data.start1 and self.plc_data.stop1:
            self.conveyors.button1_change_color(start_color='gray', stop_color='red')
        # 1 0
        elif self.plc_data.start1 and not self.plc_data.stop1:
            self.conveyors.button1_change_color(start_color='green', stop_color='gray')
        # 0 0
        else:
            self.conveyors.button1_change_color(start_color='gray', stop_color='gray')

    def button2_refresh(self):
        # 1 1
        if self.plc_data.start2 and self.plc_data.stop2:
            self.conveyors.button2_change_color(start_color='green', stop_color='red')
        # 0 1
        elif not self.plc_data.start2 and self.plc_data.stop2:
            self.conveyors.button2_change_color(start_color='gray', stop_color='red')
        # 1 0
        elif self.plc_data.start2 and not self.plc_data.stop2:
            self.conveyors.button2_change_color(start_color='green', stop_color='gray')
        # 0 0
        else:
            self.conveyors.button2_change_color(start_color='gray', stop_color='gray')

    def factory_refresh(self):
        # 1 1
        if self.plc_data.uzem1 and self.plc_data.uzem2:
            self.conveyors.factory_change_color(factory1_color='green', factory2_color='green')
        # 0 1
        elif not self.plc_data.uzem1 and self.plc_data.uzem2:
            self.conveyors.factory_change_color(factory1_color='gray', factory2_color='green')
        # 1 0
        elif self.plc_data.uzem1 and not self.plc_data.uzem2:
            self.conveyors.factory_change_color(factory1_color='green', factory2_color='gray')
        # 0 0
        else:
            self.conveyors.factory_change_color(factory1_color='gray', factory2_color='gray')

    def error_refresh(self):
        # 1 1 1
        if self.plc_data.hiba1 and self.plc_data.hiba2 and self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='red', error2_color='red', error3_color='red')
        # 0 1 1
        elif not self.plc_data.hiba1 and self.plc_data.hiba2 and self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='gray', error2_color='red', error3_color='red')
        # 1 0 1
        elif self.plc_data.hiba1 and not self.plc_data.hiba2 and self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='red', error2_color='gray', error3_color='red')
        # 0 0 1
        elif not self.plc_data.hiba1 and not self.plc_data.hiba2 and self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='gray', error2_color='gray', error3_color='red')
        # 1 1 0
        elif self.plc_data.hiba1 and self.plc_data.hiba2 and not self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='red', error2_color='red', error3_color='gray')
        # 0 1 0
        elif not self.plc_data.hiba1 and self.plc_data.hiba2 and not self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='gray', error2_color='red', error3_color='gray')
        # 1 0 0
        elif self.plc_data.hiba1 and not self.plc_data.hiba2 and not self.plc_data.hiba3:
            self.conveyors.error_change_color(error1_color='red', error2_color='gray', error3_color='gray')
        else:
            self.conveyors.error_change_color(error1_color='gray', error2_color='gray', error3_color='gray')

    def conveyor1_refresh(self):
        # 1 1
        if self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m1 and not self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor1_change_color(motor_color='grey', sensor_color='grey')

    def conveyor2_refresh(self):
        # 1 1
        if self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m2 and not self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor2_change_color(motor_color='grey', sensor_color='grey')

    def conveyor3_refresh(self):
        # 1 1
        if self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m3 and not self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor3_change_color(motor_color='grey', sensor_color='grey')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()