"""Command-line interface components for the Todo application."""

from .menu import display_menu
from .handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_mark_complete,
    handle_mark_incomplete,
    handle_update_task,
    handle_delete_task,
    handle_exit
)

__all__ = [
    "display_menu",
    "handle_add_task",
    "handle_view_tasks",
    "handle_mark_complete",
    "handle_mark_incomplete",
    "handle_update_task",
    "handle_delete_task",
    "handle_exit"
]
