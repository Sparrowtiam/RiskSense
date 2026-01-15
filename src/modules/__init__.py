"""FinApp modules package"""

from .data_collector import KenyanMarketDataCollector
from .risk_analyzer import RiskAnalyzer
from .recommendation_engine import RecommendationEngine

__all__ = [
    'KenyanMarketDataCollector',
    'RiskAnalyzer', 
    'RecommendationEngine',
]
