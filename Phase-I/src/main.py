"""Main entry point for the In-Memory Todo Console App."""

import sys
from pathlib import Path

# Add src directory to Python path for imports
src_dir = Path(__file__).parent
sys.path.insert(0, str(src_dir))

from services.task_service import TaskService
from cli.menu import display_menu
from cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_mark_complete,
    handle_mark_incomplete,
    handle_update_task,
    handle_delete_task,
    handle_exit
)


def main() -> None:
    """Main application loop."""
    service = TaskService()

    while True:
        display_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            handle_add_task(service)
        elif choice == "2":
            handle_view_tasks(service)
        elif choice == "3":
            handle_mark_complete(service)
        elif choice == "4":
            handle_mark_incomplete(service)
        elif choice == "5":
            handle_update_task(service)
        elif choice == "6":
            handle_delete_task(service)
        elif choice == "7":
            handle_exit()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
