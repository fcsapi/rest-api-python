"""
FCS API - Currency Converter Example

Shows how to convert currencies (Forex and Crypto).
Get your API key at: https://fcsapi.com

Run: python converter_example.py
"""

import sys
import os

# Add parent directory to path for import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import FcsApi

# Create API client
fcsapi = FcsApi()

print('=' * 50)
print('  FCS API - Currency Converter')
print('=' * 50)

# Forex conversion: EUR to USD
print('\n--- Forex Conversion ---')
response = fcsapi.forex.convert('EUR', 'USD', 1000)
if fcsapi.is_success():
    data = response['response']
    print(f"1000 EUR = {data['total']} USD")
    print(f"Rate: {data['price']}")

# Crypto conversion: BTC to USD
print('\n--- Crypto Conversion ---')
response = fcsapi.crypto.convert('BTC', 'USD', 1)
if fcsapi.is_success():
    data = response['response']
    print(f"1 BTC = ${data['total']:,.2f} USD")

# Crypto to Crypto: ETH to BTC
print('\n--- Crypto to Crypto ---')
response = fcsapi.crypto.convert('ETH', 'BTC', 10)
if fcsapi.is_success():
    data = response['response']
    print(f"10 ETH = {data['total']} BTC")

print('\n' + '=' * 50)
