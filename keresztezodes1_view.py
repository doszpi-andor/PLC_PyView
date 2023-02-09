from _view.plc_view import PLC_ViewA
from szalag_data.keresztezodes1_draw import Keresztezodes1_View
from szalag_data.keresztezodes_1_data import Keresztezodes1_data


class App(PLC_ViewA):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('Kereszteződés 1')
        self.name_label.config(text='')

        self.lamps = Keresztezodes1_View(self.process_frame)
        self.lamps.pack()

        self.plc_data = Keresztezodes1_data(self.ip_select.ip_address.get(), self.plc_rack, self.plc_slot)

        self.transfer_loop.start()

    def data_transfer(self):
        self.plc_data.read_data()

    def loop(self):
        super().loop()

        if self.plc_data.a_piros_is_changed() or\
                self.plc_data.a_sarga_is_changed() or\
                self.plc_data.a_zold_is_changed():
            self.a_lamp_refresh()

        if self.plc_data.b_piros_is_changed() or\
                self.plc_data.b_sarga_is_changed() or\
                self.plc_data.b_zold_is_changed():
            self.b_lamp_refresh()

    def a_lamp_refresh(self):
        # 1 1 1
        if self.plc_data.a_piros and self.plc_data.a_sarga and self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='red', yellow_color='yellow', green_color='green')
        # 0 1 1
        elif not self.plc_data.a_piros and self.plc_data.a_sarga and self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='gray', yellow_color='yellow', green_color='green')
        # 1 0 1
        elif self.plc_data.a_piros and not self.plc_data.a_sarga and self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='red', yellow_color='gray', green_color='green')
        # 0 0 1
        elif not self.plc_data.a_piros and not self.plc_data.a_sarga and self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='gray', yellow_color='gray', green_color='green')
        # 1 1 0
        elif self.plc_data.a_piros and self.plc_data.a_sarga and not self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='red', yellow_color='yellow', green_color='gray')
        # 0 1 0
        elif not self.plc_data.a_piros and self.plc_data.a_sarga and not self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='gray', yellow_color='yellow', green_color='gray')
        # 1 0 0
        elif self.plc_data.a_piros and not self.plc_data.a_sarga and not self.plc_data.a_zold:
            self.lamps.a_lamp_change_color(red_color='red', yellow_color='gray', green_color='gray')
        # 0 0 0
        else:
            self.lamps.a_lamp_change_color(red_color='gray', yellow_color='gray', green_color='gray')

    def b_lamp_refresh(self):
        # 1 1 1
        if self.plc_data.b_piros and self.plc_data.b_sarga and self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='red', yellow_color='yellow', green_color='green')
        # 0 1 1
        elif not self.plc_data.b_piros and self.plc_data.b_sarga and self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='gray', yellow_color='yellow', green_color='green')
        # 1 0 1
        elif self.plc_data.b_piros and not self.plc_data.b_sarga and self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='red', yellow_color='gray', green_color='green')
        # 0 0 1
        elif not self.plc_data.b_piros and not self.plc_data.b_sarga and self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='gray', yellow_color='gray', green_color='green')
        # 1 1 0
        elif self.plc_data.b_piros and self.plc_data.b_sarga and not self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='red', yellow_color='yellow', green_color='gray')
        # 0 1 0
        elif not self.plc_data.b_piros and self.plc_data.b_sarga and not self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='gray', yellow_color='yellow', green_color='gray')
        # 1 0 0
        elif self.plc_data.b_piros and not self.plc_data.b_sarga and not self.plc_data.b_zold:
            self.lamps.b_lamp_change_color(red_color='red', yellow_color='gray', green_color='gray')
        # 0 0 0
        else:
            self.lamps.b_lamp_change_color(red_color='gray', yellow_color='gray', green_color='gray')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()