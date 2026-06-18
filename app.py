
import streamlit as st
import pickle
import pandas as pd

# Load trained model

# Load modelpip
with open(r"mlruns/1/models/m-3fc4dca3388c4a639f96d1ad61c0ada5/artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)



st.set_page_config(
    page_title="Disaster Prediction System",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Disaster Prediction System")

st.write("Enter disaster details below:")

# Inputs



latitude = st.number_input(
    "Latitude",
    value=20.0
)

longitude = st.number_input(
    "Longitude",
    value=78.0
)

severity_level = st.slider(
    "Severity Level",
    min_value=1,
    max_value=10,
    value=5
)

affected_population = st.number_input(
    "Affected Population",
    min_value=0,
    value=1000
)

estimated_economic_loss_usd = st.number_input(
    "Economic Loss (USD)",
    min_value=0.0,
    value=50000.0
)

response_time_hours = st.number_input(
    "Response Time (Hours)",
    min_value=0.0,
    value=12.0
)

infrastructure_damage_index = st.slider(
    "Infrastructure Damage Index",
    min_value=0,
    max_value=100,
    value=50
)

disaster_type = st.selectbox(
    "Disaster Type",
    [
        "Flood",
        "Earthquake",
        "Cyclone",
        "Wildfire",
        "Drought"
    ]
)

location = st.text_input(
    "Location",
    "Mumbai"
)

aid_provided = st.selectbox(
    "Aid Provided",
    [
        "Yes",
        "No"
    ]
)

year = st.number_input(
    "Year",
    min_value=2020,
    max_value=2035,
    value=2025
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        
        "latitude": [latitude],
        "longitude": [longitude],
        "severity_level": [severity_level],
        "affected_population": [affected_population],
        "estimated_economic_loss_usd": [estimated_economic_loss_usd],
        "response_time_hours": [response_time_hours],
        "infrastructure_damage_index": [infrastructure_damage_index],
        "disaster_type": [disaster_type],
        "location": [location],
        "aid_provided": [aid_provided],
        "year": [year],
        "month": [month],
        "day": [day]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ Major Disaster Predicted")
    else:
        st.success("✅ Minor Disaster Predicted")
