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

## Using Your Own Data

If you want to use your own odds data, replace the contents of data/raw.csv with your dataset.
The file must include the following columns:

- matchid,matchname,time,preodds,liodds

#### Example

- matchid,matchname,time,preodds,liodds
- 1,Liverpool vs Chelsea,2025-01-12 14:05,1.85,1.78

#### Column Description

- matchid — Unique identifier for the match.

- matchname — Name or label of the match.

- time — Timestamp in YYYY-MM-DD HH:MM format.

- preodds — Opening or pre-match odds.

- liodds — Live odds captured at the given timestamp.

After editing the CSV, run the ETL again from the "Run ETL" tab in the dashboard to refresh the transformed data and visualizations.

## Running locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py