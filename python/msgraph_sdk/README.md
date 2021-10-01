# Python Library: `msgraph`

<!-- TOC -->

- [Python Library: `msgraph`](#python-library-msgraph)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Authentication](#authentication)
    - [Get access on behalf of a user](#get-access-on-behalf-of-a-user)
    - [Get access without a user](#get-access-without-a-user)
  - [SharePoint Sites and Lists](#sharepoint-sites-and-lists)
    - [Site Resource](#site-resource)
    - [List Resource](#list-resource)
    - [ListItem Resource](#listitem-resource)
  - [Drives and Files](#drives-and-files)
    - [Drive Resource](#drive-resource)
    - [DriveItem Resource](#driveitem-resource)

<!-- /TOC -->

## Getting Started

### Prerequisites

- Python installed on your local machine, a version between 3.7 and 3.9

In order to check which version of python you have installed, run the following in your command line, and the output should look something like this:

> **NOTE**: in all of the code blocks below, lines preceded with $ indicate commands you should enter in your command line (excluding the $ itself), while lines preceded with > indicate the expected output from the previous command.

```
$ python --version
> Python 3.9.0
```

If you receive an error message, or the version of python you have installed is not between 3.7 and 3.9, consider using a tool like [pyenv](https://github.com/pyenv/pyenv) (on Mac/Linux) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (on Windows) to manage multiple python installations.

### Installation

1. Change directory into this folder: `cd python/msgraph_sdk`
1. Create a new virtual environment: `python -m venv env`
1. Activate the virtual environment
   - On Mac/Linux: `source env/bin/activate`
   - On Windows: `.\env\Scripts\activate`
1. Install this package in editable mode by running `pip install -e .` which makes changes made to scripts within this package available without re-installing it.
1. Install the other dependencies required to contribute to the project: `pip -r requirements.txt`
1. Install `pre-commit` to autoformat your code: `pre-commit install`
1. Execute all tests by running `tox` All tests should pass with an output that ends in something like this:
   ```
    py39: commands succeeded
    lint: commands succeeded
    checkdeps: commands succeeded
    pytest: commands succeeded
    coverage: commands succeeded
    congratulations :)
   ```

## Authentication

### Get access on behalf of a user

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

### Get access without a user

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

## SharePoint Sites and Lists

### Site Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

### List Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

### ListItem Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

## Drives and Files

### Drive Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

### DriveItem Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->
