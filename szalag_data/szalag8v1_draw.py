from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag8v1_data import Szalag8v1_Address


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag8v1_View(SiloCanvas, ConveyorCanvas, IndicatorCanvas, SensorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    SENSOR_SQUARE = 20

    CONVEYOR_WIDTH = 45

    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    INDICATOR_COLUMN1_X_POSITION = CONVEYOR1_X_POSITION
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 150

    INDICATOR_COLUMN4_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH - 130
    INDICATOR_COLUMN3_X_POSITION = INDICATOR_COLUMN4_X_POSITION - 150

    INDICATOR_ROW1_Y_POSITION = 5
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    CONVEYOR1_Y_POSITION = INDICATOR_ROW3_Y_POSITION + CONVEYOR_WIDTH + 50
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH + 80
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH + 40

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.conveyor1_motor_color = 'gray'
        self.conveyor2_motor_a_color = 'gray'
        self.conveyor2_motor_b_color = 'gray'

        self.sencor_in_color = 'gray'
        self.sensor_a_color = 'gray'
        self.sensor_b_color = 'gray'

        self.start_color = 'gray'
        self.stop_color = 'gray'
        self.receipt_color = 'gray'
        self.full_a_color = 'gray'
        self.full_b_color = 'gray'
        self.process_color = 'gray'
        self.factory_color = 'gray'
        self.error_color = 'gray'

        self.__buttons_drawing()
        self.__indicators1_drawing()
        self.__indicators2_drawing()
        self.__sensor_drawing()
        self.__conveyors_drawing()

    def button_change_color(self, start_color, stop_color, receipt_color):
        if self.start_color != start_color or self.stop_color != stop_color or self.receipt_color != receipt_color:
            self.start_color = start_color
            self.stop_color = stop_color
            self.receipt_color = receipt_color
            self.__buttons_drawing()

    def indicator1_change_color(self, factory_color, error_color, process_color):
        if self.factory_color != factory_color or\
                self.error_color != error_color or\
                self.process_color != process_color:
            self.factory_color = factory_color
            self.error_color = error_color
            self.process_color = process_color
            self.__indicators1_drawing()

    def indicator2_change_color(self, full_a_color, full_b_color):
        if self.full_a_color != full_a_color or\
                self.full_b_color != full_b_color:
            self.full_a_color = full_a_color
            self.full_b_color = full_b_color
            self.__indicators2_drawing()

    def sensor_change_color(self, sensor_in_color, sensor_a_color, sensor_b_color):
        if self.sencor_in_color != sensor_in_color or self.sensor_a_color != sensor_a_color or\
                self.sensor_b_color != sensor_b_color:
            self.sencor_in_color = sensor_in_color
            self.sensor_a_color = sensor_a_color
            self.sensor_b_color = sensor_b_color
            self.__sensor_drawing()

    def conveyor1_change_color(self, motor_color):
        if self.conveyor1_motor_color != motor_color:
            self.conveyor1_motor_color = motor_color
            self.__conveyors_drawing()

    def conveyor2_change_color(self, motor_a_color, motor_b_color):
        if self.conveyor2_motor_a_color != motor_a_color or self.conveyor2_motor_b_color != motor_b_color:
            self.conveyor2_motor_a_color = motor_a_color
            self.conveyor2_motor_b_color = motor_b_color
            self.__conveyors_drawing()

    def __buttons_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start [%s]' % Szalag8v1_Address.START, color=self.start_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Stop [%s]' % Szalag8v1_Address.STOP, color=self.stop_color)
        self.create_square_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Nyugta [%s]' % Szalag8v1_Address.NYUGTA, color=self.receipt_color)

    def __indicators1_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem [%s]' % Szalag8v1_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Hiba [%s]' % Szalag8v1_Address.HIBA, color=self.error_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Folyamat [%s]' % Szalag8v1_Address.FOLYAMAT, color=self.process_color)

    def __indicators2_drawing(self):
        self.create_circle_indicator(self.INDICATOR_COLUMN3_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Megtelt A [%s]' % Szalag8v1_Address.MEGTELT_A, color=self.full_a_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN4_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Megtelt B [%s]' % Szalag8v1_Address.MEGTELT_B, color=self.full_b_color)

    def __sensor_drawing(self):
        self.create_sensor(self.CONVEYOR1_X_POSITION + 40,
                           self.CONVEYOR1_Y_POSITION - self.SENSOR_SQUARE,
                           name='SBE [%s]' % Szalag8v1_Address.SBE, color=self.sencor_in_color, line_length=40)
        self.create_sensor(self.CONVEYOR2_X_POSITION - 30,
                           self.CONVEYOR2_Y_POSITION + self.CONVEYOR_WIDTH + self.SENSOR_SQUARE,
                           name='SA\n[%s]' % Szalag8v1_Address.SA, color=self.sensor_a_color, line_length=50)
        self.create_sensor(self.CONVEYOR2_X_POSITION + self.CONVEYOR2_LENGTH - 30,
                           self.CONVEYOR2_Y_POSITION + self.CONVEYOR_WIDTH + self.SENSOR_SQUARE,
                           name='SB\n[%s]' % Szalag8v1_Address.SB, color=self.sensor_b_color, line_length=50)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1\n[%s]' % Szalag8v1_Address.M1, circle1_color=self.conveyor1_motor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M2')
        self.create_delta_indicator(self.CONVEYOR2_X_POSITION + 50,
                                    self.CONVEYOR2_Y_POSITION + (self.CONVEYOR_WIDTH - self.INDICATOR_WIDTH) // 2,
                                    direction='left',
                                    name='M2A\n[%s]' % Szalag8v1_Address.M2A, color=self.conveyor2_motor_a_color)
        self.create_delta_indicator(self.CONVEYOR2_X_POSITION + self.CONVEYOR2_LENGTH - self.INDICATOR_WIDTH - 90,
                                    self.CONVEYOR2_Y_POSITION + (self.CONVEYOR_WIDTH - self.INDICATOR_WIDTH) // 2,
                                    direction='right',
                                    name='M2B\n[%s]' % Szalag8v1_Address.M2B, color=self.conveyor2_motor_b_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Szalag8v1_View(root)
    conveyor.pack()

    root.mainloop()
