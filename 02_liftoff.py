import streamlit as st
import time

# Streamlit app title
st.title("Liftoff Countdown")

# Input for countdown start
countdown_start = st.number_input("Enter countdown start value:", min_value=1, value=10)

# Button to start the countdown
if st.button("Start Countdown"):
    for i in range(countdown_start, 0, -1):
        st.write(i)
        time.sleep(1)  # Wait for 1 second
    st.write("Liftoff!")
