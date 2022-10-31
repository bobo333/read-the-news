from argparse import ArgumentParser

import textwrap
from bs4 import BeautifulSoup
import requests

def nice_print(input_text):
    print('\n'.join(textwrap.wrap(input_text)), '\n')

headers = {
    'User-Agent': 'read-the-news'
}


def main():
    parser = ArgumentParser(description="Get the news, so you can read it",
        epilog="knowledge is power")
    parser.add_argument("url")
    args = parser.parse_args()

    page = requests.get(args.url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    sections = []

    sections.append(soup.title.text)
    byline = soup.find(class_='byline')
    sections.append(byline.find(class_='authors').text)
    sections.append("{}".format(byline.find(class_='published-date').text))
    paragraphs = soup.find(class_='rich-text-article-body-content').find_all('p')

    for p in paragraphs:
        parents = {x.name for x in p.parents}
        if 'ps-promo' in parents:
            continue
        if not p.text:
            continue
        sections.append('\n'.join(textwrap.wrap(p.text)))

    for s in sections:
        nice_print(s)


if __name__ == "__main__":
    main()
