# Gemini Project Overview: ASCII Art Converter CLI

This document provides an overview of the "ASCII Art Converter CLI" project, tailored for AI agent understanding and interaction.

## Project Purpose

The project implements a command-line interface (CLI) tool designed to convert both image files (PNG, JPG, BMP) and text strings into ASCII art representations. It's intended for generating text-based art for terminals and other text-based environments.

## Core Functionality

The CLI supports two primary conversion modes:

1.  **Image to ASCII Art**: Converts a given image file into an ASCII art representation.
2.  **Text to ASCII Art**: Transforms a text string into a colored ASCII art banner.

## Main Technologies

*   **Python 3.11+**: The primary programming language.
*   **Click**: For building the command-line interface.
*   **Pillow (PIL)**: For image loading, grayscale conversion, contrast enhancement, and resizing.
*   **PyFiglet**: For generating ASCII art from text strings.
*   **Termcolor**: For adding color to the text-based ASCII art output.
*   **SQLAlchemy**: Used in `src/database.py` for potential future database interactions, though not currently integrated into the CLI's core conversion workflow.

## Architecture Overview

The project follows a modular structure:

*   **`src/cli.py`**: The main entry point, handling command-line argument parsing, input validation, and orchestrating calls to the `converter` module.
*   **`src/converter.py`**: Contains the core logic for both image-to-ASCII and text-to-ASCII conversions, utilizing Pillow, PyFiglet, and Termcolor.
*   **`src/utils.py`**: Provides utility functions for input validation (file types, sizes, character sets, widths) to ensure robust input handling.
*   **`src/database.py`**: A placeholder for database setup, indicating potential future features like storing conversion history or user preferences.

## General Instructions

*   **Persona:** Act as a seasoned developer who is knowledgeable about best practices, especially concerning command-line applications. 
*   **Coding Style:** All Python code must be PEP 8 compliant, with a focus on readability.
*   **Docstrings:** All functions and classes must have clear and concise docstrings following the NumPy format.
*   **Error Handling:** Include robust error handling for file I/O operations.
*   **Tooling:** Use the `rich` library for terminal formatting and a better user experience.
*   **Avoid:** Do not introduce external libraries unless they are lightweight and provide significant value.

