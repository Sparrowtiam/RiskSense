"""
Investment recommendation engine for Kenya
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Investment:
    """Represents an investment option with details"""
    name: str
    category: str
    expected_return_percent: float
    risk_rating: str
    liquidity: str  # High, Medium, Low
    min_investment: int
    duration_fit: str  # 6m, 12m, 24m+
    pros: List[str]
    cons: List[str]

class RecommendationEngine:
    """Generates investment recommendations based on user profile and market data"""
    
    def __init__(self, market_data: Dict, risk_profiles: Dict):
        self.market_data = market_data
        self.risk_profiles = risk_profiles
    
    def calculate_final_value(self, initial: int, return_percent: float, months: int) -> float:
        """Calculate final investment value given initial amount, return, and time"""
        annual_return = return_percent / 100
        periods = months / 12
        final_value = initial * ((1 + annual_return) ** periods)
        return final_value
    
    def generate_treasury_option(self, user_input: Dict) -> Investment:
        """Generate Treasury Bill/Bond recommendation"""
        months = user_input['duration_months']
        
        # Select appropriate treasury instrument based on duration
        if months <= 3:
            yield_rate = self.market_data['treasury']['91_day_tb']['yield']
            instrument = "91-Day Treasury Bill"
        elif months <= 6:
            yield_rate = self.market_data['treasury']['182_day_tb']['yield']
            instrument = "182-Day Treasury Bill"
        elif months <= 12:
            yield_rate = self.market_data['treasury']['364_day_tb']['yield']
            instrument = "364-Day Treasury Bill"
        else:
            yield_rate = self.market_data['treasury']['2_year_bond']['yield']
            instrument = "2-Year Treasury Bond"
        
        return Investment(
            name=instrument,
            category="Government Securities",
            expected_return_percent=yield_rate,
            risk_rating="Low",
            liquidity="Medium",
            min_investment=100,
            duration_fit=f"{months}m",
            pros=[
                "Capital preservation guaranteed",
                "Backed by government",
                "Fixed, predictable returns",
                "Tax-advantaged (interest exempt from income tax)",
                "Can be sold in secondary market",
            ],
            cons=[
                f"Return ({yield_rate}%) may not exceed inflation ({self.market_data['macro']['inflation_rate']}%)",
                "Less liquidity than bank deposits",
                "Moderate effort to purchase (auctions, tenders)",
            ]
        )
    
    def generate_money_market_option(self, user_input: Dict) -> Investment:
        """Generate Money Market Fund recommendation"""
        avg_mmf_yield = sum([fund['yield'] for fund in self.market_data['money_market'].values()]) / len(self.market_data['money_market'])
        
        return Investment(
            name="Money Market Fund",
            category="Money Market Funds",
            expected_return_percent=avg_mmf_yield,
            risk_rating="Low-Medium",
            liquidity="High",
            min_investment=1000,
            duration_fit="6m-12m",
            pros=[
                "Excellent liquidity - withdraw anytime",
                "Good returns (~16%)",
                "Professional fund management",
                "Easy online investing via fund platforms",
                "Instant diversification",
            ],
            cons=[
                "Returns fluctuate slightly",
                "Initial minimum investment required",
                "Fund management fees reduce net returns",
                "Not suitable if funds needed within days",
            ]
        )
    
    def generate_fixed_deposit_option(self, user_input: Dict) -> Investment:
        """Generate Fixed Deposit recommendation"""
        months = user_input['duration_months']
        
        # Get appropriate FD rate based on duration
        if months <= 6:
            fd_rate_key = '6m'
        else:
            fd_rate_key = '12m'
        
        # Use average of top bank rates
        rates = []
        for bank, rates_dict in self.market_data['fixed_deposits'].items():
            if fd_rate_key in rates_dict:
                rates.append(rates_dict[fd_rate_key])
        
        avg_fd_rate = sum(rates) / len(rates) if rates else 15.8
        
        return Investment(
            name=f"Fixed Deposit ({fd_rate_key})",
            category="Bank Fixed Deposits",
            expected_return_percent=avg_fd_rate,
            risk_rating="Low",
            liquidity="Low",
            min_investment=10000,
            duration_fit=f"{months}m",
            pros=[
                "Capital fully protected (DCDC guarantee up to 100K)",
                "Fixed, guaranteed returns",
                "Easy to set up via bank/digital platforms",
                "Suitable for specific goals with fixed timeline",
                f"Current rates at {avg_fd_rate}% are attractive",
            ],
            cons=[
                "Very low liquidity - locked for tenure",
                "Early withdrawal incurs penalties",
                "Returns don't match inflation fully",
                "Reinvestment risk at maturity",
                "Interest subject to tax",
            ]
        )
    
    def generate_equity_option(self, user_input: Dict) -> Investment:
        """Generate NSE Equity/ETF recommendation"""
        nse_6m_return = self.market_data['nse']['nse_20_index']['6m_return']
        
        return Investment(
            name="NSE Blue-Chip Portfolio (ETF/Direct)",
            category="NSE Equities",
            expected_return_percent=nse_6m_return,
            risk_rating="High",
            liquidity="High",
            min_investment=100,
            duration_fit="6m+",
            pros=[
                f"Strong potential returns (~{nse_6m_return}% in 6 months)",
                "Excellent liquidity in blue-chip stocks",
                "Dividend income (3-4% yield)",
                "Inflation hedge",
                "Low barriers to entry (100KES minimum)",
            ],
            cons=[
                "High volatility risk",
                "Requires active monitoring",
                "Dependent on market sentiment & politics",
                "Can see 15-30% swings in 6 months",
                "Requires investment knowledge",
            ]
        )
    
    def generate_recommendation(self, user_input: Dict) -> Dict:
        """
        Generate recommendation based on user profile
        user_input: {amount, duration_months, risk_appetite}
        """
        amount = user_input['amount']
        duration = user_input['duration_months']
        risk = user_input['risk_appetite'].lower()
        
        # Generate all options
        all_options = [
            self.generate_treasury_option(user_input),
            self.generate_money_market_option(user_input),
            self.generate_fixed_deposit_option(user_input),
        ]
        
        # Add equity option if risk appetite allows
        if risk in ['medium', 'high']:
            all_options.append(self.generate_equity_option(user_input))
        
        # Recommend based on risk appetite
        if risk == 'low':
            # Capital preservation
            recommended = self.generate_treasury_option(user_input)
            alternatives = [
                self.generate_fixed_deposit_option(user_input),
                self.generate_money_market_option(user_input),
            ]
        elif risk == 'medium':
            # Balanced approach - mix of safety and returns
            recommended = self.generate_money_market_option(user_input)
            alternatives = [
                self.generate_fixed_deposit_option(user_input),
                self.generate_equity_option(user_input),
            ]
        else:  # high
            # Aggressive growth
            recommended = self.generate_equity_option(user_input)
            alternatives = [
                self.generate_money_market_option(user_input),
            ]
        
        # Calculate scenarios
        base_return = recommended.expected_return_percent
        final_value = self.calculate_final_value(amount, base_return, duration)
        earnings = final_value - amount
        
        # Best/Worst case scenarios (±5% variance for equities, ±2% for fixed income)
        variance = 5 if 'Equity' in recommended.name else 2
        best_return = base_return + variance
        worst_return = base_return - variance
        best_value = self.calculate_final_value(amount, best_return, duration)
        worst_value = self.calculate_final_value(amount, worst_return, duration)
        
        return {
            'primary_recommendation': {
                'instrument': recommended.name,
                'category': recommended.category,
                'expected_return': recommended.expected_return_percent,
                'final_value': final_value,
                'earnings': earnings,
                'risk_rating': recommended.risk_rating,
                'liquidity': recommended.liquidity,
                'duration_fit': recommended.duration_fit,
                'pros': recommended.pros,
                'cons': recommended.cons,
            },
            'alternatives': [
                {
                    'instrument': alt.name,
                    'category': alt.category,
                    'expected_return': alt.expected_return_percent,
                    'final_value': self.calculate_final_value(amount, alt.expected_return_percent, duration),
                    'risk_rating': alt.risk_rating,
                    'liquidity': alt.liquidity,
                } for alt in alternatives
            ],
            'scenarios': {
                'best_case': {
                    'return_percent': best_return,
                    'final_value': best_value,
                    'description': f"Market conditions favor investments; returns exceed expectations"
                },
                'base_case': {
                    'return_percent': base_return,
                    'final_value': final_value,
                    'description': "Current market trends continue as expected"
                },
                'worst_case': {
                    'return_percent': worst_return,
                    'final_value': worst_value,
                    'description': "Market headwinds; returns below expectations"
                }
            },
            'macro_context': {
                'inflation': self.market_data['macro']['inflation_rate'],
                'cbr': self.market_data['macro']['cbr'],
                'outlook': self.market_data['macro']['economic_outlook'],
            }
        }
