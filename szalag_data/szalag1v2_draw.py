from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag1v2_data import Szalag1v2_Address


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag1v2_View(SiloCanvas, ConveyorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 400

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH + 50
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    INDICATOR_COLUMN1_X_POSITION = CONVEYOR1_X_POSITION
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 150

    INDICATOR_COLUMN4_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH - 120
    INDICATOR_COLUMN3_X_POSITION = INDICATOR_COLUMN4_X_POSITION - 150

    INDICATOR_ROW1_Y_POSITION = 5
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    CONVEYOR1_Y_POSITION = INDICATOR_ROW2_Y_POSITION + CONVEYOR_WIDTH + 50
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION
    CONVEYOR3_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'
        self.conveyor3_motor_color = 'gray'
        self.conveyor3_sensor_color = 'gray'

        self.start1_color = 'gray'
        self.stop1_color = 'gray'
        self.start2_color = 'gray'
        self.stop2_color = 'gray'

        self.factory1_color = 'gray'
        self.factory2_color = 'gray'
        self.error1_color = 'gray'
        self.error2_color = 'gray'
        self.error3_color = 'gray'

        self.__buttons_drawing()
        self.__indicators_drawing()
        self.__conveyors_drawing()

    def button1_change_color(self, start_color, stop_color):
        if self.start1_color != start_color or self.stop1_color != stop_color:
            self.start1_color = start_color
            self.stop1_color = stop_color
            self.__buttons_drawing()

    def button2_change_color(self, start_color, stop_color):
        if self.start2_color != start_color or self.stop2_color != stop_color:
            self.start2_color = start_color
            self.stop2_color = stop_color
            self.__buttons_drawing()

    def factory_change_color(self, factory1_color, factory2_color):
        if self.factory1_color != factory1_color or self.factory2_color != factory2_color:
            self.factory1_color = factory1_color
            self.factory2_color = factory2_color
            self.__indicators_drawing()

    def error_change_color(self, error1_color, error2_color, error3_color):
        if self.error1_color != error1_color or\
                self.error2_color != error2_color or\
                self.error3_color != error3_color:
            self.error1_color = error1_color
            self.error2_color = error2_color
            self.error3_color = error3_color
            self.__indicators_drawing()

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

    def conveyor3_change_color(self, motor_color, sensor_color):
        if self.conveyor3_motor_color != motor_color or self.conveyor3_sensor_color != sensor_color:
            self.conveyor3_motor_color = motor_color
            self.conveyor3_sensor_color = sensor_color
            self.__conveyors_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start 1 [%s]' % Szalag1v2_Address.START1, color=self.start1_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop 1 [%s]' % Szalag1v2_Address.STOP1, color=self.stop1_color)
        self.create_square_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start 2 [%s]' % Szalag1v2_Address.START2, color=self.start2_color)
        self.create_square_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop 2 [%s]' % Szalag1v2_Address.STOP2, color=self.stop2_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem 1 [%s]' % Szalag1v2_Address.UZEM1, color=self.factory1_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Üzem 2 [%s]' % Szalag1v2_Address.UZEM2, color=self.factory2_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Hiba 1 [%s]' % Szalag1v2_Address.HIBA1, color=self.error1_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba 2 [%s]' % Szalag1v2_Address.HIBA2, color=self.error2_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Hiba 3 [%s]' % Szalag1v2_Address.HIBA3, color=self.error3_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1\n[%s]' % Szalag1v2_Address.M1, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S1\n[%s]' % Szalag1v2_Address.S1, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S2\n[%s]' % Szalag1v2_Address.S2, circle1_color=self.conveyor2_sensor_color,
                             circle2_name='M2\n[%s]' % Szalag1v2_Address.M2, circle2_color=self.conveyor2_motor_color)
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR3_LENGTH, name='Szalag 3',
                             circle1_name='M3\n[%s]' % Szalag1v2_Address.M3, circle1_color=self.conveyor3_motor_color,
                             circle2_name='S3\n[%s]' % Szalag1v2_Address.S3, circle2_color=self.conveyor3_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag1v2_View(root)
    conveyor.pack()

    root.mainloop()
