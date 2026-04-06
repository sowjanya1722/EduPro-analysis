import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EduPro Instructor & Course Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("your_file.csv")  # change this if needed
    return df

# For now, we simulate merged_df
# Replace this with your actual dataset later
st.write("Upload your dataset to proceed")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    merged_df = pd.read_csv(uploaded_file)

    st.subheader("Course Category Performance")
    category = merged_df.groupby("CourseCategory")["CourseRating"].mean()

    fig, ax = plt.subplots()
    category.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.subheader("Course Level Performance")
    level = merged_df.groupby("CourseLevel")["CourseRating"].mean()

    fig2, ax2 = plt.subplots()
    level.plot(kind="bar", ax=ax2)
    st.pyplot(fig2)
