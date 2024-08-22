from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

# Функції для отримання курсу та конвертації валют
def get_exchange_rate(base_currency, target_currency):
    api_key = "YOUR_API_KEY"  # Замість цього вставте свій ключ API
    url = f"https://kurs.com.ua/ru/konverter"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data")
    
    rates = data.get("conversion_rates", {})
    return rates.get(target_currency)

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        raise Exception("Invalid target currency")
    return amount * rate

# Клас для основного екрану
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Кнопки для навігації між екранами
        uah_to_usd_button = Button (text='Convert UAH to USD', on_press=lambda x: self.manager.current = 'uah_to_usd')
        usd_to_eur_button = Button (text='Convert USD to EUR', on_press=lambda x: self.manager.current = 'usd_to_eur')
        pln_to_uah_button = Button (text='Convert PLN to UAH', on_press=lambda x: self.manager.current = 'pln_to_uah')

        layout.add_widget(uah_to_usd_button)
        layout.add_widget(usd_to_eur_button)
        layout.add_widget(pln_to_uah_button)

        self.add_widget(layout)

# Базовий клас для конвертації валют
class CurrencyConverterScreen(Screen):
    def __init__(self, base_currency, target_currency, hint_text, result_text, **kwargs):
        super(CurrencyConverterScreen, self).__init__(**kwargs)
        self.base_currency = base_currency
        self.target_currency = target_currency

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.amount_input = TextInput(hint_text=hint_text, multiline=False, input_filter='float')
        self.result_label = Label(text=result_text)

        convert_button = Button(text=f'Convert to {target_currency}', on_press=self.convert_currency)

        layout.add_widget(self.amount_input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            result = convert_currency(amount, self.base_currency, self.target_currency)
            self.result_label.text = f'{amount} {self.base_currency} = {result:.2f} {self.target_currency}'
        except Exception as e:
            self.result_label.text = str(e)

# Класи для конкретних конверсій валют
class UAHtoUSD(CurrencyConverterScreen):
    def __init__(self, **kwargs):
        super(UAHtoUSD, self).__init__('UAH', 'USD', 'Enter amount in UAH', 'Conversion result will appear here', **kwargs)

class USDtoEUR(CurrencyConverterScreen):
    def __init__(self, **kwargs):
        super(USDtoEUR, self).__init__('USD', 'EUR', 'Enter amount in USD', 'Conversion result will appear here', **kwargs)

class PLNtoUAH(CurrencyConverterScreen):
    def __init__(self, **kwargs):
        super(PLNtoUAH, self).__init__('PLN', 'UAH', 'Enter amount in PLN', 'Conversion result will appear here', **kwargs)

# Головний клас додатка
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