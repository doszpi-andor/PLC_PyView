from tkinter import Canvas, Tk


class WagonCanvas(Canvas):
    WAGON_WIDTH = 200
    WAGON_HEIGHT = 80
    WAGON_NAME_FONT_SIZE = 12

    def create_wagon(self, x_position, y_position, wagon_name='',
                     wagon_color='light gray', wheel_color='dim gray', rail_color='black'):
        self.create_polygon(x_position,
                            y_position,
                            x_position + self.WAGON_WIDTH // 8,
                            y_position + self.WAGON_HEIGHT * 2 // 3,
                            x_position + self.WAGON_WIDTH // 8,
                            y_position + self.WAGON_HEIGHT * 2 // 3,
                            x_position + self.WAGON_WIDTH * 7 // 8,
                            y_position + self.WAGON_HEIGHT * 2 // 3,
                            x_position + self.WAGON_WIDTH * 7 // 8,
                            y_position + self.WAGON_HEIGHT * 2 // 3,
                            x_position + self.WAGON_WIDTH,
                            y_position,
                            fill=wagon_color, outline='black')
        self.create_oval(x_position + self.WAGON_WIDTH // 8,
                         y_position + self.WAGON_HEIGHT * 2 // 3,
                         x_position + self.WAGON_WIDTH * 2 // 8,
                         y_position + self.WAGON_HEIGHT * 2 // 3 + self.WAGON_WIDTH // 8,
                         fill=wheel_color)
        self.create_oval(x_position + self.WAGON_WIDTH * 6 // 8,
                         y_position + self.WAGON_HEIGHT * 2 // 3,
                         x_position + self.WAGON_WIDTH * 7 // 8,
                         y_position + self.WAGON_HEIGHT * 2 // 3 + self.WAGON_WIDTH // 8,
                         fill=wheel_color)
        self.create_rectangle(x_position,
                              y_position + self.WAGON_HEIGHT * 2 // 3 + self.WAGON_WIDTH // 8,
                              x_position + self.WAGON_WIDTH,
                              y_position + self.WAGON_HEIGHT,
                              fill=rail_color)
        self.create_text(x_position + self.WAGON_WIDTH // 2,
                         y_position + self.WAGON_HEIGHT // 3,
                         font=("Arial", self.WAGON_NAME_FONT_SIZE),
                         text=wagon_name)


if __name__ == "__main__":
    root = Tk()

    wagon = WagonCanvas(root)
    wagon.create_wagon(5, 5, wagon_name='Vagon 1')
    wagon.pack()

    root.mainloop()
