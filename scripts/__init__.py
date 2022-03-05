"""
Data scraping scripts for billboards
=====================================

Use those scripts to scrape data from the French and English music billboards.
Normally you shouldn’t have to use those scripts directly:

* the data is already in the repository
* they can be called using :code:`make data`

They use :code:`selenium` with firefox-webdriver, so they will need :code:`Firefox` installed.

French script usage
-------------------

.. argparse::
    :module: scripts.fr_charts_crawl
    :func: get_parser
    :prog: scripts/fr_charts_crawl.py


UK script usage
-------------------

.. argparse::
    :module: scripts.uk_charts_crawl
    :func: get_parser
    :prog: scripts/uk_charts_crawl.py

"""
