"""
Unit tests for converter module.
"""

import pytest
from unittest.mock import patch, MagicMock
from src import converter


class TestImageConversion:
    """Test image to ASCII conversion."""

    @patch('src.converter.Image.open')
    def test_convert_image_to_ascii_basic(self, mock_image_open):
        """Test basic image conversion."""
        # Mock PIL Image
        mock_img = MagicMock()
        mock_img.convert.return_value = mock_img
        mock_img.resize.return_value = mock_img
        mock_img.getpixel.return_value = 128  # Medium gray
        mock_img.size = (10, 10)
        mock_image_open.return_value = mock_img

        result = converter.convert_image_to_ascii('test.png', '@ ', 10)

        # Should not be None/empty
        assert result is not None
        assert isinstance(result, str)
        # Should contain only characters from char_set
        assert all(c in '@ ' for c in result if c not in '\n')

    @patch('src.converter.Image.open')
    def test_convert_image_to_ascii_custom_chars(self, mock_image_open):
        """Test with custom character set."""
        mock_img = MagicMock()
        mock_img.convert.return_value = mock_img
        mock_img.resize.return_value = mock_img
        mock_img.getpixel.return_value = 0  # Black
        mock_img.size = (5, 5)
        mock_image_open.return_value = mock_img

        result = converter.convert_image_to_ascii('test.png', '01', 5)

        assert all(c in '01\n' for c in result)


class TestTextConversion:
    """Test text to ASCII conversion."""

    def test_convert_text_to_ascii_basic(self):
        """Test basic text conversion."""
        result = converter.convert_text_to_ascii('Hello', '@ ', 10)

        assert result is not None
        assert isinstance(result, str)
        # Should contain the text in some form
        assert 'Hello' in result or 'H' in result

    def test_convert_text_to_ascii_empty(self):
        """Test empty text."""
        result = converter.convert_text_to_ascii('', '@ ', 10)

        assert result == '' or result.strip() == ''
