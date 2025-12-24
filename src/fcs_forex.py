"""
FCS API - Forex Module

@package FcsApi
@author FCS API <support@fcsapi.com>
"""

from typing import Dict, Optional, Any, List


class FcsForex:
    """Forex API Module"""

    def __init__(self, api):
        """
        Initialize Forex module

        Args:
            api: FcsApi instance
        """
        self._api = api
        self._base = 'forex/'

    # ==================== Symbol List ====================

    def get_symbols_list(self, type: Optional[str] = None, sub_type: Optional[str] = None,
                         exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get list of all forex symbols

        Args:
            type: Filter by type: forex, commodity
            sub_type: Filter: spot, synthetic
            exchange: Filter by exchange: FX, ONA, SFO, FCM

        Returns:
            API response or None
        """
        params = {}
        if type:
            params['type'] = type
        if sub_type:
            params['sub_type'] = sub_type
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'list', params)

    # ==================== Latest Prices ====================

    def get_latest_price(self, symbol: str, period: str = '1D', type: Optional[str] = None,
                         exchange: Optional[str] = None, get_profile: bool = False) -> Optional[Dict]:
        """
        Get latest prices for symbols

        Args:
            symbol: Symbol(s) comma-separated: EURUSD,GBPUSD or FX:EURUSD
            period: Time period: 1m,5m,15m,30m,1h,4h,1D,1W,1M
            type: forex or commodity
            exchange: Exchange name: FX, ONA, SFO
            get_profile: Include profile info

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period
        }
        if type:
            params['type'] = type
        if exchange:
            params['exchange'] = exchange
        if get_profile:
            params['get_profile'] = 1

        return self._api.request(self._base + 'latest', params)

    def get_all_prices(self, exchange: str, period: str = '1D', type: Optional[str] = None) -> Optional[Dict]:
        """
        Get all latest prices by exchange

        Args:
            exchange: Exchange name: FX, ONA, SFO
            period: Time period
            type: forex or commodity

        Returns:
            API response or None
        """
        params = {
            'exchange': exchange,
            'period': period
        }
        if type:
            params['type'] = type

        return self._api.request(self._base + 'latest', params)

    # ==================== Commodities ====================

    def get_commodities(self, symbol: Optional[str] = None, period: str = '1D') -> Optional[Dict]:
        """
        Get commodity prices (Gold, Silver, Oil, etc.)

        Args:
            symbol: Commodity symbol: XAUUSD, XAGUSD, USOIL, BRENT, NGAS
            period: Time period

        Returns:
            API response or None
        """
        params = {'type': 'commodity', 'period': period}
        if symbol:
            params['symbol'] = symbol

        return self._api.request(self._base + 'latest', params)

    def get_commodity_symbols(self) -> Optional[Dict]:
        """
        Get commodity symbols list

        Returns:
            API response or None
        """
        return self.get_symbols_list('commodity')

    # ==================== Currency Converter ====================

    def convert(self, pair1: str, pair2: str, amount: float = 1, type: Optional[str] = None) -> Optional[Dict]:
        """
        Currency converter

        Args:
            pair1: Currency From: EUR, USD
            pair2: Currency To: USD, GBP
            amount: Amount to convert
            type: forex or crypto

        Returns:
            API response or None
        """
        params = {
            'pair1': pair1,
            'pair2': pair2,
            'amount': amount
        }
        if type:
            params['type'] = type

        return self._api.request(self._base + 'converter', params)

    # ==================== Base Currency ====================

    def get_base_prices(self, symbol: str, type: str = 'forex', exchange: Optional[str] = None,
                        fallback: bool = False) -> Optional[Dict]:
        """
        Get base currency prices (USD to all currencies)
        Symbol accepts only single currency: USD, EUR, JPY (not USDJPY)

        Args:
            symbol: Single currency code: USD, EUR, JPY
            type: forex or crypto
            exchange: Exchange filter
            fallback: If not found, fetch from other exchanges

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'type': type
        }
        if exchange:
            params['exchange'] = exchange
        if fallback:
            params['fallback'] = 1

        return self._api.request(self._base + 'base_latest', params)

    # ==================== Cross Currency ====================

    def get_cross_rates(self, symbol: str, exchange: Optional[str] = None, type: str = 'forex',
                        period: str = '1D', crossrates: bool = False, fallback: bool = False) -> Optional[Dict]:
        """
        Get cross currency rates with OHLC data
        Returns all pairs of base currency (USD -> USDEUR, USDGBP, USDJPY, etc.)

        Args:
            symbol: Single currency: USD, EUR, JPY
            exchange: Exchange filter
            type: forex or crypto
            period: Time period
            crossrates: Return pairwise cross rates between multiple symbols
            fallback: If not found, fetch from other exchanges

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'type': type,
            'period': period
        }
        if exchange:
            params['exchange'] = exchange
        if crossrates:
            params['crossrates'] = 1
        if fallback:
            params['fallback'] = 1

        return self._api.request(self._base + 'cross', params)

    # ==================== Historical Data ====================

    def get_history(self, symbol: str, period: str = '1D', length: int = 300,
                    from_date: Optional[str] = None, to_date: Optional[str] = None,
                    page: int = 1, is_chart: bool = False) -> Optional[Dict]:
        """
        Get historical prices (OHLCV candles)

        Args:
            symbol: Single symbol: EURUSD or FX:EURUSD
            period: Time period: 1m,5m,15m,1h,1D
            length: Number of candles (max 10000)
            from_date: Start date (YYYY-MM-DD or unix)
            to_date: End date (YYYY-MM-DD or unix)
            page: Page number for pagination
            is_chart: Return chart-friendly format [timestamp,o,h,l,c,v]

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
        Get currency profile details (name, country, bank, etc.)

        Args:
            symbol: Currency codes: EUR,USD,GBP (not pairs)

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'profile', {'symbol': symbol})

    # ==================== Exchanges ====================

    def get_exchanges(self, type: Optional[str] = None, sub_type: Optional[str] = None) -> Optional[Dict]:
        """
        Get available exchanges/data sources

        Args:
            type: forex or commodity
            sub_type: spot, synthetic

        Returns:
            API response or None
        """
        params = {}
        if type:
            params['type'] = type
        if sub_type:
            params['sub_type'] = sub_type

        return self._api.request(self._base + 'exchanges', params)

    # ==================== Advanced Query ====================

    def advanced(self, params: Dict) -> Optional[Dict]:
        """
        Advanced query with filters, sorting, pagination, merging

        Args:
            params: Query parameters:
                - type: forex, commodity
                - symbol: EURUSD,GBPUSD
                - exchange: FX,ONA,SFO
                - period: 1D
                - merge: latest,perf,tech,profile,meta
                - sort_by: active.chp_desc, active.v_desc
                - filters: {"active.c_gt":1.1}
                - per_page: 200 (max 5000)
                - page: 1

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'advance', params)

    # ==================== Technical Analysis ====================

    def get_moving_averages(self, symbol: str, period: str = '1D', exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get Moving Averages (EMA & SMA)

        Args:
            symbol: Symbol(s): EURUSD or FX:EURUSD
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period
        }
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'ma_avg', params)

    def get_indicators(self, symbol: str, period: str = '1D', exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get Technical Indicators (RSI, MACD, Stochastic, ADX, ATR, etc.)

        Args:
            symbol: Symbol(s): EURUSD
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period
        }
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'indicators', params)

    def get_pivot_points(self, symbol: str, period: str = '1D', exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get Pivot Points (Classic, Fibonacci, Camarilla, Woodie, Demark)

        Args:
            symbol: Symbol(s): EURUSD
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {
            'symbol': symbol,
            'period': period
        }
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'pivot_points', params)

    # ==================== Performance ====================

    def get_performance(self, symbol: str, exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get Performance Data (historical highs/lows, percentage changes, volatility)

        Args:
            symbol: Symbol(s): EURUSD
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {'symbol': symbol}
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'performance', params)

    # ==================== Economy Calendar ====================

    def get_economy_calendar(self, symbol: Optional[str] = None, country: Optional[str] = None,
                             from_date: Optional[str] = None, to_date: Optional[str] = None) -> Optional[Dict]:
        """
        Get Economic Calendar Events

        Args:
            symbol: Filter by currency: USD, EUR, GBP
            country: Country filter: US, GB, DE, JP
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            API response or None
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        if country:
            params['country'] = country
        if from_date:
            params['from'] = from_date
        if to_date:
            params['to'] = to_date

        return self._api.request(self._base + 'economy_cal', params)

    # ==================== Top Movers ====================

    def get_top_gainers(self, type: str = 'forex', limit: int = 20, period: str = '1D',
                        exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get top gainers

        Args:
            type: forex or commodity
            limit: Number of results
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'desc', limit, type, exchange, period)

    def get_top_losers(self, type: str = 'forex', limit: int = 20, period: str = '1D',
                       exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get top losers

        Args:
            type: forex or commodity
            limit: Number of results
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'asc', limit, type, exchange, period)

    def get_most_active(self, type: str = 'forex', limit: int = 20, period: str = '1D',
                        exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get most active by volume

        Args:
            type: forex or commodity
            limit: Number of results
            period: Time period
            exchange: Exchange filter

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.v', 'desc', limit, type, exchange, period)

    # ==================== Custom Sorting ====================

    def get_sorted_data(self, sort_column: str, sort_direction: str = 'desc', limit: int = 20,
                        type: Optional[str] = 'forex', exchange: Optional[str] = None,
                        period: str = '1D') -> Optional[Dict]:
        """
        Get data with custom sorting
        User can specify any column and sort direction

        Args:
            sort_column: Column to sort: active.c, active.chp, active.v, active.h, active.l
            sort_direction: Sort direction: asc or desc
            limit: Number of results
            type: forex or commodity
            exchange: Exchange filter: FX, ONA, SFO
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
        if type:
            params['type'] = type
        if exchange:
            params['exchange'] = exchange

        return self.advanced(params)

    # ==================== Search ====================

    def search(self, query: str, type: Optional[str] = None, exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Search symbols

        Args:
            query: Search term (EUR, USD, gold)
            type: forex or commodity
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {'search': query}
        if type:
            params['type'] = type
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'search', params)

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
