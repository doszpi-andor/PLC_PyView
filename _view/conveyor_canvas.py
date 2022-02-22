from tkinter import Canvas, Tk, CENTER


class ConveyorCanvas(Canvas):
    CONVEYOR_WIDTH = 50

    def create_conveyor(self, x_position, y_position, length, name='', circle1_name='',
                        circle1_color='gray', circle2_name='', circle2_color='gray'):
        self.create_line(x_position + self.CONVEYOR_WIDTH // 2,
                         y_position,
                         x_position + length - self.CONVEYOR_WIDTH // 2,
                         y_position)
        self.create_line(x_position + self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH,
                         x_position + length - self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH)
        self.create_text(x_position + length // 2,
                         y_position + self.CONVEYOR_WIDTH // 2,
                         text=name)
        self.create_oval(x_position,
                         y_position,
                         x_position + self.CONVEYOR_WIDTH,
                         y_position + self.CONVEYOR_WIDTH,
                         fill=circle1_color)
        self.create_text(x_position + self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH // 2,
                         justify=CENTER, text=circle1_name)
        self.create_oval(x_position + length - self.CONVEYOR_WIDTH,
                         y_position,
                         x_position + length,
                         y_position + self.CONVEYOR_WIDTH,
                         fill=circle2_color)
        self.create_text(x_position + length - self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH // 2,
                         justify=CENTER, text=circle2_name)


if __name__ == "__main__":
    root = Tk()

    silo = ConveyorCanvas(root)
    silo.create_conveyor(5, 5, length=300, name='Szalag 1', circle1_name='M1\n[Q0.0]', circle2_name='S1\n[I0.0]')
    silo.pack()

    root.mainloop()
