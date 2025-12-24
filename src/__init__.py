"""
FCS API - Python REST Client

Python client library for Forex, Cryptocurrency, and Stock market data from FCS API.

@package FcsApi
@author FCS API <support@fcsapi.com>
@link https://fcsapi.com
"""

from .fcs_config import FcsConfig
from .fcs_api import FcsApi
from .fcs_forex import FcsForex
from .fcs_crypto import FcsCrypto
from .fcs_stock import FcsStock

__all__ = ['FcsApi', 'FcsConfig', 'FcsForex', 'FcsCrypto', 'FcsStock']
__version__ = '4.0.0'
