# Phase I: In-Memory Python Todo Console App

A simple, clean implementation of a console-based todo application with in-memory storage.

## Features

- Add tasks with title and optional description
- View all tasks with completion status
- Mark tasks as complete or incomplete
- Update existing tasks
- Delete tasks
- Input validation and error handling
- Automatic truncation with warnings (title: 200 chars, description: 1000 chars)

## Project Structure

```
Phase-I/
└── src/
    ├── __init__.py           # Package marker
    ├── main.py               # Application entry point
    ├── models/
    │   ├── __init__.py
    │   └── task.py           # Task data model
    ├── services/
    │   ├── __init__.py
    │   └── task_service.py   # Business logic layer
    ├── cli/
    │   ├── __init__.py
    │   ├── menu.py           # Menu display
    │   └── handlers.py       # Command handlers
    └── lib/
        ├── __init__.py
        └── validators.py     # Input validation utilities
```

## Requirements

- Python 3.13+ (uses modern type hints and features)

## Running the Application

Navigate to the Phase-I/src directory and run:

```bash
cd Phase-I/src
python main.py
```

## Usage Examples

### Adding a Task
```
Enter choice (1-7): 1
Enter task title: Complete project documentation
Enter task description (optional): Write comprehensive README and API docs
Task added successfully with ID 1.
```

### Viewing Tasks
```
Enter choice (1-7): 2

--- All Tasks ---
[ ] ID: 1 | Complete project documentation
    Description: Write comprehensive README and API docs
[✓] ID: 2 | Review pull requests
```

### Marking Complete
```
Enter choice (1-7): 3
Enter task ID to mark complete: 1
Task 1 marked as complete.
```

### Updating a Task
```
Enter choice (1-7): 5
Enter task ID to update: 1
Current title: Complete project documentation
Enter new title (press Enter to keep current):
Current description: Write comprehensive README and API docs
Enter new description (press Enter to keep current): Add API examples and architecture diagrams
Task 1 updated successfully.
```

### Deleting a Task
```
Enter choice (1-7): 6
Enter task ID to delete: 2
Task 2 deleted successfully.
```

## Error Handling

The application includes comprehensive error handling:

- **Empty titles**: "Title cannot be empty."
- **Invalid task IDs**: "Task not found with ID {id}."
- **Non-numeric IDs**: "Invalid ID. Please enter a numeric value."
- **Negative IDs**: "ID must be a positive number."
- **Invalid menu choices**: "Invalid choice. Please enter a number between 1 and 7."
- **Truncation warnings**: Automatic warnings when title/description exceed limits

## Implementation Details

### Task Model
- Uses Python dataclass for clean, immutable-by-convention data structures
- Fields: id (int), title (str), description (str), is_complete (bool)

### Service Layer
- In-memory storage using dictionary
- Auto-incrementing ID generation
- Returns boolean success indicators for operations

### Validation Layer
- Separate validators for ID, title, and description
- Returns tuples with validation status, processed value, and error/warning messages
- Supports "keep current" functionality for updates

### Clean Code Principles Applied
- Single Responsibility: Each module has one clear purpose
- DRY: Validation logic centralized in validators module
- Clear naming: Functions and variables use descriptive names
- Type hints: Full type annotations for better IDE support and safety
- Error handling: Consistent error messages and user feedback
- Separation of concerns: Models, services, CLI, and utilities in separate layers

## Design Decisions

1. **Dataclass for Task**: Provides automatic `__init__`, `__repr__`, and equality methods
2. **Dictionary storage**: O(1) lookups by task ID, simple and efficient for in-memory use
3. **Validator tuples**: Return multiple values (valid, processed_value, message) for flexible handling
4. **Service returns boolean**: Simple success/failure indication for operations
5. **Path manipulation in main**: Ensures imports work regardless of execution directory
6. **Strip whitespace**: All inputs are stripped to handle accidental spaces
7. **Optional description**: Users can press Enter to skip description input

## Testing Recommendations

To verify the implementation, test:
- All 7 menu options
- Empty title validation
- ID validation (non-numeric, negative, non-existent)
- Truncation warnings (title > 200 chars, description > 1000 chars)
- "Keep current" behavior in updates
- Empty task list message
- Exit functionality

## Future Enhancements (Out of Scope for Phase I)

- Persistent storage (database, file)
- Task filtering and search
- Due dates and priorities
- Task categories/tags
- Export/import functionality
- Multi-user support
