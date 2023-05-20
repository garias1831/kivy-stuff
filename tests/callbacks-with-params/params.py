from kivy.app import App
from kivy.uix.button import Button

def on_button_press(instance, additional_param):
    print("Button pressed with additional parameter:", additional_param)

class MyApp(App):
    def build(self):
        button = Button(text='Click me')
        additional_param = "Hello"
        button.bind(on_press=lambda instance: on_button_press(instance, additional_param))
        return button

if __name__ == '__main__':
    MyApp().run()
