# FCS API - Python Functions Reference

Quick reference for all available functions in the FCS API Python library.

---

## Authentication Methods

```python
from src import FcsApi, FcsConfig

# Method 1: Default (uses key from fcs_config.py)
fcsapi = FcsApi()

# Method 2: Pass API Key directly (override)
fcsapi = FcsApi('YOUR_API_KEY')

# Method 3: IP Whitelist (no key needed if IP whitelisted in account)
config = FcsConfig.with_ip_whitelist()
fcsapi = FcsApi(config)

# Method 4: Token-Based (secure for frontend apps)
config = FcsConfig.with_token('API_KEY', 'PUBLIC_KEY', 3600)
fcsapi = FcsApi(config)
token_data = fcsapi.generate_token()  # Send to frontend
```

### Set Default API Key
Edit `src/fcs_config.py` and set your key:
```python
self.access_key = 'YOUR_API_KEY_HERE'
```

### Token Expiry Values
| Seconds | Duration |
|---------|----------|
| 300 | 5 minutes |
| 900 | 15 minutes |
| 1800 | 30 minutes |
| 3600 | 1 hour |
| 86400 | 24 hours |

---

## Crypto Functions

```python
fcsapi.crypto.get_symbols_list(type, sub_type, exchange)
fcsapi.crypto.get_coins_list()
fcsapi.crypto.get_latest_price(symbol, period, type, exchange, get_profile)
fcsapi.crypto.get_all_prices(exchange, period, type)
fcsapi.crypto.get_coin_data(symbol, limit, sort_by)
fcsapi.crypto.get_top_by_market_cap(limit)
fcsapi.crypto.get_top_by_rank(limit)
fcsapi.crypto.convert(pair1, pair2, amount)
fcsapi.crypto.get_base_prices(symbol, exchange, fallback)
fcsapi.crypto.get_cross_rates(symbol, exchange, type, period, crossrates, fallback)
fcsapi.crypto.get_history(symbol, period, length, from_date, to_date, page, is_chart)
fcsapi.crypto.get_profile(symbol)
fcsapi.crypto.get_exchanges(type, sub_type)
fcsapi.crypto.advanced(params)
fcsapi.crypto.get_moving_averages(symbol, period, exchange)
fcsapi.crypto.get_indicators(symbol, period, exchange)
fcsapi.crypto.get_pivot_points(symbol, period, exchange)
fcsapi.crypto.get_performance(symbol, exchange)
fcsapi.crypto.get_top_gainers(exchange, limit, period, type)
fcsapi.crypto.get_top_losers(exchange, limit, period, type)
fcsapi.crypto.get_highest_volume(exchange, limit, period, type)
fcsapi.crypto.get_sorted_data(sort_column, sort_direction, limit, type, exchange, period)
fcsapi.crypto.search(query, type)
fcsapi.crypto.multi_url(urls, base)
```

### Parameters
| Parameter | Values |
|-----------|--------|
| `type` | crypto, coin, futures, dex, dominance |
| `sub_type` | spot, swap, index |
| `exchange` | BINANCE, COINBASE, KRAKEN, BYBIT |
| `period` | 1m, 5m, 15m, 30m, 1h, 4h, 1D, 1W, 1M |
| `sort_by` | perf.rank_asc, perf.market_cap_desc, perf.circulating_supply_desc |
| `sort_column` | active.c, active.chp, active.v, active.h, active.l, perf.rank, perf.market_cap |
| `sort_direction` | asc, desc |

---

## Forex Functions

```python
fcsapi.forex.get_symbols_list(type, sub_type, exchange)
fcsapi.forex.get_latest_price(symbol, period, type, exchange, get_profile)
fcsapi.forex.get_all_prices(exchange, period, type)
fcsapi.forex.get_commodities(symbol, period)
fcsapi.forex.get_commodity_symbols()
fcsapi.forex.convert(pair1, pair2, amount, type)
fcsapi.forex.get_base_prices(symbol, type, exchange, fallback)
fcsapi.forex.get_cross_rates(symbol, type, period, exchange, crossrates, fallback)
fcsapi.forex.get_history(symbol, period, length, from_date, to_date, page, is_chart)
fcsapi.forex.get_profile(symbol)
fcsapi.forex.get_exchanges(type, sub_type)
fcsapi.forex.advanced(params)
fcsapi.forex.get_moving_averages(symbol, period, exchange)
fcsapi.forex.get_indicators(symbol, period, exchange)
fcsapi.forex.get_pivot_points(symbol, period, exchange)
fcsapi.forex.get_performance(symbol, exchange)
fcsapi.forex.get_economy_calendar(symbol, country, from_date, to_date)
fcsapi.forex.get_top_gainers(type, limit, period, exchange)
fcsapi.forex.get_top_losers(type, limit, period, exchange)
fcsapi.forex.get_most_active(type, limit, period, exchange)
fcsapi.forex.get_sorted_data(sort_column, sort_direction, limit, type, exchange, period)
fcsapi.forex.search(query, type, exchange)
fcsapi.forex.multi_url(urls, base)
```

### Parameters
| Parameter | Values |
|-----------|--------|
| `type` | forex, commodity |
| `sub_type` | spot, synthetic |
| `exchange` | FX, ONA, SFO, FCM |
| `period` | 1m, 5m, 15m, 30m, 1h, 4h, 1D, 1W, 1M |
| `country` | US, GB, DE, JP, AU, CA |

---

## Stock Functions

```python
# Symbol/List
fcsapi.stock.get_symbols_list(exchange, country, sector, indices)
fcsapi.stock.search(query, exchange, country)

# Indices
fcsapi.stock.get_indices_list(country, exchange)
fcsapi.stock.get_indices_latest(symbol, country, exchange)

# Latest Prices
fcsapi.stock.get_latest_price(symbol, period, exchange, get_profile)
fcsapi.stock.get_all_prices(exchange, period)
fcsapi.stock.get_latest_by_country(country, sector, period)
fcsapi.stock.get_latest_by_indices(indices, period)

# Historical
fcsapi.stock.get_history(symbol, period, length, from_date, to_date, page, is_chart)

# Profile & Info
fcsapi.stock.get_profile(symbol)
fcsapi.stock.get_exchanges(type, sub_type)

# Financial Data
fcsapi.stock.get_earnings(symbol, duration)
fcsapi.stock.get_revenue(symbol)
fcsapi.stock.get_dividends(symbol, format)
fcsapi.stock.get_balance_sheet(symbol, duration, format)
fcsapi.stock.get_income_statements(symbol, duration, format)
fcsapi.stock.get_cash_flow(symbol, duration, format)
fcsapi.stock.get_statistics(symbol, duration)
fcsapi.stock.get_forecast(symbol)
fcsapi.stock.get_stock_data(symbol, data_column, duration, format)

# Technical Analysis
fcsapi.stock.get_moving_averages(symbol, period)
fcsapi.stock.get_indicators(symbol, period)
fcsapi.stock.get_pivot_points(symbol, period)
fcsapi.stock.get_performance(symbol)

# Top Movers & Sorting
fcsapi.stock.get_top_gainers(exchange, limit, period, country)
fcsapi.stock.get_top_losers(exchange, limit, period, country)
fcsapi.stock.get_most_active(exchange, limit, period, country)
fcsapi.stock.get_sorted_data(sort_column, sort_direction, limit, exchange, country, period)

# Filter
fcsapi.stock.get_by_sector(sector, limit, exchange)
fcsapi.stock.get_by_country(country, limit, exchange)

# Advanced
fcsapi.stock.advanced(params)
fcsapi.stock.multi_url(urls, base)
```

### Parameters
| Parameter | Values |
|-----------|--------|
| `type` | stock, index, fund, structured, dr |
| `sub_type` | spot, main, cfd, common, preferred |
| `exchange` | NASDAQ, NYSE, LSE, TSE, HKEX, BSE |
| `period` | 1m, 5m, 15m, 30m, 1h, 4h, 1D, 1W, 1M |
| `duration` | annual, interim, both |
| `format` | plain, inherit |
| `data_column` | earnings, revenue, profile, dividends, balance_sheet, income_statements, statistics, cash_flow |

---

## Common Response Fields

| Field | Description |
|-------|-------------|
| `o` | Open price |
| `h` | High price |
| `l` | Low price |
| `c` | Close/Current price |
| `v` | Volume |
| `t` | Unix timestamp |
| `ch` | Change amount |
| `chp` | Change percentage |

---

## Quick Examples

```python
# Initialize (uses key from fcs_config.py)
fcsapi = FcsApi()

# Crypto
fcsapi.crypto.get_latest_price('BINANCE:BTCUSDT')
fcsapi.crypto.get_history('BINANCE:BTCUSDT', '1D', 100)
fcsapi.crypto.get_coin_data(None, 50, 'perf.rank_asc')

# Forex
fcsapi.forex.get_latest_price('FX:EURUSD')
fcsapi.forex.convert('EUR', 'USD', 100)

# Stock
fcsapi.stock.get_latest_price('NASDAQ:AAPL')
fcsapi.stock.get_top_gainers('NASDAQ', 10)
fcsapi.stock.get_earnings('NASDAQ:AAPL', 'annual')
fcsapi.stock.get_dividends('NASDAQ:AAPL')
fcsapi.stock.get_balance_sheet('NASDAQ:AAPL', 'annual')
fcsapi.stock.get_stock_data('NASDAQ:AAPL', 'profile,earnings,dividends')
```

---

## Token Authentication Example

```python
# Backend: Generate token
config = FcsConfig.with_token('YOUR_API_KEY', 'YOUR_PUBLIC_KEY', 3600)
fcsapi = FcsApi(config)
token_data = fcsapi.generate_token()

# Send token_data to frontend:
# {
#     '_token': 'abc123...',
#     '_expiry': 1764164233,
#     '_public_key': 'your_public_key'
# }

# Frontend (JavaScript): Use token
# fetch('https://api-v4.fcsapi.com/forex/latest?symbol=EURUSD' +
#       '&_public_key=' + token_data._public_key +
#       '&_expiry=' + token_data._expiry +
#       '&_token=' + token_data._token)
```

---

## Get API Key

Get your API key at: https://fcsapi.com
