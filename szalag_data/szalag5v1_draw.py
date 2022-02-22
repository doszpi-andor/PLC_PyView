from tkinter import Tk

from _view.conveyor_canvas import ConveyorCanvas
from _view.silo_camvas import SiloCanvas
from szalag_data.szalag5v1_data import Szalag5v1_Address


class Szalag5v1_View(SiloCanvas, ConveyorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 140

    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300

    SILO1_X_POSITION = 5
    SILO2_X_POSITION = SILO1_X_POSITION + SILO_WIDTH + 10
    CONVEYOR1_X_POSITION = SILO1_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    SILO_Y_POSITION = 5
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=800, height=480, **kw)

        self.silo1_motor_color = 'gray'
        self.silo2_motor_color = 'gray'
        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.__silos_drawing()
        self.__conveyors_drawing()

    def __silos_drawing(self):
        self.create_silo(self.SILO1_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 1', motor_name='M1', motor_color=self.silo1_motor_color)
        self.create_silo(self.SILO2_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 2', motor_name='M2', motor_color=self.silo2_motor_color)

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
