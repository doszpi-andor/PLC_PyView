from _view.plc_view import PLC_ViewA
from szalag_data.szalag8v1_data import Szalag8v1_data
from szalag_data.szalag8v1_draw import Szalag8v1_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 8v1')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 8v1')

        self.conveyors = Szalag8v1_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag8v1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        super().loop()

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed() or self.plc_data.nyugta_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed() or self.plc_data.hiba_is_changed() or self.plc_data.folyamat_is_changed():
            self.indicator1_refresh()

        if self.plc_data.megtelt_a_is_changed() or self.plc_data.megtelt_b_is_changed():
            self.indicator2_refresh()

        if self.plc_data.sbe_is_changed() or self.plc_data.sb_is_changed() or self.plc_data.sa_is_changed():
            self.sensor_refresh()

        if self.plc_data.m1_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m2a_is_changed() or self.plc_data.m2b_is_changed():
            self.conveyor2_refresh()

    def button_refresh(self):
        # 1 1 1
        if self.plc_data.start and self.plc_data.stop and self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='green', stop_color='red', receipt_color='yellow')
        # 0 1 1
        elif not self.plc_data.start and self.plc_data.stop and self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='gray', stop_color='red', receipt_color='yellow')
        # 1 0 1
        elif self.plc_data.start and not self.plc_data.stop and self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='green', stop_color='gray', receipt_color='yellow')
        # 0 0 1
        elif not self.plc_data.start and not self.plc_data.stop and self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='gray', stop_color='gray', receipt_color='yellow')
        # 1 1 0
        elif self.plc_data.start and self.plc_data.stop and not self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='green', stop_color='red', receipt_color='gray')
        # 0 1 0
        elif not self.plc_data.start and self.plc_data.stop and not self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='gray', stop_color='red', receipt_color='gray')
        # 1 0 0
        elif self.plc_data.start and not self.plc_data.stop and not self.plc_data.nyugta:
            self.conveyors.button_change_color(start_color='green', stop_color='gray', receipt_color='gray')
        # 0 0 0
        else:
            self.conveyors.button_change_color(start_color='gray', stop_color='gray', receipt_color='gray')

    def indicator1_refresh(self):
        # 1 1 1
        if self.plc_data.uzem and self.plc_data.hiba and self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='green', error_color='red', process_color='green')
        # 0 1 1
        elif not self.plc_data.uzem and self.plc_data.hiba and self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='gray', error_color='red', process_color='green')
        # 1 0 1
        elif self.plc_data.uzem and not self.plc_data.hiba and self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='green', error_color='gray', process_color='green')
        # 0 0 1
        elif not self.plc_data.uzem and not self.plc_data.hiba and self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='gray', error_color='gray', process_color='green')
        # 1 1 0
        elif self.plc_data.uzem and self.plc_data.hiba and not self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='green', error_color='red', process_color='gray')
        # 0 1 0
        elif not self.plc_data.uzem and self.plc_data.hiba and not self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='gray', error_color='red', process_color='gray')
        # 1 0 0
        elif self.plc_data.uzem and not self.plc_data.hiba and not self.plc_data.folyamat:
            self.conveyors.indicator1_change_color(factory_color='green', error_color='gray', process_color='gray')
        # 0 0 0
        else:
            self.conveyors.indicator1_change_color(factory_color='gray', error_color='gray', process_color='gray')

    def indicator2_refresh(self):
        # 1 1
        if self.plc_data.megtelt_a and self.plc_data.megtelt_b:
            self.conveyors.indicator2_change_color(full_a_color='yellow', full_b_color='yellow')
        # 0 1
        elif not self.plc_data.megtelt_a and self.plc_data.megtelt_b:
            self.conveyors.indicator2_change_color(full_a_color='gray', full_b_color='yellow')
        # 1 0
        elif self.plc_data.megtelt_a and not self.plc_data.megtelt_b:
            self.conveyors.indicator2_change_color(full_a_color='yellow', full_b_color='gray')
        # 0 0
        else:
            self.conveyors.indicator2_change_color(full_a_color='gray', full_b_color='gray')

    def sensor_refresh(self):
        # 1 1 1
        if self.plc_data.sbe and self.plc_data.sa and self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='red', sensor_a_color='red', sensor_b_color='red')
        # 0 1 1
        elif not self.plc_data.sbe and self.plc_data.sa and self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='gray', sensor_a_color='red', sensor_b_color='red')
        # 1 0 1
        elif self.plc_data.sbe and not self.plc_data.sa and self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='red', sensor_a_color='gray', sensor_b_color='red')
        # 0 0 1
        elif not self.plc_data.sbe and not self.plc_data.sa and self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='gray', sensor_a_color='gray', sensor_b_color='red')
        # 1 1 0
        elif self.plc_data.sbe and self.plc_data.sa and not self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='red', sensor_a_color='red', sensor_b_color='gray')
        # 0 1 0
        elif not self.plc_data.sbe and self.plc_data.sa and not self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='gray', sensor_a_color='red', sensor_b_color='gray')
        # 1 0 0
        elif self.plc_data.sbe and not self.plc_data.sa and not self.plc_data.sb:
            self.conveyors.sensor_change_color(sensor_in_color='red', sensor_a_color='gray', sensor_b_color='gray')
        else:
            self.conveyors.sensor_change_color(sensor_in_color='gray', sensor_a_color='gray', sensor_b_color='gray')

    def conveyor1_refresh(self):
        # 1
        if self.plc_data.m1:
            self.conveyors.conveyor1_change_color(motor_color='green')
        # 0
        else:
            self.conveyors.conveyor1_change_color(motor_color='gray')

    def conveyor2_refresh(self):
        # 1 1
        if self.plc_data.m2a and self.plc_data.m2b:
            self.conveyors.conveyor2_change_color(motor_a_color='green', motor_b_color='green')
        # 0 1
        elif not self.plc_data.m2a and self.plc_data.m2b:
            self.conveyors.conveyor2_change_color(motor_a_color='gray', motor_b_color='green')
        # 1 0
        elif self.plc_data.m2a and not self.plc_data.m2b:
            self.conveyors.conveyor2_change_color(motor_a_color='green', motor_b_color='gray')
        # 0 0
        else:
            self.conveyors.conveyor2_change_color(motor_a_color='grey', motor_b_color='grey')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
