import streamlit as st

st.set_page_config(page_title="App Test", layout="wide")

st.title("✅ Streamlit is running")
st.write("If you can see this, the app is executing correctly.")

"""
Main FinApp CLI application
Kenyan Investment Recommendation System
"""

import sys
import json
from datetime import datetime
from typing import Dict
from src.modules import (
    KenyanMarketDataCollector,
    RiskAnalyzer,
    RecommendationEngine,
)

class FinAppCLI:
    """Command-line interface for FinApp investment advisor"""
    
    def __init__(self):
        self.data_collector = KenyanMarketDataCollector()
        self.market_data = None
        self.risk_analyzer = None
        self.recommendation_engine = None
    
    def print_header(self):
        """Print application header"""
        print("\n" + "="*80)
        print("  FINAPP - Kenya Investment Advisor".center(80))
        print("  Comprehensive Investment Analysis & Recommendations".center(80))
        print("="*80 + "\n")
    
    def print_disclaimer(self):
        """Print important disclaimer"""
        disclaimer = """
╔════════════════════════════════════════════════════════════════════════════╗
║                         IMPORTANT DISCLAIMER                              ║
║                                                                            ║
║ This tool provides DECISION SUPPORT ONLY and is NOT financial advice.    ║
║ Please consult with a licensed financial advisor before investing.        ║
║                                                                            ║
║ Historical performance does not guarantee future results.                 ║
║ All investments carry risk, including potential loss of principal.        ║
║ Past market conditions may not repeat.                                    ║
╚════════════════════════════════════════════════════════════════════════════╝
        """
        print(disclaimer)
    
    def get_user_inputs(self) -> Dict:
        """Collect investment parameters from user"""
        print("\n" + "-"*80)
        print("STEP 1: PROVIDE YOUR INVESTMENT DETAILS")
        print("-"*80 + "\n")
        
        # Amount
        while True:
            try:
                amount_str = input("Investment Amount (KES): ").strip()
                amount = int(amount_str)
                if amount < 100:
                    print("❌ Minimum investment is KES 100. Please try again.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")
        
        # Duration
        while True:
            try:
                duration = int(input("Investment Duration (months, minimum 6): ").strip())
                if duration < 6:
                    print("❌ Minimum duration is 6 months.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")
        
        # Risk appetite
        print("\nRisk Appetite (select one):")
        print("  1. Low (Capital preservation)")
        print("  2. Medium (Balanced growth)")
        print("  3. High (Aggressive growth)")
        
        while True:
            choice = input("\nSelect (1/2/3): ").strip()
            if choice == "1":
                risk = "Low"
                break
            elif choice == "2":
                risk = "Medium"
                break
            elif choice == "3":
                risk = "High"
                break
            else:
                print("❌ Please select 1, 2, or 3.")
        
        return {
            'amount': amount,
            'duration_months': duration,
            'risk_appetite': risk,
        }
    
    def initialize_analysis(self):
        """Fetch market data and initialize analyzers"""
        print("\n" + "-"*80)
        print("STEP 2: GATHERING MARKET DATA")
        print("-"*80)
        
        print("\n📊 Fetching latest Kenyan market data...")
        self.market_data = self.data_collector.get_all_market_data()
        
        print("✓ Treasury yields updated")
        print("✓ Money market rates updated")
        print("✓ NSE performance loaded")
        print("✓ Macro indicators loaded")
        print("✓ Fixed deposit rates updated")
        
        # Initialize analyzers
        self.risk_analyzer = RiskAnalyzer(self.market_data)
        self.recommendation_engine = RecommendationEngine(self.market_data, {})
        
        print(f"\n✓ Market data updated as of {self.market_data['timestamp'][:10]}")
    
    def display_market_overview(self):
        """Display current market conditions"""
        print("\n" + "-"*80)
        print("CURRENT KENYAN MARKET CONDITIONS")
        print("-"*80)
        
        macro = self.market_data['macro']
        print(f"\n💹 Macroeconomic Indicators:")
        print(f"   • Inflation Rate: {macro['inflation_rate']}%")
        print(f"   • Central Bank Rate (CBR): {macro['cbr']}%")
        print(f"   • Base Lending Rate: {macro['base_lending_rate']}%")
        print(f"   • USD/KES Rate: {macro['usd_kes_rate']}")
        print(f"   • Economic Outlook: {macro['economic_outlook']}")
        
        print(f"\n📈 Treasury Instruments (Current Yields):")
        treasury = self.market_data['treasury']
        print(f"   • 91-Day TB: {treasury['91_day_tb']['yield']}%")
        print(f"   • 182-Day TB: {treasury['182_day_tb']['yield']}%")
        print(f"   • 364-Day TB: {treasury['364_day_tb']['yield']}%")
        print(f"   • 2-Year Bond: {treasury['2_year_bond']['yield']}%")
        
        print(f"\n💰 Money Market Fund Yields:")
        mmf = self.market_data['money_market']
        for fund, data in list(mmf.items())[:3]:
            print(f"   • {fund.replace('_', ' ').title()}: {data['yield']}%")
        
        print(f"\n📊 NSE Market Performance:")
        nse = self.market_data['nse']
        print(f"   • NSE-20 Index: {nse['nse_20_index']['current']}")
        print(f"   • 6-Month Return: {nse['nse_20_index']['6m_return']}%")
        print(f"   • YTD Return: {nse['nse_20_index']['ytd_return']}%")
        print(f"   • Average P/E Ratio: {nse['nse_20_index']['pe_ratio']}")
    
    def display_risk_analysis(self, user_input: Dict):
        """Display risk analysis for recommended instrument"""
        print("\n" + "-"*80)
        print("STEP 3: RISK FACTOR ANALYSIS")
        print("-"*80)
        
        # Analyze main recommendation
        recommendation = self.recommendation_engine.generate_recommendation(user_input)
        instrument = recommendation['primary_recommendation']['instrument']
        
        risk_profile = self.risk_analyzer.analyze_equity_risk(
            user_input['amount'], 
            user_input['duration_months']
        ) if 'Equity' in instrument else self.risk_analyzer.analyze_treasury_risk(
            user_input['amount'], 
            user_input['duration_months']
        )
        
        print(f"\n🎯 Investment: {instrument}")
        print(f"📊 Overall Risk Rating: {risk_profile['risk_rating']}")
        print(f"📋 Assessment: {risk_profile['overall_assessment']}")
        
        print(f"\n🚨 Risk Factors Identified:")
        for i, factor in enumerate(risk_profile['risk_factors'], 1):
            severity_icon = "🔴" if factor.severity == "High" else "🟡" if factor.severity == "Medium" else "🟢"
            print(f"\n   {i}. {severity_icon} {factor.name} [{factor.severity}]")
            print(f"      Description: {factor.description}")
            print(f"      Mitigation: {factor.mitigation}")
    
    def display_recommendation(self, user_input: Dict):
        """Display final investment recommendation"""
        print("\n" + "="*80)
        print("STEP 4: INVESTMENT RECOMMENDATION")
        print("="*80)
        
        recommendation = self.recommendation_engine.generate_recommendation(user_input)
        primary = recommendation['primary_recommendation']
        
        print(f"\n✅ PRIMARY RECOMMENDATION: {primary['instrument']}")
        print(f"\n{'Category:':<20} {primary['category']}")
        print(f"{'Risk Rating:':<20} {primary['risk_rating']}")
        print(f"{'Liquidity:':<20} {primary['liquidity']}")
        print(f"{'Expected Return:':<20} {primary['expected_return']}% p.a.")
        
        print(f"\n💰 FINANCIAL PROJECTIONS (for KES {user_input['amount']:,.0f}):")
        print(f"{'Initial Investment:':<25} KES {user_input['amount']:,.0f}")
        print(f"{'Expected Earnings:':<25} KES {primary['earnings']:,.0f}")
        print(f"{'Final Value:':<25} KES {primary['final_value']:,.0f}")
        print(f"{'Investment Period:':<25} {user_input['duration_months']} months")
        
        print(f"\n✨ PROS:")
        for pro in primary['pros']:
            print(f"   ✓ {pro}")
        
        print(f"\n⚠️  CONS:")
        for con in primary['cons']:
            print(f"   ✗ {con}")
        
        # Display scenarios
        print(f"\n📊 SCENARIOS (6-Month Holding Period):")
        scenarios = recommendation['scenarios']
        
        print(f"\n   🟢 BEST CASE: {scenarios['best_case']['description']}")
        print(f"      Return: {scenarios['best_case']['return_percent']}% | Final Value: KES {scenarios['best_case']['final_value']:,.0f}")
        
        print(f"\n   🟡 BASE CASE: {scenarios['base_case']['description']}")
        print(f"      Return: {scenarios['base_case']['return_percent']}% | Final Value: KES {scenarios['base_case']['final_value']:,.0f}")
        
        print(f"\n   🔴 WORST CASE: {scenarios['worst_case']['description']}")
        print(f"      Return: {scenarios['worst_case']['return_percent']}% | Final Value: KES {scenarios['worst_case']['final_value']:,.0f}")
        
        # Display alternatives
        print(f"\n🔄 ALTERNATIVE OPTIONS:")
        for i, alt in enumerate(recommendation['alternatives'], 1):
            print(f"\n   {i}. {alt['instrument']}")
            print(f"      Category: {alt['category']}")
            print(f"      Return: {alt['expected_return']}% | Final Value: KES {alt['final_value']:,.0f}")
            print(f"      Risk: {alt['risk_rating']} | Liquidity: {alt['liquidity']}")
    
    def display_action_steps(self, user_input: Dict):
        """Display specific action steps to invest"""
        print("\n" + "="*80)
        print("STEP 5: ACTION STEPS TO INVEST")
        print("="*80)
        
        recommendation = self.recommendation_engine.generate_recommendation(user_input)
        instrument = recommendation['primary_recommendation']['instrument']
        
        print(f"\n📋 TO INVEST IN {instrument.upper()}:\n")
        
        if 'Treasury' in instrument:
            print("   1. Visit https://www.cbk.go.ke/ (Central Bank of Kenya)")
            print("   2. Look for 'Upcoming Auctions' or Treasury Bills/Bonds section")
            print("   3. Register as an investor if you haven't already")
            print("   4. Submit your bid through your bank or directly to CBK")
            print("   5. Await confirmation of allocation")
            print("   6. Funds will be deposited to your account on settlement date")
        elif 'Money Market' in instrument:
            print("   1. Choose a money market fund provider:")
            print("      • Barclays Money Market Fund")
            print("      • Equity Money Market Fund")
            print("      • Stanchart Money Market Fund")
            print("   2. Visit their website or mobile app")
            print("   3. Complete KYC registration (ID, proof of address)")
            print("   4. Link your bank account")
            print("   5. Upload initial investment amount")
            print("   6. Confirm transaction - funds typically reflect within 24 hours")
        elif 'Fixed Deposit' in instrument:
            print("   1. Choose your preferred bank:")
            print("      • Equity Bank")
            print("      • Stanchart")
            print("      • Barclays")
            print("      • Co-op Bank")
            print("   2. Visit bank branch or use online banking")
            print("   3. Select Fixed Deposit product")
            print("   4. Enter amount and duration")
            print("   5. Confirm rate (should be locked in writing)")
            print("   6. Deposit funds - FD starts immediately")
        else:  # Equities
            print("   1. Open a CDS (Central Depository System) account:")
            print("      • Visit NSE offices or authorized agents")
            print("      • Provide KYC documents")
            print("      • Get your account number")
            print("   2. Choose a stockbroker:")
            print("      • Kenia Securities")
            print("      • Standard Chartered Securities")
            print("      • CfC Stanbic")
            print("   3. Sign broking agreement and fund your account")
            print("   4. Place buy orders through broker's platform")
            print("   5. Settle trades (T+3 settlement)")
        
        print(f"\n⏰ TIMELINE:")
        print(f"   • Minimum holding period: {user_input['duration_months']} months")
        print(f"   • Expected maturity/review date: {self._calculate_maturity_date(user_input['duration_months'])}")
        print(f"   • Set reminder to reassess or reinvest")
    
    def _calculate_maturity_date(self, months: int) -> str:
        """Calculate approximate maturity date"""
        from datetime import datetime, timedelta
        future_date = datetime.now() + timedelta(days=months*30)
        return future_date.strftime("%B %d, %Y")
    
    def run(self):
        """Run the complete investment advisor workflow"""
        self.print_header()
        self.print_disclaimer()
        
        # Step 1: Collect user inputs
        user_input = self.get_user_inputs()
        
        # Step 2: Initialize analysis and fetch data
        self.initialize_analysis()
        
        # Display market overview
        self.display_market_overview()
        
        # Step 3: Risk analysis
        self.display_risk_analysis(user_input)
        
        # Step 4: Recommendation
        self.display_recommendation(user_input)
        
        # Step 5: Action steps
        self.display_action_steps(user_input)
        
        # Save report
        self.save_report(user_input)
        
        print("\n" + "="*80)
        print("Thank you for using FINAPP".center(80))
        print("For more information, visit: [website]".center(80))
        print("="*80 + "\n")
    
    def save_report(self, user_input: Dict):
        """Save analysis report to file"""
        recommendation = self.recommendation_engine.generate_recommendation(user_input)
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'user_input': user_input,
            'recommendation': recommendation,
            'market_conditions': {
                'inflation': self.market_data['macro']['inflation_rate'],
                'cbr': self.market_data['macro']['cbr'],
            }
        }
        
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = f"data/{filename}"
        
        try:
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            print(f"\n📄 Report saved to: {filepath}")
        except Exception as e:
            print(f"⚠️  Could not save report: {e}")

if __name__ == "__main__":
    app = FinAppCLI()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Application interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)
