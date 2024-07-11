from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas, AnalogCanvas
from _view.tank_canvas import TankCanvas, ValveCanvas, PipeCanvas
from tartaly_data.tartaly6_data import Tartaly6_Address


class Tartaly6_View(TankCanvas, ValveCanvas, PipeCanvas, SensorCanvas, AnalogCanvas, IndicatorCanvas):
    TANK_WIDTH = 55
    TANK_HEIGHT = 120
    VALVE_WIDTH = 15
    VALVE_HEIGHT = 25
    SENSOR_SQUARE = 15
    SENSOR_FONT_SIZE = 9
    SENSOR_LINE_LENGTH = TANK_WIDTH + 10
    SENSOR_TEXT_LENGTH = 80
    ANALOG_SENSOR_WIDTH = 15
    ANALOG_SENSOR_FONT_SIZE = 9
    PIPE_WIDTH = 6
    INDICATOR_WIDTH = 20

    T1_TANK_X_POSITION = 170
    T2_TANK_X_POSITION = T1_TANK_X_POSITION - 120
    T3_TANK_X_POSITION = T1_TANK_X_POSITION + 120
    T2_TOP_VALVE_X_POSITION = T2_TANK_X_POSITION + TANK_WIDTH // 2 - VALVE_WIDTH // 2 + 60
    T3_TOP_VALVE_X_POSITION = T3_TANK_X_POSITION + TANK_WIDTH // 2 - VALVE_WIDTH // 2 - 60
    T2_ADD_VALVE_X_POSITION = T2_TANK_X_POSITION + TANK_WIDTH // 2 - VALVE_WIDTH // 2 - 60
    T3_ADD_VALVE_X_POSITION = T3_TANK_X_POSITION + TANK_WIDTH // 2 - VALVE_WIDTH // 2 + 60

    INDICATOR_COLUMN1_X_POSITION = T1_TANK_X_POSITION + TANK_WIDTH + SENSOR_TEXT_LENGTH + 30

    T1_TOP_VALVE_Y_POSITION = 10
    T1_TANK_Y_POSITION = T1_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 5
    T1_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT // 8

    T2_T3_TOP_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 50
    T2_T3_TANK_Y_POSITION = T2_T3_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 50
    T2_T3_BOTTOM_VALVE_Y_POSITION = T2_T3_TANK_Y_POSITION + TANK_HEIGHT + 5
    T2_T3_LEVEL_SENSOR_Y_POSITION = T2_T3_TANK_Y_POSITION + TANK_HEIGHT // 8

    INDICATOR_ROW1_Y_POSITION = T1_TANK_Y_POSITION
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = T3_ADD_VALVE_X_POSITION + 120
    FULL_HEIGHT = T2_T3_TANK_Y_POSITION + TANK_HEIGHT + VALVE_HEIGHT + 20

    __tank2_analog_id = None
    __tank3_analog_id = None

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank1_sensor_color = 'gray'
        self.__tank1_top_valve_color = 'gray'
        self.__tank2_top_valve_color = 'gray'
        self.__tank2_add_valve_color = 'gray'
        self.__tank2_bottom_valve_color = 'gray'
        self.__tank3_top_valve_color = 'gray'
        self.__tank3_add_valve_color = 'gray'
        self.__tank3_bottom_valve_color = 'gray'

        self.__start_color = 'gray'
        self.__stop_color = 'gray'
        self.__factory_color = 'gray'

        self.__tank2_level_percent = 0
        self.__tank3_level_percent = 0

        self.__pipe1_drawing()
        self.__pipe2_drawing()
        self.__pipe3_drawing()

        self.__operator_interface_drawing()

        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()

    def operator_interface_change_color(self, start_color, stop_color, factory_color):
        if self.__start_color != start_color or\
                self.__stop_color != stop_color or\
                self.__factory_color != factory_color:
            self.__start_color = start_color
            self.__stop_color = stop_color
            self.__factory_color = factory_color
            self.__operator_interface_drawing()

    def tank1_change_color(self, valve_color, sensor_color):
        if self.__tank1_top_valve_color != valve_color or self.__tank1_sensor_color != sensor_color:
            self.__tank1_top_valve_color = valve_color
            self.__tank1_sensor_color = sensor_color
            self.__tank1_drawing()

    def tank2_change_color(self, top_valve_color, add_valve_color, bottom_valve_color):
        if self.__tank2_top_valve_color != top_valve_color or\
                self.__tank2_add_valve_color != add_valve_color or\
                self.__tank2_bottom_valve_color != bottom_valve_color:
            self.__tank2_top_valve_color = top_valve_color
            self.__tank2_add_valve_color = add_valve_color
            self.__tank2_bottom_valve_color = bottom_valve_color
            self.__tank2_drawing()

    def tank2_change_level(self, level_percent):
        if self.__tank2_level_percent != level_percent:
            self.__tank2_level_percent = level_percent
            self.__tank2_drawing()

    def tank3_change_color(self, top_valve_color, add_valve_color, bottom_valve_color):
        if self.__tank3_top_valve_color != top_valve_color or\
                self.__tank3_add_valve_color != add_valve_color or\
                self.__tank3_bottom_valve_color != bottom_valve_color:
            self.__tank3_top_valve_color = top_valve_color
            self.__tank3_add_valve_color = add_valve_color
            self.__tank3_bottom_valve_color = bottom_valve_color
            self.__tank3_drawing()

    def tank3_change_level(self, level_percent):
        if self.__tank3_level_percent != level_percent:
            self.__tank3_level_percent = level_percent
            self.__tank3_drawing()

    def __operator_interface_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Tartaly6_Address.START, color=self.__start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Tartaly6_Address.STOP, color=self.__stop_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Üzem [%s]' % Tartaly6_Address.UZEM, color=self.__factory_color)

    def __pipe1_drawing(self):
        self.create_vertical_pipe(
            x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T1_TANK_Y_POSITION + self.TANK_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T1_TANK_Y_POSITION + self.TANK_HEIGHT + 10,
            x_end=self.T2_TOP_VALVE_X_POSITION + self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TOP_VALVE_Y_POSITION - 10)
        self.create_diagonal_pipe(
            x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T1_TANK_Y_POSITION + self.TANK_HEIGHT + 10,
            x_end=self.T3_TOP_VALVE_X_POSITION + self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TOP_VALVE_Y_POSITION - 10)

    def __pipe2_drawing(self):
        self.create_vertical_pipe(
            x_position=self.T2_TOP_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TOP_VALVE_Y_POSITION - 10,
            length=self.VALVE_HEIGHT + 20)
        self.create_vertical_pipe(
            x_position=self.T2_ADD_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TOP_VALVE_Y_POSITION - 10,
            length=self.VALVE_HEIGHT + 20)
        self.create_diagonal_pipe(
            x_start=self.T2_TOP_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_T3_TOP_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TANK_Y_POSITION - 10)
        self.create_diagonal_pipe(
            x_start=self.T2_ADD_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_T3_TOP_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TANK_Y_POSITION - 10)
        self.create_vertical_pipe(
            x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)

    def __pipe3_drawing(self):
        self.create_vertical_pipe(
            x_position=self.T3_TOP_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TOP_VALVE_Y_POSITION - 10,
            length=self.VALVE_HEIGHT + 20)
        self.create_vertical_pipe(
            x_position=self.T3_ADD_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TOP_VALVE_Y_POSITION - 10,
            length=self.VALVE_HEIGHT + 20)
        self.create_diagonal_pipe(
            x_start=self.T3_TOP_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_T3_TOP_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TANK_Y_POSITION - 10)
        self.create_diagonal_pipe(
            x_start=self.T3_ADD_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_T3_TOP_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_T3_TANK_Y_POSITION - 10)
        self.create_vertical_pipe(
            x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_T3_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)

    def __tank1_drawing(self):
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_TOP_VALVE_Y_POSITION,
                          name='T1_Tolt [%s]' % Tartaly6_Address.T1_TOLT, color=self.__tank1_top_valve_color)
        self.create_tank(x_position=self.T1_TANK_X_POSITION,
                         y_position=self.T1_TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        self.create_sensor(x_position=self.T1_TANK_X_POSITION,
                           y_position=self.T1_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T1_Teli\n[%s]' % Tartaly6_Address.T1_TELI, color=self.__tank1_sensor_color)

    def __tank2_drawing(self):
        self.create_valve(x_position=self.T2_TOP_VALVE_X_POSITION,
                          y_position=self.T2_T3_TOP_VALVE_Y_POSITION,
                          name='T2_Tolt [%s]' % Tartaly6_Address.T2_TOLT, color=self.__tank2_top_valve_color)
        self.create_valve(x_position=self.T2_ADD_VALVE_X_POSITION,
                          y_position=self.T2_T3_TOP_VALVE_Y_POSITION,
                          name='T2_Adalek [%s]' % Tartaly6_Address.T2_ADALEK, color=self.__tank2_add_valve_color)
        self.create_tank(x_position=self.T2_TANK_X_POSITION,
                         y_position=self.T2_T3_TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        self.delete(self.__tank2_analog_id)
        self.__tank2_analog_id = self.create_analog(x_position=self.T2_TANK_X_POSITION,
                                                    y_position=self.T2_T3_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=self.__tank2_level_percent,
                                                    activ_level_print=True, active_color='red',
                                                    name='T2_Szint [%s]\n' % Tartaly6_Address.T2_SZINT)
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_T3_BOTTOM_VALVE_Y_POSITION,
                          name='T2_Urit [%s]' % Tartaly6_Address.T2_URIT, color=self.__tank2_bottom_valve_color)

    def __tank3_drawing(self):
        self.create_valve(x_position=self.T3_TOP_VALVE_X_POSITION,
                          y_position=self.T2_T3_TOP_VALVE_Y_POSITION,
                          name='T3_Tolt [%s]' % Tartaly6_Address.T3_TOLT, color=self.__tank3_top_valve_color)
        self.create_valve(x_position=self.T3_ADD_VALVE_X_POSITION,
                          y_position=self.T2_T3_TOP_VALVE_Y_POSITION,
                          name='T3_Adalek [%s]' % Tartaly6_Address.T2_ADALEK, color=self.__tank3_add_valve_color)
        self.create_tank(x_position=self.T3_TANK_X_POSITION,
                         y_position=self.T2_T3_TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        self.delete(self.__tank3_analog_id)
        self.__tank3_analog_id = self.create_analog(x_position=self.T3_TANK_X_POSITION,
                                                    y_position=self.T2_T3_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=self.__tank3_level_percent,
                                                    activ_level_print=True, active_color='red',
                                                    name='T3_Szint [%s]\n' % Tartaly6_Address.T3_SZINT)
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_T3_BOTTOM_VALVE_Y_POSITION,
                          name='T3_Urit [%s]' % Tartaly6_Address.T3_URIT, color=self.__tank3_bottom_valve_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly6_View(root)
    tank.pack()

    root.mainloop()
