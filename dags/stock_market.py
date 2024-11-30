
# This import is only this local setup
import sys

# Import necessary modules

import os
import requests
import json
import asyncio
import boto3
import logging


# This import is only this local setup
# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airflow.decorators import dag, task
from airflow.sensors.base import PokeReturnValue
from airflow.hooks.base import BaseHook 
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.alpha_vantage_download import AlphaVantageClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the DAG with a start date, schedule, and tags
@dag(
    start_date=datetime(2024, 9, 1),
    schedule=None,
    catchup=False,
    tags=['stock_prizes']
)
def stock_market():

    # Define a sensor task to check if the API is available
    @task.sensor(poke_interval=10, timeout=1000, mode="poke")
    def is_api_available() -> PokeReturnValue:
        try:
            # Get the API connection details from Airflow's connection manager
            api = BaseHook.get_connection("stock_api")
            # Construct the URL using the connection details
            url = f"{api.host}{api.extra_dejson['endpoint']}"
            logger.info(f"Checking API availability at URL: {url}")
            # Make a GET request to the API
            response = requests.get(url, headers=api.extra_dejson['headers'])
            logger.info(f"API response status code: {response.status_code}")
            # Check if the response status code is 200 (OK)
            condition = response.status_code == 200
        except requests.RequestException as e:
            # Log the exception and set the condition to False
            logger.error(f"Error occurred while checking API availability: {e}")
            condition = False
        # Return the result of the check
        return PokeReturnValue(is_done=condition, xcom_value=url if condition else None)
    
    # Define the async function to fetch data
    async def _fetch_stock_data(api_key: str, symbol: str):
        client = AlphaVantageClient(api_key)
        return await client.get_time_series_daily_adjusted(symbol)
    
    # Define the async function to fetch all data
    async def fetch_all_data(api_key: str, symbols: list):
        stock_data = {}
        delay = 60 / 75  # Calculate the delay between API calls
        for symbol in symbols:
            logger.info(f"Fetching data for symbol: {symbol}")
            stock_data[symbol] = await _fetch_stock_data(api_key, symbol)
            await asyncio.sleep(delay)  # Introduce delay to respect rate limit
        return stock_data
    
    # Define the synchronous wrapper function
    def fetch_and_save_stock_prices():
        # Load the API key from environment variables
        api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        if not api_key:
            raise ValueError("API key not found in in environment variables")
        
        # Load the BUCKET name from environment variables
        av_bucket_name = os.getenv("AV_BUCKET_NAME")
        if not av_bucket_name:
            raise ValueError("BUCKET av name not found in environment variables")
        
        # Load the BUCKET name from environment variables
        mwaa_bucket_name = os.getenv("MWAA_BUCKET_NAME")
        if not mwaa_bucket_name:
            raise ValueError("BUCKET mwaa name not found in environment variables")
        
        # Load the CONFIG file path from environment variables
        config_file_path = os.getenv("CONFIG_FILE_PATH")
        if not config_file_path:
            raise ValueError("CONFIG file path not found in environment variables")
        

        logger.info(f"Downloading config file from s3://{mwaa_bucket_name}/{config_file_path}")
        # Download the config file from S3
        s3_client = boto3.client('s3')
        try:
            config_object = s3_client.get_object(Bucket=mwaa_bucket_name, Key=config_file_path)
            config_content = config_object['Body'].read().decode('utf-8')
            config = json.loads(config_content)
        except s3_client.exceptions.NoSuchKey:
            logger.error(f"The specified key does not exist: s3://{mwaa_bucket_name}/{config_file_path}")
            raise
        symbols = config.get("symbols", [])
     

        # Run the async function using asyncio.run
        stock_data = asyncio.run(fetch_all_data(api_key, symbols))
        
        # Parse and save data to S3
        s3_client = boto3.client('s3')
        for symbol, data in stock_data.items():
            # Extract metadata and timeseries data
            metadata = data.get('Meta Data', {})
            timeseries = data.get('Time Series (Daily)', {})
            
            # Convert the metadata and timeseries to JSON strings
            metadata_json = json.dumps(metadata)
            timeseries_json = json.dumps(timeseries)
            
            # Define the S3 keys (paths) for the files
            metadata_key = f"raw/{symbol}/timeseries/{symbol}_price_metadata.json"
            timeseries_key = f"raw/{symbol}/timeseries/{symbol}_price_data.json"
            
            # Upload the metadata and timeseries data to S3
            s3_client.put_object(Bucket=av_bucket_name, Key=metadata_key, Body=metadata_json)
            s3_client.put_object(Bucket=av_bucket_name, Key=timeseries_key, Body=timeseries_json)
            logger.info(f"Saved metadata for {symbol} to s3://{av_bucket_name}/{metadata_key}")
            logger.info(f"Saved timeseries data for {symbol} to s3://{av_bucket_name}/{timeseries_key}")
        
        # Log the ETL process
        log_key = f"logs/etl_log_{datetime.now().strftime('%Y-%m-%d')}.txt"
        log_content = "\n".join([f"Fetched and saved data for {symbol}" for symbol in symbols])
        s3_client.put_object(Bucket=av_bucket_name, Key=log_key, Body=log_content)
        logger.info(f"Saved ETL log to s3://{av_bucket_name}/{log_key}")
    
    # Define the PythonOperator
    fetch_and_save_stock_prices_task = PythonOperator(
        task_id='fetch_and_save_stock_prices',
        python_callable=fetch_and_save_stock_prices
    )
    
    # Define task dependencies
    is_api_available() >> fetch_and_save_stock_prices_task

stock_market()