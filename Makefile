# Makefile for Python project with Conda
.ONESHELL:
SHELL=/bin/zsh
CONDA := $(shell which conda)
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
CONDA_CREATE_ENV = $(CONDA) env create -f environment.yml
CONDA_ACTIVATE_ENV = source $(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate $(CONDA_ENV_NAME) $(CONDA_ENV_NAME)
CONDA_INSTALL_DEPS = conda env update -f environment.yml --prune
CONDA_REMOVE_ENV = conda env remove --name $(CONDA_ENV_NAME)

.PHONY: install-deps remove-env clean test

install-deps:
	$(CONDA_INSTALL_DEPS)

clean:
	@rm -rf __pycache__ $(DOCS_DIR)/_build

test:
	@$(CONDA) run --no-capture-output -n $(CONDA_ENV_NAME) python -m unittest discover -s $(TEST_DIR)


update-requirements:
	@$(CONDA) env export --no-builds | grep -v "prefix" > environment.yml

build: $(SRC_DIR)/*.py
	@pyinstaller --onefile $(SRC_DIR)/main.py

# run the binary
run-binary:
	@./dist/main

# a makefile target to run the main.py file
run:
	@$(CONDA) run --no-capture-output -n $(CONDA_ENV_NAME) python $(SRC_DIR)/main.py