# FCS API - Python REST Client

**Python** REST API client library for **Forex**, **Cryptocurrency**, and **Stock** market data from [FCS API](https://fcsapi.com).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D3.7-blue.svg)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/fcsapi-rest.svg)](https://pypi.org/project/fcsapi-rest/)

## Features

- **Forex API** - 4000+ currency pairs, real-time rates, commodities, historical data, technical analysis
- **Crypto API** - 50,000+ coins from major exchanges (Binance, Coinbase, etc.), market cap, rank, coin data
- **Stock API** - 125,000+ global stocks, indices, earnings, financials, dividends
- **Easy to Use** - Simple method calls for all API endpoints
- **Multiple Auth Methods** - API key, IP whitelist, or secure token-based authentication

## Installation

### pip (Recommended)
```bash
pip install fcsapi-rest
```

### Examples

To download example files, clone the repository:

```bash
git clone https://github.com/fcsapi/rest-api-python
cd rest-api-python/examples
python forex_example.py
```

### Manual Installation
1. Download or clone this repository
2. Install dependencies: `pip install requests`
3. Import the library

```python
from src import FcsApi
```

## Quick Start

```python
from src import FcsApi

fcsapi = FcsApi()

# Forex
response = fcsapi.forex.get_latest_price('EURUSD')

# Crypto
response = fcsapi.crypto.get_latest_price('BINANCE:BTCUSDT')

# Stock
response = fcsapi.stock.get_latest_price('NASDAQ:AAPL')
```

---

## Usage Examples

### Example 1: Simple Price Check

```python
from src import FcsApi

fcsapi = FcsApi()

# Get EUR/USD price
response = fcsapi.forex.get_latest_price('EURUSD')

if fcsapi.is_success():
    data = response['response'][0]
    print(f"EUR/USD: {data['active']['c']}")
    print(f"Change: {data['active']['chp']}%")
else:
    print(f"Error: {fcsapi.get_error()}")
```

### Example 2: Currency Converter

```python
from src import FcsApi

fcsapi = FcsApi()

# Forex: Convert 1000 EUR to USD
response = fcsapi.forex.convert('EUR', 'USD', 1000)
if fcsapi.is_success():
    data = response['response']
    print(f"1000 EUR = {data['total']} USD")

# Crypto: Convert 1 BTC to USD
response = fcsapi.crypto.convert('BTC', 'USD', 1)
if fcsapi.is_success():
    data = response['response']
    print(f"1 BTC = ${data['total']:,.2f} USD")
```

### Example 3: Multiple Symbols with Error Handling

```python
from src import FcsApi

fcsapi = FcsApi()

# Get multiple forex pairs
symbols = ['EURUSD', 'GBPUSD', 'USDJPY']
response = fcsapi.forex.get_latest_price(','.join(symbols))

if fcsapi.is_success():
    for item in response['response']:
        symbol = item['ticker']
        price = item['active']['c']
        change = item['active']['chp']
        print(f"{symbol}: {price} ({change}%)")
else:
    print(f"Error: {fcsapi.get_error()}")
```

---

## Authentication Methods

The library supports 4 authentication methods for different security needs:

### Method 1: Default Configuration (Recommended)
Set your API key once in `src/fcs_config.py`:
```python
self.access_key = 'YOUR_API_KEY_HERE'
```
Then simply use:
```python
fcsapi = FcsApi()
```

### Method 2: Direct API Key
Pass API key directly (overrides config):
```python
fcsapi = FcsApi('YOUR_API_KEY')
```

### Method 3: IP Whitelist (No Key Required)
Whitelist your server IP at [FCS Dashboard](https://fcsapi.com/dashboard/profile):
```python
from src import FcsConfig

config = FcsConfig.with_ip_whitelist()
fcsapi = FcsApi(config)
```

### Method 4: Token-Based Authentication (Secure for Frontend)
Generate secure tokens on backend, use on frontend without exposing API key:
```python
from src import FcsConfig

# Backend: Generate token
config = FcsConfig.with_token('YOUR_API_KEY', 'YOUR_PUBLIC_KEY', 3600)
fcsapi = FcsApi(config)
token_data = fcsapi.generate_token()
# Returns: {'_token': '...', '_expiry': 1234567890, '_public_key': '...'}

# Send token_data to frontend for secure API calls
```

**Token Expiry Options:**
| Seconds | Duration |
|---------|----------|
| 300 | 5 minutes |
| 900 | 15 minutes |
| 1800 | 30 minutes |
| 3600 | 1 hour |
| 86400 | 24 hours |

## API Reference

### Forex API

```python
# ==================== Symbol List ====================
fcsapi.forex.get_symbols_list()                    # All symbols
fcsapi.forex.get_symbols_list('forex')             # Forex only
fcsapi.forex.get_symbols_list('commodity')         # Commodities only

# ==================== Latest Prices ====================
fcsapi.forex.get_latest_price('EURUSD')
fcsapi.forex.get_latest_price('EURUSD,GBPUSD,USDJPY')
fcsapi.forex.get_latest_price('EURUSD', '1D', None, True)  # with profile
fcsapi.forex.get_all_prices('FX')                  # All from exchange

# ==================== Commodities ====================
fcsapi.forex.get_commodities()                     # All commodities
fcsapi.forex.get_commodities('XAUUSD')            # Gold
fcsapi.forex.get_commodity_symbols()              # Commodity symbols list

# ==================== Currency Converter ====================
fcsapi.forex.convert('EUR', 'USD', 100)           # Convert 100 EUR to USD

# ==================== Base Currency ====================
fcsapi.forex.get_base_prices('USD')               # USD to all currencies

# ==================== Cross Rates ====================
fcsapi.forex.get_cross_rates('USD', 'forex', '1D')

# ==================== Historical Data ====================
fcsapi.forex.get_history('EURUSD')
fcsapi.forex.get_history('EURUSD', '1D', 500)
fcsapi.forex.get_history('EURUSD', '1h', 300, '2025-01-01', '2025-01-31')
fcsapi.forex.get_history('EURUSD', '1D', 300, None, None, 2)  # Page 2

# ==================== Profile ====================
fcsapi.forex.get_profile('EUR')
fcsapi.forex.get_profile('EUR,USD,GBP')

# ==================== Exchanges ====================
fcsapi.forex.get_exchanges()

# ==================== Technical Analysis ====================
fcsapi.forex.get_moving_averages('EURUSD', '1D')  # EMA & SMA
fcsapi.forex.get_indicators('EURUSD', '1D')       # RSI, MACD, Stochastic, etc.
fcsapi.forex.get_pivot_points('EURUSD', '1D')     # Pivot Points

# ==================== Performance ====================
fcsapi.forex.get_performance('EURUSD')            # Highs, lows, volatility

# ==================== Economy Calendar ====================
fcsapi.forex.get_economy_calendar()
fcsapi.forex.get_economy_calendar('US', '2025-01-01', '2025-01-31')

# ==================== Top Movers ====================
fcsapi.forex.get_top_gainers()
fcsapi.forex.get_top_losers()
fcsapi.forex.get_most_active()

# ==================== Search ====================
fcsapi.forex.search('EUR')

# ==================== Advanced Query ====================
fcsapi.forex.advanced({
    'type': 'forex',
    'period': '1D',
    'sort_by': 'active.chp_desc',
    'per_page': 50,
    'merge': 'latest,profile,tech'
})
```

### Crypto API

```python
# ==================== Symbol List ====================
fcsapi.crypto.get_symbols_list()                   # All crypto
fcsapi.crypto.get_symbols_list('crypto', 'binance') # Binance only
fcsapi.crypto.get_coins_list()                     # Coins with market cap

# ==================== Latest Prices ====================
fcsapi.crypto.get_latest_price('BTCUSDT')
fcsapi.crypto.get_latest_price('BINANCE:BTCUSDT,BINANCE:ETHUSDT')
fcsapi.crypto.get_all_prices('binance')

# ==================== Coin Data (Market Cap, Rank, Supply) ====================
fcsapi.crypto.get_coin_data()                      # Top coins with full data
fcsapi.crypto.get_top_by_market_cap(100)          # Top 100 by market cap
fcsapi.crypto.get_top_by_rank(50)                 # Top 50 by rank

# ==================== Crypto Converter ====================
fcsapi.crypto.convert('BTC', 'USD', 1)            # 1 BTC to USD
fcsapi.crypto.convert('ETH', 'BTC', 10)           # 10 ETH to BTC

# ==================== Base Currency ====================
fcsapi.crypto.get_base_prices('BTC')              # BTC to all
fcsapi.crypto.get_base_prices('USD')              # USD to all cryptos

# ==================== Cross Rates ====================
fcsapi.crypto.get_cross_rates('USD', 'crypto', '1D')

# ==================== Historical Data ====================
fcsapi.crypto.get_history('BINANCE:BTCUSDT')
fcsapi.crypto.get_history('BTCUSDT', '1D', 500)

# ==================== Profile ====================
fcsapi.crypto.get_profile('BTC')
fcsapi.crypto.get_profile('BTC,ETH,SOL')

# ==================== Exchanges ====================
fcsapi.crypto.get_exchanges()

# ==================== Technical Analysis ====================
fcsapi.crypto.get_moving_averages('BINANCE:BTCUSDT', '1D')
fcsapi.crypto.get_indicators('BINANCE:BTCUSDT', '1D')
fcsapi.crypto.get_pivot_points('BINANCE:BTCUSDT', '1D')

# ==================== Performance ====================
fcsapi.crypto.get_performance('BINANCE:BTCUSDT')

# ==================== Top Movers ====================
fcsapi.crypto.get_top_gainers()
fcsapi.crypto.get_top_gainers('binance', 50)
fcsapi.crypto.get_top_losers()
fcsapi.crypto.get_highest_volume()

# ==================== Search ====================
fcsapi.crypto.search('bitcoin')
```

### Stock API

```python
# ==================== Symbol List ====================
fcsapi.stock.get_symbols_list()                    # All stocks
fcsapi.stock.get_symbols_list('NASDAQ')           # NASDAQ only
fcsapi.stock.get_symbols_list(None, 'united-states') # US stocks
fcsapi.stock.get_symbols_list(None, None, 'technology') # Tech sector

# ==================== Indices ====================
fcsapi.stock.get_indices_list('united-states')    # US indices
fcsapi.stock.get_indices_latest()                 # All indices prices
fcsapi.stock.get_indices_latest('NASDAQ:NDX,SP:SPX') # Specific indices

# ==================== Latest Prices ====================
fcsapi.stock.get_latest_price('AAPL')
fcsapi.stock.get_latest_price('NASDAQ:AAPL,NASDAQ:GOOGL')
fcsapi.stock.get_all_prices('NASDAQ')
fcsapi.stock.get_latest_by_country('united-states', 'technology')
fcsapi.stock.get_latest_by_indices('NASDAQ:NDX')  # Stocks in NASDAQ 100

# ==================== Historical Data ====================
fcsapi.stock.get_history('NASDAQ:AAPL')
fcsapi.stock.get_history('AAPL', '1D', 500)

# ==================== Profile ====================
fcsapi.stock.get_profile('AAPL')
fcsapi.stock.get_profile('NASDAQ:AAPL,NASDAQ:GOOGL')

# ==================== Exchanges ====================
fcsapi.stock.get_exchanges()

# ==================== Financial Data ====================
fcsapi.stock.get_earnings('NASDAQ:AAPL')          # EPS, Revenue
fcsapi.stock.get_earnings('NASDAQ:AAPL', 'annual') # Annual only
fcsapi.stock.get_revenue('NASDAQ:AAPL')           # Revenue segments
fcsapi.stock.get_balance_sheet('NASDAQ:AAPL', 'annual')
fcsapi.stock.get_income_statements('NASDAQ:AAPL', 'annual')
fcsapi.stock.get_cash_flow('NASDAQ:AAPL', 'annual')
fcsapi.stock.get_dividends('NASDAQ:AAPL')         # Dividend history
fcsapi.stock.get_statistics('NASDAQ:AAPL')
fcsapi.stock.get_forecast('NASDAQ:AAPL')
fcsapi.stock.get_stock_data('NASDAQ:AAPL', 'profile,earnings,dividends')

# ==================== Technical Analysis ====================
fcsapi.stock.get_moving_averages('NASDAQ:AAPL', '1D')
fcsapi.stock.get_indicators('NASDAQ:AAPL', '1D')
fcsapi.stock.get_pivot_points('NASDAQ:AAPL', '1D')

# ==================== Performance ====================
fcsapi.stock.get_performance('NASDAQ:AAPL')

# ==================== Top Movers ====================
fcsapi.stock.get_top_gainers()
fcsapi.stock.get_top_gainers('NASDAQ', 50)
fcsapi.stock.get_top_losers()
fcsapi.stock.get_most_active()

# ==================== Search & Filter ====================
fcsapi.stock.search('Apple')
fcsapi.stock.get_by_sector('technology')
fcsapi.stock.get_by_country('united-states')

# ==================== Advanced Query ====================
fcsapi.stock.advanced({
    'exchange': 'NASDAQ',
    'sector': 'technology',
    'period': '1D',
    'sort_by': 'active.chp_desc',
    'per_page': 50,
    'merge': 'latest,profile'
})
```

## Response Handling

```python
response = fcsapi.forex.get_latest_price('EURUSD')

# Check if successful
if fcsapi.is_success():
    data = response['response']
    print(data)
else:
    print(f"Error: {fcsapi.get_error()}")

# Get last response info
last_response = fcsapi.get_last_response()

# Get response data only
data = fcsapi.get_response_data()
```

## Time Periods

Available timeframes for price data:

| Period | Description |
|--------|-------------|
| `1` or `1m` | 1 minute |
| `5` or `5m` | 5 minutes |
| `15` or `15m` | 15 minutes |
| `30` or `30m` | 30 minutes |
| `1h` or `60` | 1 hour |
| `4h` or `240` | 4 hours |
| `1D` | 1 day |
| `1W` | 1 week |
| `1M` | 1 month |

## Examples

### Forex Example
```python
from src import FcsApi

fcsapi = FcsApi()

# Get EUR/USD latest price
response = fcsapi.forex.get_latest_price('EURUSD')
if fcsapi.is_success():
    for item in response['response']:
        print(f"Symbol: {item['ticker']}")
        print(f"Price: {item['active']['c']}")
        print(f"Change: {item['active']['chp']}%")

# Convert 1000 EUR to USD
conversion = fcsapi.forex.convert('EUR', 'USD', 1000)
if fcsapi.is_success():
    print(f"1000 EUR = {conversion['response']['total']} USD")
```

### Crypto Example
```python
from src import FcsApi

fcsapi = FcsApi()

# Get Bitcoin price from Binance
response = fcsapi.crypto.get_latest_price('BINANCE:BTCUSDT')
if fcsapi.is_success():
    btc = response['response'][0]
    print(f"Bitcoin: ${btc['active']['c']:,.2f}")

# Get top 100 coins by market cap
coins = fcsapi.crypto.get_top_by_market_cap(100)
if fcsapi.is_success():
    for coin in coins['response']['data']:
        print(f"{coin['ticker']}: Rank #{coin['rank']}")
```

### Stock Example
```python
from src import FcsApi

fcsapi = FcsApi()

# Get Apple stock price
response = fcsapi.stock.get_latest_price('NASDAQ:AAPL')
if fcsapi.is_success():
    aapl = response['response'][0]
    print(f"Apple: ${aapl['active']['c']}")

# Get Apple earnings data
earnings = fcsapi.stock.get_earnings('NASDAQ:AAPL')
if fcsapi.is_success():
    print("EPS Data Available")

# Get US market indices
indices = fcsapi.stock.get_indices_latest(None, 'united-states')
if fcsapi.is_success():
    for index in indices['response']:
        print(f"{index['ticker']}: {index['active']['c']}")
```

## Get API Key

1. Visit [FCS API](https://fcsapi.com)
2. Sign up for a free account
3. Get your API key from the dashboard

## Documentation

For complete API documentation, visit:
- [Forex API Documentation](https://fcsapi.com/document/forex-api)
- [Crypto API Documentation](https://fcsapi.com/document/crypto-api)
- [Stock API Documentation](https://fcsapi.com/document/stock-api)

## Support

- Email: support@fcsapi.com
- Website: [fcsapi.com](https://fcsapi.com)

## License

MIT License - see [LICENSE](LICENSE) file for details.
