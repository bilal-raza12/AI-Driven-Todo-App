"""Task model for the Todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique identifier for the task
        title: Task title (max 200 chars)
        description: Optional task description (max 1000 chars)
        is_complete: Task completion status
    """
    id: int
    title: str
    description: str = ""
    is_complete: bool = False
