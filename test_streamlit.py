"""
Quick test to verify Streamlit app loads without errors
"""

import sys
sys.path.insert(0, r'c:\Users\HP\FinApp')

print("Testing Streamlit App Components...\n")

# Test 1: Import streamlit
try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
except ImportError as e:
    print(f"✗ Streamlit import failed: {e}")
    sys.exit(1)

# Test 2: Import app modules
try:
    from src.modules import (
        KenyanMarketDataCollector,
        RiskAnalyzer,
        RecommendationEngine,
    )
    print("✓ All modules imported successfully")
except ImportError as e:
    print(f"✗ Module import failed: {e}")
    sys.exit(1)

# Test 3: Verify streamlit_app.py syntax
try:
    with open(r'c:\Users\HP\FinApp\streamlit_app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    compile(code, 'streamlit_app.py', 'exec')
    print("✓ streamlit_app.py syntax is valid")
except SyntaxError as e:
    print(f"✗ Syntax error in streamlit_app.py: {e}")
    sys.exit(1)

# Test 4: Load market data
try:
    collector = KenyanMarketDataCollector()
    data = collector.get_all_market_data()
    print("✓ Market data collection working")
except Exception as e:
    print(f"✗ Market data collection failed: {e}")
    sys.exit(1)

# Test 5: Generate recommendation
try:
    engine = RecommendationEngine(data, {})
    rec = engine.generate_recommendation({
        'amount': 50000,
        'duration_months': 6,
        'risk_appetite': 'Medium'
    })
    print("✓ Recommendation engine working")
except Exception as e:
    print(f"✗ Recommendation generation failed: {e}")
    sys.exit(1)

print("\n" + "="*70)
print("✓ ALL TESTS PASSED - Streamlit app is ready!")
print("="*70)
print("\nTo run the app locally:")
print("  streamlit run streamlit_app.py")
print("\nOr execute:")
print("  python run_streamlit.py")
