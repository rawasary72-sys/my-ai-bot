from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class CobraApp(MDApp):
    def build(self):
        return MDLabel(text="سڵاو ڕەوا، ئەمە بەرنامەکەتە", halign="center")

if __name__ == "__main__":
    CobraApp().run()
