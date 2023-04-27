from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

#Event help from this vid: https://www.youtube.com/watch?v=KK6OXdzi6d4

'''
This script shows an example of a marginally "better" way to build UIs as compared to what I've been doing before.
With objectprops, we can let the view know about some of the more important child widgets (the ButtonGen)
without sacrificing the raw design-power of kvlang.
'''

class PropApp(App):
    pass


class TheView(BoxLayout):
    btn_gen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clear(self, obj):
        self.btn_gen.clear_widgets()


class ButtonGen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Binding with python here...
        self.btn = Button(text='Jimmy Butler')
        self.btn.bind(on_press=self.generate)
        
        self.add_widget(self.btn)
    
    def generate(self, obj):
        new_btn = Button(text='Playoff Jimmy')
        new_btn.bind(on_press=self.generate)
        
        self.add_widget(new_btn)
        

if __name__ == '__main__':
    PropApp().run()