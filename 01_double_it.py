import streamlit as st

# Streamlit app title
st.title("Double It App")

# Input for the number
number = st.number_input("Enter a number:", value=0)

# Button to double the number
if st.button("Double It"):
    doubled_value = number * 2
    st.write(f"The doubled value is: {doubled_value}")
