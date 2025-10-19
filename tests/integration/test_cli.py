"""
Integration tests for CLI.
"""

import subprocess
import pytest
import tempfile
import os
from pathlib import Path


class TestCLIImageConversion:
    """Test CLI image conversion end-to-end."""

    def test_cli_image_conversion_basic(self):
        """Test basic CLI image conversion."""
        # Create a simple test image (1x1 pixel)
        from PIL import Image

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            img = Image.new('RGB', (1, 1), color='black')
            img.save(tmp.name)
            tmp_path = tmp.name

        try:
            # Run CLI
            result = subprocess.run([
                'python', '-m', 'src.cli', tmp_path
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent.parent)

            assert result.returncode == 0
            assert result.stdout.strip()  # Should have output
            assert '@' in result.stdout or ' ' in result.stdout  # Should contain chars
        finally:
            os.unlink(tmp_path)

    def test_cli_invalid_file(self):
        """Test CLI with invalid file."""
        # Create a text file that exists but is not image
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
            tmp.write(b'not an image')
            tmp_path = tmp.name

        try:
            result = subprocess.run([
                'python', '-m', 'src.cli', tmp_path
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent.parent)

            assert result.returncode != 0
            assert 'Error:' in result.stderr
            assert 'Unsupported file type' in result.stderr
        finally:
            os.unlink(tmp_path)


class TestCLITextConversion:
    """Test CLI text conversion."""

    def test_cli_text_conversion_basic(self):
        """Test basic text conversion via CLI."""
        result = subprocess.run([
            'python', '-m', 'src.cli', 'Hello'
        ], capture_output=True, text=True, cwd=Path(__file__).parent.parent.parent)

        assert result.returncode == 0
        assert result.stdout.strip()


class TestCLICustomization:
    """Test CLI customization options."""

    def test_cli_custom_chars(self):
        """Test CLI with custom character set."""
        # Create test image
        from PIL import Image

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            img = Image.new('RGB', (2, 2), color='black')
            img.save(tmp.name)
            tmp_path = tmp.name

        try:
            result = subprocess.run([
                'python', '-m', 'src.cli', '--chars', '01', tmp_path
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent.parent)

            assert result.returncode == 0
            assert result.stdout.strip()
            # Should only contain 0, 1, or newline
            output = result.stdout
            assert all(c in '01\n' for c in output)
        finally:
            os.unlink(tmp_path)

