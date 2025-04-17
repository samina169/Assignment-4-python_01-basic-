import streamlit as st
import random

# Streamlit app title
st.title("Random Number Generator")

# Button to generate a random number
if st.button("Generate Random Number"):
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    st.write(f"The generated random number is: {random_number}")
