from _view.plc_view import PLC_ViewA
from mozgatas_data.mozgatas1_data import Mozgatas1A_data
from mozgatas_data.mozgatas1_draw import Mozgatas1A_View


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Mozgatás 1A')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Mozgatás 1A')

        self.indicator = Mozgatas1A_View(self.process_frame)
        self.indicator.pack()

        self.plc_data = Mozgatas1A_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        super().loop()

        if self.plc_data.e0_is_changed() or self.plc_data.e1_is_changed() or self.plc_data.e2_is_changed():
            self.sensor_refresh()

        if self.plc_data.m_fel_is_changed() or self.plc_data.m_le_is_changed() or self.plc_data.m_fog_is_changed():
            self.indicator_refresh()

    def sensor_refresh(self):
        # 1 1 1
        if self.plc_data.e0 or self.plc_data.e1 or self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='green', sensor1_color='green', sensor2_color='green')
        # 0 1 1
        elif not self.plc_data.e0 or self.plc_data.e1 or self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='gray', sensor1_color='green', sensor2_color='green')
        # 1 0 1
        elif self.plc_data.e0 or not self.plc_data.e1 or self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='green', sensor1_color='gray', sensor2_color='green')
        # 0 0 1
        elif not self.plc_data.e0 or not self.plc_data.e1 or self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='gray', sensor1_color='gray', sensor2_color='green')
        # 1 1 0
        elif self.plc_data.e0 or self.plc_data.e1 or not self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='green', sensor1_color='green', sensor2_color='gray')
        # 0 1 0
        elif not self.plc_data.e0 or self.plc_data.e1 or not self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='gray', sensor1_color='green', sensor2_color='gray')
        # 1 0 0
        elif self.plc_data.e0 or not self.plc_data.e1 or not self.plc_data.e2:
            self.indicator.sensor_change_color(sensor0_color='green', sensor1_color='gray', sensor2_color='gray')
        # 0 0 0
        else:
            self.indicator.sensor_change_color(sensor0_color='gray', sensor1_color='gray', sensor2_color='gray')

    def indicator_refresh(self):
        # 1 1 1
        if self.plc_data.m_fel or self.plc_data.m_fog or self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='red', motor_stack_color='red', motor_down_color='red')
        # 0 1 1
        elif not self.plc_data.m_fel or self.plc_data.m_fog or self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='gray', motor_stack_color='red', motor_down_color='red')
        # 1 0 1
        elif self.plc_data.m_fel or not self.plc_data.m_fog or self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='gray', motor_stack_color='red', motor_down_color='gray')
        # 0 0 1
        elif not self.plc_data.m_fel or not self.plc_data.m_fog or self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='gray', motor_stack_color='gray', motor_down_color='red')
        # 1 1 0
        elif self.plc_data.m_fel or self.plc_data.m_fog or not self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='red', motor_stack_color='red', motor_down_color='gray')
        # 0 1 0
        elif not self.plc_data.m_fel or self.plc_data.m_fog or not self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='gray', motor_stack_color='red', motor_down_color='gray')
        # 1 0 0
        elif self.plc_data.m_fel or not self.plc_data.m_fog or not self.plc_data.m_le:
            self.indicator.indicator_change_color(motor_up_color='red', motor_stack_color='gray', motor_down_color='gray')
        # 0 0 0
        else:
            self.indicator.indicator_change_color(motor_up_color='gray', motor_stack_color='gray', motor_down_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
