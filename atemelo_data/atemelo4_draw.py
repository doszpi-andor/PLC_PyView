from tkinter import Tk

from _view.tank_canvas import TankCanvas, PipeCanvas


class Atemelo4_View(TankCanvas, PipeCanvas):

    TANK_WIDTH = 120
    TANK_HEIGHT = 240

    TANK_X_POSITION = 5

    TANK_Y_POSITION = 5

    FULL_WIDTH = 400
    FULL_HEIGHT = 400

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__tank_drawing()

    def __tank_drawing(self):
        self.create_tank(x_position=self.TANK_X_POSITION,
                         y_position=self.TANK_Y_POSITION,
                         tank_name='', tank_color='gray')


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    tank = Atemelo4_View(root)
    tank.pack()

    root.mainloop()
