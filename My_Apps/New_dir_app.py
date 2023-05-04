from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import os


class CreateDirApp(App):
    def build(self):
        self.path = ""
        self.main_name = ""
        self.sub_names = []
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Text input for path
        path_label = Label(text="Enter the path where the directory will be created:")
        self.path_input = TextInput(text="", multiline=False)
        layout.add_widget(path_label)
        layout.add_widget(self.path_input)

        # Text input for main folder name
        main_label = Label(text="Enter the name of the main folder:")
        self.main_input = TextInput(text="", multiline=False)
        layout.add_widget(main_label)
        layout.add_widget(self.main_input)

        # Text input for sub-folder name
        sub_label = Label(text="Enter the name of a sub-folder:")
        self.sub_input = TextInput(text="", multiline=False)
        layout.add_widget(sub_label)
        layout.add_widget(self.sub_input)

        # Button to add sub-folder
        add_button = Button(text="Add Sub-folder")
        add_button.bind(on_press=self.add_sub_folder)
        layout.add_widget(add_button)

        # Finish button
        finish_button = Button(text="Create Directory")
        finish_button.bind(on_press=self.create_directory)
        layout.add_widget(finish_button)

        return layout

    def add_sub_folder(self, instance):
        sub_name = self.sub_input.text
        sub_label = Label(text=f"{sub_name}:")
        sub_input = TextInput(text="Sub-folder", multiline=False)
        self.sub_names.append(sub_name)
        self.root.add_widget(sub_label)
        self.root.add_widget(sub_input)

    def create_directory(self, instance):
        # Get user inputs
        self.path = self.path_input.text
        self.main_name = self.main_input.text

        # Create main folder
        main_path = os.path.join(self.path, self.main_name)
        os.makedirs(main_path)

        # Create sub-folders
        for sub_name in self.sub_names:
            sub_path = os.path.join(main_path, sub_name)
            os.makedirs(sub_path)


if __name__ == "__main__":
    CreateDirApp().run()
