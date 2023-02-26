from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#kv = Builder.load_file('view1.kv')

class ViewSwitchApp(App):
    pass
    #def build(self):
     #   return kv

class MainWindow(Screen):
    pass

class SettingsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

if __name__ == '__main__':
    ViewSwitchApp().run()