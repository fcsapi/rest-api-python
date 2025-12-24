"""
FCS API - Forex Example
Get your API key at: https://fcsapi.com
"""

import sys
sys.path.insert(0, '..')

from src.fcs_config import FcsConfig
from src.fcs_api import FcsApi

# Note: FcsApi will only load fcs_forex module when you access fcsapi.forex

fcsapi = FcsApi()

print("=== Symbols List ===\n")
print(fcsapi.forex.get_symbols_list('forex', 'spot'))

print("\n\n=== Latest Price ===\n")
print(fcsapi.forex.get_latest_price('FX:EURUSD'))

print("\n\n=== Historical Data ===\n")
print(fcsapi.forex.get_history('EURUSD', '1D', 5))

print("\n\n=== Profile ===\n")
print(fcsapi.forex.get_profile('EUR'))
