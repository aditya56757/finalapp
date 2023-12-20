# appp.py

import streamlit as st
from ai import fun1
from c_g import fun2
from dalle_app import fun3
from main import fun4


def main():
    st.title("DPD 360")

    # Create a sidebar with buttons for each functionality
    selected_function = st.sidebar.selectbox("Select Function", ["Email Generator", "Social Media Content Generator", "dalle", "SEO optimisation"])

    # Display the selected functionality
    if selected_function == "Email Generator":
        fun1()
    elif selected_function == "Social Media Content Generator":
        fun2()
    elif selected_function == "dalle":
        fun3()
    elif selected_function == "SEO optimisation":
        fun4()


if __name__ == "__main__":
    main()

