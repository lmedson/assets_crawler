# Assets Crawler

Structure for app :open_file_folder: :octocat:

[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Installing the dependencies

Install the dependencies with pip, running:
`$ pip install requeriments.txt`.

## Runinng

Make sure you have installed all the dependencies. Run the file:

`$ python cralwer.py`.

## Setup a site to crawl

In file `crawler.py` in should set a site to crawl, like the example in line 50 of the file, and the filename and format of output. Below is the code snippet:

```python
    # # example
    # declaring url to get using the crawler
    url = 'https://elixir-lang.org/'
    elixir_website = Crawler(url)

    # using the method crawl to get and format data
    # set filename with the format, the start and the end
    data_to_json = elixir_website.draw('my_data.txt', 1, 4)

```

## Result

If everything goes well you will have this result in your folder:

```bash
.
├── .gitignore                  # file with ignored files
├── crawler.py                  # class with crawler
├── README.md                   # Readme with how to use the crawler
├── crawled_data.txt            # your file with tables
└── requeriments.txt            # dependencies file
```
