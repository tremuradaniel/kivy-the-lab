from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

NO_OF_BUTTONS = 100

class WidgetsExample(GridLayout):
    counter = 0
    my_text = StringProperty(str(counter))
    
    def on_button_click(self):
        print("Button clicked")
        self.counter+= 1
        self.my_text = str(self.counter)
        
    def on_toogle_button_state(self, widget):
        print("toogle state")
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
        else:
            # ON
            widget.text = "ON"

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-bt"
        for i in range(0, NO_OF_BUTTONS):
            sizes = dp(100) # + i*10
            b = Button(text=str(i + 1), size_hint=(None, None), size=(sizes,sizes))
            self.add_widget(b)
            

# class GridLayoutExample(GridLayout):
#     pass
class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
