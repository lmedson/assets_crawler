from crawler import Crawler
import time

start_time = time.time()
# # example
# declaring url to get using the crawler
url_to_scrape = 'https://elixir-lang.org/'
new_crawler = Crawler(url_to_scrape)

new_crawler.run()
# using the method crawl to get and format data
new_crawler.storage_data("my_scraped_assets.txt", "my_scraped_relations.txt")

exec_time = time.time() - start_time
print("Execution time: ", exec_time)