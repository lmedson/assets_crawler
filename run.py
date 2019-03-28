from utils import plot_map, save_json
from crawler import Crawler
import time

start_time = time.time()
# example
# declaring url to get using the crawler
url_to_scrape = 'https://elixir-lang.org/'

# creating crawler
new_crawler = Crawler(url_to_scrape)

# for running crawl result with tables uncomment the line bellow
new_crawler.storage_data('my_scraped_assets.txt', 'my_scraped_relations.txt')

"""
    For run and plot graph uncomment the three lines 
    bellow(and comment the two above lines),after 
    see the result in a network map."""
# get_relations = new_crawler.run()
# json_file = save_json(get_relations, 'data.json')
# plot_map(json_file)

end_time = time.time()
exec_time = end_time - start_time

print('Execution time: ', exec_time)
