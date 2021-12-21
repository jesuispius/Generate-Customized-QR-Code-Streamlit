# ============================================================================================= #
# Name: Phuoc Nguyen
# Project: Simple customized QR Code generation application using Streamlit and QR_Code
# Filename: main.py
# Main interface of project
# ============================================================================================= #

# Import modules and dependencies
import streamlit as st
import time
from PIL import Image
from PIL import ImageColor
from page_config import do_page_config
from qr_code import generateQRCode, downloadQRCode


def renderColorPicker(label, initialValue):
    """ Rendering the color picker on Streamlit based on label and initial color.
    And converting from hex to the RGB color

    :param label: Name of the field
    :type label: str
    :param initialValue: initial color of picker
    :type initialValue: str
    :return: RGB color
    """

    # Rendering the color picker using streamlit
    color = st.color_picker(label, initialValue)

    # Converting hex color to RGB color using getcolor() built-in function from ImageColor of PIL module
    color_rgb = ImageColor.getcolor(color, "RGB")

    # Return the valid RGB color
    return color_rgb


if __name__ == "__main__":
    # Configure the web page running by streamlit
    do_page_config()

    # Set the filename to store and download qr code
    FILENAME = 'QRCode.png'

    # Title of the page
    st.title('Generate a customized QR Code')

    # Input the data to store behind the QR Code
    data_getter = st.text_input('Add information for storing behind the QR code: ')

    ver_col, bord_col = st.columns(2)
    with ver_col:
        # Set the version of QR Code using slider
        # Range of values from 1 to 40
        # Default value: 1
        version_getter = st.slider('Choose the version of QR box: ',
                                   min_value=1,
                                   max_value=40,
                                   value=1)

    with bord_col:
        # Set the border of QR Code using slider
        # Range of values from 1 to 10
        # Default value: 4
        border_getter = st.slider('Choose border of QR box: ',
                                  min_value=1,
                                  max_value=10,
                                  value=4)

    # Set the box size of QR Code
    # Default value: 10

    box_size_getter = st.number_input('Choose box size', value=10)

    fill_col, bg_col = st.columns(2)
    with fill_col:
        # Set the fill color picker
        # Default color: #000000
        fillcolor_getter = renderColorPicker('Pick a fill color: ', '#000000')

    with bg_col:
        # Set the background color picker
        # Default color: #ffffff
        background_color_getter = renderColorPicker('Pick a background color: ', '#ffffff')

    # Button for QR Code generation
    generateButton = st.button('Generate QR Code')

    # If button clicked, then passing inputs to the generateQRCode function to make a QR Code
    if generateButton:
        image_qr_getter = generateQRCode(data_getter,
                                         version=1,
                                         boxSize=box_size_getter,
                                         border=border_getter,
                                         fillColor=fillcolor_getter,
                                         backgroundColor=background_color_getter)

        # If successfully generated, save the image
        # ..., and throwing the success statement
        if image_qr_getter is not None:
            # Saving image file
            image_qr_getter.save(FILENAME)
            # Success statement
            with st.spinner('Processing...'):
                time.sleep(1)
            st.success("Successfully make a QR Code!")

    # Rendering QR Code image whenever it is available
    # ..., and displaying the download button
    try:
        # Open file
        rendered_img = Image.open(FILENAME)
        # Rendering the image of QR Code
        st.image(rendered_img)
        # Display the download button
        downloadQRCode("Download PNG", 'QRCode.png')
    except FileNotFoundError:
        print("")
