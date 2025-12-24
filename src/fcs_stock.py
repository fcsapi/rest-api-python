"""
FCS API - Stock Module

@package FcsApi
@author FCS API <support@fcsapi.com>
"""

from typing import Dict, Optional, Any, List


class FcsStock:
    """Stock API Module"""

    def __init__(self, api):
        """
        Initialize Stock module

        Args:
            api: FcsApi instance
        """
        self._api = api
        self._base = 'stock/'

    # ==================== Symbol/Stock List ====================

    def get_symbols_list(self, exchange: Optional[str] = None, country: Optional[str] = None,
                         sector: Optional[str] = None, indices: Optional[str] = None) -> Optional[Dict]:
        """
        Get list of all stock symbols

        Args:
            exchange: Filter by exchange: NASDAQ, NYSE, BSE
            country: Filter by country: united-states, japan, india
            sector: Filter by sector: technology, finance, energy
            indices: Filter by indices: DJ:DJI, NASDAQ:IXIC

        Returns:
            API response or None
        """
        params = {}
        if exchange:
            params['exchange'] = exchange
        if country:
            params['country'] = country
        if sector:
            params['sector'] = sector
        if indices:
            params['indices'] = indices

        return self._api.request(self._base + 'list', params)

    # ==================== Indices ====================

    def get_indices_list(self, country: Optional[str] = None, exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get list of market indices by country

        Args:
            country: Country name: united-states, japan
            exchange: Exchange filter: nasdaq, nyse

        Returns:
            API response or None
        """
        params = {}
        if country:
            params['country'] = country
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'indices', params)

    def get_indices_latest(self, symbol: Optional[str] = None, country: Optional[str] = None,
                           exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get latest index prices

        Args:
            symbol: Index symbol(s): NASDAQ:NDX, SP:SPX
            country: Country filter
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        if country:
            params['country'] = country
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'indices_latest', params)

    # ==================== Latest Prices ====================

    def get_latest_price(self, symbol: str, period: str = '1D', exchange: Optional[str] = None,
                         get_profile: bool = False) -> Optional[Dict]:
        """
        Get latest stock prices

        Args:
            symbol: Symbol(s): AAPL,GOOGL or NASDAQ:AAPL
            period: Time period: 1m,5m,15m,30m,1h,4h,1D,1W,1M
            exchange: Exchange name
            get_profile: Include profile info

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period,
            'get_profile': 1 if get_profile else 0
        }
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'latest', params)

    def get_all_prices(self, exchange: str, period: str = '1D') -> Optional[Dict]:
        """
        Get all latest prices by exchange

        Args:
            exchange: Exchange: NASDAQ, NYSE, LSE
            period: Time period

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'latest', {
            'exchange': exchange,
            'period': period
        })

    def get_latest_by_country(self, country: str, sector: Optional[str] = None,
                              period: str = '1D') -> Optional[Dict]:
        """
        Get latest prices by country and sector

        Args:
            country: Country: united-states, japan
            sector: Sector: technology, finance
            period: Time period

        Returns:
            API response or None
        """
        params = {
            'country': country,
            'period': period
        }
        if sector:
            params['sector'] = sector

        return self._api.request(self._base + 'latest', params)

    def get_latest_by_indices(self, indices: str, period: str = '1D') -> Optional[Dict]:
        """
        Get latest prices by indices

        Args:
            indices: Indices IDs: NASDAQ:NDX, SP:SPX
            period: Time period

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'latest', {
            'indices': indices,
            'period': period
        })

    # ==================== Historical Data ====================

    def get_history(self, symbol: str, period: str = '1D', length: int = 300,
                    from_date: Optional[str] = None, to_date: Optional[str] = None,
                    page: int = 1, is_chart: bool = False) -> Optional[Dict]:
        """
        Get historical prices (works for stocks and indices)

        Args:
            symbol: Single symbol: AAPL or NASDAQ:AAPL
            period: Time period
            length: Number of candles (max 10000)
            from_date: Start date
            to_date: End date
            page: Page number for pagination
            is_chart: Return chart-friendly format

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period,
            'length': length,
            'page': page
        }
        if from_date:
            params['from'] = from_date
        if to_date:
            params['to'] = to_date
        if is_chart:
            params['is_chart'] = 1

        return self._api.request(self._base + 'history', params)

    # ==================== Profile ====================

    def get_profile(self, symbol: str) -> Optional[Dict]:
        """
        Get stock profile/company details

        Args:
            symbol: Stock symbol: AAPL,GOOGL or NASDAQ:AAPL

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'profile', {'symbol': symbol})

    # ==================== Exchanges ====================

    def get_exchanges(self, type: Optional[str] = None, sub_type: Optional[str] = None) -> Optional[Dict]:
        """
        Get available exchanges

        Args:
            type: Filter: stock, all_stock
            sub_type: Filter: equity, etf

        Returns:
            API response or None
        """
        params = {}
        if type:
            params['type'] = type
        if sub_type:
            params['sub_type'] = sub_type

        return self._api.request(self._base + 'exchanges', params)

    # ==================== Financial Data ====================

    def get_earnings(self, symbol: str, duration: str = 'both') -> Optional[Dict]:
        """
        Get earnings data (EPS, Revenue)

        Args:
            symbol: Stock symbol: NASDAQ:AAPL (can be multiple comma-separated)
            duration: Filter: annual, interim, both

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'earnings', {
            'symbol': symbol,
            'duration': duration
        })

    def get_revenue(self, symbol: str) -> Optional[Dict]:
        """
        Get revenue segmentation data (by business and region)

        Args:
            symbol: Stock symbol: NASDAQ:AAPL (can be multiple comma-separated)

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'revenue', {'symbol': symbol})

    def get_dividends(self, symbol: str, format: str = 'plain') -> Optional[Dict]:
        """
        Get dividends data (payment dates, amounts, yield)

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            format: Response format: plain (default), inherit (nested array)

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'dividend', {
            'symbol': symbol,
            'format': format
        })

    def get_balance_sheet(self, symbol: str, duration: str = 'annual', format: str = 'plain') -> Optional[Dict]:
        """
        Get balance sheet data

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            duration: annual, interim
            format: Response format: plain, inherit

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'balance_sheet', {
            'symbol': symbol,
            'duration': duration,
            'format': format
        })

    def get_income_statements(self, symbol: str, duration: str = 'annual', format: str = 'plain') -> Optional[Dict]:
        """
        Get income statement data

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            duration: annual, interim
            format: Response format: plain, inherit

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'income_statements', {
            'symbol': symbol,
            'duration': duration,
            'format': format
        })

    def get_cash_flow(self, symbol: str, duration: str = 'annual', format: str = 'plain') -> Optional[Dict]:
        """
        Get cash flow statement data

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            duration: annual, interim
            format: Response format: plain, inherit

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'cash_flow', {
            'symbol': symbol,
            'duration': duration,
            'format': format
        })

    def get_statistics(self, symbol: str, duration: str = 'annual') -> Optional[Dict]:
        """
        Get stock statistics and financial ratios

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            duration: annual, interim

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'statistics', {
            'symbol': symbol,
            'duration': duration
        })

    def get_forecast(self, symbol: str) -> Optional[Dict]:
        """
        Get price target forecast from analysts

        Args:
            symbol: Stock symbol: NASDAQ:AAPL

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'forecast', {'symbol': symbol})

    def get_stock_data(self, symbol: str, data_column: str = 'profile,earnings,dividends',
                       duration: str = 'annual', format: str = 'plain') -> Optional[Dict]:
        """
        Get combined financial data (multiple endpoints in one call)

        Args:
            symbol: Stock symbol: NASDAQ:AAPL
            data_column: Comma-separated: earnings,revenue,profile,dividends,balance_sheet,income_statements,statistics,cash_flow
            duration: annual, interim
            format: Response format: plain, inherit

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'stock_data', {
            'symbol': symbol,
            'data_column': data_column,
            'duration': duration,
            'format': format
        })

    # ==================== Technical Analysis ====================

    def get_moving_averages(self, symbol: str, period: str = '1D') -> Optional[Dict]:
        """
        Get Moving Averages (EMA & SMA)

        Args:
            symbol: Symbol: NASDAQ:AAPL
            period: Time period

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'ma_avg', {
            'symbol': symbol,
            'period': period
        })

    def get_indicators(self, symbol: str, period: str = '1D') -> Optional[Dict]:
        """
        Get Technical Indicators (RSI, MACD, Stochastic, ADX, ATR, etc.)

        Args:
            symbol: Symbol: NASDAQ:AAPL
            period: Time period

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'indicators', {
            'symbol': symbol,
            'period': period
        })

    def get_pivot_points(self, symbol: str, period: str = '1D') -> Optional[Dict]:
        """
        Get Pivot Points

        Args:
            symbol: Symbol: NASDAQ:AAPL
            period: Time period

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'pivot_points', {
            'symbol': symbol,
            'period': period
        })

    # ==================== Performance ====================

    def get_performance(self, symbol: str) -> Optional[Dict]:
        """
        Get Performance Data (historical highs/lows, percentage changes, volatility)

        Args:
            symbol: Symbol: NASDAQ:AAPL

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'performance', {'symbol': symbol})

    # ==================== Advanced Query ====================

    def advanced(self, params: Dict) -> Optional[Dict]:
        """
        Advanced query with filters, sorting, pagination, merging

        Args:
            params: Query parameters:
                - type: stock, index
                - symbol: AAPL,GOOGL
                - exchange: NASDAQ,NYSE
                - country: united-states
                - sector: technology
                - period: 1D
                - merge: latest,perf,tech,profile,meta
                - sort_by: active.chp_desc
                - filters: {"active.c_gt":100}
                - per_page: 200
                - page: 1

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'advance', params)

    # ==================== Top Movers ====================

    def get_top_gainers(self, exchange: Optional[str] = None, limit: int = 20,
                        period: str = '1D', country: Optional[str] = None) -> Optional[Dict]:
        """
        Get top gainers

        Args:
            exchange: Exchange filter: NASDAQ, NYSE
            limit: Number of results
            period: Time period
            country: Country filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'desc', limit, exchange, country, period)

    def get_top_losers(self, exchange: Optional[str] = None, limit: int = 20,
                       period: str = '1D', country: Optional[str] = None) -> Optional[Dict]:
        """
        Get top losers

        Args:
            exchange: Exchange filter
            limit: Number of results
            period: Time period
            country: Country filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'asc', limit, exchange, country, period)

    def get_most_active(self, exchange: Optional[str] = None, limit: int = 20,
                        period: str = '1D', country: Optional[str] = None) -> Optional[Dict]:
        """
        Get most active stocks by volume

        Args:
            exchange: Exchange filter
            limit: Number of results
            period: Time period
            country: Country filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.v', 'desc', limit, exchange, country, period)

    # ==================== Custom Sorting ====================

    def get_sorted_data(self, sort_column: str, sort_direction: str = 'desc', limit: int = 20,
                        exchange: Optional[str] = None, country: Optional[str] = None,
                        period: str = '1D') -> Optional[Dict]:
        """
        Get data with custom sorting
        User can specify any column and sort direction

        Args:
            sort_column: Column to sort: active.c, active.chp, active.v, active.h, active.l
            sort_direction: Sort direction: asc or desc
            limit: Number of results
            exchange: Exchange filter: NASDAQ, NYSE, LSE
            country: Country filter
            period: Time period

        Returns:
            API response or None
        """
        params = {
            'period': period,
            'sort_by': f'{sort_column}_{sort_direction}',
            'per_page': limit,
            'merge': 'latest'
        }
        if exchange:
            params['exchange'] = exchange
        if country:
            params['country'] = country

        return self.advanced(params)

    # ==================== Search ====================

    def search(self, query: str, exchange: Optional[str] = None, country: Optional[str] = None) -> Optional[Dict]:
        """
        Search stocks

        Args:
            query: Search term
            exchange: Exchange filter
            country: Country filter

        Returns:
            API response or None
        """
        params = {'search': query}
        if exchange:
            params['exchange'] = exchange
        if country:
            params['country'] = country

        return self._api.request(self._base + 'list', params)

    # ==================== Filter by Sector/Country ====================

    def get_by_sector(self, sector: str, limit: int = 100, exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get stocks by sector

        Args:
            sector: Sector: technology, finance, energy, healthcare
            limit: Number of results
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {
            'sector': sector,
            'per_page': limit,
            'merge': 'latest'
        }
        if exchange:
            params['exchange'] = exchange

        return self.advanced(params)

    def get_by_country(self, country: str, limit: int = 100, exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get stocks by country

        Args:
            country: Country: united-states, japan, india
            limit: Number of results
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {
            'country': country,
            'per_page': limit,
            'merge': 'latest'
        }
        if exchange:
            params['exchange'] = exchange

        return self.advanced(params)

    # ==================== Multiple/Parallel Requests ====================

    def multi_url(self, urls: List[str], base: Optional[str] = None) -> Optional[Dict]:
        """
        Execute multiple API requests in parallel

        Args:
            urls: Array of API endpoints
            base: Common URL base

        Returns:
            API response or None
        """
        params = {'url': urls}
        if base:
            params['base'] = base

        return self._api.request(self._base + 'multi_url', params)
