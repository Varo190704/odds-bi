# Odds BI Platform

A small Business Intelligence project built to demonstrate ETL design, basic data processing and dashboard development. The goal is to track changes in betting odds and highlight volatility patterns.

## Features
- End-to-end ETL pipeline (CSV → SQLite → transformed table)
- Streamlit dashboard with KPIs, filters and visualizations
- Data quality checks (missing values, duplicates, outliers)
- Button-triggered ETL execution
- Persistent storage using SQLite

## Stack
- Python
- Streamlit
- SQLite
- Pandas
- Plotly

## Running locally
```bash
pip install -r requirements.txt
streamlit run app.py
