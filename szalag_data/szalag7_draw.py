from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from szalag_data.szalag7_data import Szalag7_Address


class Szalag7_View(ConveyorCanvas, IndicatorCanvas):
    CONVEYOR_WIDTH = 45
    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 300
    CONVEYOR4_LENGTH = 300

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH // 2
    CONVEYOR3_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH // 2
    CONVEYOR4_X_POSITION = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH // 2

    INDICATOR_COLUMN1_X_POSITION = CONVEYOR1_X_POSITION
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 150

    INDICATOR_ROW1_Y_POSITION = 10
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10

    CONVEYOR1_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20
    CONVEYOR3_Y_POSITION = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH + 20
    CONVEYOR4_Y_POSITION = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR4_X_POSITION + CONVEYOR4_LENGTH + 5
    FULL_HEIGHT = CONVEYOR4_Y_POSITION + CONVEYOR_WIDTH + 10

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'
        self.conveyor3_motor_color = 'gray'
        self.conveyor3_sensor_color = 'gray'
        self.conveyor4_motor_color = 'gray'
        self.conveyor4_sensor_color = 'gray'

        self.conveyor1_name_color = 'black'
        self.conveyor2_name_color = 'black'
        self.conveyor3_name_color = 'black'
        self.conveyor4_name_color = 'black'

        self.start_color = 'gray'
        self.stop_color = 'gray'

        self.factory_color = 'gray'
        self.error_color = 'gray'

        self.__buttons_drawing()
        self.__indicators_drawing()
        self.__conveyors_drawing()

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

    def conveyor4_change_color(self, motor_color, sensor_color):
        if self.conveyor4_motor_color != motor_color or self.conveyor4_sensor_color != sensor_color:
            self.conveyor4_motor_color = motor_color
            self.conveyor4_sensor_color = sensor_color
            self.__conveyors_drawing()

    def conveyor1_mame_change_color(self, name_color):
        if self.conveyor1_name_color != name_color:
            self.conveyor1_name_color = name_color
            self.__conveyors_drawing()

    def conveyor2_mame_change_color(self, name_color):
        if self.conveyor2_name_color != name_color:
            self.conveyor2_name_color = name_color
            self.__conveyors_drawing()

    def conveyor3_mame_change_color(self, name_color):
        if self.conveyor3_name_color != name_color:
            self.conveyor3_name_color = name_color
            self.__conveyors_drawing()

    def conveyor4_mame_change_color(self, name_color):
        if self.conveyor4_name_color != name_color:
            self.conveyor4_name_color = name_color
            self.__conveyors_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Szalag7_Address.START, color=self.start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Szalag7_Address.STOP, color=self.stop_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag7_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba [%s]' % Szalag7_Address.HIBA, color=self.error_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1', name_color=self.conveyor1_name_color,
                             circle1_name='M1\n[%s]' % Szalag7_Address.M1, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S1\n[%s]' % Szalag7_Address.S1, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2', name_color=self.conveyor2_name_color,
                             circle1_name='M2\n[%s]' % Szalag7_Address.M2, circle1_color=self.conveyor2_motor_color,
                             circle2_name='S2\n[%s]' % Szalag7_Address.S2, circle2_color=self.conveyor2_sensor_color)
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR3_LENGTH, name='Szalag 3', name_color=self.conveyor3_name_color,
                             circle1_name='M3\n[%s]' % Szalag7_Address.M3, circle1_color=self.conveyor3_motor_color,
                             circle2_name='S3\n[%s]' % Szalag7_Address.S3, circle2_color=self.conveyor3_sensor_color)
        self.create_conveyor(self.CONVEYOR4_X_POSITION,
                             self.CONVEYOR4_Y_POSITION,
                             length=self.CONVEYOR4_LENGTH, name='Szalag 4', name_color=self.conveyor4_name_color,
                             circle1_name='M4\n[%s]' % Szalag7_Address.M4, circle1_color=self.conveyor4_motor_color,
                             circle2_name='S4\n[%s]' % Szalag7_Address.S4, circle2_color=self.conveyor4_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag7_View(root)
    conveyor.pack()

    root.mainloop()
