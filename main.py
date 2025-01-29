from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.lang import Builder
import os

class EventToolApp(App):
    def build(self):
        # フォントの登録  
        font_path = os.path.join(os.path.dirname(__file__), "assets/fonts/NotoSansJP-Regular.ttf")
        LabelBase.register(name="NotoSansJP-Regular", fn_regular=font_path)

        Builder.load_file('main.kv')
        return MainLayout()

# メインレイアウトクラス
class MainLayout(BoxLayout):
    pass

if __name__ == "__main__":
    EventToolApp().run()