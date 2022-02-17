from tkinter import Tk

from _view.tank_canvas import TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, RotorCanvas, \
    PipeCanvas


class Tartaly4_View(TankCanvas, ValveCanvas, SensorCanvas, AnalogCanvas, HeatingCanvas, RotorCanvas, PipeCanvas):
    TANK_WIDTH = 60
    TANK_HEIGHT = 130
    VALVE_WIDTH = 20
    VALVE_HEIGHT = 30
    INDICATOR_SQUARE = 15
    INDICATOR_LINE_LENGTH = TANK_WIDTH + 10
    INDICATOR_TEXT_LENGTH = 80
    ANALOG_INDICATOR_WIDTH = 15
    HEATING_WIDTH = 30
    HEATING_HEIGHT = 30
    ROTOR_WIDTH = 40
    PIPE_WIDTH = 7

    T1_TANK_X_POSITION = 100
    T1_THERMOMETER_X_POSITION = T1_TANK_X_POSITION - ANALOG_INDICATOR_WIDTH - 10
    T2_TANK_X_POSITION = T1_TANK_X_POSITION + TANK_WIDTH + INDICATOR_TEXT_LENGTH + 50
    T2_THERMOMETER_X_POSITION = T2_TANK_X_POSITION - ANALOG_INDICATOR_WIDTH - 10
    T3_TANK_X_POSITION = T1_TANK_X_POSITION + (TANK_WIDTH * 2 + INDICATOR_TEXT_LENGTH + 50) // 2 - TANK_WIDTH // 2

    T1_TOP_VALVE_Y_POSITION = 10
    T1_TANK_Y_POSITION = T1_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 10
    T1_SENSOR_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT // 8
    T1_THERMOMETER_Y_POSITION = T1_TANK_Y_POSITION - 10
    T1_BOTTOM_VALVE_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT + 10
    T1_HEATING_Y_POSITION = T1_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T2_TOP_VALVE_Y_POSITION = 10
    T2_TANK_Y_POSITION = T2_TOP_VALVE_Y_POSITION + VALVE_HEIGHT + 10
    T2_SENSOR_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT // 8
    T2_THERMOMETER_Y_POSITION = T2_TANK_Y_POSITION - 10
    T2_BOTTOM_VALVE_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT + 10
    T2_HEATING_Y_POSITION = T2_TANK_Y_POSITION + TANK_HEIGHT * 2 // 3

    T3_TANK_Y_POSITION = T2_BOTTOM_VALVE_Y_POSITION + VALVE_HEIGHT + 70
    T3_BOTTOM_VALVE_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT + 10
    T3_ROTOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 2
    T3_TOP_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 8
    T3_HALF_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT // 2
    T3_BOTTOM_SENSOR_Y_POSITION = T3_TANK_Y_POSITION + TANK_HEIGHT * 7 // 8

    FULL_WIDTH = 800
    FULL_HEIGHT = 480

    __tank1_analog_id = None
    __tank2_analog_id = None

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank1_sensor_color = 'gray'
        self.__tank1_heating_color = 'black'
        self.__tank1_top_valve_color = 'gray'
        self.__tank1_bottom_valve_color = 'gray'
        self.__tank2_sensor_color = 'gray'
        self.__tank2_heating_color = 'black'
        self.__tank2_top_valve_color = 'gray'
        self.__tank2_bottom_valve_color = 'gray'
        self.__tank3_rotor_color = 'yellow'
        self.__tank3_bottom_valve_color = 'gray'
        self.__tank3_top_sensor_color = 'gray'
        self.__tank3_half_sensor_color = 'gray'
        self.__tank3_bottom_sensor_color = 'gray'

        self.__tank1_temperature_percent = 0
        self.__tank2_temperature_percent = 0

        self.__pipe_drawing()
        self.__tank1_drawing()
        self.__tank2_drawing()
        self.__tank3_drawing()

    def tank1_change_color(self, sensor_color, heating_color):
        if self.__tank1_sensor_color != sensor_color or self.__tank1_heating_color != heating_color:
            self.__tank1_sensor_color = sensor_color
            self.__tank1_heating_color = heating_color
            self.__tank1_drawing()

    def tank1_change_valve_color(self, top_valve_color, bottom_valve_color):
        if self.__tank1_top_valve_color != top_valve_color or self.__tank1_bottom_valve_color != bottom_valve_color:
            self.__tank1_top_valve_color = top_valve_color
            self.__tank1_bottom_valve_color = bottom_valve_color
            self.__tank1_drawing()

    def tank2_change_color(self, sensor_color, heating_color):
        if self.__tank2_sensor_color != sensor_color or self.__tank2_heating_color != heating_color:
            self.__tank2_sensor_color = sensor_color
            self.__tank2_heating_color = heating_color
            self.__tank2_drawing()

    def tank2_change_valve_color(self, top_valve_color, bottom_valve_color):
        if self.__tank2_top_valve_color != top_valve_color or self.__tank2_bottom_valve_color != bottom_valve_color:
            self.__tank2_top_valve_color = top_valve_color
            self.__tank2_bottom_valve_color = bottom_valve_color
            self.__tank2_drawing()

    def tank3_change_color(self, rotor_color, bottom_valve_color):
        if self.__tank3_rotor_color != rotor_color or self.__tank3_bottom_valve_color != bottom_valve_color:
            self.__tank3_rotor_color = rotor_color
            self.__tank3_bottom_valve_color = bottom_valve_color
            self.__tank3_drawing()

    def tank3_change_sensor_color(self, top_sensor_color, half_sensor_color, bottom_sensor_color):
        if self.__tank3_top_sensor_color != top_sensor_color or\
                self.__tank3_half_sensor_color != half_sensor_color or\
                self.__tank3_bottom_sensor_color != bottom_sensor_color:
            self.__tank3_top_sensor_color = top_sensor_color
            self.__tank3_half_sensor_color = half_sensor_color
            self.__tank3_bottom_sensor_color = bottom_sensor_color
            self.__tank3_drawing()

    def tank1_change_heating_level(self, temperature_percent):
        if self.__tank1_temperature_percent != temperature_percent:
            self.__tank1_temperature_percent = temperature_percent
            self.__tank1_drawing()

    def tank2_change_heating_level(self, temperature_percent):
        if self.__tank2_temperature_percent != temperature_percent:
            self.__tank2_temperature_percent = temperature_percent
            self.__tank2_drawing()

    def __pipe_drawing(self):

        self.create_vertical_pipe(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=0,
                                  length=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(x_start=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_start=self.T1_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
                                  x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_end=self.T3_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=0,
                                  length=self.T2_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10)
        self.create_diagonal_pipe(x_start=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_start=self.T2_BOTTOM_VALVE_Y_POSITION + self.VALVE_HEIGHT + 10,
                                  x_end=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_end=self.T3_TANK_Y_POSITION - 10)

        self.create_vertical_pipe(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.PIPE_WIDTH // 2,
                                  y_position=self.T3_TANK_Y_POSITION - 10,
                                  length=self.TANK_HEIGHT + self.VALVE_HEIGHT + 30)

    def __tank1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_TOP_VALVE_Y_POSITION,
                          name='T1_Tolt []', color=self.__tank1_top_valve_color)
        self.create_tank(x_position=self.T1_TANK_X_POSITION,
                         y_position=self.T1_TANK_Y_POSITION,
                         tank_name='T1', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T1_TANK_X_POSITION,
                           y_position=self.T1_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T1_Teli\n[]', color=self.__tank1_sensor_color)
        self.delete(self.__tank1_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank1_analog_id = self.create_analog(x_position=self.T1_THERMOMETER_X_POSITION,
                                                    y_position=self.T1_THERMOMETER_Y_POSITION,
                                                    height=80, marks_position=(40, 60),
                                                    active_level=self.__tank1_temperature_percent, active_color='red',
                                                    activ_level_print=True, name_position='left',
                                                    name='T1_Homerseklet\n[]')
        self.create_heating(x_position=self.T1_TANK_X_POSITION - 10,
                            y_position=self.T1_HEATING_Y_POSITION,
                            name='T1_Fut\n[]', color=self.__tank1_heating_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T1_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T1_BOTTOM_VALVE_Y_POSITION,
                          name='T1_Urit []', color=self.__tank1_bottom_valve_color)

    def __tank2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_TOP_VALVE_Y_POSITION,
                          name='T2_Tolt []', color=self.__tank2_top_valve_color)
        self.create_tank(x_position=self.T2_TANK_X_POSITION,
                         y_position=self.T2_TANK_Y_POSITION,
                         tank_name='T2', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_sensor(x_position=self.T2_TANK_X_POSITION,
                           y_position=self.T2_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T2_Teli\n[]', color=self.__tank2_sensor_color)
        self.delete(self.__tank2_analog_id)
        # noinspection SpellCheckingInspection
        self.__tank2_analog_id = self.create_analog(x_position=self.T2_THERMOMETER_X_POSITION,
                                                    y_position=self.T2_THERMOMETER_Y_POSITION,
                                                    height=80, marks_position=(40, 60),
                                                    active_level=self.__tank2_temperature_percent, active_color='red',
                                                    activ_level_print=True, name_position='left',
                                                    name='T2_Homerseklet\n[]')
        self.create_heating(x_position=self.T2_TANK_X_POSITION - 10,
                            y_position=self.T2_HEATING_Y_POSITION,
                            name='T2_Fut\n[]', color=self.__tank2_heating_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T2_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T2_BOTTOM_VALVE_Y_POSITION,
                          name='T2_Urit []', color=self.__tank2_bottom_valve_color)

    def __tank3_drawing(self):
        self.create_sensor(x_position=self.T3_TANK_X_POSITION,
                           y_position=self.T3_TOP_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T3_Felso\n[]', color=self.__tank3_top_sensor_color)
        self.create_sensor(x_position=self.T3_TANK_X_POSITION,
                           y_position=self.T3_HALF_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T3_Kozep\n[]', color=self.__tank3_half_sensor_color)
        self.create_sensor(x_position=self.T3_TANK_X_POSITION,
                           y_position=self.T3_BOTTOM_SENSOR_Y_POSITION,
                           line_length=self.INDICATOR_LINE_LENGTH,
                           name='T3_Also\n[]', color=self.__tank3_bottom_sensor_color)
        self.create_tank(x_position=self.T3_TANK_X_POSITION,
                         y_position=self.T3_TANK_Y_POSITION,
                         tank_name='T3', tank_color='gray')
        # noinspection SpellCheckingInspection
        self.create_rotor(x_position=self.T3_TANK_X_POSITION + 5,
                          y_position=self.T3_ROTOR_Y_POSITION,
                          name='T3_Kever []', color=self.__tank3_rotor_color)
        # noinspection SpellCheckingInspection
        self.create_valve(x_position=self.T3_TANK_X_POSITION + self.TANK_WIDTH // 2 - self.VALVE_WIDTH // 2,
                          y_position=self.T3_BOTTOM_VALVE_Y_POSITION,
                          name='T3_Urit []', color=self.__tank3_bottom_valve_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Tartaly4_View(root)
    tank.pack()

    root.mainloop()