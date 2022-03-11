from tkinter import Frame, Label, IntVar, Checkbutton, Scale, X, HORIZONTAL, DISABLED, NORMAL, OptionMenu, \
    StringVar

from _plc_data.plc_data import PLC_Address, PLC_data
from _view.plc_viewa import PLC_ViewA


# noinspection PyPep8Naming
class PLC_IO_Address(PLC_Address):

    INPUT1 = 'I0.0'
    INPUT2 = 'I0.1'
    INPUT3 = 'I0.2'
    INPUT4 = 'I0.3'
    INPUT5 = 'I0.4'
    INPUT6 = 'I0.5'
    INPUT7 = 'I0.6'
    INPUT8 = 'I0.7'

    INPUT_DIRECTION = 'write'
    INPUT_ADDRESS = ('IB0', 1)

    OUTPUT1 = 'Q0.0'
    OUTPUT2 = 'Q0.1'
    OUTPUT3 = 'Q0.2'
    OUTPUT4 = 'Q0.3'
    OUTPUT5 = 'Q0.4'
    OUTPUT6 = 'Q0.5'
    OUTPUT7 = 'Q0.6'
    OUTPUT8 = 'Q0.7'
    OUTPUT9 = 'Q1.0'
    OUTPUT10 = 'Q1.1'

    OUTPUT_DIRECTION = 'read'
    OUTPUT_ADDRESS = ('QB0', 2)

    ANALOG_INPUT_CH0 = 'IW64'
    ANALOG_INPUT_CH1 = 'IW66'

    ANALOG_DIRECTION = 'write'
    ANALOG_ADDRESS = ('IW64', 2)

    ANALOG_CH0_MAX = 27648
    ANALOG_CH0_MIN = 0

    ANALOG_CH1_MAX = 27648
    ANALOG_CH1_MIN = 0


# noinspection PyPep8Naming
class PLC_IO_Data(PLC_data):
    __input1_old = False
    __input2_old = False
    __input3_old = False
    __input4_old = False
    __input5_old = False
    __input6_old = False
    __input7_old = False
    __input8_old = False

    __output1_old = False
    __output2_old = False
    __output3_old = False
    __output4_old = False
    __output5_old = False
    __output6_old = False
    __output7_old = False
    __output8_old = False
    __output9_old = False
    __output10_old = False

    __analog_ch0_old = 0
    __analog_ch1_old = 0

    def __init__(self, ip, rack, slot):
        super().__init__(PLC_IO_Address(), ip, rack, slot)

        self.__input1 = False
        self.__input2 = False
        self.__input3 = False
        self.__input4 = False
        self.__input5 = False
        self.__input6 = False
        self.__input7 = False
        self.__input8 = False

        self.__input_direction = PLC_IO_Address.INPUT_DIRECTION

        self.__output1 = False
        self.__output2 = False
        self.__output3 = False
        self.__output4 = False
        self.__output5 = False
        self.__output6 = False
        self.__output7 = False
        self.__output8 = False
        self.__output9 = False
        self.__output10 = False

        self.__output_direction = PLC_IO_Address.OUTPUT_DIRECTION

        self.__analog_ch0 = 0
        self.__analog_ch1 = 0

        self.__analog_direction = PLC_IO_Address.ANALOG_DIRECTION

    @property
    def input1(self):
        return self.__input1

    @input1.setter
    def input1(self, data):
        if data in [True, False]:
            self.__input1 = data
        else:
            raise TypeError

    @property
    def input2(self):
        return self.__input2

    @input2.setter
    def input2(self, data):
        if data in [True, False]:
            self.__input2 = data
        else:
            raise TypeError

    @property
    def input3(self):
        return self.__input3

    @input3.setter
    def input3(self, data):
        if data in [True, False]:
            self.__input3 = data
        else:
            raise TypeError

    @property
    def input4(self):
        return self.__input4

    @input4.setter
    def input4(self, data):
        if data in [True, False]:
            self.__input4 = data
        else:
            raise TypeError

    @property
    def input5(self):
        return self.__input5

    @input5.setter
    def input5(self, data):
        if data in [True, False]:
            self.__input5 = data
        else:
            raise TypeError

    @property
    def input6(self):
        return self.__input6

    @input6.setter
    def input6(self, data):
        if data in [True, False]:
            self.__input6 = data
        else:
            raise TypeError

    @property
    def input7(self):
        return self.__input7

    @input7.setter
    def input7(self, data):
        if data in [True, False]:
            self.__input7 = data
        else:
            raise TypeError

    @property
    def input8(self):
        return self.__input8

    @input8.setter
    def input8(self, data):
        if data in [True, False]:
            self.__input8 = data
        else:
            raise TypeError

    @property
    def input_direction(self):
        return self.__input_direction

    @input_direction.setter
    def input_direction(self, direction):
        if direction in ('read', 'write'):
            self.__input_direction = direction
        else:
            raise TypeError

    @property
    def output1(self):
        return self.__output1

    @output1.setter
    def output1(self, data):
        if data in [True, False]:
            self.__output1 = data
        else:
            raise TypeError

    @property
    def output2(self):
        return self.__output2

    @output2.setter
    def output2(self, data):
        if data in [True, False]:
            self.__output2 = data
        else:
            raise TypeError

    @property
    def output3(self):
        return self.__output3

    @output3.setter
    def output3(self, data):
        if data in [True, False]:
            self.__output3 = data
        else:
            raise TypeError

    @property
    def output4(self):
        return self.__output4

    @output4.setter
    def output4(self, data):
        if data in [True, False]:
            self.__output4 = data
        else:
            raise TypeError

    @property
    def output5(self):
        return self.__output5

    @output5.setter
    def output5(self, data):
        if data in [True, False]:
            self.__output5 = data
        else:
            raise TypeError

    @property
    def output6(self):
        return self.__output6

    @output6.setter
    def output6(self, data):
        if data in [True, False]:
            self.__output6 = data
        else:
            raise TypeError

    @property
    def output7(self):
        return self.__output7

    @output7.setter
    def output7(self, data):
        if data in [True, False]:
            self.__output7 = data
        else:
            raise TypeError

    @property
    def output8(self):
        return self.__output8

    @output8.setter
    def output8(self, data):
        if data in [True, False]:
            self.__output8 = data
        else:
            raise TypeError

    @property
    def output9(self):
        return self.__output9

    @output9.setter
    def output9(self, data):
        if data in [True, False]:
            self.__output9 = data
        else:
            raise TypeError

    @property
    def output10(self):
        return self.__output10

    @output10.setter
    def output10(self, data):
        if data in [True, False]:
            self.__output10 = data
        else:
            raise TypeError

    @property
    def output_direction(self):
        return self.__output_direction

    @output_direction.setter
    def output_direction(self, direction):
        if direction in ('read', 'write'):
            self.__output_direction = direction
        else:
            raise TypeError

    @property
    def analog_input_ch0(self):
        return self.__analog_ch0

    @analog_input_ch0.setter
    def analog_input_ch0(self, data):
        if self.plc_address.ANALOG_CH0_MIN <= data <= self.plc_address.ANALOG_CH0_MAX:
            self.__analog_ch0 = data
        else:
            raise ValueError

    @property
    def analog_input_ch1(self):
        return self.__analog_ch1

    @analog_input_ch1.setter
    def analog_input_ch1(self, data):
        if self.plc_address.ANALOG_CH0_MIN <= data <= self.plc_address.ANALOG_CH0_MAX:
            self.__analog_ch1 = data
        else:
            raise ValueError

    @property
    def analog_direction(self):
        return self.__analog_direction

    @analog_direction.setter
    def analog_direction(self, direction):
        if direction in ('read', 'write'):
            self.__analog_direction = direction
        else:
            raise TypeError

    def read_data(self):

        read_byte_address_list = []
        read_word_address_list = []

        if self.__input_direction == 'read':
            read_byte_address_list.append(PLC_IO_Address.INPUT_ADDRESS)

        if self.__output_direction == 'read':
            read_byte_address_list.append(PLC_IO_Address.OUTPUT_ADDRESS)

        if self.__analog_direction == 'read':
            read_word_address_list.append(PLC_IO_Address.ANALOG_ADDRESS)

        self.plc_address.READ_BYTES_ADDRESS = read_byte_address_list
        self.plc_address.READ_WORDS_ADDRESS = read_word_address_list

        super().read_data()

        if self.__input_direction == 'read':
            self.__input1 = self.get_bit_in_page(PLC_IO_Address.INPUT1)
            self.__input2 = self.get_bit_in_page(PLC_IO_Address.INPUT2)
            self.__input3 = self.get_bit_in_page(PLC_IO_Address.INPUT3)
            self.__input4 = self.get_bit_in_page(PLC_IO_Address.INPUT4)
            self.__input5 = self.get_bit_in_page(PLC_IO_Address.INPUT5)
            self.__input6 = self.get_bit_in_page(PLC_IO_Address.INPUT6)
            self.__input7 = self.get_bit_in_page(PLC_IO_Address.INPUT7)
            self.__input8 = self.get_bit_in_page(PLC_IO_Address.INPUT8)

        if self.__output_direction == 'read':
            self.__output1 = self.get_bit_in_page(PLC_IO_Address.OUTPUT1)
            self.__output2 = self.get_bit_in_page(PLC_IO_Address.OUTPUT2)
            self.__output3 = self.get_bit_in_page(PLC_IO_Address.OUTPUT3)
            self.__output4 = self.get_bit_in_page(PLC_IO_Address.OUTPUT4)
            self.__output5 = self.get_bit_in_page(PLC_IO_Address.OUTPUT5)
            self.__output6 = self.get_bit_in_page(PLC_IO_Address.OUTPUT6)
            self.__output7 = self.get_bit_in_page(PLC_IO_Address.OUTPUT7)
            self.__output8 = self.get_bit_in_page(PLC_IO_Address.OUTPUT8)
            self.__output9 = self.get_bit_in_page(PLC_IO_Address.OUTPUT9)
            self.__output10 = self.get_bit_in_page(PLC_IO_Address.OUTPUT10)

        if self.__analog_direction == 'read':
            self.__analog_ch0 = self.get_int_in_page(PLC_IO_Address.ANALOG_INPUT_CH0)
            self.__analog_ch1 = self.get_int_in_page(PLC_IO_Address.ANALOG_INPUT_CH1)

    def write_data(self):
        write_byte_address_list = []
        write_word_address_list = []

        if self.__input_direction == 'write':
            write_byte_address_list.append(PLC_IO_Address.INPUT_ADDRESS)

        if self.__output_direction == 'write':
            write_byte_address_list.append(PLC_IO_Address.OUTPUT_ADDRESS)

        if self.__analog_direction == 'write':
            write_word_address_list.append(PLC_IO_Address.ANALOG_ADDRESS)

        self.plc_address.WRITE_BYTES_ADDRESS = write_byte_address_list
        self.plc_address.WRITE_WORDS_ADDRESS = write_word_address_list

        self.write_data_clear()

        if self.__input_direction == 'write':
            self.set_bit_in_page(PLC_IO_Address.INPUT1, self.__input1)
            self.set_bit_in_page(PLC_IO_Address.INPUT2, self.__input2)
            self.set_bit_in_page(PLC_IO_Address.INPUT3, self.__input3)
            self.set_bit_in_page(PLC_IO_Address.INPUT4, self.__input4)
            self.set_bit_in_page(PLC_IO_Address.INPUT5, self.__input5)
            self.set_bit_in_page(PLC_IO_Address.INPUT6, self.__input6)
            self.set_bit_in_page(PLC_IO_Address.INPUT7, self.__input7)
            self.set_bit_in_page(PLC_IO_Address.INPUT8, self.__input8)

        if self.__output_direction == 'write':
            self.set_bit_in_page(PLC_IO_Address.OUTPUT1, self.__output1)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT2, self.__output2)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT3, self.__output3)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT4, self.__output4)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT5, self.__output5)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT6, self.__output6)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT7, self.__output7)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT8, self.__output8)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT9, self.__output9)
            self.set_bit_in_page(PLC_IO_Address.OUTPUT10, self.__output10)

        if self.__analog_direction == 'write':
            self.set_int_in_page(PLC_IO_Address.ANALOG_INPUT_CH0, self.__analog_ch0)
            self.set_int_in_page(PLC_IO_Address.ANALOG_INPUT_CH1, self.__analog_ch1)

        super().write_data()

    def input_is_change(self):
        if self.__input1 != self.__input1_old or \
                self.__input2 != self.__input2_old or \
                self.__input3 != self.__input3_old or \
                self.__input4 != self.__input4_old or \
                self.__input5 != self.__input5_old or \
                self.__input6 != self.__input6_old or \
                self.__input7 != self.__input7_old or \
                self.__input8 != self.__input8_old:
            self.__input1_old = self.__input1
            self.__input2_old = self.__input2
            self.__input3_old = self.__input3
            self.__input4_old = self.__input4
            self.__input5_old = self.__input5
            self.__input6_old = self.__input6
            self.__input7_old = self.__input7
            self.__input8_old = self.__input8
            return True
        return False

    def output_is_change(self):
        if self.__output1 != self.__output1_old or \
                self.__output2 != self.__output2_old or \
                self.__output3 != self.__output3_old or \
                self.__output4 != self.__output4_old or \
                self.__output5 != self.__output5_old or \
                self.__output6 != self.__output6_old or \
                self.__output7 != self.__output7_old or \
                self.__output8 != self.__output8_old or \
                self.__output9 != self.__output9_old or \
                self.__output10 != self.__output10_old:
            self.__output1_old = self.__output1
            self.__output2_old = self.__output2
            self.__output3_old = self.__output3
            self.__output4_old = self.__output4
            self.__output5_old = self.__output5
            self.__output6_old = self.__output6
            self.__output7_old = self.__output7
            self.__output8_old = self.__output8
            self.__output9_old = self.__output9
            self.__output10_old = self.__output10
            return True
        return False

    def analog_is_changed(self):
        if self.__analog_ch0 != self.__analog_ch0_old or self.__analog_ch1 != self.__analog_ch1_old:
            self.__analog_ch0_old = self.__analog_ch0
            self.__analog_ch1_old = self.__analog_ch1
            return True
        return False


# noinspection PyPep8Naming
class PLC_InputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, change_process=None, state=None, change_direction=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Input').grid(row=1, column=1, columnspan=8)
        self.direction_list = ['read', 'write']
        self.direction = StringVar()
        self.direction.set(PLC_IO_Address.INPUT_DIRECTION)
        self.direction_menu = OptionMenu(self, self.direction, *self.direction_list, command=change_direction)
        self.direction_menu.grid(row=2, column=1, columnspan=8)
        self.input1_var = IntVar()
        self.input1 = Checkbutton(self, variable=self.input1_var, state=state, command=change_process)
        self.input1.grid(row=3, column=1)
        Label(self, text='%s' % PLC_IO_Address.INPUT1).grid(row=4, column=1)
        self.input2_var = IntVar()
        self.input2 = Checkbutton(self, variable=self.input2_var, state=state, command=change_process)
        self.input2.grid(row=3, column=2)
        Label(self, text='%s' % PLC_IO_Address.INPUT2).grid(row=4, column=2)
        self.input3_var = IntVar()
        self.input3 = Checkbutton(self, variable=self.input3_var, state=state, command=change_process)
        self.input3.grid(row=3, column=3)
        Label(self, text='%s' % PLC_IO_Address.INPUT3).grid(row=4, column=3)
        self.input4_var = IntVar()
        self.input4 = Checkbutton(self, variable=self.input4_var, state=state, command=change_process)
        self.input4.grid(row=3, column=4)
        Label(self, text='%s' % PLC_IO_Address.INPUT4).grid(row=4, column=4)
        self.input5_var = IntVar()
        self.input5 = Checkbutton(self, variable=self.input5_var, state=state, command=change_process)
        self.input5.grid(row=3, column=5)
        Label(self, text='%s' % PLC_IO_Address.INPUT5).grid(row=4, column=5)
        self.input6_var = IntVar()
        self.input6 = Checkbutton(self, variable=self.input6_var, state=state, command=change_process)
        self.input6.grid(row=3, column=6)
        Label(self, text='%s' % PLC_IO_Address.INPUT6).grid(row=4, column=6)
        self.input7_var = IntVar()
        self.input7 = Checkbutton(self, variable=self.input7_var, state=state, command=change_process)
        self.input7.grid(row=3, column=7)
        Label(self, text='%s' % PLC_IO_Address.INPUT7).grid(row=4, column=7)
        self.input8_var = IntVar()
        self.input8 = Checkbutton(self, variable=self.input8_var, state=state, command=change_process)
        self.input8.grid(row=3, column=8)
        Label(self, text='%s' % PLC_IO_Address.INPUT8).grid(row=4, column=8)

    def change_state(self, state):
        self.input1.configure(state=state)
        self.input2.configure(state=state)
        self.input3.configure(state=state)
        self.input4.configure(state=state)
        self.input5.configure(state=state)
        self.input6.configure(state=state)
        self.input7.configure(state=state)
        self.input8.configure(state=state)


# noinspection PyPep8Naming
class PLC_OutputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, change_process=None, state=None, change_direction=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Output').grid(row=1, column=1, columnspan=10)
        self.direction_list = ['read', 'write']
        self.direction = StringVar()
        self.direction.set(PLC_IO_Address.OUTPUT_DIRECTION)
        self.direction_menu = OptionMenu(self, self.direction, *self.direction_list, command=change_direction)
        self.direction_menu.grid(row=2, column=1, columnspan=10)
        self.output1_var = IntVar()
        self.output1 = Checkbutton(self, variable=self.output1_var, state=state, command=change_process)
        self.output1.grid(row=3, column=1)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT1).grid(row=4, column=1)
        self.output2_var = IntVar()
        self.output2 = Checkbutton(self, variable=self.output2_var, state=state, command=change_process)
        self.output2.grid(row=3, column=2)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT2).grid(row=4, column=2)
        self.output3_var = IntVar()
        self.output3 = Checkbutton(self, variable=self.output3_var, state=state, command=change_process)
        self.output3.grid(row=3, column=3)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT3).grid(row=4, column=3)
        self.output4_var = IntVar()
        self.output4 = Checkbutton(self, variable=self.output4_var, state=state, command=change_process)
        self.output4.grid(row=3, column=4)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT4).grid(row=4, column=4)
        self.output5_var = IntVar()
        self.output5 = Checkbutton(self, variable=self.output5_var, state=state, command=change_process)
        self.output5.grid(row=3, column=5)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT5).grid(row=4, column=5)
        self.output6_var = IntVar()
        self.output6 = Checkbutton(self, variable=self.output6_var, state=state, command=change_process)
        self.output6.grid(row=3, column=6)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT6).grid(row=4, column=6)
        self.output7_var = IntVar()
        self.output7 = Checkbutton(self, variable=self.output7_var, state=state, command=change_process)
        self.output7.grid(row=3, column=7)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT7).grid(row=4, column=7)
        self.output8_var = IntVar()
        self.output8 = Checkbutton(self, variable=self.output8_var, state=state, command=change_process)
        self.output8.grid(row=3, column=8)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT8).grid(row=4, column=8)
        self.output9_var = IntVar()
        self.output9 = Checkbutton(self, variable=self.output9_var, state=state, command=change_process)
        self.output9.grid(row=3, column=9)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT9).grid(row=4, column=9)
        self.output10_var = IntVar()
        self.output10 = Checkbutton(self, variable=self.output10_var, state=state, command=change_process)
        self.output10.grid(row=3, column=10)
        Label(self, text='%s' % PLC_IO_Address.OUTPUT10).grid(row=4, column=10)

    def change_state(self, state):
        self.output1.configure(state=state)
        self.output2.configure(state=state)
        self.output3.configure(state=state)
        self.output4.configure(state=state)
        self.output5.configure(state=state)
        self.output6.configure(state=state)
        self.output7.configure(state=state)
        self.output8.configure(state=state)
        self.output9.configure(state=state)
        self.output10.configure(state=state)


# noinspection PyPep8Naming
class PLC_AnalogInputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, change_process=None, state=None, change_direction=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Analog').pack()
        self.direction_list = ['read', 'write']
        self.direction = StringVar()
        self.direction.set(PLC_IO_Address.ANALOG_DIRECTION)
        self.direction_menu = OptionMenu(self, self.direction, *self.direction_list, command=change_direction)
        self.direction_menu.pack()
        self.analog_ch0_var = IntVar()
        self.analog_ch0_scale = Scale(self, variable=self.analog_ch0_var, command=change_process, state=state,
                                      from_=PLC_IO_Address.ANALOG_CH0_MIN, to=PLC_IO_Address.ANALOG_CH0_MAX,
                                      orient=HORIZONTAL)
        self.analog_ch0_scale.pack(fill=X)
        Label(self, text='Channel0 [%s]' % PLC_IO_Address.ANALOG_INPUT_CH0).pack()
        self.analog_ch1_var = IntVar()
        self.analog_ch1_scale = Scale(self, variable=self.analog_ch1_var, command=change_process, state=state,
                                      from_=PLC_IO_Address.ANALOG_CH1_MIN, to=PLC_IO_Address.ANALOG_CH1_MAX,
                                      orient=HORIZONTAL)
        self.analog_ch1_scale.pack(fill=X)
        Label(self, text='Channel1 [%s]' % PLC_IO_Address.ANALOG_INPUT_CH1).pack()

    def change_state(self, state):
        self.analog_ch0_scale.configure(state=state)
        self.analog_ch1_scale.configure(state=state)


class App(PLC_ViewA):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.resizable(True, True)

        self.title('IO Manage')
        self.name_frame.pack_forget()

        self.plc_input_frame = PLC_InputView(self.process_frame, change_process=self.change_input,
                                             change_direction=self.set_input_direction)
        self.plc_output_frame = PLC_OutputView(self.process_frame, change_process=self.change_output,
                                               change_direction=self.set_output_direction)
        self.plc_analog_frame = PLC_AnalogInputView(self.process_frame, change_process=self.change_analog,
                                                    change_direction=self.set_analog_direction)

        self.plc_input_frame.pack()
        self.plc_output_frame.pack()
        self.plc_analog_frame.pack(fill=X)

        self.plc_data = PLC_IO_Data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.plc_data.input_direction = PLC_IO_Address.INPUT_DIRECTION
        self.set_input_direction()
        self.plc_data.output_direction = PLC_IO_Address.OUTPUT_DIRECTION
        self.set_output_direction()
        self.plc_data.analog_direction = PLC_IO_Address.ANALOG_DIRECTION
        self.set_analog_direction()

    def data_transfer(self):
        self.plc_data.read_data()
        self.plc_data.write_data()

    # noinspection PyUnusedLocal
    def set_input_direction(self, *args):
        self.plc_data.input_direction = self.plc_input_frame.direction.get()
        if self.plc_data.input_direction == 'read':
            self.plc_input_frame.change_state(state=DISABLED)
        elif self.plc_data.input_direction == 'write':
            self.plc_input_frame.change_state(state=NORMAL)

    # noinspection PyUnusedLocal
    def set_output_direction(self, *args):
        self.plc_data.output_direction = self.plc_output_frame.direction.get()
        if self.plc_data.output_direction == 'read':
            self.plc_output_frame.change_state(state=DISABLED)
        elif self.plc_data.output_direction == 'write':
            self.plc_output_frame.change_state(state=NORMAL)

    # noinspection PyUnusedLocal
    def set_analog_direction(self, *args):
        self.plc_data.analog_direction = self.plc_analog_frame.direction.get()
        if self.plc_data.analog_direction == 'read':
            self.plc_analog_frame.change_state(state=DISABLED)
        elif self.plc_data.analog_direction == 'write':
            self.plc_analog_frame.change_state(state=NORMAL)

    def change_input(self):
        self.plc_data.input1 = bool(self.plc_input_frame.input1_var.get())
        self.plc_data.input2 = bool(self.plc_input_frame.input2_var.get())
        self.plc_data.input3 = bool(self.plc_input_frame.input3_var.get())
        self.plc_data.input4 = bool(self.plc_input_frame.input4_var.get())
        self.plc_data.input5 = bool(self.plc_input_frame.input5_var.get())
        self.plc_data.input6 = bool(self.plc_input_frame.input6_var.get())
        self.plc_data.input7 = bool(self.plc_input_frame.input7_var.get())
        self.plc_data.input8 = bool(self.plc_input_frame.input8_var.get())

    def change_output(self):
        self.plc_data.output1 = bool(self.plc_output_frame.output1_var.get())
        self.plc_data.output2 = bool(self.plc_output_frame.output2_var.get())
        self.plc_data.output3 = bool(self.plc_output_frame.output3_var.get())
        self.plc_data.output4 = bool(self.plc_output_frame.output4_var.get())
        self.plc_data.output5 = bool(self.plc_output_frame.output5_var.get())
        self.plc_data.output6 = bool(self.plc_output_frame.output6_var.get())
        self.plc_data.output7 = bool(self.plc_output_frame.output7_var.get())
        self.plc_data.output8 = bool(self.plc_output_frame.output8_var.get())
        self.plc_data.output9 = bool(self.plc_output_frame.output9_var.get())
        self.plc_data.output10 = bool(self.plc_output_frame.output10_var.get())

    # noinspection PyUnusedLocal
    def change_analog(self, *args):
        self.plc_data.analog_input_ch0 = self.plc_analog_frame.analog_ch0_var.get()
        self.plc_data.analog_input_ch1 = self.plc_analog_frame.analog_ch1_var.get()

    def loop(self):
        super().loop()

        if self.plc_data.input_is_change():
            self.refresh_input()

        if self.plc_data.output_is_change():
            self.refresh_output()

        if self.plc_data.analog_is_changed():
            self.refresh_analog()

    def refresh_input(self):
        self.plc_input_frame.input1_var.set(self.plc_data.input1)
        self.plc_input_frame.input2_var.set(self.plc_data.input2)
        self.plc_input_frame.input3_var.set(self.plc_data.input3)
        self.plc_input_frame.input4_var.set(self.plc_data.input4)
        self.plc_input_frame.input5_var.set(self.plc_data.input5)
        self.plc_input_frame.input6_var.set(self.plc_data.input6)
        self.plc_input_frame.input7_var.set(self.plc_data.input7)
        self.plc_input_frame.input8_var.set(self.plc_data.input8)

    def refresh_output(self):
        self.plc_output_frame.output1_var.set(self.plc_data.output1)
        self.plc_output_frame.output2_var.set(self.plc_data.output2)
        self.plc_output_frame.output3_var.set(self.plc_data.output3)
        self.plc_output_frame.output4_var.set(self.plc_data.output4)
        self.plc_output_frame.output5_var.set(self.plc_data.output5)
        self.plc_output_frame.output6_var.set(self.plc_data.output6)
        self.plc_output_frame.output7_var.set(self.plc_data.output7)
        self.plc_output_frame.output8_var.set(self.plc_data.output8)
        self.plc_output_frame.output9_var.set(self.plc_data.output9)
        self.plc_output_frame.output10_var.set(self.plc_data.output10)

    def refresh_analog(self):
        self.plc_analog_frame.analog_ch0_var.set(self.plc_data.analog_input_ch0)
        self.plc_analog_frame.analog_ch1_var.set(self.plc_data.analog_input_ch1)


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
