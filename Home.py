import streamlit as st
import pandas as pd

# Set webpage layout
st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.
"""
st.write(content)

st.subheader("Our team")

# Columns for company members
col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

# Make the dataframe with company members
df = pd.read_csv("data_company_web.csv", sep=',')

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() + " "
                     + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over the second four rows
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(row["first name"].capitalize() + " "
                     + row["last name"].capitalize())
        # Add role
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the third column
with col3:
    # Iterate over the last four rows
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " "
                     + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
