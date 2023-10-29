# Makefile for Python project with Conda
.ONESHELL:
SHELL=/bin/zsh
# Automatically determine the Conda environment name from the current folder name
CONDA_ENV_NAME = $(shell basename $(CURDIR))

# Directories
SRC_DIR = src
TEST_DIR = tests
DOCS_DIR = docs

# Python files
PYTHON_FILES = $(wildcard $(SRC_DIR)/*.py)
TEST_FILES = $(wildcard $(TEST_DIR)/*.py)

# Conda commands
CONDA_CREATE_ENV = conda env create -f environments.yml
CONDA_ACTIVATE_ENV = conda activate  $(CONDA_ENV_NAME)
CONDA_DEACTIVATE_ENV = conda deactivate
CONDA_INSTALL_DEPS = conda env update -f environments.yml --prune
CONDA_REMOVE_ENV = conda env remove --name $(CONDA_ENV_NAME)
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

.PHONY: create-env activate-env deactivate-env install-deps remove-env clean test

create-env:
	$(CONDA_CREATE_ENV)

activate-env:
	$(CONDA_ACTIVATE_ENV)

deactivate-env:
	$(CONDA_DEACTIVATE_ENV)

install-deps: #activate-env
	$(CONDA_INSTALL_DEPS)

remove-env:
	$(CONDA_REMOVE_ENV)

clean: deactivate-env
	rm -rf __pycache__ $(DOCS_DIR)/_build

test: activate-env
	python -m unittest discover -s $(TEST_DIR)
