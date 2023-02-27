import requests
from bs4 import BeautifulSoup


def get_all_links_from_page():
    url = 'https://www.gastronom.ru/recipe/4852/francuzskie-grenki'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = set()
    for link in soup.find_all('a'):
        urls.add(link.get('href'))

    with open("urls3.txt", "w") as f:
        for url_ in urls:
            if url_ and url_.startswith("/"):
                f.write("https://www.gastronom.ru" + url_ + "\n")


def remove_duplicates():
    urls = set()
    with open("urls.txt", "r") as f:
        for line in f:
            urls.add(line.strip())

    with open("urls.txt", "w") as f:
        for url_ in urls:
            f.write(url_ + "\n")


def remove():
    urls = set()
    with open("urls.txt", "r") as f:
        for line in f:
            if "russianfood" not in line:
                urls.add(line.strip())

    with open("urls.txt", "w") as f:
        for url_ in urls:
            f.write(url_ + "\n")


if __name__ == '__main__':
    # get_all_links_from_page()
    remove_duplicates()
    # remove()
