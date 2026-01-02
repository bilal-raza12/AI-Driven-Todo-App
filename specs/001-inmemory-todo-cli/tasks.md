# Tasks: In-Memory Python Todo Console App

**Input**: Design documents from `/specs/001-inmemory-todo-cli/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: Not included. Per spec: "Manual console validation" strategy for Phase I.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root (per plan.md)

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure and package files

- [ ] T001 Create directory structure: `src/`, `src/models/`, `src/services/`, `src/cli/`, `src/lib/`
- [ ] T002 [P] Create package marker `src/__init__.py` with empty content
- [ ] T003 [P] Create package marker `src/models/__init__.py` with Task import
- [ ] T004 [P] Create package marker `src/services/__init__.py` with TaskService import
- [ ] T005 [P] Create package marker `src/cli/__init__.py` with module exports
- [ ] T006 [P] Create package marker `src/lib/__init__.py` with validator exports

---

## Phase 2: Foundational (Core Infrastructure)

**Purpose**: Shared components that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Create Task dataclass in `src/models/task.py` with fields: id, title, description, is_complete
- [ ] T008 Create input validators in `src/lib/validators.py`: validate_id, validate_title, validate_description
- [ ] T009 Create TaskService class skeleton in `src/services/task_service.py` with storage dict and ID counter
- [ ] T010 Create menu display function in `src/cli/menu.py` with 7 options per spec
- [ ] T011 Create main entry point in `src/main.py` with main loop and menu routing

**Checkpoint**: Foundation ready - user story implementation can begin

---

## Phase 3: User Story 1 - Add a New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add tasks with title and description, receiving a unique sequential ID

**Independent Test**: Run app → select "add task" → enter title/description → verify task appears with ID and "incomplete" status

### Implementation for User Story 1

- [ ] T012 [US1] Implement `add_task(title, description)` method in `src/services/task_service.py`
- [ ] T013 [US1] Implement `handle_add_task()` handler in `src/cli/handlers.py` with input prompts
- [ ] T014 [US1] Wire add task option (menu choice 1) in `src/main.py` to handler
- [ ] T015 [US1] Add title validation in handler: empty/whitespace check with error message
- [ ] T016 [US1] Add title/description truncation with warning messages in handler

**Checkpoint**: User Story 1 complete - can add tasks with validation

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can see all tasks in a formatted list showing ID, title, description, status

**Independent Test**: Add several tasks → select "view tasks" → verify all display with correct format

### Implementation for User Story 2

- [ ] T017 [US2] Implement `get_all_tasks()` method in `src/services/task_service.py`
- [ ] T018 [US2] Implement `handle_view_tasks()` handler in `src/cli/handlers.py` with formatted output
- [ ] T019 [US2] Wire view tasks option (menu choice 2) in `src/main.py` to handler
- [ ] T020 [US2] Add "No tasks found." message when task list is empty

**Checkpoint**: User Stories 1+2 complete - core MVP (add and view tasks)

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status by ID

**Independent Test**: Add task → mark complete → verify status changed → mark incomplete → verify toggle

### Implementation for User Story 3

- [ ] T021 [US3] Implement `mark_complete(task_id)` method in `src/services/task_service.py`
- [ ] T022 [US3] Implement `mark_incomplete(task_id)` method in `src/services/task_service.py`
- [ ] T023 [US3] Implement `get_task(task_id)` helper method in `src/services/task_service.py`
- [ ] T024 [US3] Implement `handle_mark_complete()` handler in `src/cli/handlers.py`
- [ ] T025 [US3] Implement `handle_mark_incomplete()` handler in `src/cli/handlers.py`
- [ ] T026 [US3] Wire mark complete option (menu choice 3) in `src/main.py` to handler
- [ ] T027 [US3] Wire mark incomplete option (menu choice 4) in `src/main.py` to handler
- [ ] T028 [US3] Add ID validation and "Task not found" error handling in handlers

**Checkpoint**: User Stories 1-3 complete - add, view, and toggle completion

---

## Phase 6: User Story 4 - Update Task (Priority: P3)

**Goal**: Users can update task title and/or description by ID

**Independent Test**: Add task → update title/description → verify changes persisted

### Implementation for User Story 4

- [ ] T029 [US4] Implement `update_task(task_id, title, description)` method in `src/services/task_service.py`
- [ ] T030 [US4] Implement `handle_update_task()` handler in `src/cli/handlers.py` with current value display
- [ ] T031 [US4] Wire update task option (menu choice 5) in `src/main.py` to handler
- [ ] T032 [US4] Add "keep current" behavior when user presses Enter without input
- [ ] T033 [US4] Add title validation and "Task not found" error handling

**Checkpoint**: User Stories 1-4 complete - full CRUD except delete

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can remove tasks by ID

**Independent Test**: Add task → delete by ID → verify task no longer in list

### Implementation for User Story 5

- [ ] T034 [US5] Implement `delete_task(task_id)` method in `src/services/task_service.py`
- [ ] T035 [US5] Implement `handle_delete_task()` handler in `src/cli/handlers.py`
- [ ] T036 [US5] Wire delete task option (menu choice 6) in `src/main.py` to handler
- [ ] T037 [US5] Add ID validation and "Task not found" error handling

**Checkpoint**: User Stories 1-5 complete - full CRUD operations

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, edge cases, and exit handling

- [ ] T038 Implement exit handler (menu choice 7) in `src/main.py` with "Goodbye!" message
- [ ] T039 Add invalid menu choice handling with "Invalid choice" error message
- [ ] T040 Add edge case: negative ID handling with "ID must be a positive number" message
- [ ] T041 Add edge case: non-numeric ID handling with "Invalid ID. Please enter a numeric value" message
- [ ] T042 Run manual validation per quickstart.md scenarios
- [ ] T043 Verify 80-column terminal formatting for all output

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - start immediately
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all user stories
- **User Stories (Phases 3-7)**: Depend on Foundational completion
  - US1 + US2 are P1 (MVP) - complete first
  - US3 is P2 - can start after US1+US2
  - US4 + US5 are P3 - can start after US3
- **Polish (Phase 8)**: Depends on all user stories

### User Story Dependencies

| Story | Priority | Depends On | Can Parallel With |
|-------|----------|------------|-------------------|
| US1 (Add) | P1 | Foundational | US2 |
| US2 (View) | P1 | Foundational | US1 |
| US3 (Complete) | P2 | Foundational | - |
| US4 (Update) | P3 | Foundational | US5 |
| US5 (Delete) | P3 | Foundational | US4 |

### Within Each User Story

1. Service methods first
2. CLI handlers second
3. Wire to main.py third
4. Validation/error handling last

### Parallel Opportunities

**Phase 1 (Setup)**:
```
T002, T003, T004, T005, T006 - all package __init__.py files
```

**Phase 2 (Foundational)**:
```
T007 (Task model), T008 (validators) - different files
```

**After Foundational**:
```
US1 and US2 can proceed in parallel (different handlers)
US4 and US5 can proceed in parallel (different handlers)
```

---

## Parallel Example: Setup Phase

```bash
# Launch all package markers together:
Task: "Create package marker src/__init__.py"
Task: "Create package marker src/models/__init__.py"
Task: "Create package marker src/services/__init__.py"
Task: "Create package marker src/cli/__init__.py"
Task: "Create package marker src/lib/__init__.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Run app, add tasks, view list
6. MVP ready for demo

### Incremental Delivery

1. Setup + Foundational → Framework ready
2. US1 + US2 → MVP (add and view)
3. US3 → Progress tracking (complete/incomplete)
4. US4 + US5 → Full CRUD
5. Polish → Production ready

---

## Summary

| Metric | Count |
|--------|-------|
| Total Tasks | 43 |
| Phase 1 (Setup) | 6 |
| Phase 2 (Foundational) | 5 |
| User Story 1 (Add) | 5 |
| User Story 2 (View) | 4 |
| User Story 3 (Complete) | 8 |
| User Story 4 (Update) | 5 |
| User Story 5 (Delete) | 4 |
| Phase 8 (Polish) | 6 |
| Parallel Opportunities | 8 tasks marked [P] |

---

## Notes

- No automated tests per spec ("Manual console validation")
- All file paths relative to repository root
- Python 3.13+ required (standard library only)
- Commit after each task or logical group
- Validate each story independently before proceeding
