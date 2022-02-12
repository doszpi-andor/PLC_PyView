from tkinter import Canvas, ARC, W, CHORD, CENTER, S, N


class TankCanvas(Canvas):
    """
    Tank canvas
    :var int TANK_WIDTH: tank width
    :var int TANK_HEIGHT: tank height
    :var int NAME_FONT_SIZE: tank name font size
    """
    TANK_WIDTH = 90
    TANK_HEIGHT = 220
    NAME_FONT_SIZE = 15

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
                         font=("Arial", self.NAME_FONT_SIZE), text=tank_name)


class SensorCanvas(Canvas):
    """
    Sensor canvas
    :var int INDICATOR_SQUARE: indicator square size
    :var int INDICATOR_LINE_LENGTH: active line length
    :var int INDICATOR_TEXT_LENGTH: sensor name text length
    """
    INDICATOR_SQUARE = 20
    INDICATOR_LINE_LENGTH = 10
    INDICATOR_TEXT_LENGTH = 80

    def create_sensor(self, x_position, y_position, name, color, line_length=0) -> None:
        """
        Create discrete sensor
        :param int x_position: sensor x position
        :param int y_position: sensor y position
        :param str name: sensor name
        :param str  color: sensor color name string
        :param int line_length: sensor line length (0 - no line)
        """
        self.create_line(x_position,
                         y_position,
                         x_position + line_length,
                         y_position,
                         fill=color)
        self.create_rectangle(x_position + line_length + 2,
                              y_position - self.INDICATOR_SQUARE // 2,
                              x_position + line_length + self.INDICATOR_SQUARE + 2,
                              y_position + self.INDICATOR_SQUARE // 2,
                              fill=color)
        self.create_text(x_position + line_length + self.INDICATOR_SQUARE + 4,
                         y_position,
                         anchor=W, text=name)


class AnalogCanvas(Canvas):
    """
    Analog sensor canvas
    :var int ANALOG_INDICATOR_WIDTH: analog indicator bar size
    """
    ANALOG_INDICATOR_WIDTH = 20

    def create_analog(self, x_position, y_position, height, name, active_color, active_level=0, activ_level_print=False,
                      background_color='gray', line_length=0, name_position='right', marks_position=None) -> int:
        """
        Create analog sensor
        :param int x_position: analog indicator x position
        :param int y_position: analog indicator y position
        :param int height: indicator bar height
        :param str name: indicator name
        :param str active_color: active color name string
        :param int active_level: activ level [%]
        :param bool activ_level_print: activ level printing after sensor name
        :param str background_color: indicator bar background color name string
        :param int line_length: indicator line length (0 - no line)
        :param str name_position: name position (left or right)
        :param tuple marks_position: indicator bar marks position [%]
        :return: name text canvas id (to delete)
        """

        text_id = None

        if active_level > 100:
            active_level = 100
        if active_level < 0:
            active_level = 0

        if activ_level_print:
            name = '%s (%s%%)' % (name, active_level)

        self.create_line(x_position,
                         y_position,
                         x_position + line_length,
                         y_position,
                         fill=background_color)
        self.create_rectangle(x_position + line_length,
                              y_position,
                              x_position + line_length + self.ANALOG_INDICATOR_WIDTH,
                              y_position + height,
                              fill=background_color)
        self.create_rectangle(x_position + line_length,
                              y_position + height - int(height / 100 * active_level),
                              x_position + line_length + self.ANALOG_INDICATOR_WIDTH,
                              y_position + height,
                              fill=active_color)
        self.create_line(x_position,
                         y_position + height,
                         x_position + line_length,
                         y_position + height,
                         fill=background_color)
        if marks_position is not None:
            for item in marks_position:
                self.create_line(x_position + line_length,
                                 y_position + height - int(height / 100 * item),
                                 x_position + line_length + self.ANALOG_INDICATOR_WIDTH,
                                 y_position + height - int(height / 100 * item),
                                 dash=(1, 1))
        if name_position == 'right':
            # noinspection PyArgumentList
            text_id = self.create_text(x_position + line_length + self.ANALOG_INDICATOR_WIDTH,
                                       y_position + height // 2,
                                       angle=90, anchor=N, text=name)
        elif name_position == 'left':
            # noinspection PyArgumentList
            text_id = self.create_text(x_position,
                                       y_position + height // 2,
                                       angle=90, anchor=S, text=name)

        return text_id


class ValveCanvas(Canvas):
    """
    Valve canvas
    :var int VALVE_WIDTH: valve width
    :var int VALVE_HEIGHT: valve height
    """
    VALVE_WIDTH = 30
    VALVE_HEIGHT = 40

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
                              length,
                              self.PIPE_WIDTH,
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
                         angle=90, justify=CENTER, anchor=S, text=name)


class RotorCanvas(Canvas):
    """
    Rotor canvas
    :var int ROTOR_WIDTH: rotor width
    """
    ROTOR_WIDTH = 45

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
                         angle=90, justify=CENTER, anchor=S, text=name)

    @property
    def rotor_height(self) -> int:
        """
        Calculate rotor indicator height
        :return: rotor indicator height
        """
        return int(self.ROTOR_WIDTH * 1.155)
