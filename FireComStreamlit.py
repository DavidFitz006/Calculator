import streamlit as st
import math
import pandas as pd

st.header("Artillery Calculator")
df = pd.DataFrame("Artillary Grid","Target Grid","Azimuth","Elevation")
ArtGrid = st.text_input("Artillery grid reference (Enter the grid in the format xxxx-xxxx):")
if len(ArtGrid) == 9 and ArtGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    ArtX = int(ArtGrid[:4])  # First 4 digits
    ArtY = int(ArtGrid[5:])  # Last 4 digits
    ArtZ = st.number_input("Artillery Elevation (m):")

TarGrid = st.text_input("Target grid reference (Enter the grid in the format xxxx-xxxx):")
if len(TarGrid) == 9 and TarGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    TarX = int(TarGrid[:4])  # First 4 digits
    TarY = int(TarGrid[5:])  # Last 4 digits
    TarZ = st.number_input("Target Elevation (m):")

    # Calculate the distance
    distance = math.sqrt((TarX - ArtX)**2 + (TarY - ArtY)**2)# + (TarZ - ArtZ)**2)
    distance = distance * 10
    st.write("Distance: ", distance)

    # Calculate the bearing
    delta_x = TarX - ArtX
    delta_y = TarY - ArtY

    # Use atan2 with reversed arguments to match compass bearing conventions
    angle_radians = math.atan2(delta_x, delta_y)
    angle_degrees = math.degrees(angle_radians)

    # Normalize the angle to 0-360 degrees
    mils = ((angle_degrees + 360) % 360) * 17.7777777778
    st.write("Bearing: ", mils, "mils")
    
    elevation_diff = (ArtZ - TarZ) / 100
    st.write("Elevation difference divided by 100: ", elevation_diff)
    
    elevation = st.number_input("Elevation: ")
    d_elv = st.number_input("D elv per 100m: ")
    fin_elv = st.write("Final Elevation: ", elevation + d_elv * elevation_diff)

st.dataframe(df)
