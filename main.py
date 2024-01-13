import streamlit as st
import random
# Load the logo image
logo_path = "images/logo.png"

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'random_number' not in st.session_state:
    st.session_state.random_number = None

# Function to play the game
def guess(num):
    """
    A function that allows the user to guess a number between 1 and 100.
    Parameters:
    - num (int): The maximum number of attempts allowed to guess the number.
    Returns:
    - None
    """
    st.image(logo_path, width=300)

    if st.session_state.random_number is None:
        st.session_state.random_number = random.randint(1, 100)

    st.write(f"You have {num - st.session_state.counter} attempts remaining to guess the number.")
    ask = st.number_input("Guess a number between 1 and 100", min_value=1,max_value=100)
    submit_button = st.button("Submit")
    if submit_button:
        if ask > st.session_state.random_number:
            st.write("Too high. Guess again.")
        elif ask < st.session_state.random_number:
            st.write("Too low. Guess again.")
        else:
            st.success(f"You got it! The answer was {st.session_state.random_number}.")
        st.session_state.counter += 1

    if st.session_state.counter > num:
        st.error(f"You've run out of guesses, you lose. The actual number was {st.session_state.random_number}")

def play():
    """
    A function to play a guessing game with two difficulty levels.
    Parameters:
        None
    Returns:
        None
    """
    level = st.radio("Choose a difficulty:", options=['easy', 'hard'])

    if level == 'easy':
        guess(10)
    elif level == 'hard':
        guess(5)
    

# Main Streamlit app
st.title("🤔Number Guessing Game❓")

# Sidebar with game rules
st.sidebar.title("# Game Rules:")
st.sidebar.text("- Your goal is to guess the correct number between 1 and 100.")
st.sidebar.text(" - You can choose between easy and hard difficulty levels.")
st.sidebar.text("- If you can guess the number within the given attempts,you win!")
st.sidebar.text("Good luck!")
play()

