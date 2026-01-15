"""
Test Streamlit app locally
Run: streamlit run streamlit_app.py
"""

import subprocess
import sys

def run_streamlit():
    """Run Streamlit app"""
    print("=" * 70)
    print("Starting Streamlit App - FinApp Kenya Investment Advisor")
    print("=" * 70)
    print("\nThe app will open at: http://localhost:8501")
    print("Press Ctrl+C to stop the server\n")
    
    subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    run_streamlit()
