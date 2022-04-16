from kivy.app import App
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager

class ScreenManager(NavigationScreenManager):
    pass

class TheLabApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = ScreenManager()
        return self.manager

TheLabApp().run()
