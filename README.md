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

    # creating crawler
    new_crawler = Crawler(url_to_scrape)

    # for running crawl result with tables uncomment the line bellow
    # new_crawler.storage_data('my_scraped_assets.txt', 'my_scraped_relations.txt')

    """
    For run and plot graph uncomment the three lines
    bellow(and comment the two above lines),after
    see the result in a network map."""
    # get_relations = new_crawler.run()
    # json_file = save_json(get_relations, 'data.json')
    # plot_map(json_file)
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
├── data.json                   # Your scraped data in json, to plot, if you choose plot graph
├── README.md                   # Readme with how to use the crawler
├── requeriments.txt            # Dependencies file
├── my_scraped_assets.txt       # Your scraped data assets in tables
├── my_scraped_relations.txt    # Your scraped data relations in tables
├── run.py                      # File to run the crawler
└── utils.py                    # File with helpers
```
