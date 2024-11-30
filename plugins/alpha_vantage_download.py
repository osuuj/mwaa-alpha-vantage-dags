import aiohttp
from typing import Any, Dict

class AlphaVantageClient:
    def __init__(self, api_key: str) -> None:
        """
        Initialize the AlphaVantageClient with the provided API key.

        :param api_key: The API key for accessing Alpha Vantage.
        """
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query?'

    async def _fetch_data(self, session: aiohttp.ClientSession, function: str, **params: Any) -> Dict[str, Any]:
        """
        Fetch data from the Alpha Vantage API.

        :param session: The aiohttp ClientSession.
        :param function: The API function to call.
        :param params: Additional parameters for the API call.
        :return: The JSON response from the API as a dictionary.
        """
        params.update({'function': function, 'apikey': self.api_key})
        url = self.base_url + '&'.join([f'{key}={value}' for key, value in params.items()])
        async with session.get(url) as response:
            return await response.json()

    async def get_commodity_data(self, function: str, interval: str) -> Dict[str, Any]:
        """
        Get commodity data from the Alpha Vantage API.

        :param function: The API function to call.
        :param interval: The interval for the data.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, function, interval=interval)

    async def get_time_series_daily_adjusted(self, symbol: str, outputsize: str = 'full') -> Dict[str, Any]:
        """
        Get daily adjusted time series data for a symbol.

        :param symbol: The stock symbol to fetch data for.
        :param outputsize: The size of the data output ('compact' or 'full').
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'TIME_SERIES_DAILY_ADJUSTED', symbol=symbol, outputsize=outputsize)

    async def get_company_overview(self, symbol: str) -> Dict[str, Any]:
        """
        Get company overview data for a symbol.

        :param symbol: The stock symbol to fetch data for.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'OVERVIEW', symbol=symbol)

    async def get_income_statement(self, symbol: str) -> Dict[str, Any]:
        """
        Get income statement data for a symbol.

        :param symbol: The stock symbol to fetch data for.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'INCOME_STATEMENT', symbol=symbol)

    async def get_balance_sheet(self, symbol: str) -> Dict[str, Any]:
        """
        Get balance sheet data for a symbol.

        :param symbol: The stock symbol to fetch data for.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'BALANCE_SHEET', symbol=symbol)

    async def get_cash_flow(self, symbol: str) -> Dict[str, Any]:
        """
        Get cash flow data for a symbol.

        :param symbol: The stock symbol to fetch data for.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'CASH_FLOW', symbol=symbol)

    async def get_forex_data(self, from_symbol: str, to_symbol: str, outputsize: str) -> Dict[str, Any]:
        """
        Get the Forex data for specified currency pairs and output size.

        :param from_symbol: The base currency symbol.
        :param to_symbol: The quote currency symbol.
        :param outputsize: The size of the data output ('compact' or 'full').
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'FX_DAILY', from_symbol=from_symbol, to_symbol=to_symbol, outputsize=outputsize)

    async def get_digital_currency_data(self, symbol: str) -> Dict[str, Any]:
        """
        Get the digital currency data for a specified symbol.

        :param symbol: The digital currency symbol.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'DIGITAL_CURRENCY_DAILY', symbol=symbol, market='USD')

    async def get_treasury_yield_data(self, interval: str, maturity: str) -> Dict[str, Any]:
        """
        Get the treasury yield data for a specified interval and maturity.

        :param interval: The interval for the data ('daily', 'weekly', 'monthly').
        :param maturity: The maturity period for the data ('3month', '2year', '5year', '7year', '10year', '30year').
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'TREASURY_YIELD', interval=interval, maturity=maturity)
        
    async def search_symbol(self, keywords: str) -> Dict[str, Any]:
        """
        Search for a symbol using keywords.

        :param keywords: The keywords to search for.
        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'SYMBOL_SEARCH', keywords=keywords)

    async def get_unemployment_data(self) -> Dict[str, Any]:
        """
        Get the unemployment data.

        :return: The JSON response from the API as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, 'UNEMPLOYMENT')