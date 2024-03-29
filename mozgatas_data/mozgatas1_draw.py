from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas


class Mozgatas1A_View(IndicatorCanvas):

    INDICATOR_WIDTH = 40
    INDICATOR_FONT_SIZE = 20

    COLUMN1 = 5
    COLUMN2 = COLUMN1 + INDICATOR_WIDTH + 100

    ROW1 = 5
    ROW2 = ROW1 + INDICATOR_WIDTH + 5
    ROW3 = ROW2 + INDICATOR_WIDTH + 5

    FULL_WIDTH = COLUMN2 + INDICATOR_WIDTH + 90
    FULL_HEIGHT = ROW3 + INDICATOR_WIDTH + 5

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.sensor0_color = 'gray'
        self.sensor1_color = 'gray'
        self.sensor2_color = 'gray'

        self.motor_up_color = 'gray'
        self.motor_down_color = 'gray'
        self.motor_stack_color = 'gray'

        self.__sensor_drawing()
        self.__indicator_drawing()

    def sensor_change_color(self, sensor0_color, sensor1_color, sensor2_color):
        if self.sensor0_color != sensor0_color or\
                self.sensor1_color != sensor1_color or\
                self.sensor2_color != sensor2_color:
            self.sensor0_color = sensor0_color
            self.sensor1_color = sensor1_color
            self.sensor2_color = sensor2_color
            self.__sensor_drawing()

    def indicator_change_color(self, motor_up_color, motor_stack_color, motor_down_color):
        if self.motor_up_color != motor_up_color or\
                self.motor_stack_color != motor_stack_color or\
                self.motor_down_color != motor_down_color:
            self.motor_up_color = motor_up_color
            self.motor_stack_color = motor_stack_color
            self.motor_down_color = motor_down_color
            self.__indicator_drawing()

    def __sensor_drawing(self):
        self.create_square_indicator(self.COLUMN1, self.ROW1,
                                     name='E3', color=self.sensor2_color)

        self.create_square_indicator(self.COLUMN1, self.ROW2,
                                     name='E1', color=self.sensor1_color)

        self.create_square_indicator(self.COLUMN1, self.ROW3,
                                     name='E0', color=self.sensor0_color)

    def __indicator_drawing(self):
        self.create_delta_indicator(self.COLUMN2, self.ROW1, direction='up',
                                    name='M_Fel', color=self.motor_up_color)
        self.create_square_indicator(self.COLUMN2, self.ROW2,
                                     name='M_Fog', color=self.motor_stack_color)
        self.create_delta_indicator(self.COLUMN2, self.ROW3, direction='down',
                                    name='M_Le', color=self.motor_down_color)


class Mozgatas1B_View(IndicatorCanvas):

    INDICATOR_WIDTH = 40
    INDICATOR_FONT_SIZE = 20

    COLUMN1 = 5
    COLUMN2 = COLUMN1 + INDICATOR_WIDTH + 100

    ROW1 = 5
    ROW2 = ROW1 + INDICATOR_WIDTH + 5
    ROW3 = ROW2 + INDICATOR_WIDTH + 50
    ROW4 = ROW3 + INDICATOR_WIDTH + 5
    ROW5 = ROW4 + INDICATOR_WIDTH + 5

    FULL_WIDTH = COLUMN2 + INDICATOR_WIDTH + 90
    FULL_HEIGHT = ROW5 + INDICATOR_WIDTH + 5

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.sensor0_color = 'gray'
        self.sensor1_color = 'gray'
        self.sensor2_color = 'gray'

        self.start_color = 'gray'
        self.stop_color = 'gray'

        self.motor_up_color = 'gray'
        self.motor_down_color = 'gray'
        self.motor_stack_color = 'gray'

        self.factory_color = 'gray'

        self.__sensor_drawing()
        self.__indicator_drawing()
        self.__controls_drawing()

    def sensor_change_color(self, sensor0_color, sensor1_color, sensor2_color):
        if self.sensor0_color != sensor0_color or\
                self.sensor1_color != sensor1_color or\
                self.sensor2_color != sensor2_color:
            self.sensor0_color = sensor0_color
            self.sensor1_color = sensor1_color
            self.sensor2_color = sensor2_color
            self.__sensor_drawing()

    def indicator_change_color(self, motor_up_color, motor_stack_color, motor_down_color):
        if self.motor_up_color != motor_up_color or\
                self.motor_stack_color != motor_stack_color or\
                self.motor_down_color != motor_down_color:
            self.motor_up_color = motor_up_color
            self.motor_stack_color = motor_stack_color
            self.motor_down_color = motor_down_color
            self.__indicator_drawing()

    def controls_change_color(self, start_color, stop_color, factory_color):
        if self.start_color != start_color or self.stop_color != stop_color or self.factory_color != factory_color:
            self.start_color = start_color
            self.stop_color = stop_color
            self.factory_color = factory_color
            self.__controls_drawing()

    def __sensor_drawing(self):
        self.create_square_indicator(self.COLUMN1, self.ROW3,
                                     name='E3', color=self.sensor2_color)

        self.create_square_indicator(self.COLUMN1, self.ROW4,
                                     name='E1', color=self.sensor1_color)

        self.create_square_indicator(self.COLUMN1, self.ROW5,
                                     name='E0', color=self.sensor0_color)

    def __indicator_drawing(self):
        self.create_delta_indicator(self.COLUMN2, self.ROW3, direction='up',
                                    name='M_Fel', color=self.motor_up_color)
        self.create_square_indicator(self.COLUMN2, self.ROW4,
                                     name='M_Fog', color=self.motor_stack_color)
        self.create_delta_indicator(self.COLUMN2, self.ROW5, direction='down',
                                    name='M_Le', color=self.motor_down_color)

    def __controls_drawing(self):
        self.create_circle_indicator(self.COLUMN1, self.ROW1,
                                     name='Üzem', color=self.factory_color)
        self.create_square_indicator(self.COLUMN2, self.ROW1,
                                     name='Start', color=self.start_color)
        self.create_square_indicator(self.COLUMN2, self.ROW2,
                                     name='Stop', color=self.stop_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    indicator = Mozgatas1B_View(root)
    indicator.pack()

    root.mainloop()
