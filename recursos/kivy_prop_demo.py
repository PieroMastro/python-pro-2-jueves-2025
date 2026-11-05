from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Contador(BoxLayout):
    clicks = NumericProperty(0)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 30

        self.texto_contador = Label(text=f'Clicks: {self.clicks}')
        self.btn_contador = Button(text=f'Presioname!', font_size='30sp')
        self.btn_contador.on_press = self.incrementar

        self.add_widget(self.texto_contador)
        self.add_widget(self.btn_contador)

        self.bind(clicks=self.actualizar_contador)

    def incrementar(self):
        self.clicks += 1
        print(self.clicks)

    def actualizar_contador(self, instance, value):
        self.texto_contador.text = f'Clicks --> {value}'
        self.texto_contador.font_size += 1


class MyApp(App):
    def build(self):
        return Contador()


MyApp().run()
