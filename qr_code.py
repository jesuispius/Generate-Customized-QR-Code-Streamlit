# ============================================================================================= #
# Name: Phuoc Nguyen
# Project: Simple customized QR Code generation application using Streamlit and QR_Code
# Filename: qr_code.py
# Core function to make the QR Code generation and download it under PNG format
# ============================================================================================= #

# Import modules and dependencies
import qrcode
import streamlit as st
from color import isValidColor


def generateQRCode(data, version=1, boxSize=10, border=5, fillColor='black', backgroundColor='white'):
    """ Generate the QR Code from the customized attribute inputs

    :param data: data storing behind the QR Code
    :type data: str
    :param version: version of box size of QR Code
    :type version: int
    :param boxSize: box size of QR Code
    :type boxSize: int
    :param border: border size of QR Code
    :type border: int
    :param fillColor: color of QR Code
    :param backgroundColor: background color of QR Code
    :return: the image of QR Code
    """

    if data is None or data == '':
        # Validate the input of data
        # If empty data input, then throwing the error message to the web page
        # ..., to prevent users to make a QR Code and carefully check their data input.
        # return: None
        st.error("Please input your data to make progress!")
        return None

    if not isinstance(version, int) or not isinstance(boxSize, int) or not isinstance(border, int):
        # Validate the input of version, box size and border
        # If one of these inputs is not an integer,
        # ..., then throwing the error message to the web page
        # ..., to prevent users to make a QR Code and carefully check these kinds of input.
        # return: None
        st.error("Please check your version, box size, or border's input! Invalid type!")
        return None

    if not isValidColor(fillColor) or not isValidColor(backgroundColor):
        # Validate the input of fill color and background color
        # If one of these inputs is not a color string, or a RGB color type
        # ..., then throwing the error message to the web page
        # ..., to prevent users to make a QR Code and carefully check these kinds of input.
        # return: None
        st.error("Please check your color input!")
        return None

    # Call the function QRCode from the module qrcode
    # To create a new object qr_code to make a QR Code.
    # ..., with the customized values passed from arguments
    qr_code = qrcode.QRCode(
        version=version,
        box_size=boxSize,
        border=border
    )

    # Add/Store the data behind the QRCode
    # e.g, an url link, object, images, etc.
    qr_code.add_data(data)

    # Compile data to QR Code array,
    # ..., setting fit to True to find the best fit for the data to avoid the data overflow errors
    qr_code.make(fit=True)

    # Make the QR Code image from the customized color values
    # ..., from arguments (fill_color, background_color)
    qr_img = qr_code.make_image(
        fill_color=fillColor,
        back_color=backgroundColor
    )

    # return: the QR Code image
    # rtype: PilImage
    return qr_img


def downloadQRCode(label, filename):
    """ Download the png QR Code image

    :param label: Name of the download button
    :type label: str
    :param filename: name of the file used for storing the QR code image
    :type filename: str
    :return: Nothing
    """

    # Open the image file
    # If successfully opened it,
    # ..., display the download button.
    # ..., using the function st.download_button from module streamlit
    # .., for rendering the download button to the web page.
    # ..., this built-in function includes arguments:
    # param label: name of the download button, passed from argument
    # param data: file
    # param file_name: name of png image file, passed from argument
    # param mime: indicating the image/png
    with open(filename, "rb") as file:
        download_btn = st.download_button(
            label=label,
            data=file,
            file_name=filename,
            mime="image/png"
        )

        # Successfully downloaded, throw the success statement to the web page.
        if download_btn:
            st.success("Successfully downloaded!")
            st.balloons()
