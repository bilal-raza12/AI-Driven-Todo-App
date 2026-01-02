# Research: In-Memory Python Todo Console App

**Feature**: 001-inmemory-todo-cli
**Date**: 2026-01-01
**Status**: Complete

## Overview

This document captures research findings and architectural decisions for Phase I of the AI-Driven Todo App—a menu-driven console application with in-memory storage.

## Research Tasks

### 1. Task Data Model Structure

**Decision**: Use Python `dataclass` with four fields

**Rationale**:
- `dataclass` provides clean, type-hinted, immutable-friendly structure
- Automatic `__repr__`, `__eq__` generation reduces boilerplate
- Native to Python 3.7+ (well within Python 3.13+ constraint)

**Fields**:
| Field | Type | Default | Constraints |
|-------|------|---------|-------------|
| `id` | `int` | (required) | Positive, auto-generated, sequential |
| `title` | `str` | (required) | 1-200 characters, non-whitespace |
| `description` | `str` | `""` | 0-1000 characters |
| `is_complete` | `bool` | `False` | Toggleable |

**Alternatives Considered**:
- `NamedTuple`: Rejected—immutable, harder to update in-place
- Plain `dict`: Rejected—no type safety, less readable
- `Pydantic` model: Rejected—external dependency, overkill for Phase I

### 2. In-Memory Storage Approach

**Decision**: Dictionary (`dict[int, Task]`) with integer keys

**Rationale**:
- O(1) lookup, insertion, deletion by ID
- Natural fit for ID-keyed access pattern (all operations use ID)
- Separate `_next_id` counter for sequential ID generation

**Structure**:
```python
_tasks: dict[int, Task] = {}
_next_id: int = 1
```

**Alternatives Considered**:
- `list[Task]`: Rejected—O(n) lookup by ID, deletion leaves gaps or requires reindexing
- `OrderedDict`: Rejected—dict maintains insertion order since Python 3.7, no added benefit

### 3. CLI Interaction Style

**Decision**: Menu-driven interface with numbered options

**Rationale**:
- Matches FR-010 requirement ("menu-driven interface")
- Lower cognitive load for users—no command syntax to memorize
- Clear discoverability of available operations
- Easy validation (numeric input only for menu selection)

**Menu Structure**:
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

**Alternatives Considered**:
- Command-based (e.g., `add`, `list`, `done 3`): Rejected—requires learning syntax, more error-prone input parsing
- REPL with natural language: Rejected—out of scope for Phase I (no AI/NLP per NFR-004)

### 4. Error Handling Strategy

**Decision**: Validate at boundaries, return clear messages

**Rationale**:
- Input validation happens in CLI layer before reaching service
- Service layer returns status/message tuples or raises domain-specific exceptions
- All error messages match spec requirements (e.g., "Task not found with ID X")

**Error Categories**:
| Category | Example | Response |
|----------|---------|----------|
| Invalid ID format | "abc" or "-5" | "Invalid ID. Please enter a numeric value." or "ID must be a positive number." |
| Task not found | ID 999 | "Task not found with ID 999." |
| Empty title | "" or "   " | "Title cannot be empty." |
| Title too long | >200 chars | Truncate to 200 chars with warning |
| Description too long | >1000 chars | Truncate to 1000 chars with warning |

**Alternatives Considered**:
- Silent truncation: Rejected—user should be informed
- Rejecting oversized input: Rejected—spec says truncate with warning

### 5. ID Generation Strategy

**Decision**: Sequential integer starting at 1, never reused

**Rationale**:
- Simple, predictable, matches user expectations
- Counter increments on each add, regardless of deletions
- Avoids "ID reuse" bugs where deleted IDs could reference new tasks

**Implementation**:
```python
def _generate_id(self) -> int:
    id = self._next_id
    self._next_id += 1
    return id
```

**Alternatives Considered**:
- UUID: Rejected—harder to type in console, overkill for in-memory use
- Reuse deleted IDs: Rejected—potential for user confusion and bugs

## Dependencies

None beyond Python 3.13+ standard library.

## Performance Considerations

- All operations O(1) except "View All" which is O(n)
- Memory usage linear with task count
- No persistence overhead

## Security Considerations

- N/A for Phase I (single-user, local, no network, no storage)

## Follow-up Items

None. All research items resolved; ready for Phase 1 design.
