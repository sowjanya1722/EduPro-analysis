import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("User Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())
    st.subheader("Age Distribution")
    plt.figure()
    df["Age"].hist()
    plt.xlabel("Age")
    plt.ylabel("Count")
    st.pyplot(plt)

    st.subheader("Gender Distribution")
    plt.figure()
    df["Gender"].value_counts().plot(kind="bar")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    st.pyplot(plt)

    st.subheader("Basic Statistics")
    st.write(df.describe())
