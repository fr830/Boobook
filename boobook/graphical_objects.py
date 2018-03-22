import math
from kivy.graphics import Color, InstructionGroup, Line, Rectangle, Rotate, Scale


class GraphicalObject:
    """
    Base class for graphical objects. Contains attributes and methods common for all graphical objects.
    """
    def __init__(self, shape, x, y):
        self._shape = shape
        self._x = x
        self._y = y
        self._angle = 0
        self._scale = 0

        self._selected = None

        self._group = InstructionGroup()

        self.rot = Rotate(self._angle, 0, 0, 1)
        self.rot.origin = self._x, self._y
        self._group.add(self.rot)

        self._scale = Scale(0.0, 0.0, self._scale)
        self._scale.origin = self._x, self._y

        # add a surrounding line
        if self._shape == 'rect' or self._shape == 'circle' or self._shape == 'ellipse' or self._shape == 'polygon':
            self._line_color = Color(1.0, 0.0, 0.0, 1.0)
            self._line = Line()
            self._group.add(self._line_color)
            self._group.add(self._line)

    def rotate(self, touch_x, touch_y):
        if touch_x > self._x and touch_y > self._y:
            self._angle = int(math.degrees(math.atan((touch_y - self._y) / (touch_x - self._x))))
        if touch_x == self._x and touch_y > self._y:
            self._angle = 90
        if touch_x < self._x and touch_y > self._y:
            self._angle = int(180 - math.degrees(math.atan((touch_y - self._y) / (self._x - touch_x))))
        if touch_x < self._x and touch_y == self._y:
            self._angle = 180
        if touch_x < self._x and touch_y < self._y:
            self._angle = int(180 - math.degrees(math.atan((touch_y - self._y) / (self._x - touch_x))))
        if touch_x == self._x and touch_y < self._y:
            self._angle = 270
        if touch_x > self._x and touch_y < self._y:
            self._angle = int(360 - math.degrees(math.atan((touch_y - self._y) / (self._x - touch_x))))
        if touch_x > self._x and touch_y == self._y:
            self._angle = 360


class Rect(GraphicalObject):
    """ Rectangle class representing a rectangle with a border. """
    def __init__(self, x, y):
        super().__init__('rect', x, y)
        self._width = 1
        self._height = 1
        self._group = InstructionGroup()
        self._rec_color = Color(1.0, 1.0, 1.0, 1.0)
        self._rec = Rectangle(pos=(x, y), size=(self._width, self._height))
        # self._x, self._y | self._x + self._width, self._y | self._x + self._width, self._y + self._height |
        # self._x, self._y + self._height
        self._group.add(self._rec_color)
        self._group.add(self._rec)

    """ Draws rectangle on canvas argument """
    def draw(self, canvas):
        canvas.add(self._group)

    def resize(self, x, y):
        self._rec.size = x - self._x, y - self._y

    def get_bounding_box(self):
        return self._x, self._y, self._width, self._height

    def is_within(self, x, y):
        pass


class Circle:
    pass


class Ellipse:
    pass


class Line_:
    pass


class Polyline:
    pass


class Polygon:
    pass


