from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag1v0_data import Szalag1v0_Address


class Szalag1v0_View(SiloCanvas, ConveyorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    INDICATOR_COLUMN1_X_POSITION = CONVEYOR1_X_POSITION
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 150

    INDICATOR_COLUMN4_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH - 110
    INDICATOR_COLUMN3_X_POSITION = INDICATOR_COLUMN4_X_POSITION - 150

    INDICATOR_ROW1_Y_POSITION = 5
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10

    CONVEYOR1_Y_POSITION = INDICATOR_ROW2_Y_POSITION + CONVEYOR_WIDTH + 50
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.start_color = 'gray'
        self.stop_color = 'gray'
        self.receipt_color = 'gray'
        self.factory_color = 'gray'
        self.error1_color = 'gray'
        self.error2_color = 'gray'

        self.__buttons_drawing()
        self.__indicators_drawing()
        self.__conveyors_drawing()

    def button_change_color(self, start_color, stop_color, receipt_color):
        if self.start_color != start_color or self.stop_color != stop_color or self.receipt_color != receipt_color:
            self.start_color = start_color
            self.stop_color = stop_color
            self.receipt_color = receipt_color
            self.__buttons_drawing()

    def indicator_change_color(self, factory_color, error1_color, error2_color):
        if self.factory_color != factory_color or\
                self.error1_color != error1_color or\
                self.error2_color != error2_color:
            self.factory_color = factory_color
            self.error1_color = error1_color
            self.error2_color = error2_color
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

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start %s]' % Szalag1v0_Address.START, color=self.start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Szalag1v0_Address.STOP, color=self.stop_color)
        self.create_square_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Nyugta [%s]' % Szalag1v0_Address.NYUGTA, color=self.receipt_color)

    def __indicators_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag1v0_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Hiba 1 [%s]' % Szalag1v0_Address.HIBA1, color=self.error1_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba 2 [%s]' % Szalag1v0_Address.HIBA2, color=self.error2_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1\n[%s]' % Szalag1v0_Address.M1, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S1\n[%s]' % Szalag1v0_Address.S1, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M2\n[%s]' % Szalag1v0_Address.M2, circle1_color=self.conveyor2_motor_color,
                             circle2_name='S2\n[%s]' % Szalag1v0_Address.S2, circle2_color=self.conveyor2_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag1v0_View(root)
    conveyor.pack()

    root.mainloop()
