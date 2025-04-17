import streamlit as st
import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? Because it had too many problems."
]

# Streamlit app title
st.title("Joke Bot")

# Button to get a random joke
if st.button("Get a Joke"):
    joke = random.choice(jokes)
    st.write(joke)
