from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas, AnalogCanvas
from _view.tank_canvas import TankCanvas, ValveCanvas, HeatingCanvas, RotorCanvas, PipeCanvas
from tartaly_data.tartaly1_data import Tartaly1_Address


# noinspection PyPep8Naming,SpellCheckingInspection
class Tartaly1_View(TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, RotorCanvas, PipeCanvas,
                    IndicatorCanvas):
    TANK_WIDTH = 60
    TANK_HEIGHT = 130
    VALVE_WIDTH = 20
    VALVE_HEIGHT = 30
    SENSOR_SQUARE = 15
    SENSOR_LINE_LENGTH = TANK_WIDTH + 10
    SENSOR_TEXT_LENGTH = 80
    ANALOG_SENSOR_WIDTH = 15
    HEATING_WIDTH = 30
    HEATING_HEIGHT = 30
    ROTOR_WIDTH = 40
    PIPE_WIDTH = 7
    INDICATOR_WIDTH = 20

    T1_TANK_X_POSITION = 100
    T1_THERMOMETER_X_POSITION = T1_TANK_X_POSITION - ANALOG_SENSOR_WIDTH - 10
    T2_TANK_X_POSITION = T1_TANK_X_POSITION + TANK_WIDTH + SENSOR_TEXT_LENGTH + 10
    T3_TANK_X_POSITION = T1_TANK_X_POSITION + (TANK_WIDTH * 2 + SENSOR_TEXT_LENGTH + 10) // 2 - TANK_WIDTH // 2

    INDICATOR_COLUMN1_X_POSITION = T3_TANK_X_POSITION + TANK_WIDTH + SENSOR_TEXT_LENGTH + 10

    T1_TOP_VALVE_Y_POSITION = 10
    T1_TANK_Y_POSITION = T1_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 10
    T1_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT // 8
    T1_THERMOMETER_Y_POSITION = T1_TANK_Y_POSITION - 15
    T1_BOTTOM_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 10
    T1_HEATING_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T2_TOP_VALVE_Y_POSITION = 10
    T2_TANK_Y_POSITION = T2_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 10
    T2_SENSOR_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT // 8
    T2_BOTTOM_VALVE_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT + 10

    T3_TANK_Y_POSITION = T2_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 70
    T3_BOTTOM_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 10
    T3_LEVEL_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 8
    T3_ROTOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 2

    INDICATOR_ROW1_Y_POSITION = T3_TANK_Y_POSITION
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = T2_TANK_X_POSITION + SENSOR_LINE_LENGTH + SENSOR_SQUARE + SENSOR_TEXT_LENGTH
    FULL_HEIGHT = T3_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 10

    __tank1_analog_id = None
    __tank3_analog_id = None

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank1_sensor_color = 'gray'
        self.__tank1_heating_color = 'black'
        self.__tank1_top_valve_color = 'gray'
        self.__tank1_bottom_valve_color = 'gray'
        self.__tank2_sensor_color = 'gray'
        self.__tank2_top_valve_color = 'gray'
        self.__tank2_bottom_valve_color = 'gray'
        self.__tank3_rotor_color = 'yellow'
        self.__tank3_bottom_valve_color = 'gray'

        self.__start_color = 'gray'
        self.__stop_color = 'gray'

        self.__tank1_temperature_percent = 0
        self.__tank3_level_percent = 0

        self.__pipe_drawing()
        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()
        self.__buttons_drawing()

    def button_change_color(self, start_color, stop_color):
        if self.__stop_color != start_color or self.__stop_color != stop_color:
            self.__start_color = start_color
            self.__stop_color = stop_color
            self.__buttons_drawing()

    def tank1_change_color(self, sensor_color, heating_color):
        if self.__tank1_sensor_color != sensor_color or self.__tank1_heating_color != heating_color:
            self.__tank1_sensor_color = sensor_color
            self.__tank1_heating_color = heating_color
            self.__tank1_drawing()

    def tank1_change_valve_color(self, top_valve_color, bottom_valve_color):
        if self.__tank1_top_valve_color != top_valve_color or self.__tank1_bottom_valve_color != bottom_valve_color:
            self.__tank1_top_valve_color = top_valve_color
            self.__tank1_bottom_valve_color = bottom_valve_color
            self.__tank1_drawing()

    def tank2_change_color(self, sensor_color, top_valve_color, bottom_valve_color):
        if self.__tank2_sensor_color != sensor_color or \
                self.__tank2_top_valve_color != top_valve_color or \
                self.__tank2_bottom_valve_color != bottom_valve_color:
            self.__tank2_sensor_color = sensor_color
            self.__tank2_top_valve_color = top_valve_color
            self.__tank2_bottom_valve_color = bottom_valve_color
            self.__tank2_drawing()

    def tank3_change_color(self, rotor_color, bottom_valve_color):
        if self.__tank3_rotor_color != rotor_color or self.__tank3_bottom_valve_color != bottom_valve_color:
            self.__tank3_rotor_color = rotor_color
            self.__tank3_bottom_valve_color = bottom_valve_color
            self.__tank3_drawing()

    def tank1_change_heating_level(self, temperature_percent):
        if self.__tank1_temperature_percent != temperature_percent:
            self.__tank1_temperature_percent = temperature_percent
            self.__tank1_drawing()

    def tank3_change_level(self, level_percent):
        if self.__tank3_level_percent != level_percent:
            self.__tank3_level_percent = level_percent
            self.__tank3_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Tartaly1_Address.START, color=self.__start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Tartaly1_Address.STOP, color=self.__stop_color)

    def __pipe_drawing(self):

        self.create_vertical_pipe(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=0,
                                  length=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_start=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
                                  x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_end=self.T3_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=0,
                                  length=self.T2_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(x_start=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_start=self.T2_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
                                  x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_end=self.T3_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=self.T3_TANK_Y_POSITION - 10,
                                  length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)

    def __tank1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_TOP_VALVE_Y_POSITION,
                          name='T1_Tolt [%s]' % Tartaly1_Address.T1_TOLT, color=self.__tank1_top_valve_color)
        self.create_tank(x_position=self.T1_TANK_X_POSITION,
                         y_position=self.T1_TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T1_TANK_X_POSITION,
                           y_position=self.T1_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T1_Teli\n[%s]' % Tartaly1_Address.T1_TELI, color=self.__tank1_sensor_color)
        self.delete(self.__tank1_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank1_analog_id = self.create_analog(x_position=self.T1_THERMOMETER_X_POSITION,
                                                    y_position=self.T1_THERMOMETER_Y_POSITION,
                                                    height=80, marks_position=(40, 60),
                                                    active_level=self.__tank1_temperature_percent, active_color='red',
                                                    activ_level_print=True, name_position='left',
                                                    name='T1_Homerseklet\n[%s]' % Tartaly1_Address.T1_HOMERSEKLET)
        self.create_heating(x_position=self.T1_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T1_Fut\n[%s]' % Tartaly1_Address.T1_FUT, color=self.__tank1_heating_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_BOTTOM_VALVE_Y_POSITION,
                          name='T1_Urit [%s]' % Tartaly1_Address.T1_URIT, color=self.__tank1_bottom_valve_color)

    def __tank2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_TOP_VALVE_Y_POSITION,
                          name='T2_Tolt [%s]' % Tartaly1_Address.T2_TOLT, color=self.__tank2_top_valve_color)
        self.create_tank(x_position=self.T2_TANK_X_POSITION,
                         y_position=self.T2_TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T2_TANK_X_POSITION,
                           y_position=self.T2_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T2_Teli\n[%s]' % Tartaly1_Address.T2_TELI, color=self.__tank2_sensor_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_BOTTOM_VALVE_Y_POSITION,
                          name='T2_Urit [%s]' % Tartaly1_Address.T2_URIT, color=self.__tank2_bottom_valve_color)

    def __tank3_drawing(self):
        self.create_tank(x_position=self.T3_TANK_X_POSITION,
                         y_position=self.T3_TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        self.delete(self.__tank3_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank3_analog_id = self.create_analog(x_position=self.T3_TANK_X_POSITION,
                                                    y_position=self.T3_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=self.__tank3_level_percent,
                                                    activ_level_print=True, active_color='red',
                                                    name='T3_Szint [%s]\n' % Tartaly1_Address.T3_SZINT)
        # noinspection SpellCheckingInspection
        self.create_rotor(x_position=self.T3_TANK_X_POSITION + 5,
                          y_position=self.T3_ROTOR_Y_POSITION,
                          name='T3_Kever [%s]' % Tartaly1_Address.T3_KEVER, color=self.__tank3_rotor_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_BOTTOM_VALVE_Y_POSITION,
                          name='T3_Urit [%s]' % Tartaly1_Address.T3_URIT, color=self.__tank3_bottom_valve_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly1_View(root)
    tank.pack()

    root.mainloop()
