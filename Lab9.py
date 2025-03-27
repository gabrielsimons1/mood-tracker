import streamlit as st

st.title("Mood Tracker")

name = st.text_input("What’s your name?")
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Excited", "Tired"])
button_clicked = st.button("Tell me!")

if button_clicked:
    if mood == "Happy":
        st.write(f"Hi {name}! I’m glad you’re feeling happy today! 😊")
    elif mood == "Sad":
        st.write(f"Hi {name}! Sorry you’re feeling sad. Hope things get better soon! 🌧️")
    elif mood == "Excited":
        st.write(f"Hi {name}! That’s awesome you’re excited! What’s making you feel that way? 🎉")
    elif mood == "Tired":
        st.write(f"Hi {name}! Feeling tired? Maybe take a break! 😴")
else:
    st.write("Click the button to share your mood!")
