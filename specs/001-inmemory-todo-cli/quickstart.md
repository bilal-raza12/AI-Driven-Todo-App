# Quickstart: In-Memory Python Todo Console App

**Feature**: 001-inmemory-todo-cli
**Date**: 2026-01-01

## Prerequisites

- Python 3.13 or higher
- Terminal/console access

## Installation

No installation required. Clone the repository and run:

```bash
# Navigate to the project root
cd AI-driven-todo-App

# Run the application
python -m src.main
```

Or directly:

```bash
python src/main.py
```

## Usage

### Starting the App

```
=== Todo App ===
1. Add Task
2. View All Tasks
3. Mark Task Complete
4. Mark Task Incomplete
5. Update Task
6. Delete Task
7. Exit

Enter choice (1-7):
```

### Adding a Task

```
Enter choice (1-7): 1

=== Add Task ===
Enter title: Buy groceries
Enter description (optional): Milk, eggs, bread

Task added successfully with ID 1.
```

### Viewing All Tasks

```
Enter choice (1-7): 2

=== All Tasks ===
ID: 1 | Title: Buy groceries | Status: Incomplete
   Description: Milk, eggs, bread

ID: 2 | Title: Call mom | Status: Complete
   Description: Wish her happy birthday
```

Or when empty:

```
Enter choice (1-7): 2

No tasks found.
```

### Marking Task Complete

```
Enter choice (1-7): 3

=== Mark Task Complete ===
Enter task ID: 1

Task 1 marked as complete.
```

### Marking Task Incomplete

```
Enter choice (1-7): 4

=== Mark Task Incomplete ===
Enter task ID: 1

Task 1 marked as incomplete.
```

### Updating a Task

```
Enter choice (1-7): 5

=== Update Task ===
Enter task ID: 1
Current title: Buy groceries
Enter new title (press Enter to keep current): Buy groceries and snacks
Current description: Milk, eggs, bread
Enter new description (press Enter to keep current): Milk, eggs, bread, chips

Task 1 updated successfully.
```

### Deleting a Task

```
Enter choice (1-7): 6

=== Delete Task ===
Enter task ID: 1

Task 1 deleted successfully.
```

### Exiting

```
Enter choice (1-7): 7

Goodbye!
```

## Error Handling Examples

### Invalid Menu Choice

```
Enter choice (1-7): 9

Invalid choice. Please enter a number between 1 and 7.
```

### Invalid Task ID

```
Enter task ID: abc

Invalid ID. Please enter a numeric value.
```

### Task Not Found

```
Enter task ID: 999

Task not found with ID 999.
```

### Empty Title

```
Enter title:

Title cannot be empty.
```

### Long Title (Truncation)

```
Enter title: [very long title over 200 characters...]

Warning: Title truncated to 200 characters.
Task added successfully with ID 1.
```

## Data Persistence

**Important**: This is an in-memory application. All tasks are lost when you exit. This is expected behavior for Phase I. Persistence will be added in Phase II.

## Keyboard Shortcuts

- `Ctrl+C`: Force quit (tasks will be lost)
- Standard terminal navigation applies

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "python: command not found" | Ensure Python 3.13+ is installed and in PATH |
| "ModuleNotFoundError" | Run from project root directory |
| "Permission denied" | Check file permissions on src/main.py |

## Next Steps

1. Add tasks and explore CRUD operations
2. Test edge cases (empty title, invalid IDs)
3. Verify all acceptance scenarios from spec
