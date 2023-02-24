from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas
from _view.sensor_canvas import AnalogCanvas
from io_data.io_view_data import IO_View_Address


class IO_View(IndicatorCanvas, AnalogCanvas):
    INDICATOR_WIDTH = 30
    ANALOG_SENSOR_WIDTH = 30
    ANALOG_SENSOR_FONT_SIZE = 15

    INPUT_X_POSITION = 5
    OUTPUT_X_POSITION = INPUT_X_POSITION + 150
    ANALOG_IN_CH0_X_POSITION = OUTPUT_X_POSITION + 150
    ANALOG_IN_CH1_X_POSITION = ANALOG_IN_CH0_X_POSITION + 80

    ROW1_Y_POSITION = 5
    ROW2_Y_POSITION = ROW1_Y_POSITION + INDICATOR_WIDTH + 5
    ROW3_Y_POSITION = ROW2_Y_POSITION + INDICATOR_WIDTH + 5
    ROW4_Y_POSITION = ROW3_Y_POSITION + INDICATOR_WIDTH + 5
    ROW5_Y_POSITION = ROW4_Y_POSITION + INDICATOR_WIDTH + 5
    ROW6_Y_POSITION = ROW5_Y_POSITION + INDICATOR_WIDTH + 5
    ROW7_Y_POSITION = ROW6_Y_POSITION + INDICATOR_WIDTH + 5
    ROW8_Y_POSITION = ROW7_Y_POSITION + INDICATOR_WIDTH + 5
    ROW9_Y_POSITION = ROW8_Y_POSITION + INDICATOR_WIDTH + 5
    ROW10_Y_POSITION = ROW9_Y_POSITION + INDICATOR_WIDTH + 5

    FULL_WIDTH = ANALOG_IN_CH1_X_POSITION + ANALOG_SENSOR_WIDTH + 20
    FULL_HEIGHT = ROW10_Y_POSITION + INDICATOR_WIDTH + 5

    __analog_in_ch0_id = None
    __analog_in_ch1_id = None

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__input1_color = 'gray'
        self.__input2_color = 'gray'
        self.__input3_color = 'gray'
        self.__input4_color = 'gray'
        self.__input5_color = 'gray'
        self.__input6_color = 'gray'
        self.__input7_color = 'gray'
        self.__input8_color = 'gray'

        self.__output1_color = 'gray'
        self.__output2_color = 'gray'
        self.__output3_color = 'gray'
        self.__output4_color = 'gray'
        self.__output5_color = 'gray'
        self.__output6_color = 'gray'
        self.__output7_color = 'gray'
        self.__output8_color = 'gray'
        self.__output9_color = 'gray'
        self.__output10_color = 'gray'

        self.__analog_in_ch0_percent = 0
        self.__analog_in_ch1_percent = 0

        self.__input_drawing()
        self.__output_drawing()
        self.__analog_in_drawing()

    def input_change_color(self,
                           input_color1, input_color2, input_color3, input_color4,
                           input_color5, input_color6, input_color7, input_color8):
        if self.__input1_color != input_color1 or self.__input2_color != input_color2 \
                or self.__input3_color != input_color3 or self.__input4_color != input_color4 \
                or self.__input5_color != input_color5 or self.__input6_color != input_color6\
                or self.__input7_color != input_color7 or self.__input8_color != input_color8:
            self.__input1_color = input_color1
            self.__input2_color = input_color2
            self.__input3_color = input_color3
            self.__input4_color = input_color4
            self.__input5_color = input_color5
            self.__input6_color = input_color6
            self.__input7_color = input_color7
            self.__input8_color = input_color8
            self.__input_drawing()

    def output_change_color(self,
                            output1_color, output2_color, output3_color, output4_color, output5_color,
                            output6_color, output7_color, output8_color, output9_color, output10_color):
        if self.__output1_color != output1_color or self.__output2_color != output2_color \
                or self.__output3_color != output3_color or self.__output4_color != output4_color \
                or self.__output5_color != output5_color or self.__output6_color != output6_color \
                or self.__output7_color != output7_color or self.__output8_color != output8_color \
                or self.__output9_color != output9_color or self.__output10_color != output10_color:
            self.__output1_color = output1_color
            self.__output2_color = output2_color
            self.__output3_color = output3_color
            self.__output4_color = output4_color
            self.__output5_color = output5_color
            self.__output6_color = output6_color
            self.__output7_color = output7_color
            self.__output8_color = output8_color
            self.__output9_color = output9_color
            self.__output10_color = output10_color
            self.__output_drawing()

    def analog_in_change_level(self, ch0_percent, ch1_percent):
        if self.__analog_in_ch0_percent != ch0_percent or self.__analog_in_ch1_percent != ch1_percent:
            self.__analog_in_ch0_percent = ch0_percent
            self.__analog_in_ch1_percent = ch1_percent
            self.__analog_in_drawing()

    def analog_out_change_level(self, ch0_percent, ch1_percent):
        if self.__analog_out_ch0_percent != ch0_percent or self.__analog_out_ch1_percent != ch1_percent:
            self.__analog_out_ch0_percent = ch0_percent
            self.__analog_out_ch1_percent = ch1_percent
            self.__analog_out_drawing()

    def __input_drawing(self):
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW2_Y_POSITION,
                                     name='Bemenet1 [%s]' % IO_View_Address.INPUT1,
                                     color=self.__input1_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW3_Y_POSITION,
                                     name='Bemenet2 [%s]' % IO_View_Address.INPUT2,
                                     color=self.__input2_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW4_Y_POSITION,
                                     name='Bemenet3 [%s]' % IO_View_Address.INPUT3,
                                     color=self.__input3_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW5_Y_POSITION,
                                     name='Bemenet4 [%s]' % IO_View_Address.INPUT4,
                                     color=self.__input4_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW6_Y_POSITION,
                                     name='Bemenet5 [%s]' % IO_View_Address.INPUT5,
                                     color=self.__input5_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW7_Y_POSITION,
                                     name='Bemenet6 [%s]' % IO_View_Address.INPUT6,
                                     color=self.__input6_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW8_Y_POSITION,
                                     name='Bemenet7 [%s]' % IO_View_Address.INPUT7,
                                     color=self.__input7_color)
        self.create_square_indicator(x_position=self.INPUT_X_POSITION,
                                     y_position=self.ROW9_Y_POSITION,
                                     name='Bemenet8 [%s]' % IO_View_Address.INPUT8,
                                     color=self.__input8_color)

    def __output_drawing(self):
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW1_Y_POSITION,
                                     name='Kimenet1 [%s]' % IO_View_Address.OUTPUT1,
                                     color=self.__output1_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW2_Y_POSITION,
                                     name='Kimenet2 [%s]' % IO_View_Address.OUTPUT2,
                                     color=self.__output2_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW3_Y_POSITION,
                                     name='Kimenet3 [%s]' % IO_View_Address.OUTPUT3,
                                     color=self.__output3_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW4_Y_POSITION,
                                     name='Kimenet4 [%s]' % IO_View_Address.OUTPUT4,
                                     color=self.__output4_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW5_Y_POSITION,
                                     name='Kimenet5 [%s]' % IO_View_Address.OUTPUT5,
                                     color=self.__output5_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW6_Y_POSITION,
                                     name='Kimenet6 [%s]' % IO_View_Address.OUTPUT6,
                                     color=self.__output6_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW7_Y_POSITION,
                                     name='Kimenet7 [%s]' % IO_View_Address.OUTPUT7,
                                     color=self.__output7_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW8_Y_POSITION,
                                     name='Kimenet8 [%s]' % IO_View_Address.OUTPUT8,
                                     color=self.__output8_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW9_Y_POSITION,
                                     name='Kimenet9 [%s]' % IO_View_Address.OUTPUT9,
                                     color=self.__output9_color)
        self.create_circle_indicator(x_position=self.OUTPUT_X_POSITION,
                                     y_position=self.ROW10_Y_POSITION,
                                     name='Kimenet10 [%s]' % IO_View_Address.OUTPUT10,
                                     color=self.__output10_color)

    def __analog_in_drawing(self):
        self.delete(self.__analog_in_ch0_id)
        self.__analog_in_ch0_id =\
            self.create_analog(x_position=self.ANALOG_IN_CH0_X_POSITION,
                               y_position=self.ROW1_Y_POSITION,
                               active_level=self.__analog_in_ch0_percent, active_color='red',
                               height=self.ROW10_Y_POSITION - self.ROW1_Y_POSITION + self.INDICATOR_WIDTH,
                               activ_level_print=True,
                               name='Analóg bemenet CH0 [%s]' % IO_View_Address.ANALOG_IN_CH0)
        self.delete(self.__analog_in_ch1_id)
        self.__analog_in_ch1_id = \
            self.create_analog(x_position=self.ANALOG_IN_CH1_X_POSITION,
                               y_position=self.ROW1_Y_POSITION,
                               active_level=self.__analog_in_ch1_percent, active_color='red',
                               height=self.ROW10_Y_POSITION - self.ROW1_Y_POSITION + self.INDICATOR_WIDTH,
                               activ_level_print=True,
                               name='Analóg bemenet CH1 [%s]' % IO_View_Address.ANALOG_IN_CH1)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = IO_View(root)
    tank.pack()

    root.mainloop()
