from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.display = TextInput(
            text="",
            readonly=True,
            halign="right",
            font_size=40,
            size_hint=(1, 0.25)
        )
        self.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        for txt in buttons:
            btn = Button(text=txt, font_size=30)
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        btn_del = Button(text="DEL", font_size=26)
        btn_del.bind(on_press=self.delete_one)

        btn_eq = Button(text="=", font_size=30)
        btn_eq.bind(on_press=self.calculate)

        grid.add_widget(btn_del)
        grid.add_widget(Button(text=""))
        grid.add_widget(Button(text=""))
        grid.add_widget(btn_eq)

        self.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.display.text = ""
        else:
            self.display.text += text

    def delete_one(self, instance):
        self.display.text = self.display.text[:-1]

    def calculate(self, instance):
        try:
            expr = self.display.text
            allowed = "0123456789+-*/.() "
            if any(ch not in allowed for ch in expr):
                self.display.text = "ERROR"
                return
            self.display.text = str(eval(expr))
        except:
            self.display.text = "ERROR"


class CalculatorApp(App):
    def build(self):
        return CalculatorUI()


if __name__ == "__main__":
    CalculatorApp().run()
          
