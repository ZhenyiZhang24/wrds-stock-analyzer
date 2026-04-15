# wrds-stock-analyzer
ACC102 Track4 WRDS Stock Analyzer Tool
## Contributors

@ZhenyiZhang24

Xi’an Jiaotong-Liverpool University, ACC102 Track4

## 1. Project Introduction

This project is an interactive stock data analysis tool developed for ACC102 Track4 assignment. It is built with Python, Streamlit, and WRDS CRSP Database, aiming to provide a user-friendly interface for querying and visualizing stock data. The target users are students or beginners who need to conduct simple stock data analysis, as it allows easy operation without complex code input.

Core functions include: querying stock data by ticker and start date, automatically cleaning data, displaying structured data tables, and generating intuitive visualizations (stock price trend line and monthly return bar chart).

## 2. Data Source

The stock data used in this tool is fetched from the WRDS CRSP Database, which includes comprehensive stock price and return data. 

Accessed on: 16 April 2026

## 3. How to Run

To run this tool locally after cloning the repository, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/ZhenyiZhang24/wrds-stock-analyzer.git`

2. Enter the project folder: `cd wrds-stock-analyzer`

3. Install required dependencies: `pip install -r requirements.txt`

4. Run the Streamlit app: `streamlit run app.py`

5. A browser page will automatically open, where you can enter the stock ticker (e.g., AAPL, MSFT) and start date to analyze stock data.

## 4. Project Structure

The repository contains the following key files, with their specific uses:

- app.py: Core code file, including WRDS connection, SQL query, data cleaning, visualization, and Streamlit page construction.

- requirements.txt: Lists all required Python libraries (e.g., streamlit, wrds, pandas, matplotlib) for the tool to run smoothly.

- README.md: This document, providing detailed instructions on the project, data source, running steps, and project structure.

- .gitignore: Ignores unnecessary files (e.g., virtual environment files, cache files) to keep the repository clean.

- .pgpass (optional): Configuration file for WRDS automatic login, avoiding repeated input of account and password.

## 5. Key Outputs

After entering the stock ticker and start date and clicking the "Analyze Stock" button, the tool will generate the following outputs:

- Structured Data Table: Displays detailed stock data, including date, stock price, and return rate.

- Stock Price Trend Line: Visualizes the trend of stock prices from the specified start date to the present, helping to observe price changes intuitively.

- Monthly Return Bar Chart: Shows the monthly return rate of the stock, facilitating the analysis of short-term stock performance.
