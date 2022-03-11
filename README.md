# ECE143 project: Insights on charts and music datasets


## Installing dependencies

The simplest way to install dependencies is through pipenv. 
In the project repo, just type 
```console
$ pipenv install
```
Alternatively you can use the makefile
```console
$ make deps
```

Then to enter the virtual environment, use
```console
$ pipenv shell
```

## Building documentation

The documentation is built using `sphinx` and `sphinx-autodoc` from the files in `staticdocs/` as well as the docstrings in the python files (and this readme file).

To build it, simply run
```console
$ make docgen #this will also fetch the required dependencies such as sphinx
```
The documentation will then be available in the `doc/_build/` folder

**Note**: if you are regenerating the documentation after having already built it, you may want to run `make clean` beforehand

## Running 

### Getting the datasets.

**tldr;** to download the datasets, you can use

```console
$ make data
```
----

All the necessary datasets go in the `data/` folder.

For convenience, we have included the charts ranking datasets in the folder repository. But the *spotify* and *million songs* dataset are too big and must be downloaded separately using aforementioned command.

If needed, the scripts to scrape the French and English datasets are located in the `scripts/` folder.
To learn more about them, read the documentation in the [scripts package](scripts) (link will only work if you are reading this in the documentation).

### Running the project

The main code is located in the `notebooks/ECE143Project.ipynb` jupyter notebook.

To run it, start jupyter notebook, either directly in the virtualenv with
```console
$ pipenv run jupyter notebook notebooks/ECE143Project.ipynb
```

or install the virtualenv as a kernelspec in your regular jupyter installation with
```console
$ make install-kernel
```

## Project structure

- the `data/` folder contains the several datasets
- the `scripts/` package contains the scraping scripts
- the `utils/` package contains various utility functions used in the notebook
- the `notebooks/` folder contains the main notebook of the repo
