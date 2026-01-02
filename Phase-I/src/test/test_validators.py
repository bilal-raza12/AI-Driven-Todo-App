"""Tests for input validation utilities."""

import pytest
from lib.validators import validate_id, validate_title, validate_description


class TestValidateId:
    """Tests for ID validation."""

    def test_validate_id_valid_positive_integer(self):
        """Test validation of valid positive integer ID."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("42")

        # Assert
        assert is_valid is True
        assert task_id == 42
        assert error is None

    def test_validate_id_single_digit(self):
        """Test validation of single digit ID."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("1")

        # Assert
        assert is_valid is True
        assert task_id == 1
        assert error is None

    def test_validate_id_large_number(self):
        """Test validation of large ID number."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("999999")

        # Assert
        assert is_valid is True
        assert task_id == 999999
        assert error is None

    def test_validate_id_zero_returns_error(self):
        """Test that zero ID is invalid (edge case)."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("0")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "ID must be a positive number."

    def test_validate_id_negative_returns_error(self):
        """Test that negative ID is invalid (edge case)."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("-5")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "ID must be a positive number."

    def test_validate_id_non_numeric_returns_error(self):
        """Test that non-numeric ID is invalid (edge case)."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("abc")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "Invalid ID. Please enter a numeric value."

    def test_validate_id_float_returns_error(self):
        """Test that decimal number is invalid."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("3.14")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "Invalid ID. Please enter a numeric value."

    def test_validate_id_empty_string_returns_error(self):
        """Test that empty string is invalid."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "Invalid ID. Please enter a numeric value."

    def test_validate_id_whitespace_returns_error(self):
        """Test that whitespace is invalid."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("   ")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "Invalid ID. Please enter a numeric value."

    def test_validate_id_mixed_alphanumeric_returns_error(self):
        """Test that mixed alphanumeric string is invalid."""
        # Arrange & Act
        is_valid, task_id, error = validate_id("12abc")

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error == "Invalid ID. Please enter a numeric value."

    @pytest.mark.parametrize("id_str,expected_id", [
        ("1", 1),
        ("10", 10),
        ("100", 100),
        ("1000", 1000),
    ])
    def test_validate_id_various_valid_numbers(self, id_str, expected_id):
        """Test validation of various valid ID numbers."""
        # Arrange & Act
        is_valid, task_id, error = validate_id(id_str)

        # Assert
        assert is_valid is True
        assert task_id == expected_id
        assert error is None

    @pytest.mark.parametrize("invalid_id", [
        "0",
        "-1",
        "-100",
        "abc",
        "1.5",
        "",
        " ",
        "!@#",
    ])
    def test_validate_id_various_invalid_inputs(self, invalid_id):
        """Test validation rejects various invalid inputs."""
        # Arrange & Act
        is_valid, task_id, error = validate_id(invalid_id)

        # Assert
        assert is_valid is False
        assert task_id is None
        assert error is not None


class TestValidateTitle:
    """Tests for title validation (FR-008)."""

    def test_validate_title_valid_title(self):
        """Test validation of valid title."""
        # Arrange & Act
        is_valid, title, warning = validate_title("Buy groceries")

        # Assert
        assert is_valid is True
        assert title == "Buy groceries"
        assert warning is None

    def test_validate_title_trims_whitespace(self):
        """Test that title is trimmed of leading/trailing whitespace."""
        # Arrange & Act
        is_valid, title, warning = validate_title("  Buy groceries  ")

        # Assert
        assert is_valid is True
        assert title == "Buy groceries"
        assert warning is None

    def test_validate_title_empty_string_returns_error(self):
        """Test that empty title is invalid (FR-008)."""
        # Arrange & Act
        is_valid, title, warning = validate_title("")

        # Assert
        assert is_valid is False
        assert title == ""
        assert warning == "Title cannot be empty."

    def test_validate_title_whitespace_only_returns_error(self):
        """Test that whitespace-only title is invalid (FR-008)."""
        # Arrange & Act
        is_valid, title, warning = validate_title("   ")

        # Assert
        assert is_valid is False
        assert title == ""
        assert warning == "Title cannot be empty."

    def test_validate_title_exactly_200_chars_no_warning(self):
        """Test title at exactly 200 character limit."""
        # Arrange
        title_200 = "A" * 200

        # Act
        is_valid, title, warning = validate_title(title_200)

        # Assert
        assert is_valid is True
        assert len(title) == 200
        assert title == title_200
        assert warning is None

    def test_validate_title_over_200_chars_truncates(self):
        """Test that title over 200 characters is truncated (edge case)."""
        # Arrange
        title_250 = "B" * 250

        # Act
        is_valid, title, warning = validate_title(title_250)

        # Assert
        assert is_valid is True
        assert len(title) == 200
        assert title == "B" * 200
        assert warning == "Warning: Title truncated to 200 characters."

    def test_validate_title_201_chars_truncates(self):
        """Test that title with 201 characters is truncated."""
        # Arrange
        title_201 = "C" * 201

        # Act
        is_valid, title, warning = validate_title(title_201)

        # Assert
        assert is_valid is True
        assert len(title) == 200
        assert warning == "Warning: Title truncated to 200 characters."

    def test_validate_title_single_character(self):
        """Test validation of single character title."""
        # Arrange & Act
        is_valid, title, warning = validate_title("X")

        # Assert
        assert is_valid is True
        assert title == "X"
        assert warning is None

    def test_validate_title_with_special_characters(self):
        """Test title containing special characters."""
        # Arrange & Act
        is_valid, title, warning = validate_title("Buy milk & eggs!")

        # Assert
        assert is_valid is True
        assert title == "Buy milk & eggs!"
        assert warning is None

    def test_validate_title_with_unicode(self):
        """Test title containing unicode characters."""
        # Arrange & Act
        is_valid, title, warning = validate_title("Buy café items")

        # Assert
        assert is_valid is True
        assert title == "Buy café items"
        assert warning is None

    @pytest.mark.parametrize("input_title,expected_title", [
        ("Normal title", "Normal title"),
        ("  Trimmed  ", "Trimmed"),
        ("\tTabbed\t", "Tabbed"),
        ("\nNewlined\n", "Newlined"),
    ])
    def test_validate_title_whitespace_handling(self, input_title, expected_title):
        """Test various whitespace handling scenarios."""
        # Arrange & Act
        is_valid, title, warning = validate_title(input_title)

        # Assert
        assert is_valid is True
        assert title == expected_title
        assert warning is None


class TestValidateDescription:
    """Tests for description validation."""

    def test_validate_description_valid_description(self):
        """Test validation of valid description."""
        # Arrange & Act
        description, warning = validate_description("This is a description")

        # Assert
        assert description == "This is a description"
        assert warning is None

    def test_validate_description_trims_whitespace(self):
        """Test that description is trimmed of leading/trailing whitespace."""
        # Arrange & Act
        description, warning = validate_description("  Description  ")

        # Assert
        assert description == "Description"
        assert warning is None

    def test_validate_description_empty_string(self):
        """Test validation of empty description (allowed)."""
        # Arrange & Act
        description, warning = validate_description("")

        # Assert
        assert description == ""
        assert warning is None

    def test_validate_description_whitespace_only(self):
        """Test that whitespace-only description becomes empty."""
        # Arrange & Act
        description, warning = validate_description("   ")

        # Assert
        assert description == ""
        assert warning is None

    def test_validate_description_exactly_1000_chars_no_warning(self):
        """Test description at exactly 1000 character limit."""
        # Arrange
        desc_1000 = "A" * 1000

        # Act
        description, warning = validate_description(desc_1000)

        # Assert
        assert len(description) == 1000
        assert description == desc_1000
        assert warning is None

    def test_validate_description_over_1000_chars_truncates(self):
        """Test that description over 1000 characters is truncated (edge case)."""
        # Arrange
        desc_1500 = "B" * 1500

        # Act
        description, warning = validate_description(desc_1500)

        # Assert
        assert len(description) == 1000
        assert description == "B" * 1000
        assert warning == "Warning: Description truncated to 1000 characters."

    def test_validate_description_1001_chars_truncates(self):
        """Test that description with 1001 characters is truncated."""
        # Arrange
        desc_1001 = "C" * 1001

        # Act
        description, warning = validate_description(desc_1001)

        # Assert
        assert len(description) == 1000
        assert warning == "Warning: Description truncated to 1000 characters."

    def test_validate_description_multiline(self):
        """Test description with multiple lines."""
        # Arrange
        multiline = "Line 1\nLine 2\nLine 3"

        # Act
        description, warning = validate_description(multiline)

        # Assert
        assert description == "Line 1\nLine 2\nLine 3"
        assert warning is None

    def test_validate_description_with_special_characters(self):
        """Test description containing special characters."""
        # Arrange & Act
        description, warning = validate_description("Description with @#$ symbols!")

        # Assert
        assert description == "Description with @#$ symbols!"
        assert warning is None

    def test_validate_description_with_unicode(self):
        """Test description containing unicode characters."""
        # Arrange & Act
        description, warning = validate_description("Café ☕ description")

        # Assert
        assert description == "Café ☕ description"
        assert warning is None

    @pytest.mark.parametrize("input_desc,expected_desc", [
        ("Normal description", "Normal description"),
        ("  Trimmed  ", "Trimmed"),
        ("\tTabbed\t", "Tabbed"),
        ("\nNewlined\n", "Newlined"),
        ("", ""),
        ("   ", ""),
    ])
    def test_validate_description_whitespace_handling(self, input_desc, expected_desc):
        """Test various whitespace handling scenarios."""
        # Arrange & Act
        description, warning = validate_description(input_desc)

        # Assert
        assert description == expected_desc

    def test_validate_description_preserves_internal_whitespace(self):
        """Test that internal whitespace is preserved."""
        # Arrange & Act
        description, warning = validate_description("Multiple   spaces   between")

        # Assert
        assert description == "Multiple   spaces   between"
        assert warning is None


class TestValidatorsIntegration:
    """Integration tests for validators working together."""

    def test_typical_task_creation_flow(self):
        """Test validators in a typical task creation scenario."""
        # Arrange
        id_str = "1"
        title_str = "  Buy groceries  "
        desc_str = "  Milk, eggs, bread  "

        # Act
        id_valid, task_id, id_error = validate_id(id_str)
        title_valid, title, title_warning = validate_title(title_str)
        description, desc_warning = validate_description(desc_str)

        # Assert
        assert id_valid is True
        assert task_id == 1
        assert title_valid is True
        assert title == "Buy groceries"
        assert description == "Milk, eggs, bread"
        assert id_error is None
        assert title_warning is None
        assert desc_warning is None

    def test_task_creation_with_long_inputs(self):
        """Test validators with inputs at character limits."""
        # Arrange
        title_250 = "T" * 250
        desc_1500 = "D" * 1500

        # Act
        title_valid, title, title_warning = validate_title(title_250)
        description, desc_warning = validate_description(desc_1500)

        # Assert
        assert title_valid is True
        assert len(title) == 200
        assert title_warning == "Warning: Title truncated to 200 characters."
        assert len(description) == 1000
        assert desc_warning == "Warning: Description truncated to 1000 characters."

    def test_task_creation_with_invalid_inputs(self):
        """Test validators with invalid inputs."""
        # Arrange
        id_str = "invalid"
        title_str = "   "

        # Act
        id_valid, task_id, id_error = validate_id(id_str)
        title_valid, title, title_warning = validate_title(title_str)

        # Assert
        assert id_valid is False
        assert id_error == "Invalid ID. Please enter a numeric value."
        assert title_valid is False
        assert title_warning == "Title cannot be empty."

    def test_minimal_valid_task_data(self):
        """Test validators with minimal valid input."""
        # Arrange
        id_str = "1"
        title_str = "X"
        desc_str = ""

        # Act
        id_valid, task_id, id_error = validate_id(id_str)
        title_valid, title, title_warning = validate_title(title_str)
        description, desc_warning = validate_description(desc_str)

        # Assert
        assert id_valid is True
        assert task_id == 1
        assert title_valid is True
        assert title == "X"
        assert description == ""
        assert all(w is None for w in [id_error, title_warning, desc_warning])
