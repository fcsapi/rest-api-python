"""
FCS API - Crypto Module

@package FcsApi
@author FCS API <support@fcsapi.com>
"""

from typing import Dict, Optional, Any, List


class FcsCrypto:
    """Crypto API Module"""

    def __init__(self, api):
        """
        Initialize Crypto module

        Args:
            api: FcsApi instance
        """
        self._api = api
        self._base = 'crypto/'

    # ==================== Symbol List ====================

    def get_symbols_list(self, type: Optional[str] = 'crypto', sub_type: Optional[str] = None,
                         exchange: Optional[str] = None) -> Optional[Dict]:
        """
        Get list of all crypto symbols

        Args:
            type: Filter: crypto, coin, futures, dex, dominance
            sub_type: Filter: spot, swap, index
            exchange: Filter by exchange: BINANCE, COINBASE

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

    def get_coins_list(self) -> Optional[Dict]:
        """
        Get list of all coins (with market cap, rank, supply data)

        Returns:
            API response or None
        """
        return self.get_symbols_list('coin')

    # ==================== Latest Prices ====================

    def get_latest_price(self, symbol: str, period: str = '1D', type: Optional[str] = None,
                         exchange: Optional[str] = None, get_profile: bool = False) -> Optional[Dict]:
        """
        Get latest prices

        Args:
            symbol: Symbol(s): BTCUSDT,ETHUSDT or BINANCE:BTCUSDT
            period: Time period: 1m,5m,15m,30m,1h,4h,1D,1W,1M
            type: crypto or coin
            exchange: Exchange name (BINANCE, COINBASE)
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
            exchange: Exchange: BINANCE, COINBASE, KRAKEN
            period: Time period
            type: crypto or coin

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

    # ==================== Coin Data (Rank, Market Cap, Supply) ====================

    def get_coin_data(self, symbol: Optional[str] = None, limit: int = 100,
                      sort_by: str = 'perf.rank_asc') -> Optional[Dict]:
        """
        Get coin data with rank, market cap, supply, performance
        Note: Only works with type=coin (BTCUSD, ETHUSD, etc.)

        Args:
            symbol: Coin symbol: BTCUSD, ETHUSD (optional)
            limit: Number of results
            sort_by: Sort by: rank_asc, market_cap_desc, circulating_supply_desc

        Returns:
            API response or None
        """
        params = {
            'type': 'coin',
            'sort_by': sort_by,
            'per_page': limit,
            'merge': 'latest,perf'
        }
        if symbol:
            params['symbol'] = symbol

        return self._api.request(self._base + 'advance', params)

    def get_top_by_market_cap(self, limit: int = 100) -> Optional[Dict]:
        """
        Get top coins by market cap

        Args:
            limit: Number of results

        Returns:
            API response or None
        """
        return self.get_coin_data(None, limit, 'perf.market_cap_desc')

    def get_top_by_rank(self, limit: int = 100) -> Optional[Dict]:
        """
        Get top coins by rank

        Args:
            limit: Number of results

        Returns:
            API response or None
        """
        return self.get_coin_data(None, limit, 'perf.rank_asc')

    # ==================== Crypto Converter ====================

    def convert(self, pair1: str, pair2: str, amount: float = 1) -> Optional[Dict]:
        """
        Crypto converter (crypto to fiat or crypto to crypto)

        Args:
            pair1: From: BTC, ETH
            pair2: To: USD, EUR, BTC
            amount: Amount to convert

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'converter', {
            'pair1': pair1,
            'pair2': pair2,
            'amount': amount
        })

    # ==================== Base Currency ====================

    def get_base_prices(self, symbol: str, exchange: Optional[str] = None,
                        fallback: bool = False) -> Optional[Dict]:
        """
        Get base currency prices (USD to all cryptos, BTC to all)
        Symbol accepts only single token: BTC, ETH, USD (not BTCUSDT)

        Args:
            symbol: Single currency: BTC, ETH, USD
            exchange: Exchange filter
            fallback: If pair not found, fetch from other exchanges

        Returns:
            API response or None
        """
        params = {'symbol': symbol}
        if exchange:
            params['exchange'] = exchange
        if fallback:
            params['fallback'] = 1

        return self._api.request(self._base + 'base_latest', params)

    # ==================== Cross Currency ====================

    def get_cross_rates(self, symbol: str, exchange: Optional[str] = None, type: str = 'crypto',
                        period: str = '1D', crossrates: bool = False, fallback: bool = False) -> Optional[Dict]:
        """
        Get cross currency rates with OHLC data
        Returns all pairs of base currency (USD -> USDBTC, USDETH, etc.)

        Args:
            symbol: Single currency: USD, BTC, ETH
            exchange: Exchange filter
            type: crypto or forex
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
            symbol: Single symbol: BINANCE:BTCUSDT or BTCUSDT
            period: Time period: 1m,5m,15m,1h,1D
            length: Number of candles (max 10000)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
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
        Get coin profile details (name, website, social links, etc.)

        Args:
            symbol: Coin symbol: BTC,ETH,SOL (not pairs)

        Returns:
            API response or None
        """
        return self._api.request(self._base + 'profile', {'symbol': symbol})

    # ==================== Exchanges ====================

    def get_exchanges(self, type: Optional[str] = None, sub_type: Optional[str] = None) -> Optional[Dict]:
        """
        Get available exchanges

        Args:
            type: crypto, coin, futures, dex
            sub_type: spot, swap

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
                - type: crypto, coin, futures, dex
                - symbol: BTCUSDT,ETHUSDT
                - exchange: BINANCE,COINBASE
                - period: 1D
                - merge: latest,perf,tech,profile,meta
                - sort_by: active.chp_desc, rank_asc, market_cap_desc
                - filters: {"active.c_gt":50000}
                - per_page: 200
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
            symbol: Symbol(s): BTCUSDT or BINANCE:BTCUSDT
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
            symbol: Symbol(s): BTCUSDT
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
            symbol: Symbol(s): BTCUSDT
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
            symbol: Symbol(s): BTCUSDT
            exchange: Exchange filter

        Returns:
            API response or None
        """
        params = {'symbol': symbol}
        if exchange:
            params['exchange'] = exchange

        return self._api.request(self._base + 'performance', params)

    # ==================== Top Movers ====================

    def get_top_gainers(self, exchange: Optional[str] = None, limit: int = 20,
                        period: str = '1D', type: str = 'crypto') -> Optional[Dict]:
        """
        Get top gainers

        Args:
            exchange: Exchange filter: BINANCE, COINBASE
            limit: Number of results
            period: Time period
            type: crypto or coin

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'desc', limit, type, exchange, period)

    def get_top_losers(self, exchange: Optional[str] = None, limit: int = 20,
                       period: str = '1D', type: str = 'crypto') -> Optional[Dict]:
        """
        Get top losers

        Args:
            exchange: Exchange filter
            limit: Number of results
            period: Time period
            type: crypto or coin

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.chp', 'asc', limit, type, exchange, period)

    def get_highest_volume(self, exchange: Optional[str] = None, limit: int = 20,
                           period: str = '1D', type: str = 'crypto') -> Optional[Dict]:
        """
        Get highest volume coins

        Args:
            exchange: Exchange filter
            limit: Number of results
            period: Time period
            type: crypto or coin

        Returns:
            API response or None
        """
        return self.get_sorted_data('active.v', 'desc', limit, type, exchange, period)

    # ==================== Custom Sorting ====================

    def get_sorted_data(self, sort_column: str, sort_direction: str = 'desc', limit: int = 20,
                        type: Optional[str] = 'crypto', exchange: Optional[str] = None,
                        period: str = '1D') -> Optional[Dict]:
        """
        Get data with custom sorting
        User can specify any column and sort direction

        Args:
            sort_column: Column to sort: active.c, active.chp, active.v, active.h, active.l, rank, market_cap
            sort_direction: Sort direction: asc or desc
            limit: Number of results
            type: crypto, coin, futures, dex
            exchange: Exchange filter: BINANCE, COINBASE
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

        return self._api.request(self._base + 'advance', params)

    # ==================== Search ====================

    def search(self, query: str, type: Optional[str] = None) -> Optional[Dict]:
        """
        Search coins/tokens

        Args:
            query: Search term (BTC, ethereum, doge)
            type: crypto, coin, futures, dex

        Returns:
            API response or None
        """
        params = {'search': query}
        if type:
            params['type'] = type

        return self._api.request(self._base + 'list', params)

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
