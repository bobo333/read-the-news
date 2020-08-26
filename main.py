from bs4 import BeautifulSoup
import requests

url = 'https://www.sandiegouniontribune.com'

headers = {
    'User-Agent': 'steve'
}

# print(requests.get(url, headers=headers))

with open('examples/sdut_index.html') as f:
    body = f.read()

soup = BeautifulSoup(body, 'html.parser')

print(soup.title)

titles = soup.find_all(class_='promo-title')

unique_titles = []

for t in titles:
    clean_title = t.text.strip()
    if clean_title not in unique_titles:
        unique_titles.append(clean_title)

print(len(unique_titles))
