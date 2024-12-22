import streamlit as st
import math

st.header("Artillery Calculator")

ArtGrid = st.text_input("Artillery grid reference (Enter the grid in the format xxxx-xxxx):")
if len(ArtGrid) == 9 and ArtGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    ArtX = int(ArtGrid[:4])  # First 4 digits
    ArtY = int(ArtGrid[5:])  # Last 4 digits
    #ArtZ = st.number_input("Artillery Elevation (m):")

TarGrid = st.text_input("Target grid reference (Enter the grid in the format xxxx-xxxx):")
if len(TarGrid) == 9 and TarGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    TarX = int(TarGrid[:4])  # First 4 digits
    TarY = int(TarGrid[5:])  # Last 4 digits
    #TarZ = st.number_input("Target Elevation (m):")

    # Calculate the distance
    distance = math.sqrt((TarX - ArtX)**2 + (TarY - ArtY)**2)# + (TarZ - ArtZ)**2)
    st.write("Distance: ", distance * 10)

    # Calculate the bearing
    delta_x = TarX - ArtX
    delta_y = TarY - ArtY

    # Use atan2 with reversed arguments to match compass bearing conventions
    angle_radians = math.atan2(delta_x, delta_y)
    angle_degrees = math.degrees(angle_radians)

    # Normalize the angle to 0-360 degrees
    bearing = (angle_degrees + 360) % 360

    st.write("Bearing: ", bearing, "degrees")


