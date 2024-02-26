import streamlit as st
import pandas as pd

# Load datasets
@st.cache_data()
def load_data():
    kolkata_data = pd.read_csv('pages/kol.csv', encoding='latin1')
    mumbai_data = pd.read_csv('pages/mumbai.csv', encoding='latin1')
    chennai_data = pd.read_csv('pages/chennai.csv', encoding='latin1')
    return kolkata_data, mumbai_data, chennai_data

kolkata_data, mumbai_data, chennai_data = load_data()

# Function to display company details on a new page
def display_company_details(company_data):
    st.write(company_data)

# Function to display a graph
def display_graph(company_data):
    # Here you can customize the type of graph and data visualization based on your requirements
    st.write("## Data Visualization")
    st.bar_chart(company_data)

# Streamlit app layout
st.title(':blue[Company] :green[Data] :red[Viewer]')

# User input for location
search_location = st.selectbox(':red[Select Location:]', ['Kolkata', 'Mumbai', 'Chennai'])

# Choose the appropriate dataset based on the selected location
if search_location == 'Kolkata':
    location_data = kolkata_data
elif search_location == 'Mumbai':
    location_data = mumbai_data
else:  # Chennai
    location_data = chennai_data

# Add details button beside each column
for column in location_data.columns:
    if st.button(f"'{column}'"):
        st.write(f"'{column}'")
        display_company_details(location_data[column])
        # display_graph(location_data[column])  # Display graph after displaying company details