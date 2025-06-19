import streamlit as st
import pandas as pd

# Load your cleaned diabetes dataset
df = pd.read_csv("diabetes_clean.csv")

# Sidebar filters
st.sidebar.title("Filters")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["gender"].unique(), default=df["gender"].unique())
age_group_filter = st.sidebar.multiselect("Select Age Group", options=df["age_group"].unique(), default=df["age_group"].unique())
smoking_filter = st.sidebar.multiselect("Select Smoking History", options=df["smoking_history"].unique(), default=df["smoking_history"].unique())

# Apply filters
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age_group"].isin(age_group_filter)) &
    (df["smoking_history"].isin(smoking_filter))
]

# Title and description
st.title("🩺 Diabetes Analytics Dashboard")
st.markdown("Analyze diabetes trends by demographic and health factors.")

# Chart 1: Diabetes Prevalence by Age Group
age_group_chart = filtered_df.groupby("age_group")["diabetes"].mean().reset_index()
fig1 = px.bar(age_group_chart, x="age_group", y="diabetes",
              labels={"diabetes": "Diabetes Rate", "age_group": "Age Group"},
              title="Diabetes Prevalence by Age Group")
st.plotly_chart(fig1, use_container_width=True)

# ----------------- Chart 2 -------------------
st.subheader("Diabetes Prevalence by Gender")
gender_chart = filtered_df.groupby("gender")["diabetes"].mean().reset_index()
fig2 = px.bar(gender_chart, x="gender", y="diabetes",
              labels={"diabetes": "Diabetes Rate", "gender": "Gender"})
st.plotly_chart(fig2, use_container_width=True)

# ----------------- Chart 3 -------------------
st.subheader("Diabetes Rate by Smoking History")
smoking_chart = filtered_df.groupby("smoking_history")["diabetes"].mean().reset_index()
fig3 = px.bar(smoking_chart, x="smoking_history", y="diabetes",
              labels={"diabetes": "Diabetes Rate", "smoking_history": "Smoking History"})
st.plotly_chart(fig3, use_container_width=True)

# ----------------- Chart 4 -------------------
st.subheader("HbA1c Level Distribution by Diabetes Status")
fig4 = px.box(filtered_df, x="diabetes", y="HbA1c_level", color="diabetes",
              labels={"HbA1c_level": "HbA1c Level", "diabetes": "Diabetes Status"})
st.plotly_chart(fig4, use_container_width=True)

# ----------------- Chart 5 -------------------
st.subheader("Diabetes by Hypertension and Heart Disease")
cross_chart = filtered_df.groupby(["hypertension", "heart_disease"])["diabetes"].mean().reset_index()
fig5 = px.bar(cross_chart, x="hypertension", y="diabetes", color="heart_disease", barmode="group",
              labels={"diabetes": "Diabetes Rate", "hypertension": "Hypertension", "heart_disease": "Heart Disease"})
st.plotly_chart(fig5, use_container_width=True)
