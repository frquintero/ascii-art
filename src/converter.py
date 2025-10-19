"""
ASCII Art Converter Module

Core algorithms for converting images and text to ASCII art.
"""

from PIL import Image, ImageEnhance
import os
from pyfiglet import figlet_format
from termcolor import colored


def convert_image_to_ascii(image_path, char_set='`.:-=+*#%@', width=80):
    """
    Convert an image file to ASCII art.

    Args:
        image_path (str): Path to the image file
        char_set (str): Characters to use for ASCII art
        width (int): Width of the output in characters

    Returns:
        str: ASCII art representation
    """
    # Load and prepare image
    image = Image.open(image_path)
    image = _image_to_grayscale(image)
    image = _enhance_contrast(image)
    image = _resize_image(image, width)

    # Convert to ASCII
    ascii_art = []
    width_img, height_img = image.size

    for y in range(height_img):
        row = []
        for x in range(width_img):
            pixel = image.getpixel((x, y))
            char = _pixel_to_char(pixel, char_set)
            row.append(char)
        ascii_art.append(''.join(row))

    return '\n'.join(ascii_art)


def convert_text_to_ascii(text, char_set=None, width=80):
    """
    Convert text to colored ASCII art using pyfiglet and termcolor.

    Args:
        text (str): Input text
        char_set (str): Not used for text art.
        width (int): Output width for pyfiglet.

    Returns:
        str: Colored ASCII art text.
    """
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    
    if not text.strip():
        return ""

    # Generate ASCII art for each character and color it
    char_arts = []
    for i, char in enumerate(text):
        if char == ' ':
            # Create a blank space of the same height as a rendered character
            font_height = len(figlet_format('A', font='standard').split('\n'))
            char_arts.append([' ' * 4] * font_height)
        else:
            color = colors[i % len(colors)]
            # Render character and split into lines
            art_lines = figlet_format(char, font='standard').split('\n')
            # Color each line
            colored_lines = [colored(line, color) for line in art_lines]
            char_arts.append(colored_lines)

    # Combine the character arts horizontally
    combined_art = []
    # The height of the art is determined by the first character's art
    art_height = len(char_arts[0])
    for i in range(art_height):
        line = "".join(char_art[i] for char_art in char_arts)
        combined_art.append(line)

    return '\n'.join(combined_art)


def _image_to_grayscale(image):
    """Convert image to grayscale."""
    return image.convert('L')


def _enhance_contrast(image):
    """Enhance the contrast of the image."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(1.5)


def _resize_image(image, width):
    """Resize image maintaining aspect ratio."""
    width_img, height_img = image.size
    aspect_ratio = height_img / width_img
    new_height = int(width * aspect_ratio * 0.5)  # 0.5 for character aspect ratio
    return image.resize((width, new_height), Image.Resampling.LANCZOS)


def _pixel_to_char(pixel_value, char_set):
    """Map pixel brightness to character."""
    # Pixel value 0-255, map to char_set
    if not char_set:
        return ' '

    index = int((pixel_value / 255) * (len(char_set) - 1))
    return char_set[index]