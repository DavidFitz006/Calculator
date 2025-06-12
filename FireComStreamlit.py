import streamlit as st
import math
import pandas as pd

st.title("CPO & MFC Targeting Tool")
st.header("Input Data")
import streamlit as st
import pandas as pd
import math

# Initialize session state
if "results" not in st.session_state:
    st.session_state.results = []

def parse_grid_ref(grid_ref):
    try:
        easting_str, northing_str = grid_ref.split("-")
        return float(easting_str), float(northing_str)
    except:
        return 0.0, 0.0

st.title("Mortar Fire Control Calculator")

col1, col2 = st.columns(2)

with col1:
    mortar_grid_ref = st.text_input("Mortar Grid Reference (Easting-Northing)", value="0-0")
    mortar_easting, mortar_northing = parse_grid_ref(mortar_grid_ref)
    mortar_elevation = st.number_input("Mortar Elevation (m)", value=0.0)
    first_elevation = st.number_input("First Elevation (m)", value=0.0)
    
    # Dropdown for Effect Required
    effect_required = st.selectbox("Effect Required", options=["HE", "SMK", "ILM"])

with col2:
    target_grid_ref = st.text_input("Target Grid Reference (Easting-Northing)", value="0-0")
    target_easting, target_northing = parse_grid_ref(target_grid_ref)
    target_elevation = st.number_input("Target Elevation (m)", value=0.0)
    delv_per_100m = st.number_input("D elv / 100m", value=0.0)
    target_description = st.text_input("Target Description", value="")

    # Dropdown for Callsign
    callsign = st.selectbox("Callsign", options=["10", "11", "12", "21", "22", "41", "50", "51", "52", "70"])

# Calculate distance and bearing
dx = target_easting - mortar_easting
dy = target_northing - mortar_northing
distance = math.hypot(dx, dy) * 10

# Calculate bearing in mils (6400 mils = 360 degrees)
bearing_rad = math.atan2(dx, dy)
bearing_deg = math.degrees(bearing_rad)
if bearing_deg < 0:
    bearing_deg += 360
bearing_mils = bearing_deg * (6400 / 360)

# Calculate elevation difference
delta_elevation = (mortar_elevation - target_elevation) / 100  # DIVIDED BY 100

# Adjusted elevation output
adjusted_elevation = first_elevation + (delta_elevation * delv_per_100m)

# Display results
st.header("Results")
res_col1, res_col2 = st.columns(2)
with res_col1:
    st.metric("Distance (m)", f"{distance:.2f}")
    st.metric("Elevation Difference ÷ 100 (m)", f"{delta_elevation:.4f}")
with res_col2:
    st.metric("Bearing (mils)", f"{bearing_mils:.2f}")
    st.metric("Adjusted Elevation", f"{adjusted_elevation:.2f}")

# Store and Reset Buttons
col_store, col_reset = st.columns([1, 1])
with col_store:
    if st.button("Store Target"):
        new_entry = {
            "Target Description": target_description,
            "Target Grid": target_grid_ref,
            "Bearing (mils)": round(bearing_mils, 2),
            "Adjusted Elevation": round(adjusted_elevation, 2),
            "Distance (m)": round(distance, 2),
            "Effect Required": effect_required,
            "Callsign": callsign
        }
        st.session_state.results.append(new_entry)

with col_reset:
    if st.button("Reset All"):
        st.session_state.results = []

# Display stored targets
if st.session_state.results:
    st.subheader("Stored Targets")
    stored_df = pd.DataFrame(st.session_state.results)
    st.dataframe(stored_df, use_container_width=True)
    st.download_button("Download Results", stored_df.to_csv(index=False), "stored_targets.csv", "text/csv")
