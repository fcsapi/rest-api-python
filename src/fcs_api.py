"""
FCS API - REST API Client

Python client for Forex, Cryptocurrency, and Stock market data

@package FcsApi
@author FCS API <support@fcsapi.com>
@link https://fcsapi.com
"""

import requests
from typing import Dict, Optional, Any, Union
from .fcs_config import FcsConfig


class FcsApi:
    """
    FCS API REST Client

    Main client class for accessing Forex, Crypto, and Stock market data.
    """

    BASE_URL = 'https://api-v4.fcsapi.com/'

    def __init__(self, config: Union[str, FcsConfig, None] = None):
        """
        Constructor

        Args:
            config: API key string, FcsConfig object, or None to use default config
        """
        self._last_response: Dict = {}

        # Configure authentication
        if isinstance(config, FcsConfig):
            self.config = config
        elif isinstance(config, str):
            # Backward compatible: accept string API key
            self.config = FcsConfig.with_access_key(config)
        else:
            # Use default config (key from FcsConfig)
            self.config = FcsConfig()

        # Lazy-loaded modules
        self._forex = None
        self._crypto = None
        self._stock = None

    @property
    def forex(self):
        """Get Forex API module (lazy loading)"""
        if self._forex is None:
            from .fcs_forex import FcsForex
            self._forex = FcsForex(self)
        return self._forex

    @property
    def crypto(self):
        """Get Crypto API module (lazy loading)"""
        if self._crypto is None:
            from .fcs_crypto import FcsCrypto
            self._crypto = FcsCrypto(self)
        return self._crypto

    @property
    def stock(self):
        """Get Stock API module (lazy loading)"""
        if self._stock is None:
            from .fcs_stock import FcsStock
            self._stock = FcsStock(self)
        return self._stock

    def set_timeout(self, seconds: int) -> 'FcsApi':
        """
        Set request timeout

        Args:
            seconds: Timeout in seconds

        Returns:
            self for method chaining
        """
        self.config.timeout = seconds
        return self

    def get_config(self) -> FcsConfig:
        """
        Get config

        Returns:
            FcsConfig instance
        """
        return self.config

    def generate_token(self) -> Dict[str, Any]:
        """
        Generate token for frontend use
        Only works when auth_method is 'token'

        Returns:
            dict: {'_token': str, '_expiry': int, '_public_key': str}
        """
        return self.config.generate_token()

    def request(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make API request (POST with form data)

        Args:
            endpoint: API endpoint
            params: Request parameters

        Returns:
            Response data or None on error
        """
        if params is None:
            params = {}

        # Add authentication parameters
        auth_params = self.config.get_auth_params()
        all_params = {**params, **auth_params}

        url = self.BASE_URL + endpoint

        try:
            response = requests.post(
                url,
                data=all_params,
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json',
                    'Accept-Encoding': 'gzip, deflate'
                },
                timeout=(self.config.connect_timeout, self.config.timeout)
            )

            data = response.json()
            self._last_response = data
            return data

        except requests.exceptions.RequestException as e:
            self._last_response = {
                'status': False,
                'code': 0,
                'msg': f'Request Error: {str(e)}',
                'response': None
            }
            return None
        except ValueError as e:
            self._last_response = {
                'status': False,
                'code': 0,
                'msg': f'Invalid JSON response: {str(e)}',
                'response': None
            }
            return None

    def get_last_response(self) -> Dict:
        """
        Get last response

        Returns:
            Last response dictionary
        """
        return self._last_response

    def get_response_data(self) -> Any:
        """
        Get response data only

        Returns:
            Response data or None
        """
        return self._last_response.get('response')

    def is_success(self) -> bool:
        """
        Check if last request was successful

        Returns:
            True if successful, False otherwise
        """
        return self._last_response.get('status') is True

    def get_error(self) -> Optional[str]:
        """
        Get error message from last response

        Returns:
            Error message or None if successful
        """
        if self.is_success():
            return None
        return self._last_response.get('msg', 'Unknown error')
