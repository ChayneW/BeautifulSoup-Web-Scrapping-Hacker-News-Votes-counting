# Web Scraping Project https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://news.ycombinator.com/')
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

'''Searching for single instances'''
link = soup.find(name='a', class_="titlelink")
print(f"the first link is:{link}")

article_text = link.getText()
print(f"the article text is: {article_text}")

article_link = link.get('href')
print(f"the article link is: {article_link}")

article_upvote = soup.find(name='span', class_='score').getText()
print(f"the article upvote is: {article_upvote}")


'''multiple occurances'''
links = soup.find_all(name='a', class_="titlelink")
# print(f"the first link is:{links}")

article_texts = []
article_links = []

for article_tag in links:
    text = article_tag.getText()
    article_texts.append(text)
    article_link = article_tag.get('href')
    article_links.append(article_link) 


articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score') ]

print(article_texts)
print("\n")
print(article_links)
print("\n")
print(articles_upvotes)
