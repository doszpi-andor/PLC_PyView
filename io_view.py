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
        super().loop()


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
