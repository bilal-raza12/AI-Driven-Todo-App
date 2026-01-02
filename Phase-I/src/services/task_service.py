"""Task service for managing todo tasks in memory."""

from typing import Optional
from models.task import Task


class TaskService:
    """Manages todo tasks with in-memory storage."""

    def __init__(self):
        """Initialize task service with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task.

        Args:
            title: Task title
            description: Optional task description

        Returns:
            The newly created Task
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            is_complete=False
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks.

        Returns:
            List of all tasks, ordered by ID
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID.

        Args:
            task_id: Task identifier

        Returns:
            Task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: Task identifier

        Returns:
            True if task was found and marked, False otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.is_complete = True
        return True

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete.

        Args:
            task_id: Task identifier

        Returns:
            True if task was found and marked, False otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.is_complete = False
        return True

    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """Update a task's title and description.

        Args:
            task_id: Task identifier
            title: New task title
            description: New task description

        Returns:
            True if task was found and updated, False otherwise
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.title = title
        task.description = description
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task.

        Args:
            task_id: Task identifier

        Returns:
            True if task was found and deleted, False otherwise
        """
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True
