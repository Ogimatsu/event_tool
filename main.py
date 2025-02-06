from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
import os

# 201_損益分岐点設定項目画面に遷移
class Gamen201Layout(BoxLayout):
    pass

class EventToolApp(App):
    def build(self):
        # フォントの登録  
        font_path = os.path.join(os.path.dirname(__file__), "assets/fonts/NotoSansJP-Regular.ttf")
        LabelBase.register(name="NotoSansJP-Regular", fn_regular=font_path)

        Builder.load_file('main.kv')
        Builder.load_file('gamen201.kv')
        return MainLayout()

# メインレイアウトクラス
class MainLayout(BoxLayout):
    header_text = StringProperty("作成したい表の項目を追加してください")
    content = ObjectProperty(None)

    # 名簿ボタン押下時の処理
    def click_meibo(self):
        self.header_text = "作成したい表の項目を追加してください"

    # 収支ボタン押下時の処理
    def click_syushi(self):
        self.header_text = "収支　項目設定"
        self.content.clear_widgets()
        self.content.add_widget(Gamen201Layout())

if __name__ == "__main__":
    EventToolApp().run()