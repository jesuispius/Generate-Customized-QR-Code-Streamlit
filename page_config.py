# ============================================================================================= #
# Name: Phuoc Nguyen
# Project: Simple customized QR Code generation application using Streamlit and QR_Code
# Filename: page_config.py
# Page Configuration running by streamlit
# ============================================================================================= #


# Import modules and dependencies
import streamlit as st


def do_page_config():
    """ Function to configure the page running by streamlit.
    Setting up the page title, the page icon/favicon, the layout, and the sidebar state

    :return: Nothing
    """
    st.set_page_config(
        page_title="Generate customized QR Code App",
        page_icon=":fire:",
        layout="centered",
        initial_sidebar_state="auto",
    )
