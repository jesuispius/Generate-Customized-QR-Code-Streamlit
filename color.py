# ============================================================================================= #
# Name: Phuoc Nguyen
# Project: Simple customized QR Code generation application using Streamlit and QR_Code
# Filename: color.py
# Checking the RGB color and color validation from user input
# ============================================================================================= #

# Import modules and dependencies
from PIL import ImageColor


def checkRGB(tup):
    """ Function to check if the input is a valid RGB color or not

    e.g, (255, 255, 255)

    :param tup: A tuple of integers
    :type tup: tuple[int, int, int]
    :return: True if this input is a valid RGB color or otherwise
    :rtype: bool
    """

    # Iteration each item of tuple and check for each item if:
    # + A valid integer
    # And, it is in range between 0 and 255
    for item in tup:
        if not isinstance(item, int) or item not in range(0, 256):
            return False
    return True


def isValidColor(color):
    """ Check an input is a valid color or not

    Clarification:
        + An input may be a string. E.g, "black", "white"
        + May be a color under the RGB format. E.g, (255, 255, 255)

    :param color: the color input for checking
    :type color: str | tuple[int, int, int]
    :return: True if this input is a valid color or otherwise
    :rtype: bool
    """

    # If the input is a string type,
    # ..., try to get the RGB from the string
    # ..., using the built-in function getrgb() from ImageColor of module PIL
    # ..., if a valid color, return True
    # Else, only calling the function checkRGB above for validation.
    if isinstance(color, str):
        if checkRGB(ImageColor.getrgb(color)):
            return True

    elif checkRGB(color):
        return True

    return False
