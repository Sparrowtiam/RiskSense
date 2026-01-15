#!/usr/bin/env python3
"""Debug test for streamlit app"""

from src.modules import KenyanMarketDataCollector, RiskAnalyzer, RecommendationEngine

try:
    print("1. Testing market data collection...")
    collector = KenyanMarketDataCollector()
    market_data = collector.get_all_market_data()
    print("✓ Market data loaded")
    
    print("\n2. Testing risk analysis...")
    risk_analyzer = RiskAnalyzer(market_data)
    risk_profile = risk_analyzer.analyze_treasury_risk(50000, 6)
    print(f"✓ Risk profile generated")
    
    if risk_profile.get('risk_factors'):
        factor = risk_profile['risk_factors'][0]
        print(f"  Factor type: {type(factor).__name__}")
        print(f"  Factor: {factor}")
        print(f"  Has severity: {hasattr(factor, 'severity')}")
        if hasattr(factor, 'severity'):
            print(f"  Severity value: {factor.severity}")
    
    print("\n3. Testing recommendation engine...")
    engine = RecommendationEngine(market_data, {})
    user_input = {
        'amount': 50000,
        'duration_months': 6,
        'risk_appetite': 'Medium'
    }
    recommendation = engine.generate_recommendation(user_input)
    print(f"✓ Recommendation generated")
    print(f"  Primary: {recommendation['primary_recommendation']['instrument']}")
    
    print("\n✓ All components working correctly!")
    
except Exception as e:
    print(f"\n✗ Error: {type(e).__name__}")
    print(f"  Message: {str(e)}")
    import traceback
    traceback.print_exc()
