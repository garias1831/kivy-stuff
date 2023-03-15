from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ReferenceApp(App):
    pass

'''In order to make your own custom widgets, you need to declare them as classes before you can reference them in .kv'''
class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs) #You can also customize some properties like so, 


if __name__ == '__main__':
    ReferenceApp().run()