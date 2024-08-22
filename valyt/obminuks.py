from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "your_api_key"  
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data")
    
    data = response.json()
    rates = data.get("rates", {})
    return rates.get(target_currency)

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        raise Exception("Invalid target currency")
    return amount * rate

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        uah_to_usd_button = Button(text='Перевести UAH to USD', on_press=lambda x: self.manager.current = 'uah_to_usd')
        usd_to_eur_button = Button(text='Перевести USD to EUR', on_press=lambda x: self.manager.current = 'usd_to_eur')
        pln_to_uah_button = Button(text='Перевести PLN to UAH', on_press=lambda x: self.manager.current = 'pln_to_uah')

        layout.add_widget(uah_to_usd_button)
        layout.add_widget(usd_to_eur_button)
        layout.add_widget(pln_to_uah_button)

        self.add_widget(layout)

class UAHtoUSD(Screen):
    def __init__(self, **kwargs):
        super(UAHtoUSD, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.amount_input = TextInput(hint_text='Enter amount in UAH', multiline=False, input_filter='float')
        self.result_label = Label(text='Conversion result will appear here')
        
        convert_button = Button(text='Convert to USD', on_press=self.convert_currency)
        
        layout.add_widget(self.amount_input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            result = convert_currency(amount, 'UAH', 'USD')
            self.result_label.text = f'{amount} UAH = {result:.2f} USD'
        except Exception as e:
            self.result_label.text = str(e)

class USDtoEUR(Screen):
    def __init__(self, **kwargs):
        super(USDtoEUR, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.amount_input = TextInput(hint_text='Enter amount in USD', multiline=False, input_filter='float')
        self.result_label = Label(text='Conversion result will appear here')
        
        convert_button = Button(text='Convert to EUR', on_press=self.convert_currency)
        
        layout.add_widget(self.amount_input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            result = convert_currency(amount, 'USD', 'EUR')
            self.result_label.text = f'{amount} USD = {result:.2f} EUR'
        except Exception as e:
            self.result_label.text = str(e)

class PLNtoUAH(Screen):
    def __init__(self, **kwargs):
        super(PLNtoUAH, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.amount_input = TextInput(hint_text='Enter amount in PLN', multiline=False, input_filter='float')
        self.result_label = Label(text='Conversion result will appear here')
        
        convert_button = Button(text='Convert to UAH', on_press=self.convert_currency)
        
        layout.add_widget(self.amount_input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            result = convert_currency(amount, 'PLN', 'UAH')
            self.result_label.text = f'{amount} PLN = {result:.2f} UAH'
        except Exception as e:
            self.result_label.text = str(e)

class CurrencyConverterApp(App):
    def build(self):
        sm = ScreenManager()

        main_screen = MainScreen(name='main')
        uah_to_usd = UAHtoUSD(name='uah_to_usd')
        usd_to_eur = USDtoEUR(name='usd_to_eur')
        pln_to_uah = PLNtoUAH(name='pln_to_uah')

        sm.add_widget(main_screen)
        sm.add_widget(uah_to_usd)
        sm.add_widget(usd_to_eur)
        sm.add_widget(pln_to_uah)

        return sm

if __name__ == '__main__':
    CurrencyConverterApp().run()
