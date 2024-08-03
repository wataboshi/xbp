import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser
kivy.require('1.11.1')

class HashTagSearchApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hashtags = []

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_text = TextInput(hint_text='enter a hashtag without "#"')
        self.add_button = Button(text='search')
        self.add_button.bind(on_press=self.search_hashtag)
        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.add_button)
        return self.layout

   

    def search_hashtag(self, instance):
        hashtag = self.input_text.text.strip()
        if hashtag:
            self.hashtags.append(hashtag)
            hashtag = urllib.parse.quote(hashtag)  # キーワードをエンコード
            search_url = f'https://www.instagram.com/explore/tags/{hashtag}/'
            webbrowser.open(search_url)

            # ウィンドウを閉じないようにするためのカスタムロジックを追加
            pass


if __name__ == '__main__':
    app = HashTagSearchApp()
    app.run()
