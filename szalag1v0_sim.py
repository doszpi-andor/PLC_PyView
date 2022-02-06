from tkinter import Frame, Label, IntVar, Checkbutton

from _config.plc_config_read import PLC_Config
from _plc_data.plc_data import PLC_Address, PLC_data
from szalag1v0_view import App


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

    BYTES_ADDRESS = ('IB0', )


class IO_data(PLC_data):

    def __init__(self):
        super().__init__(IO_Address())
        self.input1 = False
        self.input2 = False
        self.input3 = False
        self.input4 = False
        self.input5 = False
        self.input6 = False
        self.input7 = False
        self.input8 = False

    def write_data(self):

        for byte_address in IO_Address.BYTES_ADDRESS:
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

        super().write_data()


class PLC_InputView(Frame):

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


class IO_App(App):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.io_data = IO_data()

        self.io_frame = PLC_InputView(self, change_process=self.change_input)
        self.io_frame.pack()

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


if __name__ == '__main__':
    app = IO_App()

    app.after(100, app.loop)

    app.mainloop()
