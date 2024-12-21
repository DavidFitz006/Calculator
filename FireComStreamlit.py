import streamlit as st
import math

st.header("Artilary Calculator")

ArtGrid = st.text_input("Artilary grid reference(Enter the grid in the format xxxx-xxxx):")
if len(ArtGrid) == 9 and ArtGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    ArtX = int(ArtGrid[:4])  # First 4 digits
    ArtY = int(ArtGrid[5:])  # Last 4 digits
    ArtZ = st.number_input("Artilary Elivation(m):")


TarGrid = st.text_input("Target grid reference(Enter the grid in the format xxxx-xxxx):")
if len(TarGrid) == 9 and TarGrid[4] == '-':
    # Extract the first 4 digits and the last 4 digits
    TarX = int(TarGrid[:4])  # First 4 digits
    TarY = int(TarGrid[5:])  # Last 4 digits
    TarZ = st.number_input("Target Elivation(m):")
    distance = (math.sqrt((TarX - ArtX)**2 + (TarY - ArtY)**2 + (TarZ - ArtZ)**2))
#     slope = (TarY - ArtY) / (TarX - ArtX)
# 
#     angle_rad = math.atan(slope)
#     angle_deg = math.degrees(angle_rad)
#     bearing = (90 - angle_deg) % 360
# 
    st.write("Distance: "distance*10)



