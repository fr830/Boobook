from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle, Scale, Translate
import curses.ascii
import boobook.graphical_objects as go


class DrawingArea(Widget):
    def __init__(self, **kwargs):
        super(DrawingArea, self).__init__(**kwargs)
        # used to store where pressed
        self._x = 0
        self._y = 0

        # label for showing info
        self._info_label = Label()
        self._typing = False

        self._graphical_objects = []
        self._selected_objects = []

        self._scale = Scale()
        self.canvas.add(self._scale)

        self._translate = Translate()
        self.canvas.add(self._translate)

        # background color and rectangle
        #self._background_color = Color(1.0, 1.0, 1.0, 1.0)
        #self._background_rect = Rectangle(pos=(0, 0), size=(10000, 10000))
        #self.canvas.add(self._background_color)
        #self.canvas.add(self._background_rect)

        # selection color and line
        self._selection_color = Color(1.0, 0.0, 0.0, 1.0)
        self._selection_line = Line(points=[0, 0])

        self._tool = None
        self._selection = True  # selection active

        # keycodes
        self._lctrl = False
        self._shift = False

        # mouse event
        self._pressed = False

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def on_touch_down(self, touch):
        self._pressed = True

        # selection
        if self._tool is None:
            self._x = touch.x
            self._y = touch.y
            self.canvas.add(self._selection_color)
            self.canvas.add(self._selection_line)

        # draw based on selected tool
        if touch.button == 'left' and self._tool:
            if self._tool == 'rect':
                self._selected_objects.append(go.Rect(touch.x, touch.y))
                self._graphical_objects.append(go.Rect(touch.x, touch.y))
                self._selected_objects[-1].draw(self.canvas)

        if touch.button == 'right':
            pass

    def on_touch_move(self, touch):
        # selection
        if self._pressed and self._tool is None:
            self._selection_line.points = [self._x, self._y,
                                           touch.x, self._y,
                                           touch.x, touch.y,
                                           self._x, touch.y,
                                           self._x, self._y]

        # move selected objects
        if self._pressed and self._lctrl and self._selected_objects and not self._tool:
            pass

        # resize selected objects
        if self._pressed and self._selected_objects:
            for object_ in self._selected_objects:
                object_.resize(touch.x, touch.y)

    def on_touch_up(self, touch):
        if self._pressed:
            self._pressed = False

        if self._tool:
            self._tool = None
        self._selected_objects.clear()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keyboard, keycode, text)
        if 'shift' in keycode:
            self._shift = True

        if 'lctrl' in keycode:
            self._lctrl = True

        try:
            if curses.ascii.isascii(keycode[-1]):
                print('true')
        except TypeError:
            pass

        if 'escape' in keycode:
            self.remove_widget(self._info_label)

        if not self._pressed and not self._tool and not self._selection:
            pass

    def _on_keyboard_up(self, keyboard, keycode):
        if 'lctrl' in keycode:
            self._lctrl = False
        if 'shift' in keycode:
            self._shift = False

    def _draw_selection(self):
        pass


class BoobookApp(App):
    Config.set('kivy', 'exit_on_escape', '0')
    Config.write()

    def build(self):
        return DrawingArea()


if __name__ == '__main__':
    BoobookApp().run()


