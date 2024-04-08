import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import webbrowser
import os

kivy.require('2.2.1')  # Kivyのバージョンを修正

class ImageSearchApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_path = None

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.image_drop_box = DropImageBox()
        self.search_button = Button(text='Search Image')
        self.search_button.bind(on_press=self.search_image)

        self.layout.add_widget(self.image_drop_box)
        self.layout.add_widget(self.search_button)
        return self.layout

    def search_image(self, instance):
        if self.image_drop_box.image_path:
            image_path = self.image_drop_box.image_path

            # 画像のURLをそのまま使用して検索
            search_url = f'https://www.google.com/searchbyimage?image_url=file://{image_path}'
            webbrowser.open(search_url)

class DropImageBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.label = Label(text='Drag and drop an image here')
        self.image_path = None

        self.add_widget(self.label)
        Window.bind(on_drop_file=self._on_drop_file)

    def _on_drop_file(self, window, file_path, *args):
        try:
            self.image_path = file_path.decode('utf-8')
            self.label.text = f'Image Path: {self.image_path}'
        except Exception as e:
            print(f"Exception in _on_drop_file: {e}")

if __name__ == '__main__':
    app = ImageSearchApp()
    app.run()
