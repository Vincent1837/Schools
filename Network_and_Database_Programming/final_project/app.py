"""
crawl the yahoo news and get the articles titles, contents, and pictures
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Yahoo News URL
url = "https://tw.news.yahoo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Scrape headlines and links
topics = soup.find_all("li", class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")
print(topics)
articles = []

for topic in topics:
    topic_title = topic.find("a").string
    topic_link = topic.find("a")["href"]
        
    # Fetch the article content
    article_response = requests.get(topic_link)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    content = "\n".join([p.get_text(strip=True) for p in article_soup.find_all('p') if not p.get_text(strip=True).startswith('更多')])

    # Fetch the article image
    image_tag = article_soup.find("img", loading_="lazy")
    
    if image_tag:
        image_url = image_tag["src"]
        print("img saved!")
    else:
        image_url = None
    
    # Append to the list
    articles.append({"Title": topic_title, "Link": topic_link, "Content": content, "Image": image_url})

# Save to csv
df = pd.DataFrame(articles)
df.to_csv("yahooNews.csv", index=False)

import sys
import requests
from io import BytesIO
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton,
    QScrollArea, QWidget, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class NewsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        from pymongo import MongoClient
        self.df = pd.read_csv("yahooNews.csv")
        self.db_client = MongoClient("mongodb+srv://yuanchan1837:ag061837@cluster0.dc6xs.mongodb.net/")
        self.db = self.db_client["yahoo_news_database"]
        self.collection = self.db["yahoo_news_collection"]

        # 窗口設置
        self.setWindowTitle("Yahoo新聞資料庫")
        self.resize(1200, 600)

        # 主容器
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # 左側控制區域
        self.control_layout = QVBoxLayout()
        self.news_list = QListWidget()  # List to display saved news titles

        btn_random = QPushButton("Random News")
        btn_store = QPushButton("Store To Database")
        self.control_layout.addWidget(btn_random)
        self.control_layout.addWidget(btn_store)
        self.control_layout.addWidget(self.news_list)
        self.control_layout.addStretch()  # 增加空白區域
        main_layout.addLayout(self.control_layout, 1)

        # 右側新聞顯示區域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area, 4)

        self.setCentralWidget(main_widget)
        self.news = {}

        # 加載新聞
        btn_random.clicked.connect(self.random_news)
        btn_store.clicked.connect(self.store_to_database)
        self.news_list.itemClicked.connect(self.load_saved_news)  # Event for loading saved news

        self.load_saved_news_list()
        self.random_news()
        self.load_news()

    def load_saved_news_list(self):
        """Load news titles from the database into the list"""
        self.news_list.clear()
        saved_news = self.collection.find({}, {"_id": 1, "Title": 1})
        for news in saved_news:
            item = QListWidgetItem(news["Title"])
            item.setData(Qt.UserRole, str(news["_id"]))
            self.news_list.addItem(item)

    def load_saved_news(self, item):
        """Load selected news from the database"""
        from bson.objectid import ObjectId
        news_id = item.data(Qt.UserRole)
        news = self.collection.find_one({"_id": ObjectId(news_id)})

        self.news = news
        self.load_news()

    # Other existing methods remain unchanged...
    def random_news(self):
        
        sample = df.sample(1)
        link = sample["Link"].values[0]
        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        title = article_soup.find('h1').get_text(strip=True)
        caasbody = article_soup.find('div', class_='caas-body')
        caasbody = caasbody.find_all(['p', 'img'])
        filtered_data = []

        for element in caasbody:
            if element.name == 'img':  # 如果是 <img> 標籤
                if element.has_attr('src'):  # 確保有 src 屬性
                    img_data = {
                        "type": "image",
                        "src": element['src'],
                        "alt": element.get('alt', '無描述')  # 如果有 alt 屬性，提取它
                    }
                    filtered_data.append(img_data)

            elif element.name == 'p':  # 如果是 <p> 標籤
                text = element.get_text(strip=True)  # 提取段落文字
                if not (text.startswith("看更多") or text.startswith("更多")):  # 過濾不需要的段落
                    paragraph_data = {
                        "type": "paragraph",
                        "text": text
                    }
                    filtered_data.append(paragraph_data)

            
        self.news = {"Title": title, "Content": filtered_data, "Link": link}
        self.load_news()
    def load_news(self):
        # 清空舊內容
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # 添加新聞標題
        title_label = QLabel(self.news["Title"])
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.scroll_layout.addWidget(title_label)

        # 添加新聞內容
        for content in self.news["Content"]:
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
            
    def store_to_database(self):
        """
        將目前新聞儲存至MongoDb
        """
        from pymongo import MongoClient
        client = MongoClient("mongodb+srv://yuanchan1837:ag061837@cluster0.dc6xs.mongodb.net/")
        db = client["yahoo_news_database"]
        collection = db["yahoo_news_collection"]
        collection.insert_one(self.news)
        print("新聞已儲存至 MongoDB")
        client.close()
        self.load_saved_news_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewsApp()
    window.show()
    sys.exit(app.exec_())

