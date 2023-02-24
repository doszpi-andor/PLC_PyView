from _view.plc_view import PLC_ViewA
from io_data.io_view_data import IO_View_Data
from io_data.io_view_draw import IO_View


class App(PLC_ViewA):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('IO view')
        self.name_label.config(text='IO megjelenítő')

        self.io = IO_View(self.process_frame)
        self.io.pack()

        self.plc_data = IO_View_Data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        if self.plc_data.input_is_changed():
            self.__input_refresh()

        if self.plc_data.output_is_changed():
            self.__output_refresh()

        if self.plc_data.analog_in_ch0_is_changed(threshold=1000) \
                or self.plc_data.analog_in_ch1_is_changed(threshold=1000):
            self.__analog_in_refresh()

        super().loop()

    def __input_refresh(self):
        if self.plc_data.input1:
            input1_color = 'red'
        else:
            input1_color = 'gray'

        if self.plc_data.input2:
            input2_color = 'red'
        else:
            input2_color = 'gray'

        if self.plc_data.input3:
            input3_color = 'red'
        else:
            input3_color = 'gray'

        if self.plc_data.input4:
            input4_color = 'red'
        else:
            input4_color = 'gray'

        if self.plc_data.input5:
            input5_color = 'red'
        else:
            input5_color = 'gray'

        if self.plc_data.input6:
            input6_color = 'red'
        else:
            input6_color = 'gray'

        if self.plc_data.input7:
            input7_color = 'red'
        else:
            input7_color = 'gray'

        if self.plc_data.input8:
            input8_color = 'red'
        else:
            input8_color = 'gray'

        self.io.input_change_color(input1_color,
                                   input2_color,
                                   input3_color,
                                   input4_color,
                                   input5_color,
                                   input6_color,
                                   input7_color,
                                   input8_color)

    def __output_refresh(self):
        if self.plc_data.output1:
            output1_color = 'red'
        else:
            output1_color = 'gray'

        if self.plc_data.output2:
            output2_color = 'red'
        else:
            output2_color = 'gray'

        if self.plc_data.output3:
            output3_color = 'red'
        else:
            output3_color = 'gray'

        if self.plc_data.output4:
            output4_color = 'red'
        else:
            output4_color = 'gray'

        if self.plc_data.output5:
            output5_color = 'red'
        else:
            output5_color = 'gray'

        if self.plc_data.output6:
            output6_color = 'red'
        else:
            output6_color = 'gray'

        if self.plc_data.output7:
            output7_color = 'red'
        else:
            output7_color = 'gray'

        if self.plc_data.output8:
            output8_color = 'red'
        else:
            output8_color = 'gray'

        if self.plc_data.output9:
            output9_color = 'red'
        else:
            output9_color = 'gray'

        if self.plc_data.output10:
            output10_color = 'red'
        else:
            output10_color = 'gray'

        self.io.output_change_color(output1_color,
                                    output2_color,
                                    output3_color,
                                    output4_color,
                                    output5_color,
                                    output6_color,
                                    output7_color,
                                    output8_color,
                                    output9_color,
                                    output10_color)

    def __analog_in_refresh(self):
        self.io.analog_in_change_level(self.plc_data.analog_in_ch0_percent, self.plc_data.analog_in_ch1_percent)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
