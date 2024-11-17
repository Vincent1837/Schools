import requests
from bs4 import BeautifulSoup
import pandas as pd

# Yahoo News URL
url = "https://tw.news.yahoo.com/"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Scrape headlines and links
articles = []
for headline_tag in soup.find_all('a', class_='js-content-viewer'):  # Adjust the tag and class based on Yahoo’s HTML structure
    headline = headline_tag.get_text(strip=True)
    link = headline_tag['href']
    
    # Ensure full URL if the link is relative
    if not link.startswith("http"):
        link = "https://tw.news.yahoo.com" + link

    # Fetch the article content
    article_response = requests.get(link)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    content = " ".join([p.get_text(strip=True) for p in article_soup.find_all('p')])

    # Append to the list
    articles.append({"Title": headline, "Link": link, "Content": content})
    
    

# Save to Excel
df = pd.DataFrame(articles)
df.to_excel("yahooNews.xlsx", index=False)
df.to_csv("yahooNews.csv")

print("Scraping completed and saved to yahooNews.xlsx")
