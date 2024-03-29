from _view.plc_view import PLC_ViewA
from szalag_data.szalag6v0_data import Szalag6v0_data
from szalag_data.szalag6v0_draw import Szalag6v0_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 6v0')

        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 6v0')

        self.conveyors = Szalag6v0_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag6v0_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        super().loop()

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed():
            self.indicator_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.silo_refresh()

        if self.plc_data.m2_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m3_is_changed():
            self.conveyor2_refresh()

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
        if self.plc_data.uzem:
            self.conveyors.indicator_change_color(factory_color='green')
        else:
            self.conveyors.indicator_change_color(factory_color='gray')

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

    def conveyor1_refresh(self):
        if self.plc_data.m2:
            self.conveyors.conveyor1_change_color(motor_color='green')
        else:
            self.conveyors.conveyor1_change_color(motor_color='gray')

    def conveyor2_refresh(self):
        if self.plc_data.m3:
            self.conveyors.conveyor2_change_color(motor_color='green')
        else:
            self.conveyors.conveyor2_change_color(motor_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
