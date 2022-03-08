from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas
from _view.wagon_canvas import WagonCanvas
from szalag_data.szalag2v1_data import Szalag2v1_Address


class Szalag2v1_View(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas, WagonCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150
    CONVEYOR_WIDTH = 40
    WAGON_WIDTH = 200
    WAGON_HEIGHT = 80
    SENSOR_SQUARE = 20
    INDICATOR_WIDTH = 30

    CONVEYOR_LENGTH = 400

    SILO_X_POSITION = 5
    SILO_SENSOR_X_POSITION = SILO_X_POSITION + 5
    CONVEYOR_X_POSITION = SILO_X_POSITION
    WAGON_X_POSITION = CONVEYOR_X_POSITION + CONVEYOR_LENGTH * 3 // 4
    WAGON_SENSOR1_X_POSITION = WAGON_X_POSITION
    WAGON_SENSOR2_X_POSITION = WAGON_X_POSITION + WAGON_WIDTH - SENSOR_SQUARE
    WIGHT_SENSOR_X_POSITION = WAGON_X_POSITION + WAGON_WIDTH // 2 - SENSOR_SQUARE // 2

    INDICATOR_COLUMN1_X_POSITION = SILO_X_POSITION + SILO_WIDTH + 160
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 120

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    WAGON_Y_POSITION = CONVEYOR_Y_POSITION + CONVEYOR_WIDTH + 20
    WAGON_SENSOR_Y_POSITION = WAGON_Y_POSITION + WAGON_HEIGHT // 3
    WIGHT_SENSOR_Y_POSITION = WAGON_SENSOR_Y_POSITION + WAGON_HEIGHT

    INDICATOR_ROW1_Y_POSITION = SILO_Y_POSITION + 10
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = WAGON_X_POSITION + WAGON_WIDTH + 30
    FULL_HEIGHT = WIGHT_SENSOR_Y_POSITION + SENSOR_SQUARE

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo_motor_color = 'gray'
        self.silo_sensor_color = 'grey'
        self.conveyor_motor_color = 'gray'
        self.conveyor_sensor_color = 'gray'
        self.wagon_sensor1_color = 'gray'
        self.wagon_sensor2_color = 'gray'
        self.wight_sensor_color = 'gray'

        self.start_color = 'gray'
        self.stop_color = 'gray'
        self.factory_color = 'gray'
        self.error_color = 'gray'

        self.__silo_drawing()
        self.__conveyor_drawing()
        self.__wagon_drawing()
        self.__buttons_drawing()
        self.__indicators_drawing()

    def button_change_color(self, start_color, stop_color):
        if self.start_color != start_color or self.stop_color != stop_color:
            self.start_color = start_color
            self.stop_color = stop_color
            self.__buttons_drawing()

    def indicator_change_color(self, factory_color, error_color):
        if self.factory_color != factory_color or self.error_color != error_color:
            self.factory_color = factory_color
            self.error_color = error_color
            self.__indicators_drawing()

    def silo_change_color(self, motor_color, sensor_color):
        if self.silo_motor_color != motor_color or self.silo_sensor_color != sensor_color:
            self.silo_motor_color = motor_color
            self.silo_sensor_color = sensor_color
            self.__silo_drawing()

    def conveyor_change_color(self, motor_color, sensor_color):
        if self.conveyor_motor_color != motor_color or self.conveyor_sensor_color != sensor_color:
            self.conveyor_motor_color = motor_color
            self.conveyor_sensor_color = sensor_color
            self.__conveyor_drawing()

    def wagon_change_color(self, sensor1_color, sensor2_color, wight_color):
        if self.wagon_sensor1_color != sensor1_color or \
                self.wagon_sensor2_color != sensor2_color or \
                self.wight_sensor_color != wight_color:
            self.wagon_sensor1_color = sensor1_color
            self.wagon_sensor2_color = sensor2_color
            self.wight_sensor_color = wight_color
            self.__wagon_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Szalag2v1_Address.START, color=self.start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Szalag2v1_Address.STOP, color=self.stop_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag2v1_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba [%s]' % Szalag2v1_Address.HIBA, color=self.error_color)

    def __silo_drawing(self):
        self.create_silo(self.SILO_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló',
                         motor_name='M1[%s]' % Szalag2v1_Address.M1, motor_color=self.silo_motor_color)
        self.create_sensor(self.SILO_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1\n[%s]' % Szalag2v1_Address.S1, color=self.silo_sensor_color)

    def __conveyor_drawing(self):
        self.create_conveyor(self.CONVEYOR_X_POSITION,
                             self.CONVEYOR_Y_POSITION,
                             length=self.CONVEYOR_LENGTH, name='Szalag 1',
                             circle1_name='M2\n[%s]' % Szalag2v1_Address.M2, circle1_color=self.conveyor_motor_color,
                             circle2_name='S2\n[%s]' % Szalag2v1_Address.S2, circle2_color=self.conveyor_sensor_color)

    def __wagon_drawing(self):
        self.create_wagon(self.WAGON_X_POSITION,
                          self.WAGON_Y_POSITION,
                          wagon_name='Vagon')
        self.create_sensor(self.WAGON_SENSOR1_X_POSITION,
                           self.WAGON_SENSOR_Y_POSITION,
                           name='KP1\n[%s]' % Szalag2v1_Address.KP1, color=self.wagon_sensor1_color)
        self.create_sensor(self.WAGON_SENSOR2_X_POSITION,
                           self.WAGON_SENSOR_Y_POSITION,
                           name='KP2\n[%s]' % Szalag2v1_Address.KP2, color=self.wagon_sensor2_color)
        self.create_sensor(self.WIGHT_SENSOR_X_POSITION,
                           self.WIGHT_SENSOR_Y_POSITION,
                           name='KS [%s]' % Szalag2v1_Address.KS, color=self.wight_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag2v1_View(root)
    conveyor.pack()

    root.mainloop()
