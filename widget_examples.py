from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.lang import Builder

Builder.load_file("widget_examples.kv")

class WidgetsExample(GridLayout):
    counter = 0
    counter_is_on = False
    counter_button_disabled = BooleanProperty(True)
    slider_value = StringProperty(str(50))
    my_text = StringProperty(str(counter))
    text_input_str = StringProperty("foo")
    
    def on_button_click(self):
        if (not(self.counter_is_on)):
            return
        print("Button clicked")
        self.counter+= 1
        self.my_text = str(self.counter)
        
    def on_toogle_button_state(self, widget):
        print("toogle state")
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.counter_is_on = False
            self.counter_button_disabled = True
        else:
            # ON
            widget.text = "ON"
            self.counter_is_on = True
            self.counter_button_disabled = False
            
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        
    def on_slider_value_change(self, widget):
        value = int(widget.value)
        self.slider_value = str(value)
        print("Slider: " + str(value))
        
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
