from tkinter import Tk

from _view.tank_canvas import TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, PipeCanvas


class Tartaly2_View(TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, PipeCanvas):
    TANK_WIDTH = 55
    TANK_HEIGHT = 120
    VALVE_WIDTH = 15
    VALVE_HEIGHT = 25
    INDICATOR_SQUARE = 15
    INDICATOR_LINE_LENGTH = TANK_WIDTH + 10
    INDICATOR_TEXT_LENGTH = 80
    ANALOG_INDICATOR_WIDTH = 15
    HEATING_WIDTH = 30
    HEATING_HEIGHT = 30
    ROTOR_WIDTH = 40
    PIPE_WIDTH = 6

    T1_TANK_X_POSITION = 100
    T1_THERMOMETER_X_POSITION = T1_TANK_X_POSITION - ANALOG_INDICATOR_WIDTH - 10
    T2_ADDITIVE_VALVE_X_POSITION = 250
    T2_TANK_X_POSITION = T1_TANK_X_POSITION + (T2_ADDITIVE_VALVE_X_POSITION - (
            T1_TANK_X_POSITION + TANK_WIDTH // 2)) // 2

    T3_TANK_X_POSITION = 350
    T3_THERMOMETER_X_POSITION = T3_TANK_X_POSITION - ANALOG_INDICATOR_WIDTH - 10
    T4_ADDITIVE_VALVE_X_POSITION = 500
    T4_TANK_X_POSITION = T3_TANK_X_POSITION + (T4_ADDITIVE_VALVE_X_POSITION - (
            T3_TANK_X_POSITION + TANK_WIDTH // 2)) // 2

    T1_TOP_VALVE_Y_POSITION = 10
    T1_TANK_Y_POSITION = T1_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 5
    T1_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT // 8
    T1_THERMOMETER_Y_POSITION = T1_TANK_Y_POSITION - 10
    T1_BOTTOM_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 5
    T1_HEATING_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T2_ADDITIVE_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 5

    T2_TANK_Y_POSITION = T1_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 60
    T2_BOTTOM_VALVE_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT + 5
    T2_LEVEL_SENSOR_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT // 8

    T3_TOP_VALVE_Y_POSITION = 10
    T3_TANK_Y_POSITION = T3_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 5
    T3_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 8
    T3_THERMOMETER_Y_POSITION = T3_TANK_Y_POSITION - 10
    T3_BOTTOM_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 5
    T3_HEATING_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T4_ADDITIVE_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 5

    T4_TANK_Y_POSITION = T3_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 60
    T4_BOTTOM_VALVE_Y_POSITION = T4_TANK_Y_POSITION + TANK_HEIGHT + 5
    T4_LEVEL_SENSOR_Y_POSITION = T4_TANK_Y_POSITION + TANK_HEIGHT // 8

    FULL_WIDTH = T4_ADDITIVE_VALVE_X_POSITION + 200
    FULL_HEIGHT = T2_TANK_Y_POSITION + TANK_HEIGHT + VALVE_HEIGHT + 80

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__pipe12_drawing()
        self.__pipe34_drawing()
        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()
        self.__tank4_drawing()

    def __pipe12_drawing(self):

        self.create_vertical_pipe(
            x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T2_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T2_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T2_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T2_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T2_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)
        self.create_diagonal_pipe(
            x_start=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 20,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2 + (
                    self.T4_TANK_X_POSITION - self.T2_TANK_X_POSITION) // 2,
            y_end=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 80)

    def __pipe34_drawing(self):

        self.create_vertical_pipe(
            x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T3_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T3_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T4_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T4_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=0,
            length=self.T4_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(
            x_start=self.T4_ADDITIVE_VALVE_X_POSITION + self.VALVE_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T4_ADDITIVE_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
            x_end=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_end=self.T4_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(
            x_position=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_position=self.T4_TANK_Y_POSITION - 10,
            length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)
        self.create_diagonal_pipe(
            x_start=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
            y_start=self.T4_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 20,
            x_end=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2 + (
                    self.T4_TANK_X_POSITION - self.T2_TANK_X_POSITION) // 2,
            y_end=self.T2_TANK_Y_POSITION + self.TANK_HEIGHT + self.VALVE_HEIGHT + 80)

    def __tank1_drawing(self):
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_TOP_VALVE_Y_POSITION,
                          name='T1_Tolt []', color='gray')
        self.create_tank(x_position=self.T1_TANK_X_POSITION,
                         y_position=self.T1_TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        self.create_sensor(x_position=self.T1_TANK_X_POSITION,
                           y_position=self.T1_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T1_Teli\n[]', color='gray')
        self.create_analog(x_position=self.T1_THERMOMETER_X_POSITION,
                           y_position=self.T1_THERMOMETER_Y_POSITION,
                           height=80, marks_position=(40, 60),
                           active_level=0, active_color='red',
                           activ_level_print=True, name_position='left',
                           name='T1_Homerseklet\n[]')
        self.create_heating(x_position=self.T1_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T1_Fut\n[]', color='black')
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_BOTTOM_VALVE_Y_POSITION,
                          name='T1_Urit []', color='gray')

    def __tank2_drawing(self):
        self.create_valve(x_position=self.T2_ADDITIVE_VALVE_X_POSITION,
                          y_position=self.T2_ADDITIVE_VALVE_Y_POSITION,
                          name='T2_Adalek\n[]', color='gray')
        self.create_tank(x_position=self.T2_TANK_X_POSITION,
                         y_position=self.T2_TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        self.__tank3_analog_id = self.create_analog(x_position=self.T2_TANK_X_POSITION,
                                                    y_position=self.T2_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=0,
                                                    activ_level_print=True, active_color='red',
                                                    name='T2_Szint []\n')
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_BOTTOM_VALVE_Y_POSITION,
                          name='T2_Urit []', color='gray')

    def __tank3_drawing(self):
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_TOP_VALVE_Y_POSITION,
                          name='T3_Tolt []', color='gray')
        self.create_tank(x_position=self.T3_TANK_X_POSITION,
                         y_position=self.T3_TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        self.create_sensor(x_position=self.T3_TANK_X_POSITION,
                           y_position=self.T3_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T3_Teli\n[]', color='gray')
        self.create_analog(x_position=self.T3_THERMOMETER_X_POSITION,
                           y_position=self.T3_THERMOMETER_Y_POSITION,
                           height=80, marks_position=(40, 60),
                           active_level=0, active_color='red',
                           activ_level_print=True, name_position='left',
                           name='T3_Homerseklet\n[]')
        self.create_heating(x_position=self.T3_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T3_Fut\n[]', color='black')
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_BOTTOM_VALVE_Y_POSITION,
                          name='T3_Urit []', color='gray')

    def __tank4_drawing(self):
        self.create_valve(x_position=self.T4_ADDITIVE_VALVE_X_POSITION,
                          y_position=self.T4_ADDITIVE_VALVE_Y_POSITION,
                          name='T4_Adalek\n[]', color='gray')
        self.create_tank(x_position=self.T4_TANK_X_POSITION,
                         y_position=self.T4_TANK_Y_POSITION,
                         tank_name='T4', tank_color='gray')
        self.__tank3_analog_id = self.create_analog(x_position=self.T4_TANK_X_POSITION,
                                                    y_position=self.T4_LEVEL_SENSOR_Y_POSITION,
                                                    height=self.TANK_HEIGHT * 6 // 8, marks_position=(20, 60, 80),
                                                    line_length=self.TANK_WIDTH + 10,
                                                    active_level=0,
                                                    activ_level_print=True, active_color='red',
                                                    name='T4_Szint []\n')
        self.create_valve(x_position=self.T4_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T4_BOTTOM_VALVE_Y_POSITION,
                          name='T4_Urit []', color='gray')


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly1_View(root)
    tank.pack()

    root.mainloop()