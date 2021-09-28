# Graph API Examples

<details open="open">
<summary>Table of Contents</summary>

<!-- TOC -->

- [Graph API Examples](#graph-api-examples)
  - [About this Project](#about-this-project)
    - [Packages Included](#packages-included)
    - [Project Navigation](#project-navigation)
      - [Getting Started](#getting-started)
      - [Examples](#examples)
  - [Additional Resources](#additional-resources)
    - [Microsoft Documentation](#microsoft-documentation)
    - [Development Dependencies](#development-dependencies)
  - [Vision and Roadmap](#vision-and-roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Maintainers](#maintainers)
  - [Acknowledgements](#acknowledgements)

<!-- /TOC -->

</details>

## About this Project

The Graph API Examples repository is designed to provide concrete examples for making calls to the Microsoft Graph API using a series of libraries in Python and R. The project is organized as a series of reference implementations  

### Packages Included

- Python Packages
  - [msgraph](https://github.com/microsoftgraph/msgraph-sdk-python-core) - Microsoft maintained software development kit (sdk) that provides a thin wrapper for the Graph API
  - [O365](https://github.com/O365/python-o365) - Third party library for utilizing Graph API with a robust feature set for Graph APIs core resources
  - [Dynaconf](https://github.com/rochacbruno/dynaconf) - 12-factor app compliant library for managing configuration settings and secret storage
- R Packages
  - [AzureGraph](https://github.com/Azure/AzureGraph) - Graph API package for R that supports multiple kinds of authentication
  - [Microsoft365R](https://github.com/Azure/Microsoft365R) - Graph API package for R centered around user-based authentication flows with a simpler interface than AzureGraph

### Project Navigation

#### Getting Started

- Graph API Overview
  - API basics
  - Using Graph API to access O365
  - Requesting access to Graph API
- With Python
  - Using `msgraph`
  - Using `O365`
- With R
  - Using `AzureGraph`
  - Using `Microsoft365R`

#### Examples

- SharePoint Sites and Lists
  - Site Resource
    - Graph API documentation
    - Using `msgraph`
    - Using `O365`
    - Using `AzureGraph`
    - Using `Microsoft365R`
  - List Resource
    - Graph API documentation
    - Using `msgraph`
    - Using `O365`
    - Using `AzureGraph`
    - Using `Microsoft365R`
  - ListItem Resource
    - Graph API documentation
    - Using `msgraph`
    - Using `O365`
    - Using `AzureGraph`
    - Using `Microsoft365R`
- SharePoint Drives and OneDrive
  - Drive Resource
    - Graph API documentation
    - Using `msgraph`
    - Using `O365`
    - Using `AzureGraph`
    - Using `Microsoft365R`
  - DriveItem Resource
    - Graph API documentation
    - Using `msgraph`
    - Using `O365`
    - Using `AzureGraph`
    - Using `Microsoft365R`

## Additional Resources

### Microsoft Documentation

- [Microsoft Graph Auth Overview](https://docs.microsoft.com/en-us/graph/auth/?view=graph-rest-1.0)
- [Graph API Documentation](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)

### Development Dependencies

- Python dependencies
  - [Dynaconf](https://github.com/rochacbruno/dynaconf) - 12-factor app compliant library for managing configuration settings and secret storage.
  - [tox](https://tox.readthedocs.io/en/latest/) - Automates and standardizes the creation of testing environments.
  - [pytest](https://docs.pytest.org/en/6.2.x/) - Simplifies the design and execution of both unit and integration testing.
  - [black](https://black.readthedocs.io/en/stable/) - Autoformats code for consistent styling.
  - [flake8](https://flake8.pycqa.org/en/latest/) - Checks that code complies with PEP8 style guidelines.
  - [pylint](https://www.pylint.org/) - Checks that code follows idiomatic best practices for Python.
  - [pre-commit](https://pre-commit.com/) - Runs code quality checks before code is committed.
- R dependencies
  - TODO: Add dependencies

## Vision and Roadmap

The vision for this template is to simplify the process of creating open source python projects with high quality codebase and mechanisms that promote smart and collaborative project governance. This project aims to fulfill this vision by:

- Adopting a common python package file structure
- Implementing basic linting and code quality checks
- Reinforcing compliance with those code quality checks using CI/CD
- Providing templates for things like documentation, issues, and pull requests
- Offering pythonic implementation examples of common data structures and scripting tasks like:
  - Creating classes, methods, and functions
  - Setting up unit and integration testing
  - Reading and writing to files

For a more detailed breakdown of the feature roadmap and other development priorities please reference the following links:

- [Feature Roadmap](https://github.com/widal001/python-boilerplate/projects/1)
- [Architecture Decisions](https://github.com/widal001/python-boilerplate/projects/2)
- [Bug Fixes](https://github.com/widal001/python-boilerplate/projects/3)
- [All Issues](https://github.com/widal001/python-boilerplate/issues)

## Contributing

Contributions are always welcome! We encourage contributions in the form of discussion on issues in this repo and pull requests for improvements to documentation and code.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Maintainers

- [@widal001](https://github.com/widal001)

## Acknowledgements

- [Python Packaging Authority Sample Project](https://github.com/pypa/sampleproject)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)
