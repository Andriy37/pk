from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class CurrencyConverter(BoxLayout):
    def __init__(self, **kwargs):
        super(CurrencyConverter, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='From Currency:'))
        self.from_currency = TextInput(multiline=False)
        self.add_widget(self.from_currency)

        self.add_widget(Label(text='To Currency:'))
        self.to_currency = TextInput(multiline=False)
        self.add_widget(self.to_currency)

        self.add_widget(Label(text='Amount:'))
        self.amount = TextInput(multiline=False)
        self.add_widget(self.amount)

        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert)
        self.add_widget(self.convert_button)

        self.result_label = Label(text='Result: ')
        self.add_widget(self.result_label)

    def convert(self, instance):
        from_currency = self.from_currency.text.upper()
        to_currency = self.to_currency.text.upper()
        amount = float(self.amount.text)

        api_url = f'https://kurs.com.ua/ru/konverter'
        response = requests.get(api_url)
        data = response.json()

        if to_currency in data['rates']:
            conversion_rate = data['rates'][to_currency]
            result = amount * conversion_rate
            self.result_label.text = f'Result: {result:.2f} {to_currency}'
        else:
            self.result_label.text = 'Invalid currency code'

class CurrencyConverterApp(App):
    def build(self):
        return CurrencyConverter()

if __name__ == '__main__':
    CurrencyConverterApp().run()