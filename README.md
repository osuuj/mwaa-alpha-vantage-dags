# mwaa-alpha-vantage-dags
## Table of Contents
- [Introduction](#introduction)
- [Folder Structure](#folderstructure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)


## Introduction
This repository contains AWS Managed Workflows for Apache Airflow (MWAA) Directed Acyclic Graphs (DAGs) designed to download financial data from Alpha Vantage. It includes Python modules, configs and a `requirements.txt` file for managing dependencies.

This project provides a set of Airflow DAGs for automating the process of fetching financial data from Alpha Vantage. The DAGs are designed to be used with AWS Managed Workflows for Apache Airflow (MWAA), simplifying the integration of financial data into your workflows.

## Folder Structure
Here is the folder structure of the repository:
```plaintext
.
├── dags
│   ├── alpha_vantage_dag.py
│   └── another_dag.py
├── plugins
│   ├── data_fetcher.py
│   └── data_processor.py
├── configs
│   ├── config.json
│   └── another_config.json
├── requirements.txt
└── README.md
```
## Features
- Automated retrieval of financial data from Alpha Vantage
- Integration with AWS Managed Workflows for Apache Airflow (MWAA)
- Modular Python code and configurable settings

## Installation
**NOTE:** Have to describe better ...
1. To run codes locally: see the [aws-mwaa-local-runner](https://github.com/aws/aws-mwaa-local-runner) on GitHub.

## Usage
 **NOTE:** Have to describe better ...
 
To use the provided DAGs with MWAA, follow these steps:

1. Upload the DAG files to your MWAA environment.
2. Configure your Alpha Vantage API key in your environment variables or secrets manager.
4. Trigger the DAGs manually or set up a schedule for automated runs.

For more detailed usage instructions, see the individual DAG files and Python modules for configuration options.

## Configuration
**NOTE:** Have to describe better ...
- **Alpha Vantage API Key**: Make sure to set your API key in the environment where MWAA is running. This can be done through environment variables or AWS Secrets Manager.
- **DAG Settings**: Adjust the settings in each DAG to match your needs (e.g., schedule intervals, data parameters).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
