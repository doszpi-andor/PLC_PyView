from tkinter import Canvas, Tk, W


class IndicatorCanvas(Canvas):
    INDICATOR_WIDTH = 20
    INDICATOR_TEXT_SHIFT = 5
    INDICATOR_FONT_SIZE = 10

    def create_square_indicator(self, x_position, y_position, name='', color='gray'):

        self.create_rectangle(x_position,
                              y_position,
                              x_position + self.INDICATOR_WIDTH,
                              y_position + self.INDICATOR_WIDTH,
                              fill=color)
        self.create_text(x_position + self.INDICATOR_WIDTH + self.INDICATOR_TEXT_SHIFT,
                         y_position + self.INDICATOR_WIDTH // 2,
                         font=("Arial", self.INDICATOR_FONT_SIZE),
                         anchor=W, text=name)

    def create_circle_indicator(self, x_position, y_position, name='', color='gray'):

        self.create_oval(x_position,
                         y_position,
                         x_position + self.INDICATOR_WIDTH,
                         y_position + self.INDICATOR_WIDTH,
                         fill=color)
        self.create_text(x_position + self.INDICATOR_WIDTH + self.INDICATOR_TEXT_SHIFT,
                         y_position + self.INDICATOR_WIDTH // 2,
                         font=("Arial", self.INDICATOR_FONT_SIZE),
                         anchor=W, text=name)

    def create_delta_indicator(self, x_position, y_position, direction='right', color='gray'):
        if direction == 'right':
            self.create_polygon(x_position,
                                y_position,
                                x_position,
                                y_position + self.INDICATOR_WIDTH,
                                x_position + self.INDICATOR_WIDTH,
                                y_position + self.INDICATOR_WIDTH // 2,
                                fill=color, outline='black')
        elif direction == 'left':
            self.create_polygon(x_position + self.INDICATOR_WIDTH,
                                y_position,
                                x_position + self.INDICATOR_WIDTH,
                                y_position + self.INDICATOR_WIDTH,
                                x_position,
                                y_position + self.INDICATOR_WIDTH // 2,
                                fill=color, outline='black')


if __name__ == "__main__":
    root = Tk()

    indicators = IndicatorCanvas(root)
    indicators.create_square_indicator(5, 5, name='Start', color='green')
    indicators.create_circle_indicator(5, 30, name='Error', color='red')
    indicators.create_delta_indicator(5, 60, direction='left')
    indicators.create_delta_indicator(30, 60, direction='right')
    indicators.pack()

    root.mainloop()
