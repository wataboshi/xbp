import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView  # ファイル選択用のウィジェットを追加
import webbrowser
import os  # ファイルパスを操作するために追加
kivy.require('1.11.1')
from kivy.config import Config


class LinkOpenerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.links = []
        self.image_path = None  # アップロードされた画像のファイルパス
        self.file_chooser = FileChooserListView()  # ファイル選択ダイアログ用のウィジェット

    # ... 以下省略 ...


    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_text1 = TextInput(hint_text='enter your account name without "@"')
        self.input_text2 = TextInput(hint_text='enter a hashtag without "#"')
        self.add_button = Button(text='create')
        self.add_button.bind(on_press=self.add_link)
        self.remove_button = Button(text='remove')
        self.remove_button.bind(on_press=self.remove_link)
        Config.set('graphics', 'multisamples', 0)
        from kivy.logger import Logger
        Logger.setLevel('debug')



        # 画像ファイル選択用のウィジェット
        self.file_chooser.path = os.path.expanduser('~')
        from kivy.utils import platform
        if platform == 'win':
            self.file_chooser.ignore_hidden = True

        # 画像選択ボタン
        self.select_image_button = Button(text='Select Image')
        self.select_image_button.bind(on_press=self.select_image)

        self.layout.add_widget(self.input_text1)
        self.layout.add_widget(self.input_text2)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.remove_button)
        self.layout.add_widget(self.select_image_button)
        self.layout.add_widget(self.file_chooser)

        return self.layout

    def add_link(self, instance):
        place = self.input_text2.text.strip()
        if place:
            link_button = Button(text=f'#{place}')
            link_button.bind(on_press=lambda x, link=place: self.open_link(link))
            self.links.append(link_button)
            self.layout.add_widget(link_button)
        self.input_text2.text = ''

    def remove_link(self, instance):
        if self.links:
            last_link_button = self.links.pop()
            self.layout.remove_widget(last_link_button)

    def select_image(self, instance):
        self.file_chooser.path = os.path.expanduser('~')  # デフォルトディレクトリをユーザーホームに設定
        self.file_chooser.bind(on_submit=self.load_image)


    def load_image(self, chooser, file_path):
        # アップロードされた画像を読み込む
        self.image_path = file_path
        self.image_widget = Image(source=file_path)
        self.layout.add_widget(self.image_widget)
        self.image_path = instance.selection[0]  # 選択された最初のファイルのパスを取得

    def open_link(self, place):
        if self.image_path:
            place = urllib.parse.quote(place)  # キーワードをエンコード
            if place:
                # エンコードされたキーワードとアカウント名を使用してURLを生成
                search_url = f'https://www.google.com/?client=avast-a-2/{place}/{self.image_path}/'
                webbrowser.open(search_url)
        else:
            print("Please select an image before opening a link.")

if __name__ == '__main__':
    LinkOpenerApp().run()





import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
import webbrowser
import os

kivy.require('1.11.1')


class LinkOpenerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.links = []
        self.image_path = None

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_text1 = TextInput(hint_text='enter your account name without "@"')
        self.input_text2 = TextInput(hint_text='enter a hashtag without "#"')
        self.add_button = Button(text='create')
        self.add_button.bind(on_press=self.add_link)
        self.remove_button = Button(text='remove')
        self.remove_button.bind(on_press=self.remove_link)

        

        # 画像ファイル選択用のウィジェット
        self.file_chooser = FileChooserListView()

        # 画像選択ボタン
        self.select_image_button = Button(text='Select Image')
        self.select_image_button.bind(on_press=self.select_image)

        self.layout.add_widget(self.input_text1)
        self.layout.add_widget(self.input_text2)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.remove_button)
        self.layout.add_widget(self.select_image_button)
        self.layout.add_widget(self.file_chooser)

        return self.layout




