from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.tank_canvas import TankCanvas, PipeCanvas, PumpCanvas
from atemelo_data.atemelo4_data import Atemelo4_Address


class Atemelo4_View(TankCanvas, PipeCanvas, SensorCanvas, PumpCanvas, IndicatorCanvas):

    TANK_WIDTH = 160
    TANK_HEIGHT = 240
    PIPE_WIDTH = 10
    PUMP_WIDTH = 40
    PUMP_NAME_SHIFT = 15
    INDICATOR_WIDTH = 25
    SENSOR_LINE_LENGTH = TANK_WIDTH + 10

    PUMP_A_PIPE_LENGTH = 150
    PUMP_B_PIPE_LENGTH = 150

    PUMP_PIPE_B_X_POSITION = 5
    TANK_X_POSITION = PUMP_B_PIPE_LENGTH - TANK_WIDTH // 4
    PUMP_PIPE_A_X_POSITION = TANK_X_POSITION + TANK_WIDTH * 3 // 4
    PUMP_A_MOTOR_X_POSITION = PUMP_PIPE_A_X_POSITION + PUMP_A_PIPE_LENGTH // 3
    PUMP_A_INDICATOR_X_POSITION = PUMP_PIPE_A_X_POSITION + PUMP_A_PIPE_LENGTH * 3 // 4
    PUMP_B_MOTOR_X_POSITION = PUMP_PIPE_B_X_POSITION + PUMP_A_PIPE_LENGTH * 2 // 3 - PUMP_WIDTH
    PUMP_B_INDICATOR_X_POSITION = PUMP_PIPE_B_X_POSITION + PUMP_A_PIPE_LENGTH // 4 - INDICATOR_WIDTH
    RECEIPT_X_POSITION = PUMP_PIPE_B_X_POSITION
    ERROR_LAMP_X_POSITION = PUMP_PIPE_B_X_POSITION

    TANK_Y_POSITION = 5
    SENSOR_1_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT * 3 // 4
    SENSOR_2_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT // 2
    SENSOR_3_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT // 4
    PUMP_PIPE_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT * 7 // 8
    PUMP_MOTOR_Y_POSITION = PUMP_PIPE_Y_POSITION - PUMP_WIDTH // 2 + PIPE_WIDTH // 2
    PUMP_INDICATOR_Y_POSITION = PUMP_PIPE_Y_POSITION - INDICATOR_WIDTH // 2 + PIPE_WIDTH // 2
    ERROR_LAMP_Y_POSITION = TANK_Y_POSITION + 15
    RECEIPT_Y_POSITION = ERROR_LAMP_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = PUMP_PIPE_A_X_POSITION + PUMP_A_PIPE_LENGTH + 5
    FULL_HEIGHT = TANK_Y_POSITION + TANK_HEIGHT + 25

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__sensor_1_color = 'gray'
        self.__sensor_2_color = 'gray'
        self.__sensor_3_color = 'gray'

        self.__motor_a_color = 'gray'
        self.__motor_b_color = 'gray'

        self.__flow_sensor_a_color = 'gray'
        self.__flow_sensor_b_color = 'gray'

        self.__receipt_color = 'gray'
        self.__error_lamp_color = 'gray'

        self.__feedback_drawing()
        self.__tank_drawing()
        self.__pump_a_drawing()
        self.__pump_b_drawing()

    def feedback_change_color(self, receipt_color, error_lamp_color, ):
        if self.__receipt_color != receipt_color or self.__error_lamp_color != error_lamp_color:
            self.__receipt_color = receipt_color
            self.__error_lamp_color = error_lamp_color
            self.__feedback_drawing()

    def tank_change_color(self, sensor_1_color, sensor_2_color, sensor_3_color):
        if self.__sensor_1_color != sensor_1_color or\
                self.__sensor_2_color != sensor_2_color or\
                self.__sensor_3_color != sensor_3_color:
            self.__sensor_1_color = sensor_1_color
            self.__sensor_2_color = sensor_2_color
            self.__sensor_3_color = sensor_3_color
            self.__tank_drawing()
            self.__pump_a_drawing()
            self.__pump_b_drawing()

    def pump_a_change_color(self, motor_color, flow_sensor_color):
        if self.__motor_a_color != motor_color or self.__flow_sensor_a_color != flow_sensor_color:
            self.__motor_a_color = motor_color
            self.__flow_sensor_a_color = flow_sensor_color
            self.__tank_drawing()
            self.__pump_a_drawing()
            self.__pump_b_drawing()

    def pump_b_change_color(self, motor_color, flow_sensor_color):
        if self.__motor_b_color != motor_color or self.__flow_sensor_b_color != flow_sensor_color:
            self.__motor_b_color = motor_color
            self.__flow_sensor_b_color = flow_sensor_color
            self.__tank_drawing()
            self.__pump_a_drawing()
            self.__pump_b_drawing()

    def __feedback_drawing(self):
        self.create_circle_indicator(x_position=self.ERROR_LAMP_X_POSITION,
                                     y_position=self.ERROR_LAMP_Y_POSITION,
                                     name='Hiba lámpa\n[%s]' % Atemelo4_Address.HIBA_LAMPA,
                                     color=self.__error_lamp_color)
        self.create_square_indicator(x_position=self.RECEIPT_X_POSITION,
                                     y_position=self.RECEIPT_Y_POSITION,
                                     name='Nyugta\n[%s]' % Atemelo4_Address.NYUGTA,
                                     color=self.__receipt_color)

    def __tank_drawing(self):
        self.create_tank(x_position=self.TANK_X_POSITION,
                         y_position=self.TANK_Y_POSITION,
                         tank_name='', tank_color='gray')
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_1_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 1 [%s]' % Atemelo4_Address.JELADO_1, color=self.__sensor_1_color)
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_2_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 2 [%s]' % Atemelo4_Address.JELADO_2, color=self.__sensor_2_color)
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_3_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 3 [%s]' % Atemelo4_Address.JELADO_3, color=self.__sensor_3_color)

    def __pump_a_drawing(self):
        self.create_horizontal_pipe(x_position=self.PUMP_PIPE_A_X_POSITION,
                                    y_position=self.PUMP_PIPE_Y_POSITION,
                                    length=self.PUMP_A_PIPE_LENGTH)
        self.create_pump(x_position=self.PUMP_A_MOTOR_X_POSITION,
                         y_position=self.PUMP_MOTOR_Y_POSITION,
                         name=' Motor A [%s]\nAramlas A [%s]' % (Atemelo4_Address.MOTOR_A, Atemelo4_Address.ARALMAS_A),
                         color=self.__motor_a_color)
        self.create_delta_indicator(x_position=self.PUMP_A_INDICATOR_X_POSITION,
                                    y_position=self.PUMP_INDICATOR_Y_POSITION,
                                    direction='right', color=self.__flow_sensor_a_color)

    def __pump_b_drawing(self):
        self.create_horizontal_pipe(x_position=self.PUMP_PIPE_B_X_POSITION,
                                    y_position=self.PUMP_PIPE_Y_POSITION,
                                    length=self.PUMP_B_PIPE_LENGTH)
        self.create_pump(x_position=self.PUMP_B_MOTOR_X_POSITION,
                         y_position=self.PUMP_MOTOR_Y_POSITION,
                         name=' Motor B[%s]\nAramlas B [%s]' % (Atemelo4_Address.MOTOR_B, Atemelo4_Address.ARAMLAS_B),
                         color=self.__motor_b_color)
        self.create_delta_indicator(x_position=self.PUMP_B_INDICATOR_X_POSITION,
                                    y_position=self.PUMP_INDICATOR_Y_POSITION,
                                    direction='left', color=self.__flow_sensor_b_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Atemelo4_View(root)
    tank.pack()

    root.mainloop()
