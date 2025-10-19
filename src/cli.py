#!/usr/bin/env python3
"""
ASCII Art Converter CLI

Convert images and text to ASCII art.
"""

import os
import click
from . import converter
from . import utils


@click.command()
@click.argument('input', type=str)
@click.option('--chars', default='@%#*+=-:. ', help='Character set for ASCII art')
@click.option('--width', type=int, default=80, help='Output width in characters')
def main(input, chars, width):
    """Convert images or text to ASCII art."""
    try:
        # Validate inputs
        utils.validate_char_set(chars)
        utils.validate_width(width)

        # Determine if input is file or text
        if os.path.exists(input):
            if utils.is_image_file(input):
                # Validate image file
                utils.validate_image_file(input)
                # Convert image
                result = converter.convert_image_to_ascii(input, chars, width)
            else:
                raise ValueError("Unsupported file type. Only image files (PNG, JPG, BMP) are supported.")
        else:
            # Validate text
            utils.validate_text(input)
            # Convert text
            result = converter.convert_text_to_ascii(input, chars, width)

        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    main()
