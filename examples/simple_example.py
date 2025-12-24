"""
FCS API - Simple Example (Quick Start)

Minimal example to get started with FCS REST API.
Get your API key at: https://fcsapi.com

Run: python simple_example.py
"""

import sys
import os

# Add parent directory to path for import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import FcsApi

# Create API client
fcsapi = FcsApi()

# Get EUR/USD price
print('Getting EUR/USD price...')
response = fcsapi.forex.get_latest_price('EURUSD')

if fcsapi.is_success():
    data = response['response'][0]
    print(f"EUR/USD: {data['active']['c']}")
    print(f"Change: {data['active']['chp']}%")
else:
    print(f"Error: {fcsapi.get_error()}")
