from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas, AnalogCanvas
from _view.silo_camvas import SiloCanvas
from _view.wagon_canvas import WagonCanvas
from szalag_data.szalag3_data import Szalag3_Address


class Szalag3v2_View(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas, WagonCanvas, AnalogCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150
    CONVEYOR_WIDTH = 45
    WAGON_WIDTH = 200
    WAGON_HEIGHT = 80
    SENSOR_SQUARE = 20
    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 300

    SILO1_X_POSITION = 5
    SILO1_SENSOR_X_POSITION = SILO1_X_POSITION + 5
    CONVEYOR1_X_POSITION = SILO1_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH + 20
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3
    SILO2_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH - SILO_WIDTH
    SILO2_SENSOR_X_POSITION = SILO2_X_POSITION + 5

    WAGON_X_POSITION = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH * 3 // 4
    WAGON_SENSOR_X_POSITION = WAGON_X_POSITION + WAGON_WIDTH - SENSOR_SQUARE
    WIGHT_SENSOR_X_POSITION = WAGON_X_POSITION - 30

    INDICATOR1_COLUMN1_X_POSITION = SILO1_X_POSITION + SILO_WIDTH + 80
    INDICATOR1_COLUMN2_X_POSITION = INDICATOR1_COLUMN1_X_POSITION + 160

    INDICATOR2_COLUMN_X_POSITION = SILO1_X_POSITION

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION
    CONVEYOR3_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20
    WAGON_Y_POSITION = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH + 20
    WAGON_SENSOR_Y_POSITION = WAGON_Y_POSITION + WAGON_HEIGHT // 3
    WIGHT_SENSOR_Y_POSITION = WAGON_Y_POSITION

    INDICATOR1_ROW1_Y_POSITION = SILO_Y_POSITION + 10

    INDICATOR2_ROW1_Y_POSITION = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH + 40
    INDICATOR2_ROW2_Y_POSITION = INDICATOR2_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR2_ROW3_Y_POSITION = INDICATOR2_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = SILO2_X_POSITION + SILO_WIDTH + 60
    FULL_HEIGHT = WAGON_Y_POSITION + WAGON_HEIGHT

    __wight_sensor_id = None

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo1_motor_color = 'gray'
        self.silo2_motor_color = 'gray'
        self.silo1_sensor_color = 'gray'
        self.silo2_sensor_color = 'gray'

        self.silo1_empty_color = 'gray'
        self.silo2_empty_color = 'gray'

        self.conveyor1_motor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor3_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'
        self.conveyor3_sensor_color = 'gray'

        self.wagon_sensor_color = 'gray'

        self.factory_color = 'gray'
        self.conveyor_error_color = 'gray'
        self.wagon_error_color = 'gray'

        self.__wight_percent = 0

        self.__silo_drawing()
        self.__conveyor_drawing()
        self.__wagon_drawing()
        self.__indicators_drawing()
        self.__silo_indicators_drawing()

    def indicator_change_color(self, factory_color, conveyor_error_color, wagon_error_color):
        if self.factory_color != factory_color or self.conveyor_error_color != conveyor_error_color or self.wagon_error_color != wagon_error_color:
            self.factory_color = factory_color
            self.conveyor_error_color = conveyor_error_color
            self.wagon_error_color = wagon_error_color
            self.__indicators_drawing()

    def silo_indicator_change_color(self, silo1_empty_color, silo2_empty_color):
        if self.silo1_empty_color != silo1_empty_color or self.silo2_empty_color != silo2_empty_color:
            self.silo1_empty_color = silo1_empty_color
            self.silo2_empty_color = silo2_empty_color
            self.__silo_indicators_drawing()

    def silo1_change_color(self, motor_color, sensor_color):
        if self.silo1_motor_color != motor_color or self.silo1_sensor_color != sensor_color:
            self.silo1_motor_color = motor_color
            self.silo1_sensor_color = sensor_color
            self.__silo_drawing()

    def silo2_change_color(self, motor_color, sensor_color):
        if self.silo2_motor_color != motor_color or self.silo2_sensor_color != sensor_color:
            self.silo2_motor_color = motor_color
            self.silo2_sensor_color = sensor_color
            self.__silo_drawing()

    def conveyor1_change_color(self, motor_color, sensor_color):
        if self.conveyor1_motor_color != motor_color or self.conveyor1_sensor_color != sensor_color:
            self.conveyor1_motor_color = motor_color
            self.conveyor1_sensor_color = sensor_color
            self.__conveyor_drawing()

    def conveyor2_change_color(self, motor_color, sensor_color):
        if self.conveyor2_motor_color != motor_color or self.conveyor2_sensor_color != sensor_color:
            self.conveyor2_motor_color = motor_color
            self.conveyor2_sensor_color = sensor_color
            self.__conveyor_drawing()

    def conveyor3_change_color(self, motor_color, sensor_color):
        if self.conveyor3_motor_color != motor_color or self.conveyor3_sensor_color != sensor_color:
            self.conveyor3_motor_color = motor_color
            self.conveyor3_sensor_color = sensor_color
            self.__conveyor_drawing()

    def wagon_change_color(self, sensor_color):
        if self.wagon_sensor_color != sensor_color:
            self.wagon_sensor_color = sensor_color
            self.__wagon_drawing()

    def wagon_wight_change(self, wight_percent):
        if self.__wight_percent != wight_percent:
            self.__wight_percent = wight_percent
            self.__wagon_drawing()

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR2_COLUMN_X_POSITION,
                                     self.INDICATOR2_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag3_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR2_COLUMN_X_POSITION,
                                     self.INDICATOR2_ROW2_Y_POSITION,
                                     name='Szalag hiba [%s]' % Szalag3_Address.SZALAG_HIBA, color=self.conveyor_error_color)
        self.create_circle_indicator(self.INDICATOR2_COLUMN_X_POSITION,
                                     self.INDICATOR2_ROW3_Y_POSITION,
                                     name='Kocsi hiba [%s]' % Szalag3_Address.KOCSI_HOBA, color=self.wagon_error_color)

    def __silo_indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR1_COLUMN1_X_POSITION,
                                     self.INDICATOR1_ROW1_Y_POSITION,
                                     name='Siló 1 üres [%s]' % Szalag3_Address.SILO1_URES, color=self.silo1_empty_color)
        self.create_circle_indicator(self.INDICATOR1_COLUMN2_X_POSITION,
                                     self.INDICATOR1_ROW1_Y_POSITION,
                                     name='Siló 2 üres [%s]' % Szalag3_Address.SILO2_URES, color=self.silo2_empty_color)

    def __silo_drawing(self):
        self.create_silo(self.SILO1_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 1',
                         motor_name='M1[%s]' % Szalag3_Address.M1, motor_color=self.silo1_motor_color)
        self.create_sensor(self.SILO1_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1\n[%s]' % Szalag3_Address.S1, color=self.silo1_sensor_color)
        self.create_silo(self.SILO2_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 2',
                         motor_name='M2[%s]' % Szalag3_Address.M2, motor_color=self.silo2_motor_color)
        self.create_sensor(self.SILO2_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S2\n[%s]' % Szalag3_Address.S2, color=self.silo2_sensor_color)

    def __conveyor_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M3\n[%s]' % Szalag3_Address.M3, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S3\n[%s]' % Szalag3_Address.S3, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S4\n[%s]' % Szalag3_Address.S4, circle1_color=self.conveyor2_sensor_color,
                             circle2_name='M4\n[%s]' % Szalag3_Address.M4, circle2_color=self.conveyor2_motor_color)
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR3_LENGTH, name='Szalag 3',
                             circle1_name='M5\n[%s]' % Szalag3_Address.M5, circle1_color=self.conveyor3_motor_color,
                             circle2_name='S5\n[%s]' % Szalag3_Address.S5, circle2_color=self.conveyor3_sensor_color)

    def __wagon_drawing(self):
        self.create_wagon(self.WAGON_X_POSITION,
                          self.WAGON_Y_POSITION,
                          wagon_name='Vagon')
        self.create_sensor(self.WAGON_SENSOR_X_POSITION,
                           self.WAGON_SENSOR_Y_POSITION,
                           name='KP\n[%s]' % Szalag3_Address.KP, color=self.wagon_sensor_color)
        self.delete(self.__wight_sensor_id)
        self.__wight_sensor_id = self.create_analog(x_position=self.WIGHT_SENSOR_X_POSITION,
                                                    y_position=self.WIGHT_SENSOR_Y_POSITION,
                                                    height=self.WAGON_HEIGHT, marks_position=(10, 16, 80),
                                                    active_level=self.__wight_percent, active_color='red',
                                                    activ_level_print=True, name_position='left',
                                                    name='KS\n[%s]' % Szalag3_Address.KS)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag3v2_View(root)
    conveyor.pack()

    root.mainloop()
