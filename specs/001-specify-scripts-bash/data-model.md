# Data Model: ASCII Art Converter CLI

## Input Source Entity

**Purpose**: Represents the source of content to convert to ASCII art

**Attributes**:
- type: enum (image, text)
- path: string (for image files)
- content: string (for text input)

**Validation Rules**:
- If type=image, path must be valid file path to supported image format
- If type=text, content must be non-empty string
- Supported image formats: PNG, JPG, BMP

## Configuration Entity

**Purpose**: Holds customization settings for ASCII art generation

**Attributes**:
- character_set: string (default: "@%#*+=-:. ")
- density: integer (default: 80, range 20-200)

**Validation Rules**:
- character_set must be non-empty string
- density must be positive integer
- Reasonable limits on character_set length (<100 chars)

**Relationships**:
- Applied to Input Source during conversion

## Output Entity

**Purpose**: Represents the generated ASCII art result

**Attributes**:
- content: string (the ASCII art text)
- width: integer (character width)
- height: integer (line height)

**Validation Rules**:
- content must be valid ASCII art string
- width and height must match content dimensions

**Relationships**:
- Generated from Input Source + Configuration

## State Transitions

None - stateless CLI tool.

## Notes

All entities are lightweight data structures passed between CLI interface and conversion logic. No persistence required.
