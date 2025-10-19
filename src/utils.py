"""
Utility functions for ASCII Art Converter

File handling, validation, and helper functions.
"""

import os
import mimetypes


def is_image_file(file_path):
    """
    Check if the file path points to a supported image file.

    Args:
        file_path (str): Path to check

    Returns:
        bool: True if it's a supported image file
    """
    if not os.path.isfile(file_path):
        return False

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and mime_type.startswith('image/'):
        # Supported formats: PNG, JPG, BMP
        return mime_type in ['image/png', 'image/jpeg', 'image/bmp']
    return False


def validate_image_file(file_path):
    """
    Validate image file for conversion.

    Args:
        file_path (str): Path to validate

    Raises:
        ValueError: If invalid
        FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not is_image_file(file_path):
        raise ValueError("Unsupported image format. Supported: PNG, JPG, BMP")

    # Check file size (under 10MB as per success criteria)
    file_size = os.path.getsize(file_path)
    if file_size > 10 * 1024 * 1024:  # 10MB
        raise ValueError("Image file too large (max 10MB)")


def validate_char_set(char_set):
    """
    Validate character set for ASCII art.

    Args:
        char_set (str): Character set to validate

    Raises:
        ValueError: If invalid
    """
    if not char_set or not isinstance(char_set, str):
        raise ValueError("Character set must be a non-empty string")


def validate_width(width):
    """
    Validate output width.

    Args:
        width (int): Width to validate

    Raises:
        ValueError: If invalid
    """
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    if width < 20 or width > 200:
        raise ValueError("Width must be between 20 and 200")


def validate_text(text):
    """
    Validate text input.

    Args:
        text (str): Text to validate

    Raises:
        ValueError: If invalid
    """
    if not isinstance(text, str):
        raise ValueError("Text must be a string")
    # Allow empty text as per spec
