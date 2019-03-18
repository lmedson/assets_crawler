from bs4 import BeautifulSoup
import urllib.request


class Crawler():
    def __init__(self, url):
        self.url = url
        self.list_links = []
        self.assets_map = []
        self.req = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.req, features='lxml')

    def crawl(self):
        for link in self.soup.find_all('a', href=True):
            if link['href'].startswith('/'):
                self.list_links.append(self.url+link['href'])

        for page in self.list_links:
            new_req = urllib.request.urlopen(page)
            new_soup = BeautifulSoup(
                new_req, features='lxml')
            for i in new_soup.find_all('img'):
                alt = i.get('alt')
                src = i.get('src')
                self.assets_map.append(
                    {'page': page, 'image': {'name': alt, 'link': self.url+src}})

        return self.assets_map


# example
# declaring site to get using the crawler
# elixir_website = Crawler('https://elixir-lang.org/')

# using the method crawl to get data
# data = elixir_website.crawl()
