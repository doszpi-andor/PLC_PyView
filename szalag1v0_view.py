
from tkinter import Frame, W, RIGHT, X, LEFT

from _view.conveyor_view import ConveyorView
from _view.indicator_view import IndicatorSquare, IndicatorOval
from _view.plc_view import PLC_View
from szalag_data.szalag1v0_data import Szalag1v0_Address, Szalag1v0_data
from szalag_data.szalag1v0_draw import Szalag1v0_View


class App(PLC_View):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Szalag 1v0')

        # noinspection SpellCheckingInspection
        self.name_label.config(text='Szalag 1v0')

        self.conveyors = Szalag1v0_View(self.process_frame)
        self.conveyors.pack()

        self.plc_data = Szalag1v0_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):
        super().loop()

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed() or self.plc_data.nyugta_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed() or self.plc_data.hiba1_is_changed() or self.plc_data.hiba2_is_changed():
            self.indicator_refresh()

        if self.plc_data.m1_is_changed() or self.plc_data.s1_is_changed():
            self.conveyor1_refresh()

        if self.plc_data.m2_is_changed() or self.plc_data.s2_is_changed():
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

    def indicator_refresh(self):
        # 1 1 1
        if self.plc_data.uzem and self.plc_data.hiba1 and self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='green', error1_color='red', error2_color='red')
        # 0 1 1
        elif not self.plc_data.uzem and self.plc_data.hiba1 and self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='gray', error1_color='red', error2_color='red')
        # 1 0 1
        elif self.plc_data.uzem and not self.plc_data.hiba1 and self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='green', error1_color='gray', error2_color='red')
        # 0 0 1
        elif not self.plc_data.uzem and not self.plc_data.hiba1 and self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='gray', error1_color='gray', error2_color='red')
        # 1 1 0
        elif self.plc_data.uzem and self.plc_data.hiba1 and not self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='green', error1_color='red', error2_color='gray')
        # 0 1 0
        elif not self.plc_data.uzem and self.plc_data.hiba1 and not self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='gray', error1_color='red', error2_color='gray')
        # 1 0 0
        elif self.plc_data.uzem and not self.plc_data.hiba1 and not self.plc_data.hiba2:
            self.conveyors.indicator_change_color(factory_color='green', error1_color='gray', error2_color='gray')
        else:
            self.conveyors.indicator_change_color(factory_color='gray', error1_color='gray', error2_color='gray')

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


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
