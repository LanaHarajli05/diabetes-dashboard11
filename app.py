import streamlit as st
import pandas as pd
import plotly.express as px  # ✅ Required for charts

st.set_page_config(page_title="🩺 Diabetes Analytics Dashboard", layout="wide")

# Load data
df = pd.read_csv("diabetes_clean.csv")

# Sidebar filters
st.sidebar.title("Filters")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
age_group_filter = st.sidebar.multiselect("Select Age Group", options=df["age_group"].unique(), default=df["age_group"].unique())
smoking_filter = st.sidebar.multiselect("Select Smoking History", options=df["smoking_history"].unique(), default=df["smoking_history"].unique())

# Filter data
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age_group"].isin(age_group_filter)) &
    (df["smoking_history"].isin(smoking_filter))
]

# Title
st.title("🩺 Diabetes Analytics Dashboard")
st.markdown("Analyze diabetes trends by demographic and health factors.")

# Row 1
col1, col2 = st.columns(2)
with col1:
    st.subheader("Diabetes by Age Group")
    age_group_chart = filtered_df.groupby("age_group")["diabetes"].mean().reset_index()
    fig1 = px.bar(age_group_chart, x="age_group", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "age_group": "Age Group"})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Diabetes by Gender")
    gender_chart = filtered_df.groupby("gender")["diabetes"].mean().reset_index()
    fig2 = px.bar(gender_chart, x="gender", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "gender": "Gender"})
    st.plotly_chart(fig2, use_container_width=True)

# Row 2
col3, col4 = st.columns(2)
with col3:
    st.subheader("Diabetes by Smoking History")
    smoke_chart = filtered_df.groupby("smoking_history")["diabetes"].mean().reset_index()
    fig3 = px.bar(smoke_chart, x="smoking_history", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "smoking_history": "Smoking History"})
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("HbA1c vs Diabetes")
    fig4 = px.box(filtered_df, x="diabetes", y="HbA1c_level",
                  labels={"diabetes": "Diabetes", "HbA1c_level": "HbA1c Level"})
    st.plotly_chart(fig4, use_container_width=True)

# Optional: Reduce vertical spacing
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

