# Quick Start: ASCII Art Converter CLI

## Installation

1. Ensure Python 3.11+ is installed
2. Install dependencies: `pip install pillow click`
3. Clone/download the source code
4. Run: `python src/cli.py [options] input`

## Basic Usage

### Convert an Image

```bash
python src/cli.py path/to/image.png
```

This converts the image to ASCII art using default settings and prints to console.

### Convert Text

```bash
python src/cli.py "Hello World"
```

Converts the text string to ASCII art representation.

## Customization

### Character Set

```bash
python src/cli.py --chars "@#*+=-:." path/to/image.jpg
```

Use custom characters for different visual effects.

### Output Width

```bash
python src/cli.py --width 120 path/to/image.png
```

Adjust the width of the ASCII art output.

### Combined Options

```bash
python src/cli.py --chars "01" --width 100 "Binary Art"
```

## Examples

### Simple Image Conversion

```bash
python src/cli.py examples/sample.png > output.txt
```

### High Detail

```bash
python src/cli.py --chars "@%#*+=-:. " --width 150 high_res.jpg
```

### Minimalist

```bash
python src/cli.py --chars "# " low_detail.png
```

## Output

The ASCII art is printed to standard output, so you can:
- View in terminal
- Redirect to file: `> output.txt`
- Pipe to other tools: `| less`

## Troubleshooting

- **File not found**: Check the path and file permissions
- **Unsupported format**: Ensure image is PNG, JPG, or BMP
- **Memory issues**: Try smaller images or reduce width
- **Poor quality**: Experiment with different character sets

## Development

To run tests:
```bash
pytest tests/
```

To run the tool during development:
```bash
python -m src.cli
```
