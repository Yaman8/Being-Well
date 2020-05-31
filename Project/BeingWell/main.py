from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image

from BeingWell.database import DataBase
from BeingWell.databasen import DataBasen

class FirstScreen(Screen):
    def sec(self):
        wm.current ="second"

class SecondScreen(Screen):
    def medi(self):
        wm.current = "medi"
    def test(self):
        wm.current = "test"
    def health(self):
        wm.current = "health"

    def ppop(self):
        pop = Popup(title='YOUR TICKET',
                    content= Image(source='code.png'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()



class MediScreen(Screen):
    namee = ObjectProperty(None)
    ref = ObjectProperty(None)
    cause= ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.ref.text != "" and self.cause.text != "":
            db.add_user(self.namee.text, self.ref.text, self.cause.text)

            self.reset()
            wm.current = "hosp"
        else:
            invalidTry()


    def first(self):
        self.reset()
        wm.current="first"

    def show(self):
        wm.current="show"

    def reset(self):
        self.ref.text = ""
        self.namee.text = ""
        self.cause.text = ""

class TestScreen(Screen):
    namee = ObjectProperty(None)
    ref = ObjectProperty(None)
    cause = ObjectProperty(None)
    add = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.ref.text != "" and self.cause.text != "" and self.add.text != "":
            dbn.add_user(self.namee.text, self.ref.text, self.cause.text, self.add.text)

            self.reset()
            wm.current = "covid"
        else:
            invalidTry()

    def first(self):
        self.reset()
        wm.current = "first"

    def show(self):
        wm.current = "show"

    def reset(self):
        self.ref.text = ""
        self.namee.text = ""
        self.cause.text = ""
        self.add.text = ""

class HealthScreen(Screen):
    def submit(self):
        pop = Popup(title='PLEASE WAIT',
                    content=Label(text='Connecting...'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def exit(self):
        wm.current = ""

class CovidScreen(Screen):
    def submit(self):
        pop = Popup(title='PLEASE WAIT',
                    content=Label(text='Connecting...'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def exit(self):
        wm.current = ""

class HospScreen(Screen):
    def submit(self):
        pop = Popup(title='PLEASE WAIT',
                    content=Label(text='Connecting...'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def exit(self):
        wm.current = ""

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
wm = WindowManager()
db = DataBase("users.txt")
dbn = DataBasen("usersn.txt")

screens = [FirstScreen(name="first"),SecondScreen(name="second"), MediScreen(name="medi"),TestScreen(name="test"),HospScreen(name="hosp"),HealthScreen(name="health"),CovidScreen(name="covid")]
for screen in screens:
    wm.add_widget(screen)

wm.current = "first"

def invalidTry():
    pop = Popup(title='Invalid Attempt',
                content=Label(text='Invalid Entry'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

class BeingWellApp(App):
    def build(self):
        return wm


if __name__ == "__main__":
    BeingWellApp().run()