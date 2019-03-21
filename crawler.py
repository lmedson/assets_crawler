from bs4 import BeautifulSoup
from prettytable import PrettyTable
import urllib.request
import json
from multiprocessing.dummy import Pool


class Crawler():
    def __init__(self, url):
        self.url = url
        self.list_links = []
        self.new_links = []
        self.assets_map = []
        self.relation_links = []
        # self.links_filtereds = []
        self.crawled = []
        self.req = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.req, features='lxml')
        # get url string links
        for link in self.soup.find_all('a', href=True):
            if link['href'].startswith('/'):
                if self.url+link['href'] not in self.list_links:
                    self.list_links.append(self.url+link['href'])
            else:
                pass

    def filter_url(self, link):
        if link.startswith('/'):
            return self.url+link

    def make_map(self):
        for url in range(len(self.list_links)):
            if len(self.list_links) == url:
                for url in range(len(self.new_links)):
                    if self.new_links[url] not in (self.crawled and self.list_links):
                        new_req = urllib.request.urlopen(self.new_links[url])
                        new_soup = BeautifulSoup(
                            new_req, features='lxml')
                        for i in new_soup.find_all('a'):
                            link = i.get('href')
                            filtered = self.filter_url(link)
                            if filtered != None:
                                self.crawled.append(self.new_links[url])
                                links_filtereds.append(filtered)
                                if filtered not in (self.list_links and self.new_links and self.crawled):
                                    self.new_links.append(filtered)
                                else:
                                    pass
                    self.relation_links.append(
                        {'page': self.new_links[url], 'related_links': links_filtereds})
            else:
                links_filtereds = []
                if self.list_links[url] not in self.crawled:
                    if self.list_links[url] in self.list_links:
                        # cria uma nova request com base na url da vez
                        new_req = urllib.request.urlopen(self.list_links[url])
                        new_soup = BeautifulSoup(
                            new_req, features='lxml')
                        # percorre todas as tags 'a' na requisição realizada
                        for i in new_soup.find_all('a'):
                            # pega o endereço da tag da vez
                            link = i.get('href')
                            # checa se é do domínio
                            filtered = self.filter_url(link)
                            if filtered != None:
                                # se for válida adiciona a url da vez na lista de crawleadas
                                self.crawled.append(self.list_links[url])
                                # adiciona ao vetor que guarda as relações da url da vez
                                links_filtereds.append(filtered)
                                if filtered not in (self.list_links and self.new_links and self.crawled):
                                    self.new_links.append(filtered)
                                else:
                                    pass
                self.relation_links.append(
                    {'page': self.list_links[url], 'related_links': links_filtereds})

    def get_map(self):
        self.make_map()
        return self.relation_links

    def crawl(self):
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

    def storage_data(self, filename1, filename2):

        save_file = open(filename1, "w+")
        data_to_print = self.crawl()
        table = PrettyTable(
            ["page", "image_name", "image_link", "css", "js"])
        for element in data_to_print:
            table.add_row(
                [element['page'], element['images']['name_image'], element['images']['link_image'], element['css'], element['js']])
        save_file.write(table.get_string(
            start=0, end=len(self.assets_map)))
        save_file.close()

        save_file_map = open(filename2, "w+")
        data_to_print_map = self.get_map()
        table_map = PrettyTable(
            ["page", "relations"])
        for element in data_to_print_map:
            table_map.add_row(
                [element['page'], element['related_links']])
        save_file_map.write(table_map.get_string(
            start=0, end=len(self.relation_links)))
        save_file_map.close()
