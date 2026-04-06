import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("User Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # FIX: Clean column names
    df.columns = df.columns.str.strip()

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Age Distribution
    if "Age" in df.columns:
        st.subheader("Age Distribution")
        plt.figure()
        df["Age"].dropna().astype(int).hist()
        plt.xlabel("Age")
        plt.ylabel("Count")
        st.pyplot(plt)
    else:
        st.error("Age column not found")

    # Gender Distribution
    if "Gender" in df.columns:
        st.subheader("Gender Distribution")
        plt.figure()
        df["Gender"].value_counts().plot(kind="bar")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        st.pyplot(plt)
    else:
        st.error("Gender column not found")

    # Basic Stats
    st.subheader("Basic Statistics")
    st.write(df.describe())
