# ASCII Art Converter CLI

A command-line tool that converts images and text into ASCII art representations. Perfect for creating text-based art from images or stylized text banners for terminals and text environments.

## Features

- **Image Conversion**: Convert PNG, JPG, and BMP images to ASCII art
- **Text Conversion**: Transform text strings into colored ASCII art banners
- **Customizable Characters**: Choose your own character set for different visual styles
- **Adjustable Density**: Control output width for different resolutions
- **Fast Processing**: Optimized for quick conversions
- **Cross-Platform**: Works on Linux, macOS, and Windows

## Requirements

- Python 3.11 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the tool:
```bash
python -m src.cli [options] input
```

## Usage

### Basic Syntax

```bash
python src/cli.py [OPTIONS] INPUT
```

- `INPUT`: Path to an image file (PNG/JPG/BMP) or text string
- If INPUT is a file path, it converts the image
- If INPUT is not a file path, it's treated as text to convert

### Options

- `--chars TEXT`: Character set for ASCII art (default: "@%#*+=-:. ")
- `--width INTEGER`: Output width in characters (default: 80, range: 20-200)
- `--help`: Show help message

### Examples

#### Convert an Image

```bash
# Basic conversion
python -m src.cli image.png

# With custom characters
python -m src.cli --chars "@#" image.jpg

# High resolution
python -m src.cli --width 120 image.png

# Combined options
python -m src.cli --chars "01" --width 100 image.bmp
```

#### Convert Text

```bash
# Basic text conversion (creates colored ASCII art banner)
python -m src.cli "Hello World"

# Output: Colored ASCII art where each character has a different color
# (red H, green E, yellow L, etc.)

# Wide output (affects future enhancements)
python -m src.cli --width 150 "Big Text Banner"
```

#### Output Examples

```bash
# Minimal style
python -m src.cli --chars "# " image.png

# Detailed style
python -m src.cli --chars "@%#*+=-:. " --width 120 image.jpg
```

## Output

- ASCII art is printed to standard output
- Can be redirected to files: `python -m src.cli image.png > output.txt`
- Can be piped to other tools: `python -m src.cli image.png | less`

## Error Handling

The tool provides clear error messages for:
- Invalid file paths
- Unsupported image formats
- Invalid option values
- File size limits (max 10MB)

## Development

### Running Tests

```bash
pip install pytest
pytest tests/
```

### Project Structure

```
.github/
├── copilot-instructions.md    # AI assistant guidelines
└── prompts/                   # Speckit agent prompts

.specify/
├── memory/                    # Constitution and project memory
└── templates/                 # Plan templates

specs/
└── [feature-branch]/          # Feature specifications and docs

src/
├── cli.py                     # Main CLI interface
├── converter.py               # Core conversion algorithms
├── database.py                # Database setup (future use)
└── utils.py                   # Helper functions and validation

tests/
├── unit/                      # Unit tests
└── integration/               # Integration tests

screenshots/                   # Sample outputs and images
```

## Technical Details

- **Image Processing**: Uses Pillow for image loading, grayscale conversion, and enhancement
- **Text Processing**: Uses PyFiglet for ASCII art text generation and Termcolor for coloring
- **Algorithm**: Maps pixel brightness to characters in the specified set
- **Aspect Ratio**: Automatically maintained with character aspect ratio correction
- **Performance**: Designed for images up to 10MB, processing in seconds

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source. See LICENSE file for details.

## Support

For issues and questions, please open a GitHub issue or check the troubleshooting section in the documentation.
