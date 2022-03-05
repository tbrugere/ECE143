# ECE143
Insights on charts and music datasets


## Installing dependencies

The simplest way to install dependencies is through pipenv. 
In the project repo, just type 
```console
$ pipenv install
```

Then to enter the virtual environment, use
```console
$ pipenv shell
```

## Running 

### Getting the datasets.

tldr; to download the datasets, you can use
```console
$ make data
```

All the necessary datasets go in the `data/` folder.

For convenience, we have included the charts ranking datasets in the folder repository.

If needed, the scripts to scrape the French and English datasets are located in the `scripts/` folder.
They are launched using the following commands

```console
$ python scripts/fr_charts_crawl.py --help

usage: fr_charts_crawl.py [-h] filename

scrape the french billboards

positional arguments:
  filename    the output filename

options:
  -h, --help  show this help message and exit
  
$ python scripts/uk_charts_crawl.py

usage: uk_charts_crawl.py [-h] filename

scrape the uk billboards

positional arguments:
  filename    the output filename

options:
  -h, --help  show this help message and exit
```


## Project structure

- the `data/` folder contains the several datasets
