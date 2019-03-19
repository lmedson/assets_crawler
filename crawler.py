from bs4 import BeautifulSoup
from prettytable import PrettyTable
import urllib.request


class Crawler():
    def __init__(self, url):
        self.url = url
        self.list_links = []
        self.assets_map = []
        self.req = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.req, features='lxml')
        self.end = 0

    def crawl(self):
        # get url string links
        for link in self.soup.find_all('a', href=True):
            if link['href'].startswith('/'):
                self.list_links.append(self.url+link['href'])
        # get urls
        for page in self.list_links:
            new_req = urllib.request.urlopen(page)
            new_soup = BeautifulSoup(
                new_req, features='lxml')
            for index in new_soup.find_all('img'):
                alt = index.get('alt')
                src = index.get('src')
                if src.startswith('/'):
                    self.assets_map.append(
                        {'page': page,  'images': {'name_image': alt, 'link_image': self.url+src}, 'css': [], 'js': []})
                else:
                    self.assets_map.append(
                        {'page': page, 'images': {'name_image': alt, 'link_image': src}, 'css': [], 'js': []})
        # get css
        for key in range(len(self.assets_map)):
            for index_css in new_soup.find_all('link'):
                if index_css['href'].endswith('.css'):
                    if index_css['href'].startswith('/'):
                        self.assets_map[key]['css'].append(
                            self.url+index_css['href'])
                    else:
                        self.assets_map[key]['css'].append(
                            index_css['href'])
                else:
                    pass
        # get scripts
        for key in range(len(self.assets_map)):
            for index_js in new_soup.find_all('script'):
                src_js = index_js.get('src')
                if src_js != None:
                    if src_js.startswith('/'):
                        self.assets_map[key]['js'].append(
                            self.url+src_js)
                    else:
                        self.assets_map[key]['js'].append(
                            src_js)
                else:
                    pass
        return self.assets_map

    def storage_assets(self, filename):
        save_file = open(filename, "w+")
        data_to_print = self.crawl()
        table = PrettyTable(
            ["page", "image_name", "image_link", "css", "js"])
        for element in data_to_print:
            table.add_row(
                [element['page'], element['images']['name_image'], element['images']['link_image'], element['css'], element['js']])
        save_file.write(table.get_string(
            start=0, end=len(self.assets_map)))
        save_file.close()
