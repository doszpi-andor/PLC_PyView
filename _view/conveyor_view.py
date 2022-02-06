from tkinter import Frame, Tk, Canvas


class ConveyorView(Frame):
    """
    Conveyor view
    :param int conv_number: conveyor number
    :param int motor_number: conveyor motor and indicator number
    :param int length: conveyor width
    :param int shift_x: shifting x coordinate
    :param str motor_color: motor color name string
    :param str indicator_color: indicator color name string
    """

    # noinspection PyDefaultArgument
    def __init__(self, master=None, conv_number=0, motor_number=0, length=460, shift_x=0,
                 motor_color='gray', indicator_color='gray', mirror='no', cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.__conv_number = conv_number
        self.__motor_number = motor_number
        self.__motor_color = motor_color
        self.__indicator_color = indicator_color
        self.__length = length
        self.__shift_x = shift_x
        self.__mirror = mirror
        self.__canvas = Canvas(self, height=60, width=self.__length + self.__shift_x)
        self.__drawing()
        self.__canvas.pack(side='left')

    def __drawing(self):
        self.__canvas.create_line(30 + self.__shift_x, 5, self.__length - 30 + self.__shift_x, 5)
        self.__canvas.create_line(30 + self.__shift_x, 55, self.__length - 30 + self.__shift_x, 55)
        # noinspection SpellCheckingInspection
        self.__canvas.create_text(self.__length / 2 + self.__shift_x, 30, text=f"Szalag {self.__conv_number}")
        if self.__mirror == 'no':
            self.__canvas.create_oval(5 + self.__shift_x, 5, 55 + self.__shift_x, 55, fill=self.__motor_color)
            self.__canvas.create_oval(self.__length - 55 + self.__shift_x, 5, self.__length - 5 + self.__shift_x, 55,
                                      fill=self.__indicator_color)
            self.__canvas.create_text(30 + self.__shift_x, 30, text=f"M{self.__motor_number}")
            self.__canvas.create_text(self.__length - 30 + self.__shift_x, 30, text=f"S{self.__motor_number}")
        elif self.__mirror == 'yes':
            self.__canvas.create_oval(self.__length - 55 + self.__shift_x, 5, self.__length - 5 + self.__shift_x, 55,
                                      fill=self.__motor_color)
            self.__canvas.create_oval(5 + self.__shift_x, 5, 55 + self.__shift_x, 55, fill=self.__indicator_color)
            self.__canvas.create_text(self.__length - 30 + self.__shift_x, 30, text=f"M{self.__motor_number}")
            self.__canvas.create_text(30 + self.__shift_x, 30, text=f"S{self.__motor_number}")

    def change_motor_color(self, color) -> None:
        """
        Motor color change
        :param str color: motor color name string
        """
        if color != self.__motor_color:
            self.__motor_color = color
            self.__drawing()

    def change_indicator_color(self, color) -> None:
        """
        Indicator color change
        :param str color: indicator color name string
        """
        if color != self.__indicator_color:
            self.__indicator_color = color
            self.__drawing()


if __name__ == "__main__":
    root = Tk()

    conveyor1 = ConveyorView(root, conv_number=1, motor_number=1, length=230)
    conveyor1.grid(row=1, column=1, sticky='W')
    conveyor2 = ConveyorView(root, conv_number=2, motor_number=2, shift_x=100)
    conveyor2.grid(row=2, column=1)

    conveyor2.change_motor_color('green')
    conveyor2.change_indicator_color('red')

    root.mainloop()
