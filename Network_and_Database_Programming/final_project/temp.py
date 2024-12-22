import sys
import requests
from io import BytesIO
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton,
    QScrollArea, QWidget, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# 示例 JSON 資料
news_json = {'Title': '天冷泡澡最忌「1事」 醫喊：會奪命！「我自己都不敢」',
 'Content': [{'type': 'paragraph', 'text': '記者施春美／台北報導'},
  {'type': 'image',
   'src': 'https://s.yimg.com/ny/api/res/1.2/EEsmLPeyolrhFKAijJQh6w--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MA--/https://media.zenfs.com/ko/setn.com.tw/716ca0483ec1c00779177e6987edc94f',
   'alt': '天冷是許多人泡澡的時節。（示意圖／Pixabay）'},
  {'type': 'paragraph', 'text': '▲天冷是許多人泡澡的時節。（示意圖／Pixabay）'},
  {'type': 'paragraph',
   'text': '許多人泡湯會交叉進入冷熱池，認為此舉有益心血管健康，腎臟科醫師郭克林表示，冷熱池交換泡，會衝擊心血管與神經健康，尤其是神經的調節，「我也無法冷熱池交叉泡，即使年輕時，我也不這麼做！」。他表示，人進入中年，常伴隨三高問題，血管內皮功能較差，更不適合忽冷忽熱的泡溫泉、泡澡。'},
  {'type': 'paragraph',
   'text': '大陸冷氣團來襲，各地氣溫驟降，許多人會泡溫泉舒緩身心。台北慈濟醫院腎臟透析中心主任郭克林在節目中表示，人體在遇到冷熱溫度快速改變時，心血管與神經會受到影響，因此泡溫泉時不建議冷熱泉交叉泡。此外，泡澡或泡溫泉的時間也勿過長。'},
  {'type': 'paragraph',
   'text': '他表示，中年人常伴隨三高（高血脂、高血壓、高血糖）問題，「尤其是糖尿病患者的血管內皮細胞功能較差，」冷熱溫度劇烈改變，會衝擊人體的心血管與神經，尤其是神經的調節。'},
  {'type': 'paragraph',
   'text': '他並表示，人在高壓下，例如工作、生活壓力下，原本的自律神經也受到影響，「例如有些年輕人喝酒，或使用助眠藥物，來舒緩精神壓力，」此時又遇到溫度劇烈改變，更容易產生致命的危險。'}]}

class NewsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 窗口設置
        self.setWindowTitle("新聞應用程式")
        self.resize(1200, 600)

        # 主容器
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # 左側控制區域
        control_layout = QVBoxLayout()
        btn_random = QPushButton("Random News")
        btn_store = QPushButton("Store To Database")
        control_layout.addWidget(btn_random)
        control_layout.addWidget(btn_store)
        control_layout.addStretch()  # 增加空白區域
        main_layout.addLayout(control_layout, 1)

        # 右側新聞顯示區域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area, 4)

        self.setCentralWidget(main_widget)

        # 加載新聞
        self.load_news(news_json)

    def load_news(self, news):
        # 清空舊內容
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # 添加新聞標題
        title_label = QLabel(news["Title"])
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.scroll_layout.addWidget(title_label)

        # 添加新聞內容
        for content in news["Content"]:
            if content["type"] == "paragraph":
                self.add_paragraph(content["text"])
            elif content["type"] == "image":
                self.add_image(content["src"], content.get("alt", ""))

        # 添加空白填充，防止滾動條過早出現
        self.scroll_layout.addStretch()

    def add_paragraph(self, text):
        """添加段落文字"""
        paragraph_label = QLabel(text)
        paragraph_label.setWordWrap(True)  # 自動換行
        paragraph_label.setStyleSheet("font-size: 14px; margin: 10px 0;")
        self.scroll_layout.addWidget(paragraph_label)

    def add_image(self, src, alt):
        """添加圖片及其描述"""
        try:
            # 獲取圖片
            response = requests.get(src)
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(response.content).read())

            # 添加圖片
            image_label = QLabel()
            image_label.setPixmap(pixmap.scaledToWidth(750, Qt.SmoothTransformation))
            self.scroll_layout.addWidget(image_label)

            # 添加圖片描述
            if alt:
                alt_label = QLabel(alt)
                alt_label.setStyleSheet("font-size: 12px; color: gray;")
                self.scroll_layout.addWidget(alt_label)
        except Exception as e:
            error_label = QLabel("圖片載入失敗")
            error_label.setStyleSheet("color: red;")
            self.scroll_layout.addWidget(error_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewsApp()
    window.show()
    sys.exit(app.exec_())
