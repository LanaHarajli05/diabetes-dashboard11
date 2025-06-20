import streamlit as st
import pandas as pd
import plotly.express as px  # ✅ Required for charts

st.set_page_config(page_title="Exploring Diabetes Risk Across Demographics and Clinical Indicators", layout="wide")

# Load data
df = pd.read_csv("diabetes_clean.csv")

# Sidebar filters
st.sidebar.title("Filters")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
age_group_filter = st.sidebar.multiselect("Select Age Group", options=df["age_group"].unique(), default=df["age_group"].unique())
smoking_filter = st.sidebar.multiselect("Select Smoking History", options=df["smoking_history"].unique(), default=df["smoking_history"].unique())
heart_disease_filter=st.sidebar.multiselect("Select Heart Disease",options=df["heart_disease"].unique(),default=df["heart_disease"].unique())
hypertension_filter=st.sidebar.multiselect("Select Hypertension",options=df["hypertension"].unique(),default=df["hypertension].unique())
# Filter data
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age_group"].isin(age_group_filter)) &
    (df["smoking_history"].isin(smoking_filter))
    (df["heart_disease"].isin(heart_disease))
    (df["hypertension"].isin(hypertension))

# Title
st.title("Exploring Diabetes Risk Across Demographics and Clinical Indicators")
st.markdown("This dashboard is built on a synthetic healthcare dataset comprising over 100,000 anonymized patient records. The dataset includes key demographic variables (age group, gender), lifestyle indicators (smoking history), and clinical features such as Body Mass Index (BMI), HbA1c levels, blood glucose levels, hypertension status, and presence of heart disease.Leveraging interactive visual analytics, this dashboard explores the prevalence and distribution of diabetes across these variables. The visualizations enable users to filter by demographic and health factors, uncover high-risk subgroups, and assess clinical patterns associated with diabetes.The goal of this dashboard is to support healthcare stakeholders in identifying risk factors, guiding preventive strategies, and enabling data-informed decisions that improve chronic disease management and population health outcomes.")

# Row 1
col1, col2 = st.columns(2)
with col1:
    st.subheader("Diabetes Prevalence by Age Group")
    age_group_chart = filtered_df.groupby("age_group")["diabetes"].mean().reset_index()
    fig1 = px.bar(age_group_chart, x="age_group", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "age_group": "Age Group"})
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("Fig1:Diabetes Prevalence by Age Group")
st.markdown("We can notice that diabetes prevalence increases with age, especially for age groups 50–65 and 65+. This highlights the elderly as a high-risk group that needs targeted interventions.")
with col2:
    st.subheader("Diabetes Rates by Gender")
    gender_chart = filtered_df.groupby("gender")["diabetes"].mean().reset_index()
    fig2 = px.bar(gender_chart, x="gender", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "gender": "Gender"})
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("Fig2:Diabetes Rate by Gender")
st.markdown("The piechart shows us the distribution of Diabetes among gender, we can notice that the % of Male with Diabetes is higher than %of female with diabetes.")

# Row 2
col3, col4 = st.columns(2)
with col3:
    st.subheader("Diabetes Rate by Smoking History")
    smoke_chart = filtered_df.groupby("smoking_history")["diabetes"].mean().reset_index()
    fig3 = px.bar(smoke_chart, x="smoking_history", y="diabetes",
                  labels={"diabetes": "Diabetes Rate", "smoking_history": "Smoking History"})
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("Fig3: Diabetes Rate by Smoking History")
st.markdown("Current and former smokers show higher rates of diabetes compared to never-smokers, supporting th evidence that smoking is modifiable risk factor for diabetes.")
with col4:
    st.subheader("HbA1c Levels by Diabetes Status")
    fig4 = px.box(filtered_df, x="diabetes", y="HbA1c_level",
                  labels={"diabetes": "Diabetes", "HbA1c_level": "HbA1c Level"})
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("Fig4:Hb1Ac Levels by Diabetes Status")
st.markdown("The boxplot shows a clear seperation in HbA1c levels between diabetic and non-diabetic individuals.Diabetic patients tend to have higher and more variable HbA1c values,supporting the use of HbA1c as a reliable marker for diabetes diagnosis.")
# Optional: Reduce vertical spacing
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

