import japanize_kivy
import urllib.parse
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser

kivy.require('1.11.1')

class HotelSearchApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.location_input = TextInput(hint_text='目的地を入力してください')
        self.check_in_input = TextInput(hint_text='チェックイン日（例: 2023-11-04）')
        self.check_out_input = TextInput(hint_text='チェックアウト日（例: 2023-11-07）')
        self.guests_input = TextInput(hint_text='宿泊人数')
        self.rooms_input = TextInput(hint_text='部屋数')
        self.search_button = Button(text='検索')
        self.search_button.bind(on_press=self.search_hotels)

        self.layout.add_widget(self.location_input)
        self.layout.add_widget(self.check_in_input)
        self.layout.add_widget(self.check_out_input)
        self.layout.add_widget(self.guests_input)
        self.layout.add_widget(self.rooms_input)
        self.layout.add_widget(self.search_button)

        return self.layout

    def search_hotels(self, instance):
        location = self.location_input.text.strip()
        check_in_date = self.check_in_input.text.strip()
        check_out_date = self.check_out_input.text.strip()
        guests = self.guests_input.text.strip()
        rooms = self.rooms_input.text.strip()

        if location and check_in_date and check_out_date:
            # 実際の宿泊サイトのURLに合わせて調整
            # 以下はBooking.comの例
            base_url = 'https://www.booking.com/search.html'
            query_parameters = {
                'ss': location,
                'checkin_monthday': check_in_date.split('-')[2],
                'checkin_year_month': f'{check_in_date.split("-")[0]}-{check_in_date.split("-")[1]}',
                'checkout_monthday': check_out_date.split('-')[2],
                'checkout_year_month': f'{check_out_date.split("-")[0]}-{check_out_date.split("-")[1]}',
                'group_adults': guests,
                'no_rooms': rooms,
            }
            query_string = urllib.parse.urlencode(query_parameters)
            search_url = f'{base_url}?{query_string}'
            webbrowser.open(search_url)

if __name__ == '__main__':
    app = HotelSearchApp()
    app.run()
