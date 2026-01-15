# Deployment Guide - GitHub & Streamlit

## Quick Start - Deploy on Streamlit Cloud in 3 Minutes

### Step 1: Push to GitHub

1. **Initialize Git Repository** (if not already done)
   ```bash
   cd c:\Users\HP\FinApp
   git init
   git add .
   git commit -m "Initial commit: FinApp Kenya Investment Advisor"
   ```

2. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Create repository named `finapp`
   - Follow the GitHub instructions to push

3. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/finapp.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Sign Up for Streamlit Cloud**
   - Go to https://streamlit.io/cloud
   - Click "Sign up" and authenticate with GitHub

2. **Deploy Your App**
   - Click "New app"
   - Select your `finapp` repository
   - Select branch: `main`
   - Set main file path to: `streamlit_app.py`
   - Click "Deploy"

3. **Access Your App**
   - Your app will be live at: `https://finapp-yourname.streamlit.app`
   - Share the link with others!

---

## File Structure for GitHub

```
finapp/
├── .github/                    # GitHub workflows (optional)
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── src/
│   └── modules/
│       ├── __init__.py
│       ├── data_collector.py
│       ├── risk_analyzer.py
│       └── recommendation_engine.py
├── streamlit_app.py           # Main Streamlit app
├── app.py                     # CLI version (alternative)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
└── LICENSE                    # License file (optional)
```

---

## Environment Setup for Local Testing

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Streamlit App Locally
```bash
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

---

## Streamlit Cloud Secrets (Optional)

If you need environment variables:

1. Go to your Streamlit Cloud app settings
2. Add secrets in the "Secrets" section:
   ```
   API_KEY = "your_key"
   ENVIRONMENT = "production"
   ```

3. Access in code:
   ```python
   import streamlit as st
   api_key = st.secrets["API_KEY"]
   ```

---

## GitHub Configuration Files

### .gitignore
Already created to exclude:
- Virtual environment (`venv/`)
- Python cache (`__pycache__/`)
- IDE files (`.vscode/`, `.idea/`)
- Environment files (`.env`)
- Data files
- Streamlit cache

### requirements.txt
Contains all dependencies:
```
requests==2.31.0
python-dotenv==1.0.0
streamlit==1.28.1
```

---

## Creating Additional Documentation for GitHub

### Create README.md (Already exists)
The existing README.md will be displayed on your GitHub repository home page.

### Create CONTRIBUTING.md (Optional)
For open-source contributions:
```bash
echo "# Contributing to FinApp

## How to Contribute
1. Fork the repository
2. Create a branch for your feature
3. Submit a pull request

## Issues
Report issues on the GitHub Issues page.
" > CONTRIBUTING.md
```

### Create LICENSE (Optional)
```bash
echo "MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge...
" > LICENSE
```

---

## Pushing to GitHub - Step by Step

### First Time Setup
```bash
# Navigate to project
cd c:\Users\HP\FinApp

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: FinApp Kenya Investment Advisor v1.0.0"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/finapp.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Future Updates
```bash
# Make changes, then:
git add .
git commit -m "Description of changes"
git push
```

---

## Streamlit App Features Deployed

✓ **Market Overview Tab**
- Real-time Kenyan market conditions
- Treasury instrument rates
- NSE performance metrics

✓ **Recommendation Tab**
- Interactive investment amount input
- Duration slider (6-60 months)
- Risk appetite selection (Low/Medium/High)
- Personalized recommendations
- Financial projections
- Best/Base/Worst case scenarios
- Alternative options

✓ **Risk Analysis Tab**
- Comprehensive risk factor analysis
- Risk severity ratings
- Mitigation strategies

✓ **About Tab**
- Project information
- Feature overview
- Usage guidelines

---

## GitHub Pages (Optional)

For additional documentation:

1. Go to repository settings
2. Under "Pages", select `main` branch
3. Upload documentation to `docs/` folder
4. Your docs will be at: `https://finapp-yourname.streamlit.app`

---

## Continuous Deployment

### Automatic Updates
Streamlit Cloud automatically deploys when you push to GitHub:
1. Make changes locally
2. Commit and push to GitHub
3. Streamlit Cloud detects changes
4. App automatically redeploys (usually within 1-2 minutes)

### Monitoring Deployments
- Check app logs in Streamlit Cloud dashboard
- View deployment history
- Manage app secrets and settings

---

## Troubleshooting

### App Won't Deploy
- Check `requirements.txt` format
- Ensure `streamlit_app.py` exists
- Verify no syntax errors
- Check Streamlit Cloud logs

### Dependencies Missing
```bash
# Reinstall all requirements
pip install --upgrade -r requirements.txt
```

### Port Already in Use
```bash
# Run on different port
streamlit run streamlit_app.py --server.port 8502
```

### Clear Streamlit Cache
```bash
# Windows
rmdir /s %USERPROFILE%/.streamlit

# Clear cache in app:
# Go to Settings (gear icon) → Clear cache
```

---

## Security Considerations

✓ Never commit `.env` files
✓ Never commit API keys
✓ Use Streamlit Cloud Secrets for sensitive data
✓ Keep dependencies updated
✓ Review `requirements.txt` before pushing

---

## Performance Tips for Streamlit Cloud

1. **Cache Data**
   ```python
   @st.cache_data
   def load_data():
       return expensive_operation()
   ```

2. **Limit API Calls**
   - Cache market data (currently done)
   - Refresh at reasonable intervals

3. **Optimize Images**
   - Use compressed images
   - Lazy load content

4. **Monitor App Metrics**
   - Check CPU/RAM usage
   - Optimize heavy computations

---

## Next Steps

1. ✓ Push code to GitHub
2. ✓ Deploy on Streamlit Cloud
3. ✓ Share app link
4. ✓ Gather user feedback
5. ✓ Plan enhancements

---

## Useful Links

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Cloud**: https://streamlit.io/cloud
- **GitHub Help**: https://docs.github.com
- **Python Requirements**: https://pip.pypa.io/en/latest/reference/requirements-file-format/

---

**Happy deploying! 🚀**
