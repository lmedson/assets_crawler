from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable


class Crawler():
    def __init__(self, url):
        self.url = url
        self.list_links = [url]
        self.assets_map = []
        self.relation_links = []
        self.crawled = []

    def filter_url(self, link, baseUrl):
        new_url = self.url[:-1]+link
        if link.startswith('/'):
            return new_url
        elif link.startswith(baseUrl):
            return link
        else:
            pass

    def get_urls_map(self):
        urls_to_crawl = self.list_links.copy()
        crawled_list = []
        while len(urls_to_crawl) != 0:
            current_url = urls_to_crawl[0]
            if current_url not in crawled_list:
                links_relateds = []
                try:
                    req = urllib.request.urlopen(current_url)
                    soup = BeautifulSoup(req, features='lxml')
                except:
                    pass
                # add current url to crawleds list
                crawled_list.append(current_url)
                for i in soup.find_all("a"):
                    # get found url
                    found_url = i["href"]
                    # check if found url belongs to base url
                    filtered_url = self.filter_url(found_url, self.url)
                    if filtered_url != None and filtered_url not in links_relateds:
                        # print(filtered_url)
                        """
                        if filtered belongs to base url, and not yet in current
                        crawled url, push to array with relashionships
                        """
                        links_relateds.append(filtered_url)
                        # if the found url yet not crawled, push to array to craw
                        if filtered_url not in crawled_list and filtered_url not in urls_to_crawl:
                            # add found url inside current_url to crawl list
                            urls_to_crawl.append(filtered_url)
                        else:
                            pass
                self.relation_links.append(
                    {'page': current_url, 'related_links': links_relateds})
                urls_to_crawl.pop(urls_to_crawl.index(current_url))
            else:
                self.crawled = crawled_list
                return print("Crawling finished")

    def run(self):
        self.get_urls_map()
        return self.relation_links

    def crawl_assets(self):
        # get urls
        for page in self.list_links:
            new_req = urllib.request.urlopen(page)
            new_soup = BeautifulSoup(
                new_req, features='lxml')
            for index in new_soup.find_all('img'):
                alt = index.get('alt')
                src = index.get('src')
                filtered_url = self.filter_url(src, self.url)
                self.assets_map.append(
                    {'page': page,  'images': {'name_image': alt, 'link_image': filtered_url}, 'css': [], 'js': []})
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
        data_to_print = self.crawl_assets()
        table = PrettyTable(
            ["page", "image_name", "image_link", "css", "js"])
        for element in data_to_print:
            table.add_row(
                [element['page'], element['images']['name_image'], element['images']['link_image'], element['css'], element['js']])
        save_file.write(table.get_string(
            start=0, end=len(self.assets_map)))
        save_file.close()

        save_file_map = open(filename2, "w+")
        data_to_print_map = self.run()
        table_map = PrettyTable(
            ["page", "relations"])
        for element in data_to_print_map:
            table_map.add_row(
                [element['page'], element['related_links']])
        save_file_map.write(table_map.get_string(
            start=0, end=len(self.relation_links)))
        save_file_map.close()