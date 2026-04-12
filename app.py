import streamlit as st
import wrds
import pandas as pd
import matplotlib.pyplot as plt

# 页面配置
st.set_page_config(page_title="WRDS Stock Analyzer", layout="wide")
st.title("📈 WRDS Stock Analyzer (ACC102 Track4)")
st.markdown("Built with Python + SQL + Streamlit")

# 用户输入
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Enter Ticker", "AAPL")
start_date = st.sidebar.text_input("Start Date (YYYY-MM-DD)", "2020-01-01")

# WRDS 连接函数
def load_data(ticker, start):
    try:
        # 🔥 这里必须改成你的 WRDS 用户名 🔥
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
        
        # 数据清洗
        df = df.dropna()
        df['date'] = pd.to_datetime(df['date'])
        df = df.rename(columns={'prc': 'Price', 'ret': 'Return'})
        return df
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return None

# 点击按钮运行
if st.sidebar.button("Analyze Stock"):
    df = load_data(ticker, start_date)
    
    if df is not None and not df.empty:
        st.success("✅ Data loaded successfully from WRDS!")
        
        # 显示数据
        st.dataframe(df.head(10))
        
        # 股价图
        st.subheader("Stock Price Trend")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(df['date'], df['Price'], color='blue')
        st.pyplot(fig1)
        
        # 收益率图
        st.subheader("Monthly Return")
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.bar(df['date'], df['Return'], color='orange', alpha=0.7)
        st.pyplot(fig2)
        
        # 分析结论
        st.subheader("Key Insights")
        st.write(f"Average Return: {df['Return'].mean():.4f}")
        st.write("Data Source: WRDS CRSP Database")