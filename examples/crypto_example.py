"""
FCS API - Crypto Example
Get your API key at: https://fcsapi.com
"""

import sys
sys.path.insert(0, '..')

from src.fcs_config import FcsConfig
from src.fcs_api import FcsApi

# Note: FcsApi will only load fcs_crypto module when you access fcsapi.crypto

fcsapi = FcsApi()

print("=== Symbols List ===\n")
print(fcsapi.crypto.get_symbols_list('crypto', 'spot', 'BINANCE'))

print("\n\n=== Latest Price ===\n")
print(fcsapi.crypto.get_latest_price('BINANCE:BTCUSDT'))

print("\n\n=== Historical Data ===\n")
print(fcsapi.crypto.get_history('BINANCE:BTCUSDT', '1D', 5))

print("\n\n=== Profile ===\n")
print(fcsapi.crypto.get_profile('BTC'))
