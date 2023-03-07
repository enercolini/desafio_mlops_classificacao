# Lighthouse MLOps Challenge - Titanic Survivors Classification

## Overview

This is the MLOps Challenge for the Lighthouse Program on Data Science.

This challange presents a problem with classifying Titanic survivors, on which the available data show several characteristics of the passengers of the Titanic. There are 2 datasets available, `train.csv` with information about the passenger survival (objective variable) and the `test.cv` where these information are not available. The goal is to classify passengers regarding to the binary variable `survival`. The training dataset is used to train the model and then apply it to the test dataset to generate the predictive model.

Both `train.csv` and `test.csv` can be downloaded from https://www.kaggle.com/competitions/titanic/data

Also you can use your CLI to download kaggle files through their API. To do so, first you will need to install and configure your account along with kaggle's API. Read more on how to configure it on https://github.com/Kaggle/kaggle-api.

If you choose to download through your CLI and have everything ready to use kaggle's API, you can download both `train.csv`and `test.csv` using the code:

`kaggle competitions download -c titanic`

Also we recommend you to take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## Starting Your Project

To start a project on Kedro, you must create a new project with the line command below and name it:

```
kedro new
```

## Set Up the Development Environment

Before start coding a new project, it's recommended to set up the development environment. 

This preparation usually starts by creating a virtual enviroment (i.e. venv) allowing to install all the necessary packages, libs and project's dependencies.

Creating the Virtual Environment: 
```
python3 -m venv venv
```
Activating venv: 
```
source venv/bin/activate
```

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## Data and Catalog

To start with kedro and your analysis, you'll need to download the raw data files as explained earlier and allocate them in `data -> 01_raw`. After both raw data files are set on this folder, the next step is to declare/list them in the `catalog.yml` folder (`conf -> base -> catalog.yml`). To list these files, the following codes were used:

```
train_dataset:                          test_dataset:
  type: pandas.CSVDataSet                   type: pandas.CSVDataSet
  filepath: data/01_raw/train.csv           filepath: data/01_raw/test.csv
  load_args:                                load_args:
    sep: ","                                    sep: ","
```

When the catalog is done, you can use jupyter lab to start analysing the dataset and later on build your ML project on kedro.

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
