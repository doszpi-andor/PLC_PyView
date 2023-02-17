from tkinter import Tk

from _view.sensor_canvas import SensorCanvas
from _view.tank_canvas import TankCanvas, PipeCanvas


class Atemelo4_View(TankCanvas, PipeCanvas, SensorCanvas):

    TANK_WIDTH = 160
    TANK_HEIGHT = 240
    SENSOR_LINE_LENGTH = TANK_WIDTH + 10

    PUMP_A_PIPE_LENGTH = 100
    PUMP_B_PIPE_LENGTH = 100

    PUMP_PIPE_B_X_POSITION = 0
    TANK_X_POSITION = PUMP_B_PIPE_LENGTH - TANK_WIDTH // 4
    PUMP_PIPE_A_X_POSITION = TANK_X_POSITION + TANK_WIDTH * 3 // 4

    TANK_Y_POSITION = 5
    SENSOR_1_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT * 3 // 4
    SENSOR_2_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT // 2
    SENSOR_3_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT // 4
    PUMP_PIPE_Y_POSITION = TANK_Y_POSITION + TANK_HEIGHT * 7 // 8

    FULL_WIDTH = 400
    FULL_HEIGHT = 400

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank_drawing()

    def __tank_drawing(self):
        self.create_tank(x_position=self.TANK_X_POSITION,
                         y_position=self.TANK_Y_POSITION,
                         tank_name='', tank_color='gray')
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_1_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 1', color='red')
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_2_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 2', color='gray')
        self.create_sensor(x_position=self.TANK_X_POSITION,
                           y_position=self.SENSOR_3_Y_POSITION,
                           line_length=self.SENSOR_LINE_LENGTH,
                           name='Jelado 3', color='gray')
        self.create_horizontal_pipe(x_position=self.PUMP_PIPE_A_X_POSITION,
                                    y_position=self.PUMP_PIPE_Y_POSITION,
                                    length=self.PUMP_A_PIPE_LENGTH)
        self.create_horizontal_pipe(x_position=self.PUMP_PIPE_B_X_POSITION,
                                    y_position=self.PUMP_PIPE_Y_POSITION,
                                    length=self.PUMP_A_PIPE_LENGTH)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Atemelo4_View(root)
    tank.pack()

    root.mainloop()
