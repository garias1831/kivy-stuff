from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import NumericProperty

class MyButton(Button):
    count = NumericProperty(0)

    def on_count(self, instance, value):
        print(f'Count changed to {value}')

    '''
    Note that in this example, we didn't explicitly bind the on_count method to the count property. 
    Kivy automatically detects that there is a method with the correct name (on_count) and binds it to the property. 
    If you have a different naming convention for your callback methods, you can use the ObjectProperty class to explicitly bind your callbacks to your properties.
    '''

    def on_release(self):
        self.count += 1

class PropsApp(App):
    pass

if __name__ == '__main__':
    PropsApp().run()