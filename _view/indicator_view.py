from tkinter import Frame, Canvas, Tk, W


class IndicatorView(Frame):
    """
    Indicator view
    :param str text: indicator name
    :param str color: indicator color name string
    :param int length: indicator width (optional)
    """

    # noinspection PyDefaultArgument
    def __init__(self, master=None, text='', color='gray', length=None, cnf={}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self.text = text
        self.color = color
        self.length = length
        self.canvas = Canvas(self, height=40, width=length)
        self.drawing()
        self.canvas.pack()

    def drawing(self) -> None:
        """
        Drawing an indicator
        """
        name = self.canvas.create_text(40, 20, anchor='w', text=self.text)
        length = self.canvas.bbox(name)[2]
        if self.length is None:
            self.canvas.config(width=length)

    def change_color(self, color) -> None:
        """
        Indicator color change
        :param str color: color name string
        """
        if color != self.color:
            self.color = color
            self.drawing()


class IndicatorOval(IndicatorView):
    """
    Oval indicator
    """

    def drawing(self) -> None:
        """
        Drawing an oval indicator
        """
        super().drawing()
        self.canvas.create_oval(5, 5, 35, 35, fill=self.color)


class IndicatorSquare(IndicatorView):
    """
    Square indicator
    """

    def drawing(self) -> None:
        """
        Drawing a square indicator
        """
        super().drawing()
        self.canvas.create_rectangle(5, 5, 35, 35, fill=self.color)


def flash():
    if indicator1.color == 'gray':
        indicator1.change_color('red')
    else:
        indicator1.change_color('gray')
    root.after(500, flash)


if __name__ == "__main__":
    root = Tk()

    indicator1 = IndicatorOval(root, text='Running')
    indicator2 = IndicatorSquare(root, text='Start')
    indicator1.grid(row=1, column=1, sticky=W)
    indicator2.grid(row=2, column=1, sticky=W)

    root.after(500, flash)

    root.mainloop()
