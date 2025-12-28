# Research: Todo Console App

**Feature**: 001-todo-console
**Date**: 2025-12-29
**Purpose**: Document technology decisions and best practices for implementing the Todo Console App

## Technology Stack Decisions

### Python 3.13+ with Standard Library

**Decision**: Use Python 3.13 or higher with only standard library modules

**Rationale**:
- Constitution principle II (Simplicity) prohibits external dependencies
- Python's standard library provides all necessary functionality:
  - `input()` and `print()` for console I/O
  - `list` and `dict` for in-memory task storage
  - String methods for validation and formatting
  - `str.format()` for table-like output formatting
- Reduces complexity and eliminates dependency management overhead
- Ensures broad platform compatibility

**Alternatives Considered**:

| Option | Status | Reason |
|--------|--------|--------|
| Python + rich (terminal formatting) | Rejected | Violates principle II (external dependency) |
| Python + click (CLI framework) | Rejected | Violates principle II (external dependency) |
| JavaScript (Node.js) | Rejected | Not specified in user requirements |
| Ruby | Rejected | Not specified in user requirements |

---

### In-Memory Storage: list[dict]

**Decision**: Store tasks in a global list of dictionaries

**Rationale**:
- Constitution principle VI (In-Memory Storage) mandates list[dict] structure
- Simple and straightforward: `tasks: list[dict] = []`
- Each task as dict with keys: 'id', 'title', 'description', 'completed'
- Volatile storage eliminates file I/O complexity
- Aligns with hackathon Phase I scope (no persistence)

**Alternatives Considered**:

| Option | Status | Reason |
|--------|--------|--------|
| JSON file persistence | Rejected | Violates principle VI (no persistence) |
| SQLite database | Rejected | Violates principle VI (no persistence) |
| Pickle serialization | Rejected | Violates principle VI (no persistence) |

---

### Application Architecture

**Decision**: Single-file (main.py) or minimal two-file structure (main.py + todo.py)

**Rationale**:
- Constitution principle II (Simplicity) favors single-file structure
- Constitution principle III (Modularity) requires separate functions for each operation
- Balance: Main file handles menu loop, optional secondary file separates CRUD operations
- Single-file approach: All functions in main.py for maximum simplicity
- Two-file approach: main.py (menu), todo.py (functions) for better testability

**Alternatives Considered**:

| Option | Status | Reason |
|--------|--------|--------|
| Single monolithic file | Alternative | Good for simplicity, harder to test |
| Two-file (main.py + todo.py) | Alternative | Better modularity and testability |
| Package structure with src/ | Rejected | Over-engineering for console app |

**Recommendation**: Start with single-file (main.py), refactor to two-file if modularity needs increase.

---

### ID Generation Strategy

**Decision**: Generate unique IDs using `max(task['id'] for task in tasks) + 1`

**Rationale**:
- Ensures unique, sequential IDs even after task deletions
- Handles empty list gracefully with default 0
- Simple implementation: `next_id = max([t['id'] for t in tasks], default=0) + 1`
- Alternative `len(tasks) + 1` would cause non-unique IDs if tasks are deleted

**Alternatives Considered**:

| Option | Status | Reason |
|--------|--------|--------|
| len(tasks) + 1 | Rejected | Causes non-unique IDs after deletions |
| UUID (uuid4) | Rejected | Over-engineering for simple app |
| Timestamp-based ID | Rejected | Complex and unnecessary |

---

### Console Interface Design

**Decision**: Numbered text menu with input() for user interaction

**Rationale**:
- Constitution principle IV (User-Friendly) requires clear text menus
- Standard CLI pattern that users understand immediately
- Menu options: 1) Add Task, 2) View Tasks, 3) Toggle Complete, 4) Update Task, 5) Delete Task, 0) Exit
- input() for all user input: strings (titles, descriptions), integers (menu choices, task IDs)
- print() for all output: menu, task lists, error messages

**Alternatives Considered**:

| Option | Status | Reason |
|--------|--------|--------|
| Argument-based CLI (--add, --list) | Rejected | Less interactive for iterative use |
| Graphical UI (Tkinter) | Rejected | Violates principle II (no dependencies) |
| Web interface | Rejected | Violates principle II and scope |

---

### Error Handling Strategy

**Decision**: Graceful error handling with try-except blocks and validation

**Rationale**:
- Constitution principle IV requires "no crashes" for any edge case
- Validate user input before processing (empty titles, non-numeric IDs)
- Use try-except for unexpected errors
- Provide clear, user-friendly error messages explaining what went wrong

**Error Types to Handle**:

1. Empty title input: Display "Title is required."
2. Title > 200 characters: Display "Title too long (max 200 characters)."
3. Invalid task ID: Display "Task not found."
4. Non-numeric ID input: Display "Please enter a valid number."
5. Empty task list: Display "No tasks yet."

---

### Output Formatting

**Decision**: Use str.format() for table-like display of tasks

**Rationale**:
- Python stdlib provides str.format() for string formatting
- Create columns: ID, Title, Description, Status
- Visual indicators: [✓] for completed, [ ] for incomplete
- Handle long text by allowing wrapping (not truncating)
- Clear, readable format for users to scan tasks

**Example Format**:
```
ID  Title                   Description         Status
--- ---------------------- -------------------- ------
1   Complete assignment      Due tomorrow         [✓]
2   Buy groceries                                [ ]
```

---

## Best Practices Summary

1. **Modularity**: Each operation (add, view, update, delete, toggle) as separate function
2. **Type Hints**: Use for all function signatures (e.g., `def add_task(tasks: list[dict]) -> None`)
3. **PEP 8 Compliance**: Follow Python style guidelines throughout
4. **Comments**: Link to spec.md sections for traceability
5. **Error Handling**: Validate all inputs, catch exceptions, provide friendly messages
6. **Simplicity**: Avoid over-engineering, use straightforward solutions

---

## Unresolved Questions

**None** - All technical decisions have been resolved based on constitutional principles and requirements.
