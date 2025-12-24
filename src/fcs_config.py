"""
FCS API - Configuration

Authentication options:
1. access_key - Simple API key authentication
2. ip_whitelist - No key needed if IP is whitelisted in your account https://fcsapi.com/dashboard/profile
3. token - Secure token-based authentication (recommended for frontend)

@package FcsApi
@author FCS API <support@fcsapi.com>
"""

import hmac
import hashlib
import time
from typing import Dict, Optional


class FcsConfig:
    """
    FCS API Configuration class

    Supports multiple authentication methods:
    - access_key: Simple API key authentication
    - ip_whitelist: IP whitelist (no key needed)
    - token: Secure token-based authentication
    """

    def __init__(self):
        """Initialize configuration with default values"""
        # Authentication method: 'access_key', 'ip_whitelist', 'token'
        self.auth_method: str = 'access_key'

        # API Access Key (Private Key) - Get from: https://fcsapi.com/dashboard
        self.access_key: str = 'YOUR_ACCESS_KEY_HERE'

        # Public Key (for token-based auth) - Get from: https://fcsapi.com/dashboard
        self.public_key: str = 'YOUR_PUBLIC_KEY_HERE'

        # Token expiry time in seconds
        # Options: 300 (5min), 900 (15min), 1800 (30min), 3600 (1hr), 86400 (24hr)
        self.token_expiry: int = 3600

        # Request timeout in seconds
        self.timeout: int = 30

        # Connection timeout in seconds
        self.connect_timeout: int = 5

    @classmethod
    def with_access_key(cls, access_key: str) -> 'FcsConfig':
        """
        Create config with access_key method

        Args:
            access_key: Your API access key

        Returns:
            FcsConfig instance
        """
        config = cls()
        config.auth_method = 'access_key'
        config.access_key = access_key
        return config

    @classmethod
    def with_ip_whitelist(cls) -> 'FcsConfig':
        """
        Create config with IP whitelist method (no key needed)

        Returns:
            FcsConfig instance
        """
        config = cls()
        config.auth_method = 'ip_whitelist'
        return config

    @classmethod
    def with_token(cls, access_key: str, public_key: str, token_expiry: int = 3600) -> 'FcsConfig':
        """
        Create config with token-based authentication

        Args:
            access_key: Your private API key (kept on server)
            public_key: Your public key
            token_expiry: Token validity in seconds

        Returns:
            FcsConfig instance
        """
        config = cls()
        config.auth_method = 'token'
        config.access_key = access_key
        config.public_key = public_key
        config.token_expiry = token_expiry
        return config

    def generate_token(self) -> Dict[str, any]:
        """
        Generate authentication token
        Use this on your backend, then send token to frontend

        Returns:
            dict: {'_token': str, '_expiry': int, '_public_key': str}
        """
        expiry = int(time.time()) + self.token_expiry
        message = f"{self.public_key}{expiry}"
        token = hmac.new(
            self.access_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        return {
            '_token': token,
            '_expiry': expiry,
            '_public_key': self.public_key
        }

    def get_auth_params(self) -> Dict[str, any]:
        """
        Get authentication parameters for API request

        Returns:
            dict: Authentication parameters
        """
        if self.auth_method == 'ip_whitelist':
            return {}
        elif self.auth_method == 'token':
            return self.generate_token()
        else:  # access_key
            return {'access_key': self.access_key}
