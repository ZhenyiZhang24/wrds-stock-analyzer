import streamlit as st
import wrds
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="WRDS Stock Analyzer", layout="wide")
st.title("📈 WRDS Stock Analyzer (ACC102 Track4)")
st.markdown("Built with Python + SQL + Streamlit")

# User input area
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Enter Ticker", "AAPL")
start_date = st.sidebar.text_input("Start Date (YYYY-MM-DD)", "2020-01-01")

# WRDS connection and data loading function
def load_data(ticker, start):
    try:
        db = wrds.Connection(wrds_username="jennyjenny")
        
        sql = f"""
            SELECT a.date, a.prc, a.ret
            FROM crsp.msf a
            LEFT JOIN crsp.msfhdr b ON a.permno = b.permno
            WHERE b.htsymbol = '{ticker}' AND a.date >= '{start}'
            ORDER BY a.date
        """
        df = db.raw_sql(sql)
        db.close()
        
        # Data cleaning and formatting
        df = df.dropna()
        df['date'] = pd.to_datetime(df['date'])
        df = df.rename(columns={'prc': 'Price', 'ret': 'Return'})
        return df
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None

# Run analysis when button is clicked
if st.sidebar.button("Analyze Stock"):
    df = load_data(ticker, start_date)
    
    if df is not None and not df.empty:
        st.success("✅ Data loaded successfully from WRDS!")
        
        # Display the first 10 rows of data
        st.dataframe(df.head(10))
        
        # Plot stock price trend
        st.subheader("Stock Price Trend")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(df['date'], df['Price'], color='blue')
        st.pyplot(fig1)
        
        # Plot monthly return bar chart
        st.subheader("Monthly Return")
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.bar(df['date'], df['Return'], color='orange', alpha=0.7)
        st.pyplot(fig2)
        
        # Show key analysis results
        st.subheader("Key Insights")
        st.write(f"Average Return: {df['Return'].mean():.4f}")
        st.write("Data Source: WRDS CRSP Database")
