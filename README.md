
# mwaa-alpha-vantage-dags

## Table of Contents
- [mwaa-alpha-vantage-dags](#mwaa-alpha-vantage-dags)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Folder Structure](#folder-structure)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [License](#license)

---

## Introduction

This repository provides Airflow DAGs designed to automate the retrieval of financial data from Alpha Vantage. The DAGs are optimized for use with AWS Managed Workflows for Apache Airflow (MWAA), making it easy to incorporate financial data into your workflows. The project includes all necessary Python modules, configurations, and a `requirements.txt` file for dependency management.

---

## Folder Structure

Below is the organized folder structure of this repository:

```plaintext
.
├── configs
│   └── config.json          # Contains settings for Alpha Vantage API and DAG configurations
├── dags
│   └── stock_market.py      # Airflow DAG to retrieve stock market data
├── plugins
│   ├── __init__.py          # Initializes the plugin
│   └── alpha_vantage_download.py  # Module for interacting with Alpha Vantage API
├── requirements
│   └── requirements.txt     # Python dependencies required for the project
├── startup_script
│   └── example_startup.sh   # Example startup script for setting up the environment
├── .gitignore               # Files and folders to exclude from version control
└── README.md                # Project documentation
```

---

## Features

- **Automated Financial Data Retrieval**  
  Easily fetch financial data such as stock prices, forex rates, and cryptocurrency values.
  
- **AWS MWAA Integration**  
  Seamlessly integrates with AWS Managed Workflows for Apache Airflow (MWAA).
  
- **Configurable and Modular Design**  
  Provides flexibility to adjust settings for your specific requirements.

---

## Installation

Follow these steps to install and set up the project:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/mwaa-alpha-vantage-dags.git
   cd mwaa-alpha-vantage-dags
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements/requirements.txt
   ```

3. If testing locally, refer to the [aws-mwaa-local-runner](https://github.com/aws/aws-mwaa-local-runner) for setting up a local MWAA environment.

---

## Usage

To use the provided DAGs with MWAA:

1. **Upload DAGs and Plugins**  
   Upload the contents of the `dags` and `plugins` directories to the S3 bucket associated with your MWAA environment.

2. **Set Environment Variables**  
   Configure the Alpha Vantage API key as an environment variable in MWAA. Alternatively, use AWS Secrets Manager for enhanced security.

3. **Trigger DAGs**  
   - Use the Airflow UI or CLI to trigger DAGs manually.  
   - Alternatively, schedule the DAGs for periodic execution.

4. **Monitor Execution**  
   Monitor the execution of the DAGs using the Airflow UI.

---

## Configuration

Here’s how to configure the project:

1. **Alpha Vantage API Key**  
   Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and set it in the MWAA environment as an environment variable (e.g., `ALPHA_VANTAGE_API_KEY`).

2. **DAG Parameters**  
   Customize the DAG settings (e.g., schedule intervals and data parameters) in the `stock_market.py` file.

3. **Config File**  
   Edit `config.json` in the `configs` folder to set API endpoints, symbols, and other data-specific configurations.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
