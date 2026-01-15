# FINAPP - Kenya Investment Advisor

A comprehensive Python application for analyzing and recommending suitable investment opportunities in Kenya based on real-time market data, risk analysis, and individual user profiles.

## Features

✓ **Real-time Market Data Collection**
- Treasury bill and bond yields
- Money market fund rates
- NSE stock market performance
- Fixed deposit rates from major banks
- Macroeconomic indicators (inflation, interest rates, currency)

✓ **Comprehensive Risk Analysis**
- Risk factor identification and severity rating
- Risk mitigation strategies
- Risk profiles for each investment type:
  - Government Treasury Bills/Bonds
  - Money Market Funds
  - Fixed Deposits
  - NSE Equities
  - REITs

✓ **Intelligent Recommendation Engine**
- Personalized recommendations based on:
  - Investment amount
  - Investment duration (minimum 6 months)
  - Risk appetite (Low, Medium, High)
- Final value projections
- Best/Base/Worst case scenarios
- Alternative investment options

✓ **User-Friendly CLI Interface**
- Step-by-step guided investment analysis
- Clear investment actionsteps
- Report generation and saving

## Project Structure

```
FinApp/
├── src/
│   └── modules/
│       ├── __init__.py
│       ├── data_collector.py      # Market data collection
│       ├── risk_analyzer.py       # Risk analysis engine
│       └── recommendation_engine.py  # Recommendation logic
├── venv/                          # Virtual environment
├── data/                          # Output reports directory
├── app.py                         # Main CLI application
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Installation

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\Activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

### Step-by-Step Process

1. **Provide Investment Details**
   - Investment amount (KES)
   - Duration (minimum 6 months)
   - Risk appetite (Low/Medium/High)

2. **Market Data Collection**
   - Application fetches real-time Kenyan market data
   - Displays current market conditions

3. **Risk Analysis**
   - Identifies relevant risk factors
   - Provides risk severity ratings
   - Suggests risk mitigation strategies

4. **Investment Recommendation**
   - Primary recommendation based on profile
   - Financial projections (initial, earnings, final value)
   - Pros and cons analysis
   - Best/Base/Worst case scenarios
   - Alternative investment options

5. **Action Steps**
   - Specific instructions on how to invest
   - Investment platforms and procedures
   - Timeline and next steps

## Investment Options Analyzed

### 1. Government Treasury Bills/Bonds
- **Duration**: 91-day, 182-day, 364-day bills; 2-5-10 year bonds
- **Current Yields**: 16.85% - 18.10% p.a.
- **Risk**: Low
- **Best For**: Capital preservation

### 2. Money Market Funds
- **Current Yields**: ~16.3% p.a. average
- **Risk**: Low-Medium
- **Liquidity**: High
- **Best For**: Balanced approach

### 3. Fixed Deposits
- **Duration**: 6-12 months
- **Current Rates**: 15.3% - 16.5% p.a.
- **Risk**: Low
- **Liquidity**: Low
- **Best For**: Specific financial goals

### 4. NSE Equities (Blue-Chip Stocks)
- **Average Returns**: 12.5% - 22.1% (6-month historical)
- **Risk**: High
- **Liquidity**: High
- **Best For**: Aggressive growth

## Risk Ratings

- **Low Risk**: Suitable for capital preservation (Treasury, FDs)
- **Medium Risk**: Balanced risk-return profile (MMFs, REITs)
- **High Risk**: Suitable for growth-oriented investors (Equities)

## Market Data Sources

The application simulates real-time data collection from:
- Central Bank of Kenya (CBK) - Treasury data
- NSE - Equity market data
- Commercial banks - Fixed deposit rates
- Fund managers - Money market fund data

**Note**: For production use, integrate with actual market data APIs:
- CBK Open Data API
- NSE Market Data Feed
- CMA Data Portal
- Bank APIs

## Important Disclaimers

⚠️ **This is NOT Financial Advice**

- This tool provides decision support only
- Consult a licensed financial advisor before investing
- Past performance does not guarantee future results
- All investments carry risk, including potential loss of principal
- Market conditions can change rapidly

## Recommendations by Risk Profile

### Low Risk Profile (Capital Preservation)
**Recommended**: Government Treasury Bills/Bonds
- Guaranteed returns
- No default risk (government backed)
- Fixed, predictable income
- Best for emergency funds or safe reserves

**Consider if**: You prioritize security over returns

### Medium Risk Profile (Balanced Growth)
**Recommended**: Money Market Funds
- Balance of safety and returns
- Good liquidity
- Professional management
- Can access funds when needed

**Consider if**: You want steady growth with flexibility

### High Risk Profile (Aggressive Growth)
**Recommended**: NSE Blue-Chip Equities
- Highest return potential
- Dividend income
- Inflation hedge
- Long-term wealth building

**Consider if**: You can tolerate volatility and have time horizon

## Output Files

The application generates reports in `data/` directory:
- Format: `report_YYYYMMDD_HHMMSS.json`
- Contains: User inputs, recommendations, market conditions
- Useful for: Record keeping, comparing recommendations over time

## Testing

Run the test script to verify installation:
```bash
python test_simple.py
```

Expected output shows a sample recommendation for KES 50,000 investment.

## Dependencies

- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management

## Future Enhancements

- [ ] Integration with live market data APIs
- [ ] Portfolio diversification recommendations
- [ ] Tax optimization strategies
- [ ] Web UI (Flask/Django)
- [ ] Mobile app version
- [ ] Historical performance tracking
- [ ] Email notifications
- [ ] Multi-currency support
- [ ] Comparison with global investments

## Support

For issues, questions, or suggestions, please contact the development team.

## License

Copyright (c) 2026. All rights reserved.

---

**Last Updated**: January 15, 2026
**Version**: 1.0.0
