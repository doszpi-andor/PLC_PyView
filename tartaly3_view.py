
from tkinter import Frame, RIGHT, W

from _view.plc_view import PLC_View
from tartaly_data.tartaly3_data import Tartaly3_Address, Tartaly3_data
from tartaly_data.tartaly3_draw import Tartaly3_View
from _view.indicator_view import IndicatorSquare, IndicatorOval


class Indicators(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.start = IndicatorSquare(self, text='Start [%s]' % Tartaly3_Address.START)
        self.stop = IndicatorSquare(self, text='Stop [%s]' % Tartaly3_Address.STOP)
        # noinspection SpellCheckingInspection
        self.bekapcsolva = IndicatorOval(self, text='Bekapcsolva [%s]' % Tartaly3_Address.BEKAPCSOLVA)
        # noinspection SpellCheckingInspection
        self.kikapcsolva = IndicatorOval(self, text='Kikapcsolva [%s]' % Tartaly3_Address.KIKAPCSOLVA)

        self.start.grid(row=1, column=1, sticky=W)
        self.stop.grid(row=2, column=1, sticky=W)
        self.bekapcsolva.grid(row=3, column=1, sticky=W)
        self.kikapcsolva.grid(row=4, column=1, sticky=W)


class App(PLC_View):
    __closed = False

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.title('Tartály 3')
        # noinspection SpellCheckingInspection
        self.name_label.config(text='Tartály 3')

        self.indicators = Indicators(self.process_frame)
        self.tanks = Tartaly3_View(self.process_frame)

        self.indicators.pack(side=RIGHT)
        self.tanks.pack()

        self.plc_data = Tartaly3_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

    def loop(self):

        if self.plc_data.start_is_change():
            self.start_refresh()

        if self.plc_data.stop_is_change():
            self.stop_refresh()

        if self.plc_data.bekapcsolva_is_changed():
            self.bekapcsolva_refresh()

        if self.plc_data.kikapcsolva_is_changed():
            self.kikapcsolva_refresh()

        if self.plc_data.t1_felso_is_changed() or self.plc_data.t1_also_is_changed() \
                or self.plc_data.t1_tolt_is_changed():
            self.tank1_refresh()

        if self.plc_data.t2_felso_is_changed() or self.plc_data.t2_also_is_changed() \
                or self.plc_data.t2_tolt_is_changed():
            self.tank2_refresh()

        if self.plc_data.t3_felso_is_changed() or self.plc_data.t3_also_is_changed() \
                or self.plc_data.t3_tolt_is_changed():
            self.tank3_refresh()

        super().loop()

    def start_refresh(self):
        if self.plc_data.start:
            self.indicators.start.change_color('green')
        else:
            self.indicators.start.change_color('gray')

    def stop_refresh(self):
        if self.plc_data.stop:
            self.indicators.stop.change_color('red')
        else:
            self.indicators.stop.change_color('gray')

    # noinspection SpellCheckingInspection
    def bekapcsolva_refresh(self):
        if self.plc_data.bekapcsolva:
            self.indicators.bekapcsolva.change_color('green')
        else:
            self.indicators.bekapcsolva.change_color('gray')

    # noinspection SpellCheckingInspection
    def kikapcsolva_refresh(self):
        if self.plc_data.kikapcsolva:
            self.indicators.kikapcsolva.change_color('red')
        else:
            self.indicators.kikapcsolva.change_color('gray')

    def tank1_refresh(self):
        # 1 1 1
        if self.plc_data.t1_tolt and self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t1_tolt and self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t1_tolt and not self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t1_tolt and not self.plc_data.t1_felso and self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t1_tolt and self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t1_tolt and self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t1_tolt and not self.plc_data.t1_felso and not self.plc_data.t1_also:
            self.tanks.tank1_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank1_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')

    def tank2_refresh(self):
        # 1 1 1
        if self.plc_data.t2_tolt and self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t2_tolt and self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t2_tolt and not self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t2_tolt and not self.plc_data.t2_felso and self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t2_tolt and self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t2_tolt and self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t2_tolt and not self.plc_data.t2_felso and not self.plc_data.t2_also:
            self.tanks.tank2_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank2_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')

    def tank3_refresh(self):
        # 1 1 1
        if self.plc_data.t3_tolt and self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='blue')
        # 0 1 1
        elif not self.plc_data.t3_tolt and self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='blue')
        # 1 0 1
        elif self.plc_data.t3_tolt and not self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='blue')
        # 0 0 1
        elif not self.plc_data.t3_tolt and not self.plc_data.t3_felso and self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='blue')
        # 1 1 0
        elif self.plc_data.t3_tolt and self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='green', top_sensor_color='blue', bottom_sensor_color='gray')
        # 0 1 0
        elif not self.plc_data.t3_tolt and self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='gray', top_sensor_color='blue', bottom_sensor_color='gray')
        # 1 0 0
        elif self.plc_data.t3_tolt and not self.plc_data.t3_felso and not self.plc_data.t3_also:
            self.tanks.tank3_change_colors(top_valve_color='green', top_sensor_color='gray', bottom_sensor_color='gray')
        # 0 0 0
        else:
            self.tanks.tank3_change_colors(top_valve_color='gray', top_sensor_color='gray', bottom_sensor_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
