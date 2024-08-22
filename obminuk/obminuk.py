from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CurrencyConverterApp(App):
    def build(self):
        self.title = 'Currency Converter'
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.amount_input = TextInput(hint_text='Введіть суму', multiline=False, input_filter='float')
        self.base_currency_input = TextInput(hint_text='Базова валюта (USD)', multiline=False)
        self.target_currency_input = TextInput(hint_text='Цільова валюта (євро)', multiline=False)
        
        self.result_label = Label(text='Тут з’явиться результат переведення')
        
        convert_button = Button(text='Convert', on_press=self.convert_currency)
        
        layout.add_widget(self.amount_input)
        layout.add_widget(self.base_currency_input)
        layout.add_widget(self.target_currency_input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)
        
        return layout
    
    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            base_currency = self.base_currency_input.text.upper()
            target_currency = self.target_currency_input.text.upper()
            result = convert_currency(amount, base_currency, target_currency)
            self.result_label.text = f'{amount} {base_currency} = {result:.2f} {target_currency}'
        except Exception as e:
            self.result_label.text = str(e)

if __name__ == '__main__':
    CurrencyConverterApp().run()