# Feature Specification: In-Memory Python Todo Console App

**Feature Branch**: `001-inmemory-todo-cli`
**Created**: 2026-01-01
**Status**: Draft
**Phase**: I (Foundation)
**Input**: User description: "Phase I – In-Memory Python Todo Console App with CRUD operations"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a New Task (Priority: P1)

As a user, I want to add a new task with a title and description so that I can track work items I need to complete.

**Why this priority**: Adding tasks is the foundational operation. Without the ability to create tasks, no other functionality is useful. This enables the core value proposition of the todo app.

**Independent Test**: Can be fully tested by running the app, selecting "add task", entering a title and description, and verifying the task appears in the list with a unique ID and "incomplete" status.

**Acceptance Scenarios**:

1. **Given** the app is running with no tasks, **When** user selects "add task" and enters title "Buy groceries" and description "Milk, eggs, bread", **Then** a new task is created with a unique numeric ID, the provided title and description, and completion status set to "incomplete".

2. **Given** the app has existing tasks with IDs 1, 2, 3, **When** user adds a new task, **Then** the new task receives ID 4 (next sequential ID).

3. **Given** the app is running, **When** user attempts to add a task with an empty title, **Then** the system displays an error message "Title cannot be empty" and does not create the task.

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I want to view all my tasks in a clear list format so that I can see what work I have pending and completed.

**Why this priority**: Viewing tasks is essential for the app to be useful. Users need to see their tasks to decide what to work on next. This is tied with adding tasks as the core MVP.

**Independent Test**: Can be fully tested by adding several tasks, then selecting "view tasks" and verifying all tasks display with ID, title, description, and completion status in a readable format.

**Acceptance Scenarios**:

1. **Given** the app has tasks (ID: 1, Title: "Buy groceries", Status: incomplete) and (ID: 2, Title: "Call mom", Status: complete), **When** user selects "view all tasks", **Then** all tasks display showing ID, title, description, and completion status in a formatted list.

2. **Given** the app has no tasks, **When** user selects "view all tasks", **Then** the system displays "No tasks found."

---

### User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

As a user, I want to toggle a task's completion status so that I can track my progress on work items.

**Why this priority**: Marking tasks complete is the primary way users track progress. Without this, the app cannot fulfill its purpose of helping users manage completed vs pending work.

**Independent Test**: Can be fully tested by adding a task, marking it complete, viewing tasks to verify status changed, then marking it incomplete again and verifying the toggle works.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists and is marked "incomplete", **When** user selects "mark complete" and enters ID 1, **Then** the task's status changes to "complete" and a confirmation message displays.

2. **Given** a task with ID 1 exists and is marked "complete", **When** user selects "mark incomplete" and enters ID 1, **Then** the task's status changes to "incomplete" and a confirmation message displays.

3. **Given** no task exists with ID 999, **When** user attempts to mark task 999 complete, **Then** the system displays "Task not found with ID 999."

---

### User Story 4 - Update Task (Priority: P3)

As a user, I want to update a task's title or description so that I can correct mistakes or add more details.

**Why this priority**: Updating tasks is important for maintaining accurate task information but is less critical than the core add/view/complete workflow.

**Independent Test**: Can be fully tested by adding a task, updating its title and/or description, then viewing tasks to verify the changes persisted.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists with title "Buy grocries", **When** user selects "update task", enters ID 1, and provides new title "Buy groceries", **Then** the task's title is updated and a confirmation message displays.

2. **Given** a task with ID 1 exists, **When** user updates only the description (leaving title unchanged), **Then** only the description is modified.

3. **Given** no task exists with ID 999, **When** user attempts to update task 999, **Then** the system displays "Task not found with ID 999."

4. **Given** a task exists, **When** user attempts to update with an empty title, **Then** the system displays "Title cannot be empty" and does not modify the task.

---

### User Story 5 - Delete Task (Priority: P3)

As a user, I want to delete a task so that I can remove items that are no longer relevant.

**Why this priority**: Deleting tasks is useful for cleanup but is the least critical operation. Users can mark tasks complete instead of deleting them.

**Independent Test**: Can be fully tested by adding a task, deleting it by ID, then viewing tasks to verify it no longer appears.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** user selects "delete task" and enters ID 1, **Then** the task is removed from the system and a confirmation message displays.

2. **Given** no task exists with ID 999, **When** user attempts to delete task 999, **Then** the system displays "Task not found with ID 999."

3. **Given** tasks with IDs 1, 2, 3 exist, **When** user deletes task ID 2, **Then** only task 2 is removed; tasks 1 and 3 remain unchanged.

---

### Edge Cases

- What happens when user enters non-numeric input for task ID? System displays "Invalid ID. Please enter a numeric value."
- What happens when user enters negative ID? System displays "Invalid ID. ID must be a positive number."
- What happens when title exceeds reasonable length (>200 characters)? System truncates to 200 characters with a warning message.
- What happens when description exceeds reasonable length (>1000 characters)? System truncates to 1000 characters with a warning message.
- What happens when user provides only whitespace for title? System treats as empty and displays "Title cannot be empty."
- What happens when user exits without saving? All tasks are lost (expected behavior for in-memory storage).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a new task with a title (required) and description (optional).
- **FR-002**: System MUST assign a unique, sequential numeric ID to each new task.
- **FR-003**: System MUST set new tasks to "incomplete" status by default.
- **FR-004**: System MUST display all tasks with their ID, title, description, and completion status.
- **FR-005**: System MUST allow users to update a task's title and/or description by ID.
- **FR-006**: System MUST allow users to delete a task by ID.
- **FR-007**: System MUST allow users to toggle a task's completion status (complete/incomplete) by ID.
- **FR-008**: System MUST validate that task title is non-empty and non-whitespace.
- **FR-009**: System MUST display clear error messages for invalid operations (task not found, invalid ID format).
- **FR-010**: System MUST provide a menu-driven interface for all operations.
- **FR-011**: System MUST allow users to exit the application gracefully.
- **FR-012**: System MUST store all tasks in memory only (no persistence between sessions).

### Non-Functional Requirements

- **NFR-001**: System MUST run on Python 3.13+.
- **NFR-002**: System MUST operate as a console/terminal application only.
- **NFR-003**: System MUST NOT include any GUI, web interface, or networking capabilities.
- **NFR-004**: System MUST NOT include any AI, machine learning, or natural language processing features.
- **NFR-005**: System MUST NOT persist data to files, databases, or any external storage.

### Key Entities

- **Task**: Represents a single todo item with the following attributes:
  - `id`: Unique numeric identifier (auto-generated, sequential)
  - `title`: Short description of the task (required, max 200 characters)
  - `description`: Detailed description of the task (optional, max 1000 characters)
  - `is_complete`: Boolean indicating completion status (default: false)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a new task with title and description in under 30 seconds.
- **SC-002**: Users can view all tasks and identify any specific task within 5 seconds of display.
- **SC-003**: Users can mark a task complete or incomplete in under 10 seconds.
- **SC-004**: Users can update a task's title or description in under 30 seconds.
- **SC-005**: Users can delete a task in under 10 seconds.
- **SC-006**: All five CRUD operations (Create, Read, Update, Delete, Toggle status) function correctly on first use.
- **SC-007**: System displays clear, actionable error messages for 100% of invalid inputs.
- **SC-008**: Application runs without errors for an entire session of at least 20 operations.
- **SC-009**: Output is clearly formatted and readable in a standard 80-column terminal.

## Assumptions

- Users are familiar with command-line interfaces and menu-driven applications.
- A "session" ends when the user exits the application; all data is expected to be lost.
- Task IDs are positive integers starting from 1 and incrementing sequentially.
- The application will be run in a terminal that supports standard text output.
- Description field is optional; if not provided, it defaults to an empty string.

## Out of Scope

- Data persistence (files, databases)
- User authentication or multi-user support
- Graphical user interface
- Web interface
- AI/ML features or natural language processing
- Networking or API endpoints
- Task categories, tags, or priorities
- Due dates or reminders
- Search or filter functionality
- Undo/redo operations
