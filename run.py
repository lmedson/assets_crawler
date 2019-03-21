from crawler import Crawler
import time
from threading import Thread
# # example
# declaring url to get using the crawler
url_to_scrape = 'https://elixir-lang.org/'
new_crawler = Crawler(url_to_scrape)

# using the method crawl to get and format data
new_crawler.storage_data(
    'my_scraped_data.txt', 'my_scraped_data1.txt',)
