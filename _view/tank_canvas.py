from tkinter import Canvas, ARC, W, CHORD, CENTER, S, Tk


class TankCanvas(Canvas):
    """
    Tank canvas
    :var int TANK_WIDTH: tank width
    :var int TANK_HEIGHT: tank height
    :var int NAME_FONT_SIZE: tank name font size
    """
    TANK_WIDTH = 90
    TANK_HEIGHT = 220
    TANK_NAME_FONT_SIZE = 15

    def create_tank(self, x_position, y_position, tank_name, tank_color) -> None:
        """
        Create tank
        :param int x_position: tank x position
        :param int y_position: tank y position
        :param str tank_name:  tank name
        :param str tank_color: tank color name string
        """
        self.create_arc(x_position,
                        y_position,
                        x_position + self.TANK_WIDTH,
                        y_position + self.TANK_WIDTH,
                        start=0, extent=180, style=CHORD, fill=tank_color, outline=tank_color)
        self.create_rectangle(x_position,
                              y_position + self.TANK_WIDTH // 2,
                              x_position + self.TANK_WIDTH,
                              y_position + self.TANK_HEIGHT - self.TANK_WIDTH // 2,
                              fill=tank_color, outline=tank_color)
        self.create_arc(x_position,
                        y_position + self.TANK_HEIGHT - self.TANK_WIDTH,
                        x_position + self.TANK_WIDTH,
                        y_position + self.TANK_HEIGHT,
                        start=180, extent=180, style=CHORD, fill=tank_color, outline=tank_color)

        self.create_arc(x_position,
                        y_position,
                        x_position + self.TANK_WIDTH,
                        y_position + self.TANK_WIDTH,
                        start=0, extent=180, style=ARC)
        self.create_line(x_position,
                         y_position + self.TANK_WIDTH // 2,
                         x_position,
                         y_position + self.TANK_HEIGHT - self.TANK_WIDTH // 2)
        self.create_line(x_position + self.TANK_WIDTH,
                         y_position + self.TANK_WIDTH // 2,
                         x_position + self.TANK_WIDTH,
                         y_position + self.TANK_HEIGHT - self.TANK_WIDTH // 2)
        self.create_arc(x_position,
                        y_position + self.TANK_HEIGHT - self.TANK_WIDTH,
                        x_position + self.TANK_WIDTH,
                        y_position + self.TANK_HEIGHT,
                        start=180, extent=180, style=ARC)

        self.create_text(x_position + self.TANK_WIDTH // 2,
                         y_position + self.TANK_HEIGHT // 2,
                         font=("Arial", self.TANK_NAME_FONT_SIZE), text=tank_name)


class ValveCanvas(Canvas):
    """
    Valve canvas
    :var int VALVE_WIDTH: valve width
    :var int VALVE_HEIGHT: valve height
    """
    VALVE_WIDTH = 30
    VALVE_HEIGHT = 40
    VALVE_NAME_FONT_SIZE = 10

    def create_valve(self, x_position, y_position, name, color) -> None:
        """
        Create valve
        :param int x_position: valve x position
        :param int y_position: valve y position
        :param str name: valve name
        :param str color: valve color name string
        """
        self.create_polygon(x_position,
                            y_position,
                            x_position + self.VALVE_WIDTH,
                            y_position,
                            x_position + self.VALVE_WIDTH // 2,
                            y_position + self.VALVE_HEIGHT // 2,
                            outline='black',
                            fill=color)
        self.create_polygon(x_position,
                            y_position + self.VALVE_HEIGHT,
                            x_position + self.VALVE_WIDTH,
                            y_position + self.VALVE_HEIGHT,
                            x_position + self.VALVE_WIDTH // 2,
                            y_position + self.VALVE_HEIGHT // 2,
                            outline='black',
                            fill=color)

        self.create_text(x_position + self.VALVE_WIDTH,
                         y_position + self.VALVE_HEIGHT // 2,
                         font=("Arial", self.VALVE_NAME_FONT_SIZE),
                         anchor=W, text=name)


class PipeCanvas(Canvas):
    """
    Pipe canvas
    :var int PIPE_WIDTH: pipe width
    """
    PIPE_WIDTH = 10

    def create_horizontal_pipe(self, x_position, y_position, length, color='black') -> None:
        """
        Create horizontal pipe
        :param int x_position: pipe x position
        :param int y_position: pipe y position
        :param int length: pipe y length
        :param str color: pipe color name string
        """
        self.create_rectangle(x_position,
                              y_position,
                              x_position + length,
                              y_position + self.PIPE_WIDTH,
                              outline=color,
                              fill=color)

    def create_vertical_pipe(self, x_position, y_position, length, color='black') -> None:
        """
        Create vertical pipe
        :param int x_position: pipe x position
        :param int y_position: pipe y position
        :param int length: pipe x length
        :param str color: pipe color name string
        """
        self.create_rectangle(x_position,
                              y_position,
                              x_position + self.PIPE_WIDTH,
                              y_position + length,
                              outline=color,
                              fill=color)

    def create_diagonal_pipe(self, x_start, y_start, x_end, y_end, color='black') -> None:
        """
        Create diagonal pipe
        :param int x_start: pipe x start position
        :param int y_start: pipe y start position
        :param int x_end: pipe x end position
        :param int y_end: pipe y end position
        :param str color: color name string
        """
        self.create_polygon(x_start,
                            y_start,
                            x_start + self.PIPE_WIDTH,
                            y_start,
                            x_end + self.PIPE_WIDTH + 1,
                            y_end,
                            x_end,
                            y_end,
                            outline=color,
                            fill=color)


class HeatingCanvas(Canvas):
    """
    Heating canvas
    :var int HEATING_WIDTH: heating width
    :var int HEATING_HEIGHT: heating height
    """
    HEATING_WIDTH = 50
    HEATING_HEIGHT = 50
    HEATING_NAME_FONT_SIZE = 10

    def create_heating(self, x_position, y_position, name, color='black') -> None:
        """
        Create heating indicator
        :param int x_position: heating indicator x position
        :param int y_position: heating indicator y position
        :param str name: heating indicator name
        :param str color: heating indicator color name string
        """
        self.create_line(x_position,
                         y_position,
                         x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position,
                         width=2)

        self.create_line(x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position,
                         x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT // 12,
                         width=2)

        self.create_line(x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT // 12,
                         x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT // 6,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT // 6,
                         x_position + self.HEATING_WIDTH,
                         y_position + self.HEATING_HEIGHT // 3,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH,
                         y_position + self.HEATING_HEIGHT // 3,
                         x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT // 2,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT // 2,
                         x_position + self.HEATING_WIDTH,
                         y_position + self.HEATING_HEIGHT * 2 // 3,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH,
                         y_position + self.HEATING_HEIGHT * 2 // 3,
                         x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT * 5 // 6,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH * 3 // 5,
                         y_position + self.HEATING_HEIGHT * 5 // 6,
                         x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT * 11 // 12,
                         width=2, fill=color)

        self.create_line(x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT * 11 // 12,
                         x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT,
                         width=2)

        self.create_line(x_position,
                         y_position + self.HEATING_HEIGHT,
                         x_position + self.HEATING_WIDTH * 4 // 5,
                         y_position + self.HEATING_HEIGHT,
                         width=2)

        # noinspection PyArgumentList
        self.create_text(x_position,
                         y_position + self.HEATING_HEIGHT // 2,
                         font=("Arial", self.HEATING_NAME_FONT_SIZE),
                         angle=90, justify=CENTER, anchor=S, text=name)


class RotorCanvas(Canvas):
    """
    Rotor canvas
    :var int ROTOR_WIDTH: rotor width
    """
    ROTOR_WIDTH = 45
    ROTOR_NAME_FONT_SIZE = 10

    def create_rotor(self, x_position, y_position, name, color) -> None:
        """
        Create rotor indicator
        :param int x_position: rotor indicator x position
        :param int y_position: rotor indicator y position
        :param str name: rotor indicator name
        :param str color: rotor indicator color name string
        """
        arc_diameter = self.ROTOR_WIDTH * 4 // 3

        self.create_arc(x_position - arc_diameter * 3 // 4,
                        y_position - int(arc_diameter * 0.067),
                        x_position + arc_diameter // 4,
                        y_position + int(arc_diameter * 0.933),
                        start=0, extent=60, style=CHORD, fill=color)

        self.create_arc(x_position - arc_diameter * 3 // 4,
                        y_position - int(arc_diameter * 0.067),
                        x_position + arc_diameter // 4,
                        y_position + int(arc_diameter * 0.933),
                        start=300, extent=60, style=CHORD, fill=color)

        self.create_arc(x_position,
                        y_position - arc_diameter // 2,
                        x_position + arc_diameter,
                        y_position + arc_diameter // 2,
                        start=180, extent=60, style=CHORD, fill=color)

        self.create_arc(x_position,
                        y_position - arc_diameter // 2,
                        x_position + arc_diameter,
                        y_position + arc_diameter // 2,
                        start=240, extent=60, style=CHORD, fill=color)

        self.create_arc(x_position,
                        y_position + int(arc_diameter * 0.366),
                        x_position + arc_diameter,
                        y_position + int(arc_diameter * 1.366),
                        start=120, extent=60, style=CHORD, fill=color)

        self.create_arc(x_position,
                        y_position + int(arc_diameter * 0.366),
                        x_position + arc_diameter,
                        y_position + int(arc_diameter * 1.366),
                        start=60, extent=60, style=CHORD, fill=color)

        # noinspection PyArgumentList
        self.create_text(x_position - 10,
                         y_position + int(arc_diameter * 0.433),
                         font=("Arial", self.ROTOR_NAME_FONT_SIZE),
                         angle=90, justify=CENTER, anchor=S, text=name)

    @property
    def rotor_height(self) -> int:
        """
        Calculate rotor indicator height
        :return: rotor indicator height
        """
        return int(self.ROTOR_WIDTH * 1.155)


if __name__ == "__main__":
    root = Tk()

    tank = TankCanvas(root)
    tank.create_tank(5, 5, tank_name='T1', tank_color='gray')
    tank.pack()

    root.mainloop()
