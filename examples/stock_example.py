"""
FCS API - Stock Example
Get your API key at: https://fcsapi.com
"""

import sys
sys.path.insert(0, '..')

from src.fcs_config import FcsConfig
from src.fcs_api import FcsApi

# Note: FcsApi will only load fcs_stock module when you access fcsapi.stock

fcsapi = FcsApi()

print("=== Symbols List ===\n")
print(fcsapi.stock.get_symbols_list('NASDAQ'))

print("\n\n=== Latest Price ===\n")
print(fcsapi.stock.get_latest_price('NASDAQ:AAPL'))

print("\n\n=== Historical Data ===\n")
print(fcsapi.stock.get_history('NASDAQ:AAPL', '1D', 5))

print("\n\n=== Profile ===\n")
print(fcsapi.stock.get_profile('AAPL'))
