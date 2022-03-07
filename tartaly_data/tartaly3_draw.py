from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.tank_canvas import TankCanvas, ValveCanvas, PipeCanvas
from tartaly_data.tartaly3_data import Tartaly3_Address


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly3_View(TankCanvas, SensorCanvas, ValveCanvas, PipeCanvas, IndicatorCanvas):
    TANK_WIDTH = 90
    TANK_HEIGHT = 220
    SENSOR_SQUARE = 20
    SENSOR_LINE_LENGTH = TANK_WIDTH + 10
    SENSOR_TEXT_LENGTH = 80
    VALVE_WIDTH = 30
    VALVE_HEIGHT = 40
    PIPE_WIDTH = 10
    INDICATOR_WIDTH = 30

    TANK1_X_POSITION = 4
    TANK2_X_POSITION = TANK1_X_POSITION + SENSOR_LINE_LENGTH + SENSOR_SQUARE + SENSOR_TEXT_LENGTH
    TANK3_X_POSITION = TANK2_X_POSITION + SENSOR_LINE_LENGTH + SENSOR_SQUARE + SENSOR_TEXT_LENGTH

    INDICATOR_COLUMN1_X_POSITION = TANK3_X_POSITION + SENSOR_LINE_LENGTH + SENSOR_SQUARE + SENSOR_TEXT_LENGTH

    TOP_VALVE_Y_POSITION = PIPE_WIDTH + 10
    TANK_Y_POSITION = TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 10
    TOP_SENSOR_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT // 8
    BOTTOM_SENSOR_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT - TANK_HEIGHT // 8
    BOTTOM_VALVE_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT + 10
    BOTTOM_SHIFT = 10

    INDICATOR_ROW1_Y_POSITION = TANK_Y_POSITION
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 40
    INDICATOR_ROW4_Y_POSITION = INDICATOR_ROW3_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = INDICATOR_COLUMN1_X_POSITION + 150
    FULL_HEIGHT = BOTTOM_VALVE_Y_POSITION + ValveCanvas.VALVE_HEIGHT + BOTTOM_SHIFT

    HORIZONTAL_PIPE_LENGTH = TANK3_X_POSITION + TANK_WIDTH // 2 + PipeCanvas.PIPE_WIDTH // 2

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank1_top_valve_color = 'gray'
        self.__tank1_top_sensor_color = 'gray'
        self.__tank1_bottom_sensor_color = 'gray'
        self.__tank2_top_valve_color = 'gray'
        self.__tank2_top_sensor_color = 'gray'
        self.__tank2_bottom_sensor_color = 'gray'
        self.__tank3_top_valve_color = 'gray'
        self.__tank3_top_sensor_color = 'gray'
        self.__tank3_bottom_sensor_color = 'gray'

        self.__start_color = 'gray'
        self.__stop_color = 'gray'

        self.__on_color = 'gray'
        self.__off_color = 'gray'

        self.__pipe_drawing()
        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()
        self.__buttons_drawing()
        self.__indicators_drawing()

    def button_change_color(self, start_color, stop_color):
        if self.__start_color != start_color or self.__stop_color != stop_color:
            self.__start_color = start_color
            self.__stop_color = stop_color
            self.__buttons_drawing()

    def indicators_change_color(self, on_color, off_color):
        if self.__on_color != on_color or self.__off_color != off_color:
            self.__on_color = on_color
            self.__off_color = off_color
            self.__indicators_drawing()

    def tank1_change_color(self, top_valve_color, top_sensor_color, bottom_sensor_color):
        """
        T1 tank colors change (valve and sensors)
        :param top_valve_color: color name string
        :param top_sensor_color: color name string
        :param bottom_sensor_color: color name string
        """
        if self.__tank1_top_valve_color != top_valve_color or \
                self.__tank1_top_sensor_color != top_sensor_color or \
                self.__tank1_bottom_sensor_color != bottom_sensor_color:
            self.__tank1_top_valve_color = top_valve_color
            self.__tank1_top_sensor_color = top_sensor_color
            self.__tank1_bottom_sensor_color = bottom_sensor_color
            self.__tank1_drawing()

    def tank2_change_color(self, top_valve_color, top_sensor_color, bottom_sensor_color):
        """
        T2 tank colors change (valve and sensors)
        :param top_valve_color: color name string
        :param top_sensor_color: color name string
        :param bottom_sensor_color: color name string
        """
        if self.__tank2_top_valve_color != top_valve_color or \
                self.__tank2_top_sensor_color != top_sensor_color or \
                self.__tank2_bottom_sensor_color != bottom_sensor_color:
            self.__tank2_top_valve_color = top_valve_color
            self.__tank2_top_sensor_color = top_sensor_color
            self.__tank2_bottom_sensor_color = bottom_sensor_color
            self.__tank2_drawing()

    def tank3_change_color(self, top_valve_color, top_sensor_color, bottom_sensor_color):
        """
        T3 tank colors change (valve and sensors)
        :param top_valve_color: color name string
        :param top_sensor_color: color name string
        :param bottom_sensor_color: color name string
        """
        if self.__tank3_top_valve_color != top_valve_color or \
                self.__tank3_top_sensor_color != top_sensor_color or \
                self.__tank3_bottom_sensor_color != bottom_sensor_color:
            self.__tank3_top_valve_color = top_valve_color
            self.__tank3_top_sensor_color = top_sensor_color
            self.__tank3_bottom_sensor_color = bottom_sensor_color
            self.__tank3_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Tartaly3_Address.START, color=self.__start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Tartaly3_Address.STOP, color=self.__stop_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Bekapcsolva [%s]' % Tartaly3_Address.BEKAPCSOLVA, color=self.__on_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW4_Y_POSITION,
                                     name='Kikapcsolva [%s]' % Tartaly3_Address.KIKAPCSOLVA, color=self.__off_color)

    def __pipe_drawing(self):
        self.create_horizontal_pipe(x_position=1, y_position=1,
                                    length=self.HORIZONTAL_PIPE_LENGTH)
        self.create_vertical_pipe(x_position=self.TANK1_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=self.PIPE_WIDTH,
                                  length=self.FULL_HEIGHT)
        self.create_vertical_pipe(x_position=self.TANK2_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=self.PIPE_WIDTH,
                                  length=self.FULL_HEIGHT)
        self.create_vertical_pipe(x_position=self.TANK3_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=self.PIPE_WIDTH,
                                  length=self.FULL_HEIGHT)

    def __tank1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.TANK1_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.TOP_VALVE_Y_POSITION,
                          name='T1_Tolt [%s]' % Tartaly3_Address.T1_TOLT, color=self.__tank1_top_valve_color)
        self.create_tank(x_position=self.TANK1_X_POSITION,
                         y_position=self.TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.TANK1_X_POSITION,
                           y_position=self.TOP_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T1_Felso\n[%s]' % Tartaly3_Address.T1_FELSO, color=self.__tank1_top_sensor_color)
        self.create_sensor(x_position=self.TANK1_X_POSITION,
                           y_position=self.BOTTOM_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T1_Also\n[%s]' % Tartaly3_Address.T1_ALSO, color=self.__tank1_bottom_sensor_color)
        self.create_valve(x_position=self.TANK1_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.BOTTOM_VALVE_Y_POSITION,
                          name='', color='gray')

    def __tank2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.TANK2_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.TOP_VALVE_Y_POSITION,
                          name='T2_Tolt [%s]' % Tartaly3_Address.T2_TOLT, color=self.__tank2_top_valve_color)
        self.create_tank(x_position=self.TANK2_X_POSITION,
                         y_position=self.TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.TANK2_X_POSITION,
                           y_position=self.TOP_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T2_Felso\n[%s]' % Tartaly3_Address.T2_FELSO, color=self.__tank2_top_sensor_color)
        self.create_sensor(x_position=self.TANK2_X_POSITION,
                           y_position=self.BOTTOM_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T2_Also\n[%s]' % Tartaly3_Address.T2_ALSO, color=self.__tank2_bottom_sensor_color)
        self.create_valve(x_position=self.TANK2_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.BOTTOM_VALVE_Y_POSITION,
                          name='', color='gray')

    def __tank3_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.TANK3_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.TOP_VALVE_Y_POSITION,
                          name='T3_Tolt [%s]' % Tartaly3_Address.T3_TOLT, color=self.__tank3_top_valve_color)
        self.create_tank(x_position=self.TANK3_X_POSITION, y_position=self.TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.TANK3_X_POSITION,
                           y_position=self.TOP_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T3_Felso\n[%s]' % Tartaly3_Address.T3_FELSO, color=self.__tank3_top_sensor_color)
        self.create_sensor(x_position=self.TANK3_X_POSITION,
                           y_position=self.BOTTOM_SENSOR_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='T3_Also\n[%s]' % Tartaly3_Address.T3_ALSO, color=self.__tank3_bottom_sensor_color)
        self.create_valve(x_position=self.TANK3_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.BOTTOM_VALVE_Y_POSITION,
                          name='', color='gray')


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly3_View(root)
    tank.pack()

    tank.tank1_change_color('red', 'green', 'blue')
    tank.tank2_change_color('blue', 'red', 'green')
    tank.tank3_change_color('green', 'blue', 'red')

    root.mainloop()
