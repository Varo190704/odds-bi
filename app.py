import streamlit as st
import pandas as pd
import plotly.express as px
from db import init_db, get_connection
from etl import run_etl, LOGS
import numpy as np

st.set_page_config(page_title="Odds Dashboard", layout="wide")

init_db()

st.title("Odds Dashboard")

tab1, tab2, tab3 = st.tabs(["Dashboard", "Run ETL", "Data Quality"])

# ---------------- ETL ----------------
with tab2:
    st.header("ETL")
    if st.button("Run ETL"):
        logs = run_etl()
        st.success("ETL finished")
        st.text("\n".join(logs))

# ---------------- Dashboard ----------------
with tab1:
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM codds", conn)
    conn.close()

    if df.empty:
        st.info("No data available. Run the ETL first.")
    else:
        match_ids = sorted(df["matchid"].unique())
        selected = st.selectbox("Match", match_ids)

        data = df[df["matchid"] == selected]

        # KPIs
        c1, c2, c3 = st.columns(3)
        c1.metric("Avg % Change", f"{data['pctchange'].mean():.2f}%")
        c2.metric("Max % Change", f"{data['pctchange'].max():.2f}%")
        c3.metric("Volatility Flags", int(data["volat"].sum()))

        # Line chart
        fig1 = px.line(
            data,
            x="time",
            y="liodds",
            title="Live Odds Over Time",
            markers=True
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Bar chart
        fig2 = px.bar(
            data,
            x="time",
            y="pctchange",
            title="Percentage Change",
            color="volat"
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Data")
        st.dataframe(data)

# ---------------- Data Quality ----------------
with tab3:
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM codds", conn)
    conn.close()

    if df.empty:
        st.info("No data available. Run the ETL first.")
    else:
        st.subheader("Missing values")
        st.write(df.isna().sum())

        st.subheader("Duplicate rows")
        st.write(df.duplicated().sum())

        st.subheader("Outliers (Z-score > 3)")
        df["z"] = (df["pctchange"] - df["pctchange"].mean()) / df["pctchange"].std()
        outliers = df[df["z"].abs() > 3]
        st.dataframe(outliers)
