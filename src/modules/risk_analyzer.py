"""
Risk analysis module for investment vehicles in Kenya
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class RiskFactor:
    """Represents a risk factor with description and severity"""
    name: str
    description: str
    severity: str  # Low, Medium, High
    mitigation: str

class RiskAnalyzer:
    """Analyzes and rates risks for different investment vehicles"""
    
    def __init__(self, market_data: Dict):
        self.market_data = market_data
        self.risk_profiles = {}
    
    def analyze_treasury_risk(self, investment_amount: int, duration_months: int) -> Dict:
        """Analyze risks for Treasury Bills/Bonds"""
        risks = []
        
        # Interest rate risk
        if self.market_data['macro']['inflation_outlook'] == 'rising':
            risks.append(RiskFactor(
                name="Interest Rate Risk",
                description="If rates decline significantly, existing bond prices fall",
                severity="Medium",
                mitigation="Hold to maturity to avoid market price loss"
            ))
        else:
            risks.append(RiskFactor(
                name="Interest Rate Risk",
                description="Low in current stable environment",
                severity="Low",
                mitigation="Monitor CBK policy decisions"
            ))
        
        # Liquidity risk
        risks.append(RiskFactor(
            name="Liquidity Risk",
            description="Government securities have secondary market but not as liquid as deposits",
            severity="Low",
            mitigation="Plan withdrawal timing; use secondary market if needed"
        ))
        
        # Credit risk (very low for government)
        risks.append(RiskFactor(
            name="Credit/Default Risk",
            description="Essentially zero - backed by government of Kenya",
            severity="Low",
            mitigation="Monitor government fiscal health (very stable)"
        ))
        
        # Inflation risk
        inflation_eroded_value = investment_amount * ((self.market_data['macro']['inflation_rate'] / 100) ** (duration_months / 12))
        risks.append(RiskFactor(
            name="Inflation Risk",
            description=f"Real returns reduced by {self.market_data['macro']['inflation_rate']}% inflation",
            severity="Medium",
            mitigation="Invest in inflation-linked bonds or consider equities for higher nominal returns"
        ))
        
        return {
            'instrument': 'Government Treasury/Bonds',
            'risk_rating': 'Low',
            'risk_factors': risks,
            'overall_assessment': 'Safest option; suitable for capital preservation',
        }
    
    def analyze_money_market_risk(self, investment_amount: int, duration_months: int) -> Dict:
        """Analyze risks for Money Market Funds"""
        risks = []
        
        # Market volatility
        risks.append(RiskFactor(
            name="Market Volatility Risk",
            description="MMFs exposed to money market instruments fluctuations",
            severity="Low",
            mitigation="Choose funds with established track records"
        ))
        
        # Interest rate risk
        risks.append(RiskFactor(
            name="Interest Rate Risk",
            description="Short-term rate fluctuations affect returns slightly",
            severity="Low",
            mitigation="Rates relatively stable in current environment"
        ))
        
        # Inflation risk
        risks.append(RiskFactor(
            name="Inflation Risk",
            description=f"Inflation at {self.market_data['macro']['inflation_rate']}% erodes real returns",
            severity="Medium",
            mitigation="Ensure fund return exceeds inflation rate"
        ))
        
        # Manager risk
        risks.append(RiskFactor(
            name="Fund Manager Risk",
            description="Returns depend on fund manager's skill and decisions",
            severity="Medium",
            mitigation="Choose reputable fund managers (Barclays, Equity, Stanchart)"
        ))
        
        return {
            'instrument': 'Money Market Funds',
            'risk_rating': 'Low-Medium',
            'risk_factors': risks,
            'overall_assessment': 'Balanced; good liquidity with modest returns',
        }
    
    def analyze_fixed_deposit_risk(self, investment_amount: int, duration_months: int) -> Dict:
        """Analyze risks for Fixed Deposits"""
        risks = []
        
        # Credit risk
        risks.append(RiskFactor(
            name="Bank Credit Risk",
            description="Risk of bank failure; covered by DCDC up to KES 100K per bank",
            severity="Low",
            mitigation="Spread funds across multiple banks if amount exceeds 100K"
        ))
        
        # Liquidity risk
        risks.append(RiskFactor(
            name="Liquidity Risk",
            description="Funds locked for agreed period; early withdrawal incurs penalties",
            severity="High" if duration_months > 12 else "Medium",
            mitigation="Only invest funds you won't need before maturity"
        ))
        
        # Inflation risk
        risks.append(RiskFactor(
            name="Inflation Risk",
            description=f"Real returns reduced by {self.market_data['macro']['inflation_rate']}% inflation",
            severity="Medium",
            mitigation="Compare FD rates against inflation; consider higher-yielding alternatives"
        ))
        
        # Reinvestment risk
        risks.append(RiskFactor(
            name="Reinvestment Risk",
            description="On maturity, rates might be lower, requiring reinvestment at worse terms",
            severity="Medium",
            mitigation="Ladder investments across different maturity dates"
        ))
        
        return {
            'instrument': 'Fixed Deposits',
            'risk_rating': 'Low',
            'risk_factors': risks,
            'overall_assessment': 'Safe and predictable; best for stable capital',
        }
    
    def analyze_equity_risk(self, investment_amount: int, duration_months: int) -> Dict:
        """Analyze risks for NSE Equities/ETFs"""
        risks = []
        
        # Market risk
        risks.append(RiskFactor(
            name="Market/Price Volatility Risk",
            description="Stock prices fluctuate; 6-month horizon can see 15-30% swings",
            severity="High",
            mitigation="Diversify across sectors; invest only surplus capital"
        ))
        
        # Company-specific risk
        risks.append(RiskFactor(
            name="Company-Specific Risk",
            description="Individual stocks subject to company performance, management changes",
            severity="High",
            mitigation="Diversify across 8-15 stocks or use ETFs for instant diversification"
        ))
        
        # Liquidity risk
        risks.append(RiskFactor(
            name="Liquidity Risk (NSE)",
            description="Some stocks have low trading volumes; difficult to exit large positions",
            severity="Medium",
            mitigation="Stick to NSE-20 stocks (high liquidity) for easier exit"
        ))
        
        # Economic/Political risk
        risks.append(RiskFactor(
            name="Economic/Political Risk",
            description="Kenya political events, policy changes affect market sentiment",
            severity="Medium",
            mitigation="Stay informed; avoid investing during periods of high uncertainty"
        ))
        
        # Currency risk
        risks.append(RiskFactor(
            name="Currency Risk",
            description="KES depreciation doesn't affect local investors directly",
            severity="Low",
            mitigation="N/A for KES-based investors"
        ))
        
        return {
            'instrument': 'NSE Equities/ETFs',
            'risk_rating': 'High',
            'risk_factors': risks,
            'overall_assessment': 'Aggressive; for 6+ month horizon with high risk tolerance',
        }
    
    def analyze_reit_risk(self, investment_amount: int, duration_months: int) -> Dict:
        """Analyze risks for REITs"""
        risks = []
        
        # Real estate market risk
        risks.append(RiskFactor(
            name="Real Estate Market Risk",
            description="Property market downturns reduce REIT valuations",
            severity="Medium",
            mitigation="Diversify across multiple REITs or property sectors"
        ))
        
        # Interest rate risk
        risks.append(RiskFactor(
            name="Interest Rate Risk",
            description="REIT values sensitive to interest rate changes",
            severity="Medium",
            mitigation="Monitor CBK rate decisions; REITs less attractive when rates rise sharply"
        ))
        
        # Liquidity risk
        risks.append(RiskFactor(
            name="Liquidity Risk",
            description="REITs less liquid than blue-chip stocks",
            severity="Medium",
            mitigation="Plan exit strategy; allow 1-2 weeks for sale execution"
        ))
        
        # Inflation risk (hedge)
        risks.append(RiskFactor(
            name="Inflation Risk (Hedging)",
            description="REITs can serve as inflation hedge; property values rise with inflation",
            severity="Low",
            mitigation="This is actually a benefit in inflationary environment"
        ))
        
        return {
            'instrument': 'REITs',
            'risk_rating': 'Medium',
            'risk_factors': risks,
            'overall_assessment': 'Moderate; for diversification and inflation protection',
        }
    
    def get_risk_profile(self, instrument: str, amount: int, duration: int) -> Dict:
        """Get complete risk profile for any instrument"""
        if 'Treasury' in instrument or 'Bond' in instrument:
            return self.analyze_treasury_risk(amount, duration)
        elif 'Money Market' in instrument:
            return self.analyze_money_market_risk(amount, duration)
        elif 'Fixed Deposit' in instrument:
            return self.analyze_fixed_deposit_risk(amount, duration)
        elif 'Equity' in instrument or 'Stock' in instrument:
            return self.analyze_equity_risk(amount, duration)
        elif 'REIT' in instrument:
            return self.analyze_reit_risk(amount, duration)
        else:
            return {'error': 'Instrument type not recognized'}
