import textwrap
from bs4 import BeautifulSoup

def nice_print(input_text):
    print('\n'.join(textwrap.wrap(input_text)), '\n')

with open('examples/sdut_article.html') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sections = []

sections.append(soup.title.text)
byline = soup.find(class_='byline')
sections.append(byline.find(class_='authors').text)
sections.append("{} {}".format(byline.find(class_='published-day').text, byline.find(class_='published-time').text))
paragraphs = soup.find(class_='rich-text-article-body-content').find_all('p')


for p in paragraphs:
    if not p.text:
        continue
    sections.append('\n'.join(textwrap.wrap(p.text)))

for s in sections:
    nice_print(s)
