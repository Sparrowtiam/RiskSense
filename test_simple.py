"""
Quick test of FinApp modules
"""

import sys
sys.path.insert(0, r'c:\Users\HP\FinApp')

from src.modules import (
    KenyanMarketDataCollector,
    RiskAnalyzer,
    RecommendationEngine,
)

# Initialize
print("Initializing FinApp...")
collector = KenyanMarketDataCollector()
market_data = collector.get_all_market_data()
recommendation_engine = RecommendationEngine(market_data, {})

# Test with sample user input
user_input = {
    'amount': 50000,
    'duration_months': 6,
    'risk_appetite': 'Medium'
}

# Generate recommendation
recommendation = recommendation_engine.generate_recommendation(user_input)

# Display results
print("\n" + "="*80)
print("FINAPP - INVESTMENT RECOMMENDATION TEST")
print("="*80)

primary = recommendation['primary_recommendation']
print(f"\nPRIMARY RECOMMENDATION: {primary['instrument']}")
print(f"\nCategory: {primary['category']}")
print(f"Risk Rating: {primary['risk_rating']}")
print(f"Expected Return: {primary['expected_return']}% p.a.")
print(f"\nFINANCIAL PROJECTIONS (for KES {user_input['amount']:,.0f}):")
print(f"Initial Investment: KES {user_input['amount']:,.0f}")
print(f"Expected Earnings: KES {primary['earnings']:,.0f}")
print(f"Final Value: KES {primary['final_value']:,.0f}")
print(f"Investment Period: {user_input['duration_months']} months")

print(f"\nPROS:")
for pro in primary['pros'][:3]:
    print(f"   - {pro}")

print(f"\nCONS:")
for con in primary['cons'][:2]:
    print(f"   - {con}")

print(f"\nMARKET CONDITIONS:")
macro = market_data['macro']
print(f"   - Inflation Rate: {macro['inflation_rate']}%")
print(f"   - CBR: {macro['cbr']}%")
print(f"   - Economic Outlook: {macro['economic_outlook']}")

print(f"\nTest completed successfully!")
