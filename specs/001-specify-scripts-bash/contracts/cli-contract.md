# CLI Interface Contract

## Command Signature

```
ascii-art [OPTIONS] INPUT

Convert images or text to ASCII art.

INPUT can be:
- Path to an image file (.png, .jpg, .bmp)
- Text string (enclosed in quotes if contains spaces)

Options:
  --chars TEXT     Character set for ASCII art [default: @%#*+=-:. ]
  --width INTEGER  Output width in characters [default: 80]
  --help           Show this message and exit.
```

## Input Validation

- INPUT is required
- If INPUT is a file path, it must exist and be readable
- If INPUT is not a file path, treated as text
- --chars must be non-empty string
- --width must be positive integer between 20-200

## Output Format

- ASCII art printed to stdout
- Each line ends with newline
- No trailing whitespace on lines
- Error messages printed to stderr with exit code 1

## Examples

Convert image:
```
ascii-art image.png
ascii-art --chars "01" --width 120 image.jpg
```

Convert text:
```
ascii-art "Hello World"
ascii-art --chars "#@" "Custom Text"
```

## Error Handling

- Invalid file: "Error: File not found or not readable"
- Unsupported format: "Error: Unsupported image format"
- Invalid options: "Error: Invalid width value"
