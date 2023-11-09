import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
import requests
import urllib.parse
import webbrowser
import os
import japanize_kivy
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform

class LinkOpenerApp(App):
    # ... (他のコード)

    def select_image(self, instance):
        # ファイル選択ダイアログのデフォルトディレクトリをユーザーホームに設定
        if platform == 'win':
            self.file_chooser.ignore_hidden = True  # Windowsの場合は隠しファイルを無視
        self.file_chooser.path = os.path.expanduser('~')

        # ファイル選択ダイアログを開いたときに呼び出されるコールバックを設定
        self.file_chooser.bind(on_submit=self.load_image)

    # ... (他のコード)

kivy.require('1.11.1')

class ImageSearchApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # ファイル選択ダイアログ
        self.file_chooser = FileChooserListView()
        self.file_chooser.bind(on_submit=self.load_image)
        self.layout.add_widget(self.file_chooser)

        # 画像表示エリア
        self.image = Image(source='default_image.png')  # デフォルトの画像を表示
        self.layout.add_widget(self.image)

        # 検索ボタン
        self.search_button = Button(text='Search Online')
        self.search_button.bind(on_press=self.search_online)
        self.layout.add_widget(self.search_button)

        return self.layout

    def load_image(self, instance, selection, touch):
        # 画像を読み込んで表示
        if selection:
            image_path = selection[0]
            self.image.source = image_path
            self.selected_image_path = image_path

    def search_online(self, instance):
        if hasattr(self, 'selected_image_path'):
            # 画像をオンラインで検索
            image_path = self.selected_image_path

            # 画像をアップロード
            with open(image_path, 'rb') as image_file:
                files = {'image': image_file}
                response = requests.post('https://example.com/image-upload', files=files)

            # レスポンスを処理し、結果を表示
            if response.status_code == 200:
                result_url = response.text  # 画像検索結果のURLを取得
                webbrowser.open(result_url)
            else:
                print('Error uploading image.')

if __name__ == '__main__':
    app = ImageSearchApp()
    app.run()
