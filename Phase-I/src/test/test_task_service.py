"""Tests for the TaskService CRUD operations."""

import pytest
from models.task import Task
from services.task_service import TaskService


class TestTaskServiceInitialization:
    """Tests for TaskService initialization."""

    def test_initialization_creates_empty_task_list(self):
        """Test that new service starts with empty task list."""
        # Arrange & Act
        service = TaskService()

        # Assert
        assert service.get_all_tasks() == []

    def test_initialization_sets_next_id_to_one(self):
        """Test that new service starts with ID counter at 1 (FR-002)."""
        # Arrange & Act
        service = TaskService()
        task = service.add_task("First Task")

        # Assert
        assert task.id == 1


class TestAddTask:
    """Tests for adding tasks."""

    @pytest.fixture
    def service(self):
        """Fixture providing a fresh TaskService instance."""
        return TaskService()

    def test_add_task_with_title_only(self, service):
        """Test adding task with title only (FR-001)."""
        # Arrange & Act
        task = service.add_task("Buy groceries")

        # Assert
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.is_complete is False
        assert task.id == 1

    def test_add_task_with_title_and_description(self, service):
        """Test adding task with both title and description (FR-001)."""
        # Arrange & Act
        task = service.add_task("Buy groceries", "Milk, eggs, bread")

        # Assert
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert task.is_complete is False

    def test_add_task_assigns_sequential_ids(self, service):
        """Test that tasks receive sequential IDs (FR-002)."""
        # Arrange & Act
        task1 = service.add_task("First")
        task2 = service.add_task("Second")
        task3 = service.add_task("Third")

        # Assert
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_default_incomplete_status(self, service):
        """Test that new tasks default to incomplete status (FR-003)."""
        # Arrange & Act
        task = service.add_task("Test Task")

        # Assert
        assert task.is_complete is False

    def test_add_task_returns_task_object(self, service):
        """Test that add_task returns the created Task."""
        # Arrange & Act
        result = service.add_task("Test")

        # Assert
        assert isinstance(result, Task)

    def test_add_multiple_tasks_all_stored(self, service):
        """Test that multiple added tasks are all stored."""
        # Arrange & Act
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")

        # Assert
        tasks = service.get_all_tasks()
        assert len(tasks) == 3

    def test_add_task_with_empty_description(self, service):
        """Test adding task with explicitly empty description."""
        # Arrange & Act
        task = service.add_task("Task", "")

        # Assert
        assert task.description == ""


class TestGetAllTasks:
    """Tests for retrieving all tasks."""

    @pytest.fixture
    def service(self):
        """Fixture providing a fresh TaskService instance."""
        return TaskService()

    def test_get_all_tasks_empty_list_when_no_tasks(self, service):
        """Test that get_all_tasks returns empty list when no tasks exist."""
        # Arrange & Act
        tasks = service.get_all_tasks()

        # Assert
        assert tasks == []
        assert isinstance(tasks, list)

    def test_get_all_tasks_returns_all_tasks(self, service):
        """Test that get_all_tasks returns all added tasks."""
        # Arrange
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")

        # Act
        tasks = service.get_all_tasks()

        # Assert
        assert len(tasks) == 3
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"

    def test_get_all_tasks_ordered_by_id(self, service):
        """Test that tasks are returned in ID order."""
        # Arrange
        service.add_task("First")
        service.add_task("Second")
        service.add_task("Third")

        # Act
        tasks = service.get_all_tasks()

        # Assert
        assert tasks[0].id < tasks[1].id < tasks[2].id


class TestGetTask:
    """Tests for retrieving a specific task."""

    @pytest.fixture
    def service(self):
        """Fixture providing a TaskService with sample tasks."""
        svc = TaskService()
        svc.add_task("Task 1", "Description 1")
        svc.add_task("Task 2", "Description 2")
        svc.add_task("Task 3", "Description 3")
        return svc

    def test_get_task_existing_id_returns_task(self, service):
        """Test retrieving an existing task by ID."""
        # Arrange & Act
        task = service.get_task(2)

        # Assert
        assert task is not None
        assert task.id == 2
        assert task.title == "Task 2"

    def test_get_task_nonexistent_id_returns_none(self, service):
        """Test retrieving a non-existent task returns None."""
        # Arrange & Act
        task = service.get_task(999)

        # Assert
        assert task is None

    def test_get_task_negative_id_returns_none(self, service):
        """Test that negative ID returns None (edge case)."""
        # Arrange & Act
        task = service.get_task(-1)

        # Assert
        assert task is None

    def test_get_task_zero_id_returns_none(self, service):
        """Test that zero ID returns None (edge case)."""
        # Arrange & Act
        task = service.get_task(0)

        # Assert
        assert task is None

    @pytest.mark.parametrize("task_id", [1, 2, 3])
    def test_get_task_all_valid_ids(self, service, task_id):
        """Test retrieving each valid task ID."""
        # Arrange & Act
        task = service.get_task(task_id)

        # Assert
        assert task is not None
        assert task.id == task_id


class TestMarkComplete:
    """Tests for marking tasks as complete."""

    @pytest.fixture
    def service(self):
        """Fixture providing a TaskService with sample tasks."""
        svc = TaskService()
        svc.add_task("Task 1")
        svc.add_task("Task 2")
        return svc

    def test_mark_complete_existing_task_returns_true(self, service):
        """Test marking an existing task as complete."""
        # Arrange & Act
        result = service.mark_complete(1)

        # Assert
        assert result is True

    def test_mark_complete_updates_task_status(self, service):
        """Test that mark_complete actually updates the task."""
        # Arrange
        service.mark_complete(1)

        # Act
        task = service.get_task(1)

        # Assert
        assert task.is_complete is True

    def test_mark_complete_nonexistent_task_returns_false(self, service):
        """Test marking non-existent task returns False."""
        # Arrange & Act
        result = service.mark_complete(999)

        # Assert
        assert result is False

    def test_mark_complete_already_complete_task(self, service):
        """Test marking an already complete task."""
        # Arrange
        service.mark_complete(1)

        # Act
        result = service.mark_complete(1)

        # Assert
        assert result is True
        assert service.get_task(1).is_complete is True

    def test_mark_complete_does_not_affect_other_tasks(self, service):
        """Test that marking one task complete doesn't affect others."""
        # Arrange & Act
        service.mark_complete(1)

        # Assert
        assert service.get_task(1).is_complete is True
        assert service.get_task(2).is_complete is False


class TestMarkIncomplete:
    """Tests for marking tasks as incomplete."""

    @pytest.fixture
    def service(self):
        """Fixture providing a TaskService with completed tasks."""
        svc = TaskService()
        svc.add_task("Task 1")
        svc.add_task("Task 2")
        svc.mark_complete(1)
        svc.mark_complete(2)
        return svc

    def test_mark_incomplete_existing_task_returns_true(self, service):
        """Test marking an existing task as incomplete."""
        # Arrange & Act
        result = service.mark_incomplete(1)

        # Assert
        assert result is True

    def test_mark_incomplete_updates_task_status(self, service):
        """Test that mark_incomplete actually updates the task."""
        # Arrange
        service.mark_incomplete(1)

        # Act
        task = service.get_task(1)

        # Assert
        assert task.is_complete is False

    def test_mark_incomplete_nonexistent_task_returns_false(self, service):
        """Test marking non-existent task returns False."""
        # Arrange & Act
        result = service.mark_incomplete(999)

        # Assert
        assert result is False

    def test_mark_incomplete_already_incomplete_task(self, service):
        """Test marking an already incomplete task."""
        # Arrange
        service.mark_incomplete(1)

        # Act
        result = service.mark_incomplete(1)

        # Assert
        assert result is True
        assert service.get_task(1).is_complete is False


class TestUpdateTask:
    """Tests for updating task title and description."""

    @pytest.fixture
    def service(self):
        """Fixture providing a TaskService with sample tasks."""
        svc = TaskService()
        svc.add_task("Original Title", "Original Description")
        return svc

    def test_update_task_existing_task_returns_true(self, service):
        """Test updating an existing task returns True."""
        # Arrange & Act
        result = service.update_task(1, "New Title", "New Description")

        # Assert
        assert result is True

    def test_update_task_updates_title_and_description(self, service):
        """Test that update_task actually updates both fields."""
        # Arrange
        service.update_task(1, "Updated Title", "Updated Description")

        # Act
        task = service.get_task(1)

        # Assert
        assert task.title == "Updated Title"
        assert task.description == "Updated Description"

    def test_update_task_nonexistent_task_returns_false(self, service):
        """Test updating non-existent task returns False."""
        # Arrange & Act
        result = service.update_task(999, "Title", "Description")

        # Assert
        assert result is False

    def test_update_task_preserves_completion_status(self, service):
        """Test that update preserves the completion status."""
        # Arrange
        service.mark_complete(1)

        # Act
        service.update_task(1, "New Title", "New Desc")

        # Assert
        task = service.get_task(1)
        assert task.is_complete is True

    def test_update_task_with_empty_description(self, service):
        """Test updating with empty description."""
        # Arrange & Act
        service.update_task(1, "Title", "")

        # Assert
        task = service.get_task(1)
        assert task.description == ""

    def test_update_task_preserves_id(self, service):
        """Test that update preserves the task ID."""
        # Arrange
        service.update_task(1, "New Title", "New Desc")

        # Act
        task = service.get_task(1)

        # Assert
        assert task.id == 1


class TestDeleteTask:
    """Tests for deleting tasks."""

    @pytest.fixture
    def service(self):
        """Fixture providing a TaskService with sample tasks."""
        svc = TaskService()
        svc.add_task("Task 1")
        svc.add_task("Task 2")
        svc.add_task("Task 3")
        return svc

    def test_delete_task_existing_task_returns_true(self, service):
        """Test deleting an existing task returns True."""
        # Arrange & Act
        result = service.delete_task(2)

        # Assert
        assert result is True

    def test_delete_task_removes_task(self, service):
        """Test that delete_task actually removes the task."""
        # Arrange
        service.delete_task(2)

        # Act
        task = service.get_task(2)

        # Assert
        assert task is None

    def test_delete_task_nonexistent_task_returns_false(self, service):
        """Test deleting non-existent task returns False."""
        # Arrange & Act
        result = service.delete_task(999)

        # Assert
        assert result is False

    def test_delete_task_reduces_task_count(self, service):
        """Test that deleting reduces the task count."""
        # Arrange
        initial_count = len(service.get_all_tasks())

        # Act
        service.delete_task(2)

        # Assert
        assert len(service.get_all_tasks()) == initial_count - 1

    def test_delete_task_does_not_affect_other_tasks(self, service):
        """Test that deleting one task doesn't affect others."""
        # Arrange & Act
        service.delete_task(2)

        # Assert
        assert service.get_task(1) is not None
        assert service.get_task(3) is not None

    def test_delete_all_tasks(self, service):
        """Test deleting all tasks."""
        # Arrange & Act
        service.delete_task(1)
        service.delete_task(2)
        service.delete_task(3)

        # Assert
        assert len(service.get_all_tasks()) == 0

    def test_delete_task_does_not_reset_id_counter(self, service):
        """Test that deleting tasks doesn't reset the ID counter."""
        # Arrange
        service.delete_task(1)
        service.delete_task(2)
        service.delete_task(3)

        # Act
        new_task = service.add_task("New Task")

        # Assert
        assert new_task.id == 4


class TestTaskServiceIntegration:
    """Integration tests for TaskService workflows."""

    def test_complete_crud_workflow(self):
        """Test a complete Create-Read-Update-Delete workflow."""
        # Arrange
        service = TaskService()

        # Act & Assert - Create
        task = service.add_task("Learn Python", "Study pytest testing")
        assert task.id == 1

        # Act & Assert - Read
        retrieved = service.get_task(1)
        assert retrieved.title == "Learn Python"

        # Act & Assert - Update
        service.update_task(1, "Master Python", "Advanced pytest")
        updated = service.get_task(1)
        assert updated.title == "Master Python"

        # Act & Assert - Complete
        service.mark_complete(1)
        assert service.get_task(1).is_complete is True

        # Act & Assert - Delete
        service.delete_task(1)
        assert service.get_task(1) is None

    def test_multiple_tasks_independent_operations(self):
        """Test that operations on multiple tasks work independently."""
        # Arrange
        service = TaskService()
        service.add_task("Task A")
        service.add_task("Task B")
        service.add_task("Task C")

        # Act
        service.mark_complete(1)
        service.update_task(2, "Task B Updated", "New description")
        service.delete_task(3)

        # Assert
        task_a = service.get_task(1)
        task_b = service.get_task(2)
        task_c = service.get_task(3)

        assert task_a.is_complete is True
        assert task_b.title == "Task B Updated"
        assert task_c is None
        assert len(service.get_all_tasks()) == 2
