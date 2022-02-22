from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag5v1_data import Szalag5v1_Address


class Szalag5v1_View(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    INDICATOR_WIDTH = 30

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    SILO1_X_POSITION = 5
    SILO2_X_POSITION = SILO1_X_POSITION + SILO_WIDTH + 80
    SILO1_SENSOR_X_POSITION = SILO1_X_POSITION + 5
    SILO2_SENSOR_X_POSITION = SILO2_X_POSITION + 5
    CONVEYOR1_X_POSITION = SILO1_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    INDICATOR_COLUMN1_X_POSITION = SILO2_X_POSITION + SILO_WIDTH + 220
    INDICATOR_COLUMN2_X_POSITION = INDICATOR_COLUMN1_X_POSITION + 100

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    INDICATOR_ROW1_Y_POSITION = SILO_Y_POSITION + 10
    INDICATOR_ROW2_Y_POSITION = INDICATOR_ROW1_Y_POSITION + INDICATOR_WIDTH + 10
    INDICATOR_ROW3_Y_POSITION = INDICATOR_ROW2_Y_POSITION + INDICATOR_WIDTH + 10

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo1_motor_color = 'gray'
        self.silo2_motor_color = 'gray'
        self.silo1_sensor_color = 'grey'
        self.silo2_sensor_color = 'gray'
        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.start1_color = 'gray'
        self.start2_color = 'gray'
        self.stop_color = 'gray'
        self.factory_color = 'gray'
        self.error_color = 'gray'

        self.__silos_drawing()
        self.__conveyors_drawing()
        self.__indicators_drawing()

    def __indicators_drawing(self):
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Start 1\n[%s]' % Szalag5v1_Address.START1, color=self.start1_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Start 2\n[%s]' % Szalag5v1_Address.START2, color=self.start2_color)
        self.create_square_indicator(self.INDICATOR_COLUMN1_X_POSITION,
                                     self.INDICATOR_ROW3_Y_POSITION,
                                     name='Stop\n[%s]' % Szalag5v1_Address.STOP, color=self.stop_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW1_Y_POSITION,
                                     name='Üzem\n[%s]' % Szalag5v1_Address.UZEM, color=self.factory_color)
        self.create_circle_indicator(self.INDICATOR_COLUMN2_X_POSITION,
                                     self.INDICATOR_ROW2_Y_POSITION,
                                     name='Hiba\n[%s]' % Szalag5v1_Address.HIBA, color=self.error_color)

    def __silos_drawing(self):
        self.create_silo(self.SILO1_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 1',
                         motor_name='M1[%s]' % Szalag5v1_Address.M1, motor_color=self.silo1_motor_color)
        self.create_sensor(self.SILO1_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1\n[%s]' % Szalag5v1_Address.S1, color=self.silo1_sensor_color)
        self.create_silo(self.SILO2_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 2',
                         motor_name='M2[%s]' % Szalag5v1_Address.M2, motor_color=self.silo2_motor_color)
        self.create_sensor(self.SILO2_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S2\n[%s]' % Szalag5v1_Address.S2, color=self.silo2_sensor_color)

    def __conveyors_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1\n[%s]' % Szalag5v1_Address.M1, circle1_color=self.conveyor1_motor_color,
                             circle2_name='S1\n[%s]' % Szalag5v1_Address.S1, circle2_color=self.conveyor1_sensor_color)
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M2\n[%s]' % Szalag5v1_Address.M2, circle1_color=self.conveyor2_motor_color,
                             circle2_name='S2\n[%s]' % Szalag5v1_Address.S2, circle2_color=self.conveyor2_sensor_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Szalag5v1_View(root)
    tank.pack()

    root.mainloop()
