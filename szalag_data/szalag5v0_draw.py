from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag5v0_data import Szalag5v0_Address


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag5v0_View(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    SILO_X_POSITION = 5
    SILO_SENSOR_X_POSITION = SILO_X_POSITION + 5
    CONVEYOR1_X_POSITION = SILO_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    INDICATOR_COLUMN1_X_POSITION = SILO_X_POSITION + SILO_WIDTH + 320
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 120

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    INDICATOR_ROW1_Y_POSITION = SILO_Y_POSITION + 10
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo_motor_color = 'gray'
        self.silo_sensor_color = 'grey'
        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.nyugta_color = 'gray'
        self.start_color = 'gray'
        self.stop_color = 'gray'
        self.factory_color = 'gray'
        self.error_color = 'gray'

        self.__silo_drawing()
        self.__conveyors_drawing()
        self.__buttons_drawing()
        self.__indicators_drawing()

    def button_change_color(self, nyugta_color, start_color, stop_color):
        if self.nyugta_color != nyugta_color or self.start_color != start_color or self.stop_color != stop_color:
            self.nyugta_color = nyugta_color
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

    def conveyor1_change_color(self, motor_color, sensor_color):
        if self.conveyor1_motor_color != motor_color or self.conveyor1_sensor_color != sensor_color:
            self.conveyor1_motor_color = motor_color
            self.conveyor1_sensor_color = sensor_color
            self.__conveyors_drawing()

    def conveyor2_change_color(self, motor_color, sensor_color):
        if self.conveyor2_motor_color != motor_color or self.conveyor2_sensor_color != sensor_color:
            self.conveyor2_motor_color = motor_color
            self.conveyor2_sensor_color = sensor_color
            self.__conveyors_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Szalag5v0_Address.START, color=self.start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Szalag5v0_Address.STOP, color=self.stop_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Nyugta [%s]' % Szalag5v0_Address.NYUGTA, color=self.nyugta_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag5v0_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba [%s]' % Szalag5v0_Address.HIBA, color=self.error_color)

    def __silo_drawing(self):
        self.create_silo(self.SILO_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló',
                         motor_name='M1[%s]' % Szalag5v0_Address.M1, motor_color=self.silo_motor_color)
        self.create_sensor(self.SILO_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1\n[%s]' % Szalag5v0_Address.S1, color=self.silo_sensor_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M2\n[%s]' % Szalag5v0_Address.M2, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S2\n[%s]' % Szalag5v0_Address.S2, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M3\n[%s]' % Szalag5v0_Address.M3, circle1_color=self.conveyor2_motor_color,
                             circle2_name='S3\n[%s]' % Szalag5v0_Address.S3, circle2_color=self.conveyor2_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag5v0_View(root)
    conveyor.pack()

    root.mainloop()