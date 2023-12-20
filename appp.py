import json
import streamlit as st
from streamlit_lottie import st_lottie
from ai import fun1
from c_g import fun2
from dalle_app import fun3
from main import fun4


def main():
    # Set the page configuration
    st.set_page_config(layout="wide")

    # Page Title, Logo, and Version
    st.title("DPD 360 Marketing")
    st.image("seo_optimised_blog_generator/Publications-Division-removebg-preview.png",
             caption="Company Logo", use_column_width=True)
    st.write("2.1.0 Alpha Version")
    # Description
    st.title("What would you like to try first?")

    # Buttons
    options = [
        "AI Magazine Email Generator",
        "Social Media Content Generator",
        "DPD Publication Image Generator",
        "SEO optimisation",
        "View DPD Site (Made with Atomic Design)",
        "Lead Magnet",
        "Posts Scheduler",
        "Install Employment News App"
    ]

    # Display buttons horizontally
    cols = st.columns(4)

    for i, option in enumerate(options):
        # Use button click event to trigger the action directly
        if cols[i % 4].button(option, key=f"button_{i}"):
            execute_action(option)


def execute_action(selected_function):
    # Execute the corresponding function based on the selected option
    if selected_function == "AI Magazine Email Generator":
        fun1()
    elif selected_function == "Social Media Content Generator":
        fun2()
    elif selected_function == "DPD Publication Image Generator":
        fun3()
    elif selected_function == "SEO optimisation":
        fun4()
    elif selected_function == "Lead Magnet":
        # Add the corresponding function for Lead Magnet
        pass
    elif selected_function == "Posts Scheduler":
        # Add the corresponding function for Posts Scheduler
        pass
    elif selected_function == "Install Employment News App":
        # Add the corresponding function for Install Employment News App
        pass
