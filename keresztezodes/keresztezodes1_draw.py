from tkinter import Tk

from _view.indicator_canvas import IndicatorCanvas


class Keresztezodes1_View(IndicatorCanvas):
    INDICATOR_WIDTH = 40

    PADDING = 3

    A_LAMP_X_POSITION = 20
    B_LAMP_X_POSITION = 120

    TEXT_Y_POSITION = 10
    LAMP_Y_POSITION = 25

    FULL_WIDTH = B_LAMP_X_POSITION + INDICATOR_WIDTH + PADDING * 2 + 10
    FULL_HEIGHT = LAMP_Y_POSITION + INDICATOR_WIDTH * 3 + PADDING * 4

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.a_red_color = 'gray'
        self.a_yellow_color = 'gray'
        self.a_green_color = 'gray'

        self.b_red_color = 'gray'
        self.b_yellow_color = 'gray'
        self.b_green_color = 'gray'

        self.__a_lamp_drawing()
        self.__b_lamp_drawing()

    def a_lamp_change_color(self, red_color, yellow_color, green_color):
        if self.a_red_color != red_color or self.a_yellow_color != yellow_color or self.a_green_color != green_color:
            self.a_red_color = red_color
            self.a_yellow_color = yellow_color
            self.a_green_color = green_color

            self.__a_lamp_drawing()

    def b_lamp_change_color(self, red_color, yellow_color, green_color):
        if self.b_red_color != red_color or self.b_yellow_color != yellow_color or self.b_green_color != green_color:
            self.b_red_color = red_color
            self.b_yellow_color = yellow_color
            self.b_green_color = green_color

            self.__b_lamp_drawing()

    def __a_lamp_drawing(self):
        self.create_text(self.A_LAMP_X_POSITION + self.INDICATOR_WIDTH / 2 + self.PADDING,
                         self.TEXT_Y_POSITION,
                         text='A irány', font=('Arial 15 bold'))

        self.create_rectangle(self.A_LAMP_X_POSITION,
                              self.LAMP_Y_POSITION,
                              self.A_LAMP_X_POSITION + self.INDICATOR_WIDTH + self.PADDING * 2,
                              self.LAMP_Y_POSITION + self.INDICATOR_WIDTH * 3 + self.PADDING * 4,
                              fill='black')

        self.create_circle_indicator(self.A_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.PADDING,
                                     color=self.a_red_color)

        self.create_circle_indicator(self.A_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.INDICATOR_WIDTH + self.PADDING * 2,
                                     color=self.a_yellow_color)

        self.create_circle_indicator(self.A_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.INDICATOR_WIDTH * 2 + self.PADDING * 3,
                                     color=self.a_green_color)

    def __b_lamp_drawing(self):
        self.create_text(self.B_LAMP_X_POSITION + self.INDICATOR_WIDTH / 2 + self.PADDING,
                         self.TEXT_Y_POSITION,
                         text='B irány', font=('Arial 15 bold'))

        self.create_rectangle(self.B_LAMP_X_POSITION,
                              self.LAMP_Y_POSITION,
                              self.B_LAMP_X_POSITION + self.INDICATOR_WIDTH + self.PADDING * 2,
                              self.LAMP_Y_POSITION + self.INDICATOR_WIDTH * 3 + self.PADDING * 4,
                              fill='black')

        self.create_circle_indicator(self.B_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.PADDING,
                                     color=self.b_red_color)

        self.create_circle_indicator(self.B_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.INDICATOR_WIDTH + self.PADDING * 2,
                                     color=self.b_yellow_color)

        self.create_circle_indicator(self.B_LAMP_X_POSITION + self.PADDING,
                                     self.LAMP_Y_POSITION + self.INDICATOR_WIDTH * 2 + self.PADDING * 3,
                                     color=self.b_green_color)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x480")

    conveyor = Keresztezodes1_View(root)
    conveyor.pack()

    root.mainloop()
