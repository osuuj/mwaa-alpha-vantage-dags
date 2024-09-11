# mwaa-alpha-vantage-dags
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

This repository contains AWS Managed Workflows for Apache Airflow (MWAA) Directed Acyclic Graphs (DAGs) designed to download financial data from Alpha Vantage. It includes Python modules and a `requirements.txt` file for managing dependencies.

## Folder Structure

Here is the folder structure of the repository:

```plaintext
.
├── dags
│   ├── alpha_vantage_dag.py
│   └── another_dag.py
├── modules
│   ├── data_fetcher.py
│   └── data_processor.py
├── tests
│   ├── test_alpha_vantage_dag.py
│   └── test_data_fetcher.py
├── requirements.txt
└── README.md
```

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a set of Airflow DAGs for automating the process of fetching financial data from Alpha Vantage. The DAGs are designed to be used with AWS Managed Workflows for Apache Airflow (MWAA), simplifying the integration of financial data into your workflows.

## Features

- Automated retrieval of financial data from Alpha Vantage
- Integration with AWS Managed Workflows for Apache Airflow (MWAA)
- Modular Python code and configurable settings

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mwaa-alpha-vantage-dags.git

## Usage
To use the provided DAGs with MWAA, follow these steps:

1. Upload the DAG files to your MWAA environment.
2. Configure your Alpha Vantage API key in your environment variables or secrets manager.
3. Trigger the DAGs manually or set up a schedule for automated runs.

For more detailed usage instructions, see the individual DAG files and Python modules for configuration options.

## Configuration
- **Alpha Vantage API Key**: Make sure to set your API key in the environment where MWAA is running. This can be done through environment variables or AWS Secrets Manager.
- **DAG Settings**: Adjust the settings in each DAG to match your needs (e.g., schedule intervals, data parameters).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
