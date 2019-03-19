# Assets Crawler

Structure for app :open_file_folder: :octocat:

[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Installing the dependencies

Install the dependencies with pip, running:
`$ pip install -r requeriments.txt`.

## Setup a site to crawl

In file `run.py` in should set a site to crawl, like the example in line 50 of the file, and the filename and format of output. Below is the code snippet:

```python
    # example
    # declaring url to get using the crawler
    url_to_scrape = 'https://elixir-lang.org/'
    new_crawler = Crawler(url_to_scrape)

    # set the filename with the format, like "txt"
    new_crawler.storage_assets('my_scraped_data.txt')

```

## Runinng

Make sure you have installed all the dependencies. Run the file:

`$ python run.py`.

## Result

If everything goes well you will have this result in your folder:

```bash
.
├── .gitignore                  # File with ignored files
├── crawler.py                  # Module with crawler
├── README.md                   # Readme with how to use the crawler
├── requeriments.txt            # Dependencies file
├── my_scraped_data.txt         # Your scraped data in tables
└── run.py                      # File to run the crawler
```
