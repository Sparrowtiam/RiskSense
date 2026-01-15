"""
FinApp - Streamlit Web Interface
Kenya Investment Advisor
"""

import streamlit as st
import json
from datetime import datetime
from src.modules import (
    KenyanMarketDataCollector,
    RiskAnalyzer,
    RecommendationEngine,
)

# Page configuration
st.set_page_config(
    page_title="FinApp - Kenya Investment Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'market_data' not in st.session_state:
    st.session_state.market_data = None
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None

@st.cache_data(ttl=3600)
def load_market_data():
    """Load and cache market data for 1 hour"""
    try:
        collector = KenyanMarketDataCollector()
        market_data = collector.get_all_market_data()
        return market_data
    except Exception as e:
        st.error(f"Error loading market data: {str(e)}")
        return None

def display_header():
    """Display application header"""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("💰 FinApp")
        st.markdown("### Kenya Investment Advisor")
    with col2:
        st.markdown("---")
        st.markdown("**v1.0.0**")

def display_disclaimer():
    """Display important disclaimer"""
    st.warning("""
    ⚠️ **DISCLAIMER**: This tool provides decision-support only and is NOT financial advice.
    - Consult a licensed financial advisor before investing
    - Past performance doesn't guarantee future results
    - All investments carry risk, including loss of principal
    - Market conditions can change rapidly
    """)

def display_market_conditions(market_data):
    """Display current market conditions"""
    st.subheader("📊 Current Market Conditions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    macro = market_data['macro']
    with col1:
        st.metric("Inflation Rate", f"{macro['inflation_rate']}%", "Current")
    with col2:
        st.metric("CBR (Policy Rate)", f"{macro['cbr']}%", "Current")
    with col3:
        st.metric("Base Lending Rate", f"{macro['base_lending_rate']}%", "Current")
    with col4:
        st.metric("USD/KES", f"{macro['usd_kes_rate']}", "Current")
    
    st.info(f"📈 Economic Outlook: **{macro['economic_outlook'].title()}**")

def display_treasury_rates(market_data):
    """Display Treasury instrument rates"""
    st.subheader("🏛️ Treasury Instruments")
    
    treasury = market_data['treasury']
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("91-Day TB", f"{treasury['91_day_tb']['yield']}%", "Yield p.a.")
    with col2:
        st.metric("182-Day TB", f"{treasury['182_day_tb']['yield']}%", "Yield p.a.")
    with col3:
        st.metric("364-Day TB", f"{treasury['364_day_tb']['yield']}%", "Yield p.a.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("2-Year Bond", f"{treasury['2_year_bond']['yield']}%", "Yield p.a.")
    with col2:
        st.metric("5-Year Bond", f"{treasury['5_year_bond']['yield']}%", "Yield p.a.")
    with col3:
        st.metric("10-Year Bond", f"{treasury['10_year_bond']['yield']}%", "Yield p.a.")

def display_nse_performance(market_data):
    """Display NSE market performance"""
    st.subheader("📈 NSE Market Performance")
    
    nse = market_data['nse']
    index = nse['nse_20_index']
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("NSE-20 Index", f"{index['current']:.2f}", "Current")
    with col2:
        st.metric("6-Month Return", f"{index['6m_return']:.1f}%", "Performance")
    with col3:
        st.metric("YTD Return", f"{index['ytd_return']:.1f}%", "Performance")
    with col4:
        st.metric("P/E Ratio", f"{index['pe_ratio']}", "Average")
    
    st.markdown("**Top Stocks:**")
    cols = st.columns(4)
    for i, (stock, data) in enumerate(nse['top_stocks'].items()):
        with cols[i % 4]:
            st.text(f"**{stock}**")
            st.text(f"Price: KES {data['price']}")
            st.text(f"6m Change: {data['change_6m']:.1f}%")
            st.text(f"Dividend: {data['dividend_yield']}%")

def get_investment_recommendation(market_data, amount, duration, risk):
    """Get investment recommendation"""
    engine = RecommendationEngine(market_data, {})
    user_input = {
        'amount': amount,
        'duration_months': duration,
        'risk_appetite': risk
    }
    return engine.generate_recommendation(user_input)

def display_recommendation(market_data, amount, duration, risk):
    """Display investment recommendation"""
    with st.spinner("Generating recommendation..."):
        recommendation = get_investment_recommendation(market_data, amount, duration, risk)
    
    primary = recommendation['primary_recommendation']
    
    # Main recommendation
    st.subheader("✅ Primary Recommendation")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Instrument", primary['instrument'], primary['category'])
    with col2:
        st.metric("Risk Rating", primary['risk_rating'], primary['liquidity'])
    with col3:
        st.metric("Expected Return", f"{primary['expected_return']:.2f}%", "p.a.")
    with col4:
        st.metric("Expected Earnings", f"KES {primary['earnings']:,.0f}", f"in {duration}m")
    
    # Financial projections
    st.subheader("💰 Financial Projections")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Initial Investment", f"KES {amount:,.0f}", "Your input")
    with col2:
        st.metric("Expected Earnings", f"KES {primary['earnings']:,.0f}", f"at {primary['expected_return']:.2f}%")
    with col3:
        st.metric("Final Value", f"KES {primary['final_value']:,.0f}", "After maturity")
    
    # Pros and Cons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✨ Pros:**")
        for pro in primary['pros']:
            st.markdown(f"• {pro}")
    
    with col2:
        st.markdown("**⚠️ Cons:**")
        for con in primary['cons']:
            st.markdown(f"• {con}")
    
    # Scenarios
    st.subheader("📊 Investment Scenarios")
    scenarios = recommendation['scenarios']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success(f"🟢 **Best Case**")
        st.markdown(f"Return: **{scenarios['best_case']['return_percent']:.2f}%**")
        st.markdown(f"Final Value: **KES {scenarios['best_case']['final_value']:,.0f}**")
        st.caption(scenarios['best_case']['description'])
    
    with col2:
        st.info(f"🟡 **Base Case** (Expected)")
        st.markdown(f"Return: **{scenarios['base_case']['return_percent']:.2f}%**")
        st.markdown(f"Final Value: **KES {scenarios['base_case']['final_value']:,.0f}**")
        st.caption(scenarios['base_case']['description'])
    
    with col3:
        st.error(f"🔴 **Worst Case**")
        st.markdown(f"Return: **{scenarios['worst_case']['return_percent']:.2f}%**")
        st.markdown(f"Final Value: **KES {scenarios['worst_case']['final_value']:,.0f}**")
        st.caption(scenarios['worst_case']['description'])
    
    # Alternatives
    st.subheader("🔄 Alternative Investment Options")
    
    for i, alt in enumerate(recommendation['alternatives'], 1):
        with st.expander(f"Option {i}: {alt['instrument']}"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Category", alt['category'])
            with col2:
                st.metric("Expected Return", f"{alt['expected_return']:.2f}%", "p.a.")
            with col3:
                st.metric("Final Value", f"KES {alt['final_value']:,.0f}", "After maturity")
            with col4:
                st.metric("Risk", alt['risk_rating'])
            
            st.markdown(f"**Liquidity**: {alt['liquidity']}")

def display_risk_analysis(market_data, primary_instrument):
    """Display risk analysis"""
    st.subheader("⚠️ Risk Analysis")
    
    try:
        risk_analyzer = RiskAnalyzer(market_data)
        
        if 'Treasury' in primary_instrument or 'Bond' in primary_instrument:
            risk_profile = risk_analyzer.analyze_treasury_risk(50000, 6)
        elif 'Money Market' in primary_instrument:
            risk_profile = risk_analyzer.analyze_money_market_risk(50000, 6)
        elif 'Fixed Deposit' in primary_instrument:
            risk_profile = risk_analyzer.analyze_fixed_deposit_risk(50000, 6)
        else:
            risk_profile = risk_analyzer.analyze_equity_risk(50000, 6)
        
        st.markdown(f"**Overall Risk Rating**: {risk_profile.get('risk_rating', 'N/A')}")
        st.markdown(f"**Assessment**: {risk_profile.get('overall_assessment', 'N/A')}")
        
        st.markdown("**Risk Factors:**")
        risk_factors = risk_profile.get('risk_factors', [])
        
        if risk_factors:
            for idx, factor in enumerate(risk_factors, 1):
                try:
                    # Handle both dataclass and dict formats
                    if hasattr(factor, 'severity'):
                        severity = factor.severity
                        name = factor.name
                        description = factor.description
                        mitigation = factor.mitigation
                    else:
                        severity = factor.get('severity', 'Unknown')
                        name = factor.get('name', f'Factor {idx}')
                        description = factor.get('description', 'No description')
                        mitigation = factor.get('mitigation', 'No mitigation provided')
                    
                    color = "🔴" if severity == "High" else "🟡" if severity == "Medium" else "🟢"
                    with st.expander(f"{color} {name} ({severity})"):
                        st.markdown(f"**Description**: {description}")
                        st.markdown(f"**Mitigation**: {mitigation}")
                except Exception as e:
                    st.warning(f"Error displaying factor: {str(e)}")
        else:
            st.info("No specific risk factors identified.")
            
    except Exception as e:
        st.error(f"Error in risk analysis: {str(e)}")

def main():
    """Main application"""
    display_header()
    display_disclaimer()
    
    # Load market data with error handling
    try:
        market_data = load_market_data()
        if market_data is None:
            st.error("Failed to load market data. Please refresh the page.")
            return
    except Exception as e:
        st.error(f"Error loading market data: {str(e)}")
        return
    
    # Sidebar for input
    st.sidebar.markdown("## 📋 Investment Details")
    
    # Investment amount
    amount = st.sidebar.number_input(
        "Investment Amount (KES)",
        min_value=100,
        max_value=10000000,
        value=50000,
        step=1000,
        help="Minimum investment is KES 100"
    )
    
    # Investment duration
    duration = st.sidebar.slider(
        "Investment Duration (Months)",
        min_value=6,
        max_value=60,
        value=6,
        step=1,
        help="Minimum duration is 6 months"
    )
    
    # Risk appetite
    risk_options = {
        "Low Risk": "Low",
        "Medium Risk": "Medium",
        "High Risk": "High"
    }
    
    risk_display = st.sidebar.radio(
        "Risk Appetite",
        options=list(risk_options.keys()),
        help="Choose your investment risk profile"
    )
    risk = risk_options[risk_display]
    
    # Submit button
    st.sidebar.markdown("---")
    generate_button = st.sidebar.button(
        "🚀 Generate Recommendation",
        use_container_width=True,
        type="primary"
    )
    
    # Tabs for display
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Market Overview", "Recommendation", "Risk Analysis", "About"]
    )
    
    with tab1:
        st.markdown("---")
        try:
            display_market_conditions(market_data)
            st.markdown("---")
            display_treasury_rates(market_data)
            st.markdown("---")
            display_nse_performance(market_data)
        except Exception as e:
            st.error(f"Error displaying market data: {str(e)}")
    
    with tab2:
        st.markdown("---")
        if generate_button or st.session_state.recommendation is not None:
            try:
                recommendation = get_investment_recommendation(market_data, amount, duration, risk)
                st.session_state.recommendation = recommendation
                display_recommendation(market_data, amount, duration, risk)
            except Exception as e:
                st.error(f"Error generating recommendation: {str(e)}")
        else:
            st.info("👈 Click 'Generate Recommendation' in the sidebar to get started")
    
    with tab3:
        st.markdown("---")
        if generate_button or st.session_state.recommendation is not None:
            try:
                if st.session_state.recommendation:
                    primary_instrument = st.session_state.recommendation['primary_recommendation']['instrument']
                    display_risk_analysis(market_data, primary_instrument)
            except Exception as e:
                st.error(f"Error displaying risk analysis: {str(e)}")
        else:
            st.info("👈 Click 'Generate Recommendation' in the sidebar to analyze risks")
    
    with tab4:
        st.markdown("""
        ## About FinApp
        
        FinApp is a comprehensive investment decision-support system designed specifically for the Kenyan investment market.
        
        ### Features
        - **Real-Time Market Data**: Current Treasury yields, NSE performance, and macroeconomic indicators
        - **Comprehensive Risk Analysis**: Identifies and rates 20+ risk factors across investment types
        - **Personalized Recommendations**: Based on your investment amount, duration, and risk appetite
        - **Financial Projections**: Best/Base/Worst case scenarios with expected returns
        - **Professional Guidance**: Step-by-step action plans to invest
        
        ### Investment Options Analyzed
        - 🏛️ Government Treasury Bills & Bonds
        - 💰 Money Market Funds
        - 🏦 Bank Fixed Deposits
        - 📈 NSE Equities
        - 🏢 REITs
        
        ### Key Information
        - **Market Focus**: Kenya
        - **Minimum Duration**: 6 months
        - **Primary Currency**: KES
        - **Target Users**: Individual investors
        
        ### Disclaimer
        This tool provides **decision-support only** and is **NOT financial advice**. 
        Please consult a licensed financial advisor before making investment decisions.
        
        ### Links
        - [GitHub Repository](https://github.com/yourusername/finapp)
        - [Documentation](https://github.com/yourusername/finapp/blob/main/README.md)
        
        **Version**: 1.0.0  
        **Last Updated**: January 15, 2026
        """)

if __name__ == "__main__":
    main()
