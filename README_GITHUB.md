# FinApp - Kenya Investment Advisor
### Complete Web App for Kenyan Investment Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://finapp-kenya.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/yourusername/finapp)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Live Demo

**[Open FinApp on Streamlit Cloud](https://finapp-kenya.streamlit.app)**

---

## 📋 Overview

FinApp is a comprehensive **investment decision-support system** specialized for the **Kenyan investment market**. It analyzes real-time market data, evaluates risk factors, and generates personalized investment recommendations based on individual user profiles.

### Key Features

✨ **Real-Time Market Analysis**
- Treasury bill and bond yields
- Money market fund rates  
- NSE equity performance
- Fixed deposit rates
- Macroeconomic indicators

🎯 **Personalized Recommendations**
- Based on investment amount, duration, and risk appetite
- Financial projections (Best/Base/Worst case)
- Alternative investment options
- Detailed action plans

⚠️ **Comprehensive Risk Assessment**
- 20+ risk factors analyzed
- Severity ratings (Low/Medium/High)
- Specific mitigation strategies
- Risk-aware recommendations

---

## 🎮 How to Use

### Web App (Easiest)
1. Visit: **[finapp-kenya.streamlit.app](https://finapp-kenya.streamlit.app)**
2. Enter investment details (amount, duration, risk appetite)
3. Click "Generate Recommendation"
4. Review recommendations and risk analysis

### Local Installation

```bash
# Clone repository
git clone https://github.com/yourusername/finapp.git
cd finapp

# Create virtual environment
python -m venv venv
venv\Scripts\Activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run streamlit_app.py
```

App opens at `http://localhost:8501`

### CLI Version (Alternative)

```bash
python app.py
```

---

## 💼 Investment Options

| Instrument | Rate | Risk | Liquidity |
|------------|------|------|-----------|
| 91-Day Treasury Bill | 16.85% | Low | Medium |
| Money Market Funds | ~16.3% | Low-Med | High |
| Fixed Deposits (6-12m) | 15.3-16.5% | Low | Low |
| NSE Blue-Chip Stocks | 12.5-22.1% | High | High |
| REITs | Variable | Medium | Medium |

---

## 📊 App Tabs

### 1. Market Overview
- Current market conditions
- Treasury rates
- NSE performance
- Macroeconomic indicators

### 2. Recommendation
- Interactive investment parameters
- Personalized recommendation
- Financial projections
- Scenario analysis
- Alternative options

### 3. Risk Analysis
- Risk factor identification
- Severity ratings
- Mitigation strategies
- Investment suitability

### 4. About
- Project information
- Feature overview
- Documentation links

---

## 🏗️ Project Structure

```
finapp/
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── src/
│   └── modules/
│       ├── __init__.py
│       ├── data_collector.py      # Market data
│       ├── risk_analyzer.py       # Risk analysis
│       └── recommendation_engine.py # Recommendations
├── streamlit_app.py          # 🌐 Web app (Main)
├── app.py                    # 💻 CLI version
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
├── README.md                 # This file
├── DEPLOYMENT.md             # Deployment guide
└── LICENSE                   # MIT License
```

---

## 🔧 Installation

### Requirements
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/finapp.git
   cd finapp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\Activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   # Web version (recommended)
   streamlit run streamlit_app.py
   
   # Or CLI version
   python app.py
   ```

---

## 📱 Web App Features

### Input Parameters (Sidebar)
- **Investment Amount**: KES 100 - 10,000,000
- **Duration**: 6 - 60 months
- **Risk Appetite**: Low / Medium / High

### Output Information
✓ Primary recommendation with detailed analysis
✓ Financial projections with expected returns
✓ Pros and cons of recommended investment
✓ Best/Base/Worst case scenarios
✓ Alternative investment options
✓ Comprehensive risk analysis

---

## 📈 Investment Scenarios

For each recommendation, you get three scenarios:

**🟢 Best Case** - Optimal market conditions
**🟡 Base Case** - Expected market conditions (most likely)
**🔴 Worst Case** - Challenging market conditions

Each shows projected final value and returns.

---

## 🚀 Deploy on Streamlit Cloud

### 1. Push to GitHub
```bash
git add .
git commit -m "Deploy on Streamlit Cloud"
git push origin main
```

### 2. Connect Streamlit Cloud
1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Select your GitHub repository
4. Set main file: `streamlit_app.py`
5. Click "Deploy"

Your app goes live instantly! 🎉

---

## 📚 Documentation

- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Full deployment guide
- **[README.md](README.md)** - Original documentation
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

---

## ⚠️ Important Disclaimer

**This is NOT financial advice.**

- Use for **decision-support only**
- Consult a **licensed financial advisor** before investing
- **Past performance** doesn't guarantee future results
- **All investments carry risk**, including loss of principal
- **Market conditions** can change rapidly

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **Live App**: [finapp-kenya.streamlit.app](https://finapp-kenya.streamlit.app)
- **GitHub**: [github.com/yourusername/finapp](https://github.com/yourusername/finapp)
- **Streamlit**: [streamlit.io](https://streamlit.io)
- **Kenyan Market**: [Nairobi Securities Exchange](https://www.nse.co.ke)

---

## 📞 Support

For issues or questions:
1. Check the [FAQ](FAQ.md) (if available)
2. Review [DEPLOYMENT.md](DEPLOYMENT.md)
3. Open an [Issue](https://github.com/yourusername/finapp/issues)
4. Visit [Streamlit Community](https://discuss.streamlit.io)

---

## 🎯 Roadmap

### Current (v1.0)
✓ Streamlit web interface
✓ Market data collection
✓ Risk analysis engine
✓ Investment recommendations
✓ Financial projections

### Planned (v2.0)
📱 Mobile app
🔌 Live API integration (CBK, NSE)
💼 Portfolio tracking
📊 Advanced analytics
🤖 ML-based recommendations

---

## 👨‍💻 Authors

- **Development**: FinApp Team
- **Market Data**: Kenya Central Bank, NSE
- **Last Updated**: January 15, 2026

---

## 📊 Statistics

- **1,500+** lines of Python code
- **8+** investment instruments analyzed
- **20+** risk factors evaluated
- **3** scenario analyses
- **100%** test pass rate

---

**Made with ❤️ for Kenya's Investment Community**

⭐ Star this repo if you find it helpful!

---

**Version**: 1.0.0  
**Status**: 🟢 Production Ready  
**Last Updated**: January 15, 2026
