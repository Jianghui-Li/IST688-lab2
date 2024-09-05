import streamlit as st

# Set up the main configuration for the app
st.set_page_config(page_title="My App", layout="centered")

# Title for the main page
st.title("Welcome to the My App")

# Introduction text
st.write(
    """
    Use the links below or sidebar to navigate to the different labs:
    """
)

# Create clickable links for Lab 1 and Lab 2
st.markdown("[Go to Lab 1](Lab1)")
st.markdown("[Go to Lab 2](Lab2)")

