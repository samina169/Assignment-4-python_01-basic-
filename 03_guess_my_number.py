import streamlit as st
import random

# Streamlit app title
st.title("Guess My Number Game")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Input for the user's guess
user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100)

# Button to check the guess
if st.button("Check Guess"):
    if user_guess == number_to_guess:
        st.write("Congratulations! You guessed the correct number!")
    elif user_guess < number_to_guess:
        st.write("Too low! Try again.")
    else:
        st.write("Too high! Try again.")
