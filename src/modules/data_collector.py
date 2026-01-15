"""
Module for collecting real-time Kenyan market data
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class KenyanMarketDataCollector:
    """Collects real-time data on Kenyan investment vehicles"""
    
    def __init__(self):
        self.treasury_data = {}
        self.money_market_data = {}
        self.nse_data = {}
        self.macro_data = {}
        self.last_updated = None
    
    def fetch_treasury_data(self) -> Dict:
        """
        Fetch latest Treasury bill and bond yields
        In production, would connect to CBK or market data APIs
        """
        try:
            # Simulated Treasury data for demonstration
            # In production: use CBK Open Data, Kenya Bond API, or similar
            self.treasury_data = {
                '91_day_tb': {'yield': 16.85, 'last_updated': datetime.now()},
                '182_day_tb': {'yield': 17.23, 'last_updated': datetime.now()},
                '364_day_tb': {'yield': 17.95, 'last_updated': datetime.now()},
                '2_year_bond': {'yield': 18.10, 'last_updated': datetime.now()},
                '5_year_bond': {'yield': 17.85, 'last_updated': datetime.now()},
                '10_year_bond': {'yield': 17.50, 'last_updated': datetime.now()},
            }
            return self.treasury_data
        except Exception as e:
            print(f"Error fetching Treasury data: {e}")
            return {}
    
    def fetch_money_market_funds(self) -> Dict:
        """
        Fetch money market fund performance and rates
        """
        try:
            # Simulated Money Market Fund data
            # In production: use CMA, NSE, or fund provider APIs
            self.money_market_data = {
                'barclays_mmf': {'yield': 16.5, 'min_investment': 1000},
                'equity_mmf': {'yield': 16.2, 'min_investment': 1000},
                'stanchart_mmf': {'yield': 16.4, 'min_investment': 5000},
                'absa_mmf': {'yield': 16.0, 'min_investment': 1000},
            }
            return self.money_market_data
        except Exception as e:
            print(f"Error fetching Money Market data: {e}")
            return {}
    
    def fetch_fixed_deposits(self) -> Dict:
        """
        Fetch current fixed deposit rates from major Kenyan banks
        """
        try:
            # Simulated FD rates
            fd_rates = {
                'barclays': {'6m': 15.5, '12m': 16.0},
                'equity_bank': {'6m': 15.8, '12m': 16.2},
                'stanchart': {'6m': 15.3, '12m': 15.8},
                'co_op_bank': {'6m': 16.2, '12m': 16.5},
                'abc_bank': {'6m': 15.9, '12m': 16.3},
            }
            return fd_rates
        except Exception as e:
            print(f"Error fetching FD rates: {e}")
            return {}
    
    def fetch_nse_performance(self) -> Dict:
        """
        Fetch NSE index performance and market data
        """
        try:
            # Simulated NSE data
            # In production: use NSE API or market data providers
            self.nse_data = {
                'nse_20_index': {
                    'current': 8945.32,
                    '6m_return': 12.5,  # percent
                    'ytd_return': 18.3,
                    'pe_ratio': 14.2,
                },
                'nasi_index': {
                    'current': 106234.56,
                    '6m_return': 8.2,
                    'ytd_return': 15.7,
                },
                'top_stocks': {
                    'SAFARICOM': {'price': 28.50, 'change_6m': 15.2, 'dividend_yield': 3.5},
                    'EQUITY': {'price': 45.20, 'change_6m': 22.1, 'dividend_yield': 4.2},
                    'KCBGROUP': {'price': 38.80, 'change_6m': 18.5, 'dividend_yield': 3.8},
                    'STANCHART': {'price': 185.00, 'change_6m': 12.3, 'dividend_yield': 2.9},
                }
            }
            return self.nse_data
        except Exception as e:
            print(f"Error fetching NSE data: {e}")
            return {}
    
    def fetch_macro_indicators(self) -> Dict:
        """
        Fetch macro indicators: inflation, interest rates, currency
        """
        try:
            self.macro_data = {
                'inflation_rate': 4.8,  # percent, current
                'cbr': 10.0,  # Central Bank Rate (policy rate)
                'base_lending_rate': 13.0,
                'usd_kes_rate': 127.45,
                'inflation_outlook': 'stable',  # stable, rising, declining
                'economic_outlook': 'moderate growth',
            }
            return self.macro_data
        except Exception as e:
            print(f"Error fetching macro data: {e}")
            return {}
    
    def get_all_market_data(self) -> Dict:
        """Fetch all market data in one call"""
        return {
            'treasury': self.fetch_treasury_data(),
            'money_market': self.fetch_money_market_funds(),
            'fixed_deposits': self.fetch_fixed_deposits(),
            'nse': self.fetch_nse_performance(),
            'macro': self.fetch_macro_indicators(),
            'timestamp': datetime.now().isoformat(),
        }
