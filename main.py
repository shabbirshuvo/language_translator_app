from kivy.graphics import Rectangle, Color
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivymd.uix.relativelayout import MDRelativeLayout
from translate import Translator
from kivy.core.window import Window
from kivy.uix.label import Label

# Setting the size of the application window
Window.size = (300, 500)


class MyApp(MDApp):

    # Function to update the position and size of the 'to' label's background rectangle
    def update_rect(self, instance, value):
        self.to_rect.pos = instance.pos
        self.to_rect.size = instance.size

    # Function to handle the translation process
    def translate(self, event):
        # Clearing any previous translations and errors
        self.output_box.text = ""
        self.error_label.text = ""
        self.error_label.opacity = 0

        # Fetching the text to be translated
        original_text = self.input_box.text

        # Checking if the text is not empty
        if original_text != "":
            try:
                # Creating a translator object with selected source and target languages
                translator = Translator(to_lang=self.main_button2.text, from_lang=self.main_button1.text)

                # Translating the text
                translation = translator.translate(original_text)

                # Displaying the translation
                self.output_box.text = translation
            except:
                # Handling any errors during translation (e.g., network issues)
                self.error_label.text = "Network error.",
                self.error_label.opacity = 1
        else:
            # If no text was entered, display an error
            self.error_label.text = "Please enter text to translate"
            self.error_label.opacity = 1

    # Function to build the user interface of the application
    def build(self):
        # Creating the main layout with a black background
        self.root = MDRelativeLayout(md_bg_color=(0, 0, 0, 1))

        # Adding the title label
        self.title_label = Label(text='Translator', font_size=50, color=(1, 1, 1, 1), height=50,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.root.add_widget(self.title_label)

        # Adding an input box for users to enter text to be translated
        self.input_box = TextInput(text='', size_hint=(.8, 0.35),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.75},
                                   font_size=30, height=250, hint_text='Enter text to translate')
        self.root.add_widget(self.input_box)

        # Creating a dropdown list for source language selection
        self.choices = ['English', 'Spanish', 'French', 'German', 'Italian', 'Russian', 'Chinese', 'Japanese']
        self.dropdown1 = DropDown()
        for choice in self.choices:
            btn = Button(text=choice, size_hint_y=None, height=30,
                         on_release=lambda btn: self.dropdown1.select(btn.text))
            self.dropdown1.add_widget(btn)
        self.main_button1 = Button(text='English', size_hint=(.25, .1), pos_hint={'center_x': 0.15, 'center_y': 0.5},
                                   font_size=30, height=0, size=(100, 30), bold=True,
                                   on_release=self.dropdown1.open, background_color=(1, 0, 0))
        self.dropdown1.bind(on_select=lambda instance, x: setattr(self.main_button1, 'text', x))
        self.root.add_widget(self.main_button1)

        # Adding a 'to' label with a white background
        self.to_label = Label(text='To', font_size=30, color=(1, 0, 0, 1), size=(50, 40),
                              pos_hint={'center_x': 0.32, 'center_y': 0.5}, bold=True, size_hint=(.1, .1))
        with self.to_label.canvas.before:
            Color(1, 1, 1, 1)  # Setting the color to white
            self.to_rect = Rectangle(size=self.to_label.size, pos=self.to_label.pos)
        self.to_label.bind(size=self.update_rect, pos=self.update_rect)
        self.root.add_widget(self.to_label)

        # Creating a dropdown list for target language selection
        self.dropdown2 = DropDown()
        for choice in self.choices:
            btn = Button(text=choice, size_hint_y=None, height=30,
                         on_release=lambda btn: self.dropdown2.select(btn.text))
            self.dropdown2.add_widget(btn)
        self.main_button2 = Button(text='English', size_hint=(.25, .1), pos_hint={'center_x': 0.49, 'center_y': 0.5},
                                   font_size=30, height=0, size=(100, 30), bold=True,
                                   on_release=self.dropdown2.open, background_color=(1, 0, 0))
        self.dropdown2.bind(on_select=lambda instance, x: setattr(self.main_button2, 'text', x))
        self.root.add_widget(self.main_button2)

        # Adding a button to trigger the translation process
        self.translate_button = Button(text='Translate', size_hint=(.25, 0.1),
                                       pos_hint={'center_x': 0.8, 'center_y': 0.5},
                                       font_size=30, height=0, size=(100, 30), bold=True,
                                       on_press=self.translate, background_color=(0, 1, 0))
        self.root.add_widget(self.translate_button)

        # Adding an output box to display the translated text
        self.output_box = TextInput(text='', size_hint=(0.8, 0.35),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                    font_size=30, height=250, readonly=True, hint_text='Translation')
        self.root.add_widget(self.output_box)

        # Adding an error label to display any error messages
        self.error_label = Label(text='', font_size=40, color=(1, 0, 0, 1), opacity=0,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.05})
        self.root.add_widget(self.error_label)

        return self.root


# Running the application
if __name__ == '__main__':
    MyApp().run()
