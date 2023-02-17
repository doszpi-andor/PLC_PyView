from _view.plc_view import PLC_ViewA
from atemelo_data.atemelo4_data import Atemelo4_data
from atemelo_data.atemelo4_draw import Atemelo4_View


class App(PLC_ViewA):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('Átemelő 4')
        self.name_label.config(text='Átemelő 4')

        self.tank = Atemelo4_View(self.process_frame)
        self.tank.pack()

        self.plc_data = Atemelo4_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        if self.plc_data.jeladi_1_is_changed() or\
                self.plc_data.jeladi_2_is_changed() or\
                self.plc_data.jeladi_3_is_changed():
            self.sensor_refresh()

        if self.plc_data.motor_a_is_changed() or self.plc_data.aramlas_a_is_changed():
            self.pump_a_refresh()

        if self.plc_data.motor_b_is_changed() or self.plc_data.aramlas_b_is_changed():
            self.pump_b_refresh()

        if self.plc_data.nyugta_is_changed() or self.plc_data.hiba_lampa_is_changed():
            self.feedback_refresh()

        super().loop()

    def sensor_refresh(self):
        # 1 1 1
        if self.plc_data.jelado_1 and self.plc_data.jelado_2 and self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='red', sensor_2_color='red', sensor_3_color='red')
        # 0 1 1
        elif not self.plc_data.jelado_1 and self.plc_data.jelado_2 and self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='gray', sensor_2_color='red', sensor_3_color='red')
        # 1 0 1
        elif self.plc_data.jelado_1 and not self.plc_data.jelado_2 and self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='red', sensor_2_color='gray', sensor_3_color='red')
        # 0 0 1
        elif not self.plc_data.jelado_1 and not self.plc_data.jelado_2 and self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='gray', sensor_2_color='gray', sensor_3_color='red')
        # 1 1 0
        elif self.plc_data.jelado_1 and self.plc_data.jelado_2 and not self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='red', sensor_2_color='red', sensor_3_color='gray')
        # 0 1 0
        elif not self.plc_data.jelado_1 and self.plc_data.jelado_2 and not self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='gray', sensor_2_color='red', sensor_3_color='gray')
        # 1 0 0
        elif self.plc_data.jelado_1 and not self.plc_data.jelado_2 and not self.plc_data.jelado_3:
            self.tank.tank_change_color(sensor_1_color='red', sensor_2_color='gray', sensor_3_color='gray')
        else:
            self.tank.tank_change_color(sensor_1_color='gray', sensor_2_color='gray', sensor_3_color='gray')

    def pump_a_refresh(self):
        # 1 1
        if self.plc_data.motor_a and self.plc_data.aramlas_a:
            self.tank.pump_a_change_color(motor_color='green', flow_sensor_color='yellow')
        # 0 1
        elif not self.plc_data.motor_a and self.plc_data.aramlas_a:
            self.tank.pump_a_change_color(motor_color='gray', flow_sensor_color='yellow')
        # 1 0
        elif self.plc_data.motor_a and not self.plc_data.aramlas_a:
            self.tank.pump_a_change_color(motor_color='green', flow_sensor_color='gray')
        # 0 0
        else:
            self.tank.pump_a_change_color(motor_color='gray', flow_sensor_color='gray')

    def pump_b_refresh(self):
        # 1 1
        if self.plc_data.motor_b and self.plc_data.aramlas_b:
            self.tank.pump_b_change_color(motor_color='green', flow_sensor_color='yellow')
        # 0 1
        elif not self.plc_data.motor_b and self.plc_data.aramlas_b:
            self.tank.pump_b_change_color(motor_color='gray', flow_sensor_color='yellow')
        # 1 0
        elif self.plc_data.motor_b and not self.plc_data.aramlas_b:
            self.tank.pump_b_change_color(motor_color='green', flow_sensor_color='gray')
        # 0 0
        else:
            self.tank.pump_b_change_color(motor_color='gray', flow_sensor_color='gray')

    def feedback_refresh(self):
        # 1 1
        if self.plc_data.nyugta and self.plc_data.hiba_lampa:
            self.tank.feedback_change_color(receipt_color='yellow', error_lamp_color='red')
        # 0 1
        elif not self.plc_data.nyugta and self.plc_data.hiba_lampa:
            self.tank.feedback_change_color(receipt_color='gray', error_lamp_color='red')
        # 1 0
        elif self.plc_data.nyugta and not self.plc_data.hiba_lampa:
            self.tank.feedback_change_color(receipt_color='yellow', error_lamp_color='gray')
        # 0 0
        else:
            self.tank.feedback_change_color(receipt_color='gray', error_lamp_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()