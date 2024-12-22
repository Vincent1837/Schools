import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read from Excel

df = pd.read_excel("yahooNews.xlsx")

sample = df.head(1)

link = sample["Link"].values[0]

article_response = requests.get(link)

article_soup = BeautifulSoup(article_response.content, 'html.parser')

print(link)

title = article_soup.find('h1').get_text(strip=True)

caasbody = article_soup.find('div', class_='caas-body')
paragraphs = caasbody.find_all('p')




artical_content = ""
# 擷取純文字訊息
for paragraph in paragraphs:
    content = paragraph.get_text(strip=True)
    if not content.startswith("更多") and not content.startswith("看更多"):
        artical_content += content + "\n"
    
print(artical_content)

# 展示所有圖片
images = caasbody.find_all('img', src=True)
for image in images:
    img_url = image['src']
    print(f'Image URL: {img_url}')  
    img_response = requests.get(img_url)
    img_data = img_response.content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)
        print('Image saved!')
        
    import matplotlib.pyplot as plt
    img = plt.imread('image.jpg')
    plt.imshow(img)
    plt.show()
        
#caasbody.contents

images