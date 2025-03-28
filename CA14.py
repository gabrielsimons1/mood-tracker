import streamlit as st

def main():
    st.title("Streamlit Widgets Example")

    name = st.text_input("Name", "Enter your name")

    if name:
        st.write(f"Hello, {name}!")

    color = st.selectbox(
        'Pick a color',
        ['Red', 'Blue', 'Green'],
        index=0
    )

    if color:
        st.write(f'You selected: {color}')

if __name__ == "__main__":
    main()

