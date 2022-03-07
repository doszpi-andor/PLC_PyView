from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag4v1_data import Szalag4v1_Address


class Szalag4v1_View(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    INDICATOR_WIDTH = 25

    CONVEYOR_WIDTH = 40

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 300

    CONVEYOR2_X_POSITION = 5
    CONVEYOR1_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH * 2 // 3
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    DIRECTION1_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION - 60
    DIRECTION2_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH - 30

    INDICATOR_COLUMN1_X_POSITION = CONVEYOR2_X_POSITION + 10
    INDICATOR_COLUMN2_X_POSITION = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH - 120

    SILO_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH // 2 - SILO_WIDTH // 2
    SILO_SENSOR_X_POSITION = SILO_X_POSITION + 5

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8

    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 40
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20
    CONVEYOR3_Y_POSITION = CONVEYOR2_Y_POSITION

    DIRECTION1_INDICATOR_Y_POSITION = CONVEYOR1_Y_POSITION - INDICATOR_WIDTH - 10
    DIRECTION2_INDICATOR_Y_POSITION = DIRECTION1_INDICATOR_Y_POSITION

    INDICATOR_ROW1_Y_POSITION = SILO_Y_POSITION + 10
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__silo_motor_color = 'gray'
        self.__silo_sensor_color = 'gray'

        self.__conveyor1_motor_color = 'gray'
        self.__conveyor1_left_color = 'gray'
        self.__conveyor1_right_color = 'gray'
        self.__conveyor1_sensor_color = 'gray'
        self.__conveyor2_motor_color = 'gray'
        self.__conveyor2_sensor_color = 'gray'
        self.__conveyor3_motor_color = 'gray'
        self.__conveyor3_sensor_color = 'gray'

        self.__start1_color = 'gray'
        self.__start2_color = 'gray'
        self.__stop_color = 'gray'

        self.__factory1_color = 'gray'
        self.__factory2_color = 'gray'
        self.__error_color = 'gray'

        self.__silo_drawing()
        self.__conveyors_drawing()
        self.__direction_drawing()
        self.__buttons_drawing()
        self.__indicators_drawing()

    def button_change_color(self, start1_color, start2_color, stop_color):
        if self.__start1_color != start1_color or \
                self.__start2_color != start2_color or \
                self.__stop_color != stop_color:
            self.__start1_color = start1_color
            self.__start2_color = start2_color
            self.__stop_color = stop_color
            self.__buttons_drawing()

    def indicator_change_color(self, factory1_color, factory2_color, error_color):
        if self.__factory1_color != factory1_color or \
                self.__factory2_color != factory2_color or \
                self.__error_color != error_color:
            self.__factory1_color = factory1_color
            self.__factory2_color = factory2_color
            self.__error_color = error_color
            self.__indicators_drawing()

    def silo_change_color(self, motor_color, sensor_color):
        if self.__silo_motor_color != motor_color or self.__silo_sensor_color != sensor_color:
            self.__silo_motor_color = motor_color
            self.__silo_sensor_color = sensor_color
            self.__silo_drawing()

    def conveyor1_change_color(self, motor_color, left_color, right_color, sensor_color):
        if self.__conveyor1_motor_color != motor_color or \
                self.__conveyor1_left_color != left_color or \
                self.__conveyor1_right_color != right_color or \
                self.__conveyor1_sensor_color != sensor_color:
            self.__conveyor1_motor_color = motor_color
            self.__conveyor1_left_color = left_color
            self.__conveyor1_right_color = right_color
            self.__conveyor1_sensor_color = sensor_color
            self.__direction_drawing()
            self.__conveyors_drawing()

    def conveyor2_change_color(self, motor_color, sensor_color):
        if self.__conveyor2_motor_color != motor_color or \
                self.__conveyor2_sensor_color != sensor_color:
            self.__conveyor2_motor_color = motor_color
            self.__conveyor2_sensor_color = sensor_color
            self.__conveyors_drawing()

    def conveyor3_change_color(self, motor_color, sensor_color):
        if self.__conveyor3_motor_color != motor_color or \
                self.__conveyor3_sensor_color != sensor_color:
            self.__conveyor3_motor_color = motor_color
            self.__conveyor3_sensor_color = sensor_color
            self.__conveyors_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start 1 [%s]' % Szalag4v1_Address.START1, color=self.__start1_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Start 2 [%s]' % Szalag4v1_Address.START2, color=self.__start2_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Stop [%s]' % Szalag4v1_Address.STOP, color=self.__stop_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem 1 [%s]' % Szalag4v1_Address.UZEM1, color=self.__factory1_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Üzem 2 [%s]' % Szalag4v1_Address.UZEM2, color=self.__factory2_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Hiba [%s]' % Szalag4v1_Address.HIBA, color=self.__error_color)

    def __silo_drawing(self):
        self.create_silo(self.SILO_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló',
                         motor_name='M1[%s]' % Szalag4v1_Address.M1, motor_color=self.__silo_motor_color)
        self.create_sensor(self.SILO_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1\n[%s]' % Szalag4v1_Address.S1, color=self.__silo_sensor_color)

    def __direction_drawing(self):
        self.create_delta_indicator(self.DIRECTION1_INDICATOR_X_POSITION,
                                    self.DIRECTION1_INDICATOR_Y_POSITION,
                                    name='M2_BAL\n[%s]' % Szalag4v1_Address.M2_BAL,
                                    direction='left',
                                    color=self.__conveyor1_left_color)
        self.create_delta_indicator(self.DIRECTION2_INDICATOR_X_POSITION,
                                    self.DIRECTION2_INDICATOR_Y_POSITION,
                                    name='M2_JOBB\n[%s]' % Szalag4v1_Address.M2_JOBB,
                                    direction='right',
                                    color=self.__conveyor1_right_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M2',
                             circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S2\n[%s]' % Szalag4v1_Address.S2,
                             circle2_color=self.__conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S3\n[%s]' % Szalag4v1_Address.S3,
                             circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M3\n[%s]' % Szalag4v1_Address.M3,
                             circle2_color=self.__conveyor2_motor_color)
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 3',
                             circle1_name='M4\n[%s]' % Szalag4v1_Address.M4,
                             circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S4\n[%s]' % Szalag4v1_Address.S4,
                             circle2_color=self.__conveyor3_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag4v1_View(root)
    conveyor.pack()

    root.mainloop()
