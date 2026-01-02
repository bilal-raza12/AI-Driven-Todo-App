"""CLI command handlers for the Todo application."""

from services.task_service import TaskService
from lib.validators import validate_id, validate_title, validate_description


def handle_add_task(service: TaskService) -> None:
    """Handle adding a new task.

    Args:
        service: TaskService instance
    """
    title_input = input("Enter task title: ")
    is_valid, title, warning = validate_title(title_input)

    if not is_valid:
        print(warning)
        return

    if warning:
        print(warning)

    description_input = input("Enter task description (optional): ")
    description, desc_warning = validate_description(description_input)

    if desc_warning:
        print(desc_warning)

    task = service.add_task(title, description)
    print(f"Task added successfully with ID {task.id}.")


def handle_view_tasks(service: TaskService) -> None:
    """Handle viewing all tasks.

    Args:
        service: TaskService instance
    """
    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- All Tasks ---")
    for task in tasks:
        status = "✓" if task.is_complete else " "
        print(f"[{status}] ID: {task.id} | {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
    print()


def handle_mark_complete(service: TaskService) -> None:
    """Handle marking a task as complete.

    Args:
        service: TaskService instance
    """
    id_input = input("Enter task ID to mark complete: ")
    is_valid, task_id, error = validate_id(id_input)

    if not is_valid:
        print(error)
        return

    success = service.mark_complete(task_id)
    if success:
        print(f"Task {task_id} marked as complete.")
    else:
        print(f"Task not found with ID {task_id}.")


def handle_mark_incomplete(service: TaskService) -> None:
    """Handle marking a task as incomplete.

    Args:
        service: TaskService instance
    """
    id_input = input("Enter task ID to mark incomplete: ")
    is_valid, task_id, error = validate_id(id_input)

    if not is_valid:
        print(error)
        return

    success = service.mark_incomplete(task_id)
    if success:
        print(f"Task {task_id} marked as incomplete.")
    else:
        print(f"Task not found with ID {task_id}.")


def handle_update_task(service: TaskService) -> None:
    """Handle updating a task.

    Args:
        service: TaskService instance
    """
    id_input = input("Enter task ID to update: ")
    is_valid, task_id, error = validate_id(id_input)

    if not is_valid:
        print(error)
        return

    task = service.get_task(task_id)
    if task is None:
        print(f"Task not found with ID {task_id}.")
        return

    print(f"Current title: {task.title}")
    title_input = input("Enter new title (press Enter to keep current): ")

    if title_input.strip():
        is_valid, title, warning = validate_title(title_input)
        if not is_valid:
            print(warning)
            return
        if warning:
            print(warning)
    else:
        title = task.title

    print(f"Current description: {task.description}")
    description_input = input("Enter new description (press Enter to keep current): ")

    if description_input.strip():
        description, desc_warning = validate_description(description_input)
        if desc_warning:
            print(desc_warning)
    else:
        description = task.description

    service.update_task(task_id, title, description)
    print(f"Task {task_id} updated successfully.")


def handle_delete_task(service: TaskService) -> None:
    """Handle deleting a task.

    Args:
        service: TaskService instance
    """
    id_input = input("Enter task ID to delete: ")
    is_valid, task_id, error = validate_id(id_input)

    if not is_valid:
        print(error)
        return

    success = service.delete_task(task_id)
    if success:
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task not found with ID {task_id}.")


def handle_exit() -> None:
    """Handle application exit."""
    print("Goodbye!")
