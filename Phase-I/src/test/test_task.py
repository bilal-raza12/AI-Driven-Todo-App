"""Tests for the Task dataclass model."""

import pytest
from models.task import Task


class TestTaskModel:
    """Tests for Task dataclass."""

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields specified."""
        # Arrange & Act
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            is_complete=True
        )

        # Assert
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.is_complete is True

    def test_task_creation_with_minimal_fields(self):
        """Test creating a task with only required fields."""
        # Arrange & Act
        task = Task(id=1, title="Minimal Task")

        # Assert
        assert task.id == 1
        assert task.title == "Minimal Task"
        assert task.description == ""
        assert task.is_complete is False

    def test_task_default_description_is_empty_string(self):
        """Test that default description is empty string."""
        # Arrange & Act
        task = Task(id=1, title="Test")

        # Assert
        assert task.description == ""
        assert isinstance(task.description, str)

    def test_task_default_is_complete_is_false(self):
        """Test that default is_complete is False (FR-003)."""
        # Arrange & Act
        task = Task(id=1, title="Test")

        # Assert
        assert task.is_complete is False

    def test_task_with_long_title(self):
        """Test task with title at 200 character limit."""
        # Arrange
        long_title = "A" * 200

        # Act
        task = Task(id=1, title=long_title)

        # Assert
        assert len(task.title) == 200
        assert task.title == long_title

    def test_task_with_long_description(self):
        """Test task with description at 1000 character limit."""
        # Arrange
        long_description = "B" * 1000

        # Act
        task = Task(id=1, title="Test", description=long_description)

        # Assert
        assert len(task.description) == 1000
        assert task.description == long_description

    def test_task_id_is_integer(self):
        """Test that task ID is an integer."""
        # Arrange & Act
        task = Task(id=42, title="Test")

        # Assert
        assert isinstance(task.id, int)
        assert task.id == 42

    def test_task_is_dataclass(self):
        """Test that Task is a proper dataclass."""
        # Arrange & Act
        task1 = Task(id=1, title="Test")
        task2 = Task(id=1, title="Test")

        # Assert - dataclasses are equal if fields are equal
        assert task1 == task2

    def test_task_repr_contains_fields(self):
        """Test that task repr contains all field information."""
        # Arrange & Act
        task = Task(id=1, title="Test", description="Desc", is_complete=True)
        repr_str = repr(task)

        # Assert
        assert "id=1" in repr_str
        assert "title='Test'" in repr_str
        assert "description='Desc'" in repr_str
        assert "is_complete=True" in repr_str

    @pytest.mark.parametrize("task_id,expected", [
        (1, 1),
        (999, 999),
        (100000, 100000),
    ])
    def test_task_with_various_ids(self, task_id, expected):
        """Test task creation with various valid ID values."""
        # Arrange & Act
        task = Task(id=task_id, title="Test")

        # Assert
        assert task.id == expected

    def test_task_completion_toggle(self):
        """Test toggling task completion status."""
        # Arrange
        task = Task(id=1, title="Test", is_complete=False)

        # Act & Assert - toggle to complete
        task.is_complete = True
        assert task.is_complete is True

        # Act & Assert - toggle back to incomplete
        task.is_complete = False
        assert task.is_complete is False

    def test_task_field_mutation(self):
        """Test that task fields can be mutated after creation."""
        # Arrange
        task = Task(id=1, title="Original", description="Original Desc")

        # Act
        task.title = "Updated"
        task.description = "Updated Desc"
        task.is_complete = True

        # Assert
        assert task.title == "Updated"
        assert task.description == "Updated Desc"
        assert task.is_complete is True
