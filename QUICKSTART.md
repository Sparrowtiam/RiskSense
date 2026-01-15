# FINAPP - Quick Start Guide

## One-Time Setup (Already Completed!)

✓ Virtual environment created  
✓ Dependencies installed  
✓ All modules built and tested  

---

## How to Run FinApp

### Step 1: Open PowerShell Terminal
```
Windows Key + X → Windows PowerShell (Admin)
```

### Step 2: Navigate to FinApp Directory
```powershell
cd c:\Users\HP\FinApp
```

### Step 3: Activate Virtual Environment
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your terminal prompt.

### Step 4: Run the Application
```powershell
python app.py
```

---

## What to Expect

The application will guide you through these steps:

### Step 1: Provide Investment Details
```
Investment Amount (KES): [Enter amount]
Investment Duration (months, minimum 6): [Enter months]
Risk Appetite (select one):
  1. Low (Capital preservation)
  2. Medium (Balanced growth)
  3. High (Aggressive growth)
Select (1/2/3): [Enter choice]
```

### Step 2: Market Data Collection
The application fetches:
- Treasury yields
- Money market rates
- NSE performance
- Fixed deposit rates
- Macroeconomic data

### Step 3: Analysis
You'll receive:
- Current market overview
- Risk analysis for your chosen investment
- Detailed recommendation
- Financial projections
- Action steps to invest

### Step 4: Report
A JSON report is automatically saved to `data/` directory for your records.

---

## Example Recommendations

### For Conservative Investors (Low Risk)
**Recommendation**: Government Treasury Bills
- 91-Day TB: 16.85% p.a.
- Capital fully guaranteed
- Low volatility

### For Balanced Investors (Medium Risk)
**Recommendation**: Money Market Funds
- Average: 16.3% p.a.
- Good liquidity
- Professional management

### For Aggressive Investors (High Risk)
**Recommendation**: NSE Blue-Chip Equities
- 6-Month Historical: 12.5% - 22.1%
- Highest growth potential
- Higher volatility

---

## Investment Options Available

1. **Treasury Bills/Bonds** - 16.85% - 18.10%
   - Best for: Capital preservation
   - Risk: Low

2. **Money Market Funds** - ~16.3%
   - Best for: Balanced approach
   - Risk: Low-Medium

3. **Fixed Deposits** - 15.3% - 16.5%
   - Best for: Fixed income
   - Risk: Low

4. **NSE Equities** - 12.5% - 22.1% (6m)
   - Best for: Growth
   - Risk: High

5. **REITs** - Property Investment
   - Best for: Diversification
   - Risk: Medium

---

## Quick Test

To verify everything is working:

```powershell
cd c:\Users\HP\FinApp
venv\Scripts\python test_simple.py
```

Expected output: Successful recommendation for KES 50,000 investment.

---

## Troubleshooting

### Issue: "venv is not activated"
**Solution**: 
```powershell
venv\Scripts\Activate.ps1
```

### Issue: "ModuleNotFoundError: No module named 'src'"
**Solution**: Make sure you're in the `c:\Users\HP\FinApp` directory:
```powershell
cd c:\Users\HP\FinApp
python app.py
```

### Issue: "Permission denied" on Activate.ps1
**Solution**: Enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Key Features Explained

### 1. Market Data Collection
Real-time Kenyan market data including:
- CBK Treasury yields
- NSE stock performance
- Bank FD rates
- Economic indicators

### 2. Risk Analysis
Comprehensive identification of:
- Market risks
- Inflation impact
- Liquidity constraints
- Default risks
- Mitigation strategies

### 3. Recommendations
Personalized based on:
- Investment amount
- Investment period
- Risk tolerance
- Market conditions

### 4. Scenario Analysis
Three projections:
- Best case (+5% variance)
- Base case (expected)
- Worst case (-5% variance)

---

## Investment Duration Requirements

- **Minimum**: 6 months
- **Examples**:
  - 6 months: 91-day TB (4 cycles)
  - 12 months: 1-year fixed deposit
  - 24+ months: Long-term equities

---

## Risk Ratings

| Rating | Description | Examples |
|--------|-------------|----------|
| Low | Capital preservation | Treasury, Fixed Deposits |
| Medium | Balanced growth | Money Market Funds, REITs |
| High | Aggressive growth | NSE Equities |

---

## Current Market Conditions (Jan 15, 2026)

- **Inflation Rate**: 4.8%
- **CBR (Policy Rate)**: 10.0%
- **Base Lending Rate**: 13.0%
- **USD/KES Rate**: 127.45
- **Economic Outlook**: Moderate growth
- **NSE 6-Month Return**: 8.2% - 18.3%

---

## Important Disclaimers

⚠️ **NOT Financial Advice**
- Use for decision-support only
- Consult licensed advisors
- Past performance ≠ future results
- All investments carry risk
- Market conditions change rapidly

---

## File Locations

| Item | Location |
|------|----------|
| Main App | `c:\Users\HP\FinApp\app.py` |
| Configuration | `c:\Users\HP\FinApp\config.ini` |
| Reports | `c:\Users\HP\FinApp\data\` |
| Documentation | `c:\Users\HP\FinApp\README.md` |
| Test Script | `c:\Users\HP\FinApp\test_simple.py` |

---

## Next Steps

1. ✓ Run the application: `python app.py`
2. ✓ Enter your investment details
3. ✓ Review the recommendation
4. ✓ Check the action steps
5. ✓ Review the saved report

---

## Support

For issues or questions:
1. Check the README.md file
2. Review PROJECT_SUMMARY.md
3. Run test_simple.py to verify setup
4. Check config.ini for settings

---

**Version**: 1.0.0  
**Last Updated**: January 15, 2026  
**Status**: Ready to Use
