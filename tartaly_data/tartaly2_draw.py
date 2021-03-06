from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas, AnalogCanvas
from _view.tank_canvas import TankCanvas, ValveCanvas, HeatingCanvas, PipeCanvas
from tartaly_data.tartaly2_data import Tartaly2_Address


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly2_View(TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, PipeCanvas, IndicatorCanvas):
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
    HEATING_WIDTH = 30
    HEATING_HEIGHT = 30
    ROTOR_WIDTH = 40
    PIPE_WIDTH = 6
    INDICATOR_WIDTH = 20

    T1_TANK_X_POSITION = 50
    T1_TANK_THERMO_SENSOR_POSITION = T1_TANK_X_POSITION + 65
    T2_ADDITIVE_VALVE_X_POSITION = 250
    T2_TANK_X_POSITION = T1_TANK_X_POSITION + (T2_ADDITIVE_VALVE_X_POSITION - (
            T1_TANK_X_POSITION + TANK_WIDTH // 2)) // 2

    T3_TANK_X_POSITION = 350
    T3_TANK_THERMO_SENSOR_POSITION = T3_TANK_X_POSITION + 65
    T4_ADDITIVE_VALVE_X_POSITION = 500
    T4_TANK_X_POSITION = T3_TANK_X_POSITION + (T4_ADDITIVE_VALVE_X_POSITION - (
            T3_TANK_X_POSITION + TANK_WIDTH // 2)) // 2

    INDICATOR_COLUMN1_X_POSITION = 5

    T1_TOP_VALVE_Y_POSITION = 10
    T1_TANK_Y_POSITION = T1_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 5
    T1_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT // 8
    T1_HOT_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + (TANK_HEIGHT // 8) * 5
    T1_COLD_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + (TANK_HEIGHT // 8) * 7
    T1_BOTTOM_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 5
    T1_HEATING_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T2_ADDITIVE_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 5

    T2_TANK_Y_POSITION = T1_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 60
    T2_BOTTOM_VALVE_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT + 5
    T2_LEVEL_SENSOR_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT // 8

    T3_TOP_VALVE_Y_POSITION = 10
    T3_TANK_Y_POSITION = T3_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 5
    T3_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 8
    T3_HOT_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + (TANK_HEIGHT // 8) * 5
    T3_COLD_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + (TANK_HEIGHT // 8) * 7
    T3_BOTTOM_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 5
    T3_HEATING_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T4_ADDITIVE_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 5

    T4_TANK_Y_POSITION = T3_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 60
    T4_BOTTOM_VALVE_Y_POSITION = T4_TANK_Y_POSITION + TANK_HEIGHT + 5
    T4_LEVEL_SENSOR_Y_POSITION = T4_TANK_Y_POSITION + TANK_HEIGHT // 8

    INDICATOR_ROW1_Y_POSITION = T4_TANK_Y_POSITION
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = T4_ADDITIVE_VALVE_X_POSITION + 200
    FULL_HEIGHT = T2_TANK_Y_POSITION + TANK_HEIGHT + VALVE_HEIGHT + 80

    __tank2_analog_id = None
    __tank4_analog_id = None

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank1_top_valve_color = 'gray'
        self.__tank1_sensor_color = 'gray'
        self.__tank1_hot_sensor_color = 'gray'
        self.__tank1_cold_sensor_color = 'gray'
        self.__tank1_heating_color = 'black'
        self.__tank1_bottom_valve_color = 'gray'
        self.__tank2_add_valve_color = 'gray'
        self.__tank2_bottom_valve_color = 'gray'

        self.__tank2_level_percent = 0

        self.__tank3_top_valve_color = 'gray'
        self.__tank3_sensor_color = 'gray'
        self.__tank3_hot_sensor_color = 'gray'
        self.__tank3_cold_sensor_color = 'gray'
        self.__tank3_heating_color = 'black'
        self.__tank3_bottom_valve_color = 'gray'
        self.__tank4_add_valve_color = 'gray'
        self.__tank4_bottom_valve_color = 'gray'

        self.__start_color = 'gray'
        self.__stop_color = 'gray'

        self.__tank4_level_percent = 0

        self.__pipe12_drawing()
        self.__pipe34_drawing()
        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()
        self.__tank4_drawing()
        self.__buttons_drawing()

    def button_change_color(self, start_color, stop_color):
        if self.__stop_color != start_color or self.__stop_color != stop_color:
            self.__start_color = start_color
            self.__stop_color = stop_color
            self.__buttons_drawing()

    def tank1_change_color(self, top_valve_color, bottom_valve_color, heating_color):
        if self.__tank1_top_valve_color != top_valve_color or\
                self.__tank1_bottom_valve_color != bottom_valve_color or\
                self.__tank1_heating_color != heating_color:
            self.__tank1_top_valve_color = top_valve_color
            self.__tank1_bottom_valve_color = bottom_valve_color
            self.__tank1_heating_color = heating_color
            self.__tank1_drawing()

    def tank1_change_sensor_color(self, sensor_color, hot_sensor_color, clod_sensor_color):
        if self.__tank1_sensor_color != sensor_color or\
                self.__tank1_hot_sensor_color != hot_sensor_color or\
                self.__tank1_cold_sensor_color != clod_sensor_color:
            self.__tank1_sensor_color = sensor_color
            self.__tank1_hot_sensor_color = hot_sensor_color
            self.__tank1_cold_sensor_color = clod_sensor_color
            self.__tank1_drawing()

    def tank2_change_color(self, add_valve_color, bottom_valve_color):
        if self.__tank2_add_valve_color != add_valve_color or self.__tank2_bottom_valve_color != bottom_valve_color:
            self.__tank2_add_valve_color = add_valve_color
            self.__tank2_bottom_valve_color = bottom_valve_color
            self.__tank2_drawing()

    def tank2_change_level(self, level_percent):
        if self.__tank2_level_percent != level_percent:
            self.__tank2_level_percent = level_percent
            self.__tank2_drawing()

    def tank3_change_color(self, top_valve_color, bottom_valve_color, heating_color):
        if self.__tank3_top_valve_color != top_valve_color or \
                self.__tank3_bottom_valve_color != bottom_valve_color or \
                self.__tank3_heating_color != heating_color:
            self.__tank3_top_valve_color = top_valve_color
            self.__tank3_bottom_valve_color = bottom_valve_color
            self.__tank3_heating_color = heating_color
            self.__tank3_drawing()

    def tank3_change_sensor_color(self, sensor_color, hot_sensor_color, clod_sensor_color):
        if self.__tank3_sensor_color != sensor_color or \
                self.__tank3_hot_sensor_color != hot_sensor_color or \
                self.__tank3_cold_sensor_color != clod_sensor_color:
            self.__tank3_sensor_color = sensor_color
            self.__tank3_hot_sensor_color = hot_sensor_color
            self.__tank3_cold_sensor_color = clod_sensor_color
            self.__tank3_drawing()

    def tank4_change_color(self, add_valve_color, bottom_valve_color):
        if self.__tank4_add_valve_color != add_valve_color or self.__tank4_bottom_valve_color != bottom_valve_color:
            self.__tank4_add_valve_color = add_valve_color
            self.__tank4_bottom_valve_color = bottom_valve_color
            self.__tank4_drawing()

    def tank4_change_level(self, level_percent):
        if self.__tank4_level_percent != level_percent:
            self.__tank4_level_percent = level_percent
            self.__tank4_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Tartaly2_Address.START, color=self.__start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Tartaly2_Address.STOP, color=self.__stop_color)

    def __pipe12_drawing(self):

        self.create_vertical_pipe(
            x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T2_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T2_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T2_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)
        self.create_diagonal_pipe(
            x_start=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 20,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2 + (
                    self.T4_TANK_X_POSITION - self.T2_TANK_X_POSITION) // 2,
            y_end=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 80)

    def __pipe34_drawing(self):

        self.create_vertical_pipe(
            x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T3_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T3_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T4_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T4_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T4_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T4_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T4_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T4_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T4_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)
        self.create_diagonal_pipe(
            x_start=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T4_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 20,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2 + (
                    self.T4_TANK_X_POSITION - self.T2_TANK_X_POSITION) // 2,
            y_end=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 80)

    def __tank1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_TOP_VALVE_Y_POSITION,
                          name='T1_Tolt [%s]' % Tartaly2_Address.T1_TOLT, color=self.__tank1_top_valve_color)
        self.create_tank(x_position=self.T1_TANK_X_POSITION,
                         y_position=self.T1_TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T1_TANK_X_POSITION,
                           y_position=self.T1_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T1_Teli\n[%s]' % Tartaly2_Address.T1_TELI, color=self.__tank1_sensor_color)
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T1_TANK_THERMO_SENSOR_POSITION,
                           y_position=self.T1_HOT_SENSOR_Y_POSITION,
                           name='T1_Meleg\n[%s]' % Tartaly2_Address.T1_MELEG, color=self.__tank1_hot_sensor_color)
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T1_TANK_THERMO_SENSOR_POSITION,
                           y_position=self.T1_COLD_SENSOR_Y_POSITION,
                           name='T1_Hideg\n[%s]' % Tartaly2_Address.T1_HIDEG, color=self.__tank1_cold_sensor_color)
        self.create_heating(x_position=self.T1_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T1_Fut\n[%s]' % Tartaly2_Address.T1_FUT, color=self.__tank1_heating_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_BOTTOM_VALVE_Y_POSITION,
                          name='T1_Urit [%s]' % Tartaly2_Address.T1_URIT, color=self.__tank1_bottom_valve_color)

    def __tank2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_ADDITIVE_VALVE_X_POSITION,
                          y_position=self.T2_ADDITIVE_VALVE_Y_POSITION,
                          name='T2_Adalek\n[%s]' % Tartaly2_Address.T2_ADALEK, color=self.__tank2_add_valve_color)
        self.create_tank(x_position=self.T2_TANK_X_POSITION,
                         y_position=self.T2_TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        self.delete(self.__tank2_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank2_analog_id = self.create_analog(x_position=self.T2_TANK_X_POSITION,
                                                    y_position=self.T2_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=self.__tank2_level_percent,
                                                    activ_level_print=True, active_color='red',
                                                    name='T2_Szint [%s]\n' % Tartaly2_Address.T2_SZINT)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_BOTTOM_VALVE_Y_POSITION,
                          name='T2_Urit [%s]' % Tartaly2_Address.T2_URIT, color=self.__tank2_bottom_valve_color)

    def __tank3_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_TOP_VALVE_Y_POSITION,
                          name='T3_Tolt [%s]' % Tartaly2_Address.T3_TOLT, color=self.__tank3_top_valve_color)
        self.create_tank(x_position=self.T3_TANK_X_POSITION,
                         y_position=self.T3_TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T3_TANK_X_POSITION,
                           y_position=self.T3_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T3_Teli\n[%s]' % Tartaly2_Address.T3_TELI, color=self.__tank3_sensor_color)
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T3_TANK_THERMO_SENSOR_POSITION,
                           y_position=self.T3_HOT_SENSOR_Y_POSITION,
                           name='T3_Meleg\n[%s]' % Tartaly2_Address.T3_MELEG, color=self.__tank3_hot_sensor_color)
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T3_TANK_THERMO_SENSOR_POSITION,
                           y_position=self.T3_COLD_SENSOR_Y_POSITION,
                           name='T3_Hideg\n[%s]' % Tartaly2_Address.T3_HIDEG, color=self.__tank3_cold_sensor_color)
        self.create_heating(x_position=self.T3_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T3_Fut\n[%s]' % Tartaly2_Address.T3_FUT, color=self.__tank3_heating_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_BOTTOM_VALVE_Y_POSITION,
                          name='T3_Urit [%s]' % Tartaly2_Address.T3_URIT, color=self.__tank3_bottom_valve_color)

    def __tank4_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T4_ADDITIVE_VALVE_X_POSITION,
                          y_position=self.T4_ADDITIVE_VALVE_Y_POSITION,
                          name='T4_Adalek\n[%s]' % Tartaly2_Address.T4_ADALEK, color=self.__tank4_add_valve_color)
        self.create_tank(x_position=self.T4_TANK_X_POSITION,
                         y_position=self.T4_TANK_Y_POSITION,
                         tank_name='T4', tank_color='gray')
        self.delete(self.__tank4_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank4_analog_id = self.create_analog(x_position=self.T4_TANK_X_POSITION,
                                                    y_position=self.T4_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=self.__tank4_level_percent,
                                                    activ_level_print=True, active_color='red',
                                                    name='T4_Szint [%s]\n' % Tartaly2_Address.T4_SZINT)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T4_BOTTOM_VALVE_Y_POSITION,
                          name='T4_Urit [%s]' % Tartaly2_Address.T4_URIT, color=self.__tank4_bottom_valve_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly2_View(root)
    tank.pack()

    root.mainloop()
