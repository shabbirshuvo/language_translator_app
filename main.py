from kivy.graphics import Rectangle, Color
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivymd.uix.relativelayout import MDRelativeLayout
from translate import Translator

Window.size = (300, 500)

# class ColoredBoxLayout(BoxLayout):
#     def __init__(self, color, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas.before:
#             Color(*color)
#             self.rect = Rectangle(pos=self.pos, size=self.size)
#             self.bind(pos=self.update_rect, size=self.update_rect)
#
#     def update_rect(self, *args):
#         self.rect.pos = self.pos
#         self.rect.size = self.size



class MyApp(MDApp):
    def build(self):
        # create primary box layout with black background
        # self.root = ColoredBoxLayout(color=(0, 0, 0, 1), orientation='vertical', padding=10, spacing=10)
        self.root = MDRelativeLayout(md_bg_color=(0, 0, 0, 1))
        self.title_label = Label(text='Translator', font_size=50, color=(1, 1, 1, 1), height=50,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.root.add_widget(self.title_label)

        return self.root

if __name__ == '__main__':
    MyApp().run()

