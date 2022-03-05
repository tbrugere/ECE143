million_url="http://millionsongdataset.com/sites/default/files/AdditionalFiles/msd_summary_file.h5"
spotify_url="https://transfer.sh/DBb1S7/spotify_new.txt"

all: docgen data

deps:
	pipenv install

dev-deps: 
	pipenv install --dev
	
data: data/spotify_new.csv data/msd_summary_file.h5 data/UK_charts.csv data/french_charts.csv data/billboard_data.csv

data/msd_summary_file.h5:
	wget $(million_url) -O data/msd_summary_file.h5 

data/spotify_new.csv:
	wget $(spotify_url) -O data/spotify_new.csv
	#origin https://www.kaggle.com/geomack/spotifyclassification

data/UK_charts.csv:
	python scripts/uk_charts_crawl.py data/UK_charts.csv

data/french_charts.csv:
	python scripts/fr_charts_crawl.py data/french_charts.csv

docgen: docs dev-deps
	pipenv run  $(MAKE) -C docs html

docs: docs-dir autodoc docs/source/README.md nbconvert

docs-dir: staticdocs
	cp -Rf staticdocs docs

autodoc: docs-dir dev-deps
	pipenv run sphinx-apidoc -f -e -o docs/source scripts

docs/source/README.md:
	cp ./README.md docs/source/README.md

nbconvert: docs-dir dev-deps
# 	pipenv run jupyter-nbconvert --to rst tests/Process.ipynb  --output-dir ./docs/source
# 	sed -i "/^\s*INFO:/d" ./docs/source/Process.rst #remove the innumerable INFO: lines

clean:
	rm -rf docs

.PHONY: clean docs docs-dir autodoc nbconvert docgen
