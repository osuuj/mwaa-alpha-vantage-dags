#!/bin/sh

export ALPHA_VANTAGE_API_KEY=<put_value>
export AV_BUCKET_NAME=<put_value>
export AIRFLOW_BUCKET_NAME=<put_value>
export CONFIG_FILE_PATH=<put_value>
# This is only for this local setup
export PYTHONPATH=/path/to/dags:$PYTHONPATH