from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable


class Crawler():
    def __init__(self, url):
        self.url = url
        self.list_links = []
        self.assets_map = []
        self.req = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.req, features='lxml')
        self.data = {}
        self.start = 0
        self.end = 0

    def crawl(self):
        for link in self.soup.find_all('a', href=True):
            if link['href'].startswith('/'):
                self.list_links.append(self.url+link['href'])

        for page in self.list_links:
            new_req = urllib.request.urlopen(page)
            new_soup = BeautifulSoup(
                new_req, features='lxml')
            for index in new_soup.find_all('img'):
                alt = index.get('alt')
                src = index.get('src')
                self.assets_map.append(
                    {'page': page, 'name_image': alt, 'link_image': self.url+src})

        return self.assets_map

    def draw(self, filename, start, end):
        save_file = open(filename, "w+")
        data_to_print = self.crawl()
        table = PrettyTable(
            ["page", "name", "link"])
        for element in data_to_print:
            table.add_row(
                [element['page'], element['name_image'], element['link_image']])

        save_file.write(table.get_string(start=1, end=20))
        save_file.close()


# # example
# declaring url to get using the crawler
url = 'https://elixir-lang.org/'
elixir_website = Crawler(url)

# using the method crawl to get and format data
data_to_json = elixir_website.draw('my_data.txt', 1, 4)
