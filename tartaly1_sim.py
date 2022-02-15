from tkinter import Frame, IntVar, Checkbutton, Label, Scale, HORIZONTAL, NORMAL, X, LEFT, RIGHT

from _config.plc_config_read import PLC_Config
from _plc_data.plc_data import PLC_Address, PLC_data
from tartaly1_view import App


class IO_Address(PLC_Address):
    IP, RACK, SLOT = PLC_Config.read_plc_config('_config/config.xml')

    INPUT1 = 'I0.0'
    INPUT2 = 'I0.1'
    INPUT3 = 'I0.2'
    INPUT4 = 'I0.3'
    INPUT5 = 'I0.4'
    INPUT6 = 'I0.5'
    INPUT7 = 'I0.6'
    INPUT8 = 'I0.7'

    WRITE_BYTES_ADDRESS = ('IB0',)

    OUTPUT_ADDRESS = ('QB0',)

    ANALOG_INPUT_CH0 = 'IW64'
    ANALOG_INPUT_CH1 = 'IW66'

    WRITE_WORDS_ADDRESS = ('IW64', 'IW66')

    ANALOG_CH0_MAX = 27648
    ANALOG_CH0_MIN = 0

    ANALOG_CH1_MAX = 27648
    ANALOG_CH1_MIN = 0


class IO_data(PLC_data):

    def __init__(self, ip, rack, slot):
        super().__init__(IO_Address(), ip, rack, slot)
        self.input1 = False
        self.input2 = False
        self.input3 = False
        self.input4 = False
        self.input5 = False
        self.input6 = False
        self.input7 = False
        self.input8 = False

        self.analog_ch0 = 0
        self.analog_ch1 = 0

    def write_data(self):

        for byte_address in IO_Address.WRITE_BYTES_ADDRESS:
            self.write_byte_data[byte_address] = [False, False, False, False, False, False, False, False]

        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT1)][
            PLC_Address.bit_index(IO_Address.INPUT1)] = self.input1
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT2)][
            PLC_Address.bit_index(IO_Address.INPUT2)] = self.input2
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT3)][
            PLC_Address.bit_index(IO_Address.INPUT3)] = self.input3
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT4)][
            PLC_Address.bit_index(IO_Address.INPUT4)] = self.input4
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT5)][
            PLC_Address.bit_index(IO_Address.INPUT5)] = self.input5
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT6)][
            PLC_Address.bit_index(IO_Address.INPUT6)] = self.input6
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT7)][
            PLC_Address.bit_index(IO_Address.INPUT7)] = self.input7
        self.write_byte_data[PLC_Address.byte_address(IO_Address.INPUT8)][
            PLC_Address.bit_index(IO_Address.INPUT8)] = self.input8

        for word_address in IO_Address.WRITE_WORDS_ADDRESS:
            self.write_word_data[word_address] = 0

        self.write_word_data[IO_Address.ANALOG_INPUT_CH0] = self.analog_ch0
        self.write_word_data[IO_Address.ANALOG_INPUT_CH1] = self.analog_ch1

        super().write_data()


class PLC_InputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, change_process=None, state=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Input').grid(row=1, column=1, columnspan=8)
        self.input1_var = IntVar()
        self.input1 = Checkbutton(self, variable=self.input1_var, state=state, command=change_process)
        self.input1.grid(row=2, column=1)
        Label(self, text='%s' % IO_Address.INPUT1).grid(row=3, column=1)
        self.input2_var = IntVar()
        self.input2 = Checkbutton(self, variable=self.input2_var, state=state, command=change_process)
        self.input2.grid(row=2, column=2)
        Label(self, text='%s' % IO_Address.INPUT2).grid(row=3, column=2)
        self.input3_var = IntVar()
        self.input3 = Checkbutton(self, variable=self.input3_var, state=state, command=change_process)
        self.input3.grid(row=2, column=3)
        Label(self, text='%s' % IO_Address.INPUT3).grid(row=3, column=3)
        self.input4_var = IntVar()
        self.input4 = Checkbutton(self, variable=self.input4_var, state=state, command=change_process)
        self.input4.grid(row=2, column=4)
        Label(self, text='%s' % IO_Address.INPUT4).grid(row=3, column=4)
        self.input5_var = IntVar()
        self.input5 = Checkbutton(self, variable=self.input5_var, state=state, command=change_process)
        self.input5.grid(row=2, column=5)
        Label(self, text='%s' % IO_Address.INPUT5).grid(row=3, column=5)
        self.input6_var = IntVar()
        self.input6 = Checkbutton(self, variable=self.input6_var, state=state, command=change_process)
        self.input6.grid(row=2, column=6)
        Label(self, text='%s' % IO_Address.INPUT6).grid(row=3, column=6)
        self.input7_var = IntVar()
        self.input7 = Checkbutton(self, variable=self.input7_var, state=state, command=change_process)
        self.input7.grid(row=2, column=7)
        Label(self, text='%s' % IO_Address.INPUT7).grid(row=3, column=7)
        self.input8_var = IntVar()
        self.input8 = Checkbutton(self, variable=self.input8_var, state=state, command=change_process)
        self.input8.grid(row=2, column=8)
        Label(self, text='%s' % IO_Address.INPUT8).grid(row=3, column=8)


class PLC_AnalogInputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, change_process=None, state=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.analog_ch0_frame = Frame(self)
        self.analog_ch1_frame = Frame(self)

        self.analog_ch0_var = IntVar()
        self.analog_ch0_scale = Scale(self.analog_ch0_frame,
                                      variable=self.analog_ch0_var, command=change_process, state=state,
                                      from_=IO_Address.ANALOG_CH0_MIN, to=IO_Address.ANALOG_CH0_MAX, orient=HORIZONTAL)
        self.analog_ch0_scale.pack(fill=X)
        Label(self.analog_ch0_frame, text='Channel0 [%s]' % IO_Address.ANALOG_INPUT_CH0).pack(side=LEFT)
        self.analog_ch1_var = IntVar()
        self.analog_ch1_scale = Scale(self.analog_ch1_frame,
                                      variable=self.analog_ch1_var, command=change_process, state=state,
                                      from_=IO_Address.ANALOG_CH1_MIN, to=IO_Address.ANALOG_CH1_MAX, orient=HORIZONTAL)
        self.analog_ch1_scale.pack(fill=X)
        Label(self.analog_ch1_frame, text='Channel1 [%s]' % IO_Address.ANALOG_INPUT_CH1).pack()

        self.analog_ch0_frame.pack(side=LEFT)
        self.analog_ch1_frame.pack(side=RIGHT)


class IO_App(App):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.io_data = IO_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.geometry("800x620")

        self.io_frame = PLC_InputView(self, change_process=self.change_input)
        self.plc_analog_frame = PLC_AnalogInputView(self, change_process=self.change_analog, state=NORMAL)
        self.io_frame.pack()
        self.plc_analog_frame.pack()

    def ip_selected(self, *args):
        super().ip_selected(*args)
        self.io_data.reconnect(self.ip_select.ip_address.get())

    def data_transfer(self):
        super().data_transfer()
        self.io_data.write_data()

    def change_input(self):
        self.io_data.input1 = bool(self.io_frame.input1_var.get())
        self.io_data.input2 = bool(self.io_frame.input2_var.get())
        self.io_data.input3 = bool(self.io_frame.input3_var.get())
        self.io_data.input4 = bool(self.io_frame.input4_var.get())
        self.io_data.input5 = bool(self.io_frame.input5_var.get())
        self.io_data.input6 = bool(self.io_frame.input6_var.get())
        self.io_data.input7 = bool(self.io_frame.input7_var.get())
        self.io_data.input8 = bool(self.io_frame.input8_var.get())

    # noinspection PyUnusedLocal
    def change_analog(self, *args):
        self.io_data.analog_ch0 = self.plc_analog_frame.analog_ch0_var.get()
        self.io_data.analog_ch1 = self.plc_analog_frame.analog_ch1_var.get()


if __name__ == '__main__':
    app = IO_App()

    app.after(100, app.loop)

    app.mainloop()
