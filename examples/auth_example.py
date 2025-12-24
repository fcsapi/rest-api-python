"""
FCS API - Authentication Examples

Three authentication methods:
1. access_key - Simple API key (default)
2. ip_whitelist - IP whitelist (no key needed)
3. token - Secure token-based (recommended for frontend)

Get your API key at: https://fcsapi.com
"""

import sys
sys.path.insert(0, '..')

from src.fcs_config import FcsConfig
from src.fcs_api import FcsApi

# ============================================================
# Method 1: Simple API Key (Backward Compatible)
# ============================================================
print("=== Method 1: Simple API Key ===\n")

fcsapi = FcsApi('YOUR_API_KEY')
print(fcsapi.forex.get_latest_price('FX:EURUSD'))


# ============================================================
# Method 2: IP Whitelist (No key needed)
# ============================================================
print("\n\n=== Method 2: IP Whitelist ===\n")

# First, whitelist your server IP in your account:
# https://fcsapi.com/dashboard/profile -> IP Whitelist

config = FcsConfig.with_ip_whitelist()
fcsapi = FcsApi(config)
print(fcsapi.forex.get_latest_price('FX:EURUSD'))


# ============================================================
# Method 3: Token-Based Authentication (Secure)
# ============================================================
print("\n\n=== Method 3: Token-Based (Secure) ===\n")

# Step 1: On your BACKEND - Generate token
config = FcsConfig.with_token(
    'YOUR_API_KEY',      # Private key (keep secret on server)
    'YOUR_PUBLIC_KEY',   # Public key (can be exposed)
    3600                 # Token valid for 1 hour
)

fcsapi = FcsApi(config)

# Generate token to send to frontend
token_data = fcsapi.generate_token()
print("Token for frontend:")
print(token_data)

# This token data can be sent to frontend JavaScript:
# {
#     '_token': 'abc123...',
#     '_expiry': 1764164233,
#     '_public_key': 'your_public_key'
# }

# API request with token auth
print("\nAPI Response:")
print(fcsapi.forex.get_latest_price('FX:EURUSD'))


# ============================================================
# Using Config Object (Advanced)
# ============================================================
print("\n\n=== Advanced: Custom Config ===\n")

config = FcsConfig()
config.auth_method = 'access_key'
config.access_key = 'YOUR_API_KEY'
config.timeout = 60         # Custom timeout
config.connect_timeout = 10 # Custom connect timeout

fcsapi = FcsApi(config)
print(fcsapi.forex.get_latest_price('FX:EURUSD'))
