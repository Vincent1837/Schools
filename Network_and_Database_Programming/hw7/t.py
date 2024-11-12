import requests
from bs4 import BeautifulSoup
import pandas as pd

# Yahoo News URL
url = "https://tw.news.yahoo.com/"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

topics = soup.find_all("li", class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")

with open("soup.txt", "w+", encoding="utf-8") as f:
    f.write(str(topics))
    
    
articles = []    
for topic in topics:
    topic_title = topic.find("a").string
    topic_link = topic.find("a")["href"]

    # Fetch the topic content
    """ topic_response = requests.get(topic_link)
    topic_soup = BeautifulSoup(topic_response.content, 'html.parser')
    topic_content = " ".join([p.get_text(strip=True) for p in topic_soup.find_all('p')]) """
    
    topic_response = requests.get(topic_link)
    topic_soup = BeautifulSoup(topic_response.content, 'html.parser')
    caasbody = topic_soup.find("div", class_="caas-body")
    topic_content = ""
    for p in (caasbody.find_all("p")):
        if (p.string):
            topic_content += p.string + "\n"

    # Append to the list
    articles.append({"Topic": topic_title, "Link": topic_link, "Content": topic_content})
    
    
    

# Save to Excel
df = pd.DataFrame(articles)
df.to_excel("yahooNews.xlsx", index=False)
df.to_csv("yahooNews.csv")

print("Scraping completed and saved to yahooNews.xlsx")

""" topic_link = topics[2].find("a")["href"]
print(topic_link)



with open("topic.txt", "w+", encoding="utf-8") as f:
    f.write(str(caasbody))
    pass

for p in (caasbody.find_all("p")):
    print(p.string) """