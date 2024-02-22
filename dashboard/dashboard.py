# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px

# Define the load_data function
@st.cache
def load_data():
    # Make sure to use the correct path where your CSV files are located
    data_day = pd.read_csv("../data/day.csv")
    data_hour = pd.read_csv("../data/hour.csv")
    return data_day, data_hour

data_day, data_hour = load_data()

# TITLE DASHBOARD
st.title("Bike Sharing Dashboard")

# SIDEBAR
st.sidebar.title("Information:")
# Your personal information
st.sidebar.markdown("**• Nama: Ahmad Bujai Rimi**")
st.sidebar.markdown("**• Email: ahmadbujai20@gmail.com**")

# Show raw data based on user selection
st.sidebar.title("Dataset Bike Share")
if st.sidebar.checkbox("Show Day Dataset"):
    st.subheader("Raw Data - Day")
    st.write(data_day)

if st.sidebar.checkbox("Show Hour Dataset"):
    st.subheader("Raw Data - Hour")
    st.write(data_hour)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data_day.describe())  # Assuming you want to show stats for day dataset

# VISUALIZATION AND ANALYSIS BASED ON YOUR JUPYTER NOTEBOOK
# You can convert your matplotlib plots to Plotly figures or use Plotly directly as in your friend's code

# Example visualization: Number of Rentals by Season
st.subheader("Number of Rentals by Season")
fig_season = px.box(data_day, x='season', y='cnt', title='Number of Rentals by Season')
st.plotly_chart(fig_season, use_container_width=True)

# FOOTER
# Include any additional information or credits
st.sidebar.markdown("**Weather Categories:**")
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')