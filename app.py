import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np  # Required for comorbidity logic

# Page configuration
st.set_page_config(page_title="Exploring Diabetes Risk Across Demographics and Clinical Indicators", layout="wide")

# Load data
df = pd.read_csv("diabetes_clean.csv")

# Sidebar filters
st.sidebar.title("Filters")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
age_group_filter = st.sidebar.multiselect("Select Age Group", options=df["age_group"].unique(), default=df["age_group"].unique())
smoking_filter = st.sidebar.multiselect("Select Smoking History", options=df["smoking_history"].unique(), default=df["smoking_history"].unique())
heart_disease_filter = st.sidebar.multiselect("Select Heart Disease", options=df["heart_disease"].unique(), default=df["heart_disease"].unique())
hypertension_filter = st.sidebar.multiselect("Select Hypertension", options=df["hypertension"].unique(), default=df["hypertension"].unique())

# Filter data
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age_group"].isin(age_group_filter)) &
    (df["smoking_history"].isin(smoking_filter)) &
    (df["heart_disease"].isin(heart_disease_filter)) &
    (df["hypertension"].isin(hypertension_filter))
]

# Dashboard title and intro
st.title("Exploring Diabetes Risk Across Demographics and Clinical Indicators")
st.markdown("""
This dashboard is built on a synthetic healthcare dataset comprising over 100,000 anonymized patient records. The dataset includes key demographic variables (age group, gender), lifestyle indicators (smoking history), and clinical features such as Body Mass Index (BMI), HbA1c levels, blood glucose levels, hypertension status, and presence of heart disease.

Leveraging interactive visual analytics, this dashboard explores the prevalence and distribution of diabetes across these variables. The goal is to help healthcare stakeholders identify risk factors, guide preventive strategies, and enable data-informed decisions to improve chronic disease management and population health outcomes.
""")

# Dashboard title (collapsed)
with st.expander("Project Overview"):
    st.markdown("""
    This dashboard is built on a synthetic healthcare dataset comprising over 100,000 anonymized patient records...
    """)

# Organize visualizations into tabs
tab1, tab2, tab3, tab4 = st.tabs(["Demographics", "Clinical Indicators", "Comorbidities", "Correlations"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Diabetes by Age Group")
        st.plotly_chart(fig1, use_container_width=True, height=300)
        with st.expander("Interpretation"): st.markdown("...")

    with col2:
        st.subheader("Diabetes by Gender")
        st.plotly_chart(fig2, use_container_width=True, height=300)
        with st.expander("Interpretation"): st.markdown("...")

with tab2:
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Smoking History")
        st.plotly_chart(fig3, use_container_width=True, height=300)
        with st.expander("Interpretation"): st.markdown("...")

    with col4:
        st.subheader("HbA1c Level")
        st.plotly_chart(fig4, use_container_width=True, height=300)
        with st.expander("Interpretation"): st.markdown("...")

# Repeat for tab3, tab4 etc.

# Footer
st.markdown("---")
st.markdown("*\u201cNever be ashamed of being diabetic. It\u2019s not a weakness; it\u2019s a story of strength and resilience.\u201d*")
st.markdown("*Developed by Lana Harajli*")

# Optional: reduce padding
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

