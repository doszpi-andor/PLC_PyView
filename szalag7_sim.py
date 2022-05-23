from threading import Timer
from tkinter import Frame, Checkbutton, IntVar

from _view.plc_view import PLC_ViewA
from szalag_data.szalag7_data import Szalag7_data
from szalag_data.szalag7_draw import Szalag7_View


class ConveyorError(Frame):

    def __init__(self, master=None, error1_process=None, error2_process=None,
                 error3_process=None, error4_process=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.error1_var = IntVar()
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')
        self.error3_var = IntVar()
        self.error3 = Checkbutton(self, variable=self.error3_var, command=error3_process, text='Szalag 3 hiba')
        self.error4_var = IntVar()
        self.error4 = Checkbutton(self, variable=self.error4_var, command=error4_process, text='Szalag 4 hiba')
        self.error1.grid(row=1, column=1)
        self.error2.grid(row=1, column=2)
        self.error3.grid(row=1, column=3)
        self.error4.grid(row=1, column=4)


class App(PLC_ViewA):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('Szalag 7')
        self.name_label.config(text='Szalag 7')

        self.conveyor_error = ConveyorError(error1_process=self.error1_change,
                                            error2_process=self.error2_change,
                                            error3_process=self.error3_change,
                                            error4_process=self.error4_change)
        self.conveyors = Szalag7_View(self.process_frame)
        self.conveyor_error.pack()
        self.conveyors.pack()

        self.plc_data = Szalag7_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def data_transfer(self):
        super().data_transfer()
        self.plc_data.write_data()

    def error1_change(self):
        if self.conveyor_error.error1_var.get():
            self.plc_data.s1 = False
            self.conveyors.conveyor1_mame_change_color(name_color='red')
        else:
            self.s1_on_delay()
            self.conveyors.conveyor1_mame_change_color(name_color='black')
        self.conveyor1_refresh()

    def error2_change(self):
        if self.conveyor_error.error2_var.get():
            self.plc_data.s2 = False
            self.conveyors.conveyor2_mame_change_color(name_color='red')
        else:
            self.s2_on_delay()
            self.conveyors.conveyor2_mame_change_color(name_color='black')
        self.conveyor2_refresh()

    def error3_change(self):
        if self.conveyor_error.error3_var.get():
            self.plc_data.s3 = False
            self.conveyors.conveyor3_mame_change_color(name_color='red')
        else:
            self.s3_on_delay()
            self.conveyors.conveyor3_mame_change_color(name_color='black')
        self.conveyor3_refresh()

    def error4_change(self):
        if self.conveyor_error.error4_var.get():
            self.plc_data.s4 = False
            self.conveyors.conveyor4_mame_change_color(name_color='red')
        else:
            self.s4_on_delay()
            self.conveyors.conveyor4_mame_change_color(name_color='black')
        self.conveyor4_refresh()

    def loop(self):
        super().loop()

        if self.plc_data.start_is_changed() or self.plc_data.stop_is_changed():
            self.button_refresh()

        if self.plc_data.uzem_is_changed() or self.plc_data.hiba_is_changed():
            self.indicator_refresh()

        if self.plc_data.m1_is_changed():
            self.plc_data.s1 = False
            if self.plc_data.m1 and not self.conveyor_error.error1_var.get():
                self.s1_on_delay()
            self.conveyor1_refresh()

        if self.plc_data.m2_is_changed():
            self.plc_data.s2 = False
            if self.plc_data.m2 and not self.conveyor_error.error2_var.get():
                self.s2_on_delay()
            self.conveyor2_refresh()

        if self.plc_data.m3_is_changed():
            self.plc_data.s3 = False
            if self.plc_data.m3 and not self.conveyor_error.error3_var.get():
                self.s3_on_delay()
            self.conveyor3_refresh()

        if self.plc_data.m4_is_changed():
            self.plc_data.s4 = False
            if self.plc_data.m4 and not self.conveyor_error.error4_var.get():
                self.s4_on_delay()
            self.conveyor4_refresh()

    def s1_on_delay(self):
        timer = Timer(1.5, self.s1_changed)
        timer.start()

    def s1_changed(self):
        if self.plc_data.m1 and not self.conveyor_error.error1_var.get():
            self.plc_data.s1 = True
        self.conveyor1_refresh()

    def s2_on_delay(self):
        timer = Timer(1.5, self.s2_changed)
        timer.start()

    def s2_changed(self):
        if self.plc_data.m2 and not self.conveyor_error.error2_var.get():
            self.plc_data.s2 = True
        self.conveyor2_refresh()

    def s3_on_delay(self):
        timer = Timer(1.5, self.s3_changed)
        timer.start()

    def s3_changed(self):
        if self.plc_data.m3 and not self.conveyor_error.error3_var.get():
            self.plc_data.s3 = True
        self.conveyor3_refresh()

    def s4_on_delay(self):
        timer = Timer(1.5, self.s4_changed)
        timer.start()

    def s4_changed(self):
        if self.plc_data.m4 and not self.conveyor_error.error4_var.get():
            self.plc_data.s4 = True
        self.conveyor4_refresh()

    def button_refresh(self):
        # 1 1
        if self.plc_data.start and self.plc_data.stop:
            self.conveyors.button_change_color(start_color='green', stop_color='red')
        # 0 1
        elif not self.plc_data.start and self.plc_data.stop:
            self.conveyors.button_change_color(start_color='gray', stop_color='red')
        # 1 0
        elif self.plc_data.start and not self.plc_data.stop:
            self.conveyors.button_change_color(start_color='green', stop_color='gray')
        # 0 0
        else:
            self.conveyors.button_change_color(start_color='gray', stop_color='gray')

    def indicator_refresh(self):
        # 1 1
        if self.plc_data.uzem and self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='green', error_color='red')
        # 0 1
        elif not self.plc_data.uzem and self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='gray', error_color='red')
        # 1 0
        elif self.plc_data.uzem and not self.plc_data.hiba:
            self.conveyors.indicator_change_color(factory_color='green', error_color='gray')
        # 0 0
        else:
            self.conveyors.indicator_change_color(factory_color='gray', error_color='gray')

    def conveyor1_refresh(self):
        # 1 1
        if self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m1 and self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m1 and not self.plc_data.s1:
            self.conveyors.conveyor1_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor1_change_color(motor_color='grey', sensor_color='grey')

    def conveyor2_refresh(self):
        # 1 1
        if self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m2 and self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m2 and not self.plc_data.s2:
            self.conveyors.conveyor2_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor2_change_color(motor_color='grey', sensor_color='grey')

    def conveyor3_refresh(self):
        # 1 1
        if self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m3 and self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m3 and not self.plc_data.s3:
            self.conveyors.conveyor3_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor3_change_color(motor_color='grey', sensor_color='grey')

    def conveyor4_refresh(self):
        # 1 1
        if self.plc_data.m4 and self.plc_data.s4:
            self.conveyors.conveyor4_change_color(motor_color='green', sensor_color='green')
        # 0 1
        elif not self.plc_data.m4 and self.plc_data.s4:
            self.conveyors.conveyor4_change_color(motor_color='gray', sensor_color='yellow')
        # 1 0
        elif self.plc_data.m4 and not self.plc_data.s4:
            self.conveyors.conveyor4_change_color(motor_color='green', sensor_color='red')
        # 0 0
        else:
            self.conveyors.conveyor4_change_color(motor_color='grey', sensor_color='grey')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
