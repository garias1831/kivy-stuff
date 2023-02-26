from kivy.app import App
from kivy.uix.widget import Widget

class MouseApp(App):
    pass

class Touch(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos): 
            #This print will only fire if the touch is inside the rectangle       
            print('Mouse down:', touch)

    def on_touch_up(self, touch):
        #This print will fire anywhere, both inside and outside the rectangle
        print('Mouse up', touch)

if __name__ =='__main__':
    MouseApp().run()