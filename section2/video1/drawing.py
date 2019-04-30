from kivy.config import Config
from kivy.app import App


Config.set("graphics", "width", 1365)
Config.set("graphics", "height", 768)


class DrawingApp(App):
    pass


if __name__ == "__main__":
    DrawingApp().run()
