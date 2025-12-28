# Data Model: Todo Console App

**Feature**: 001-todo-console
**Date**: 2025-12-29
**Purpose**: Define task entity structure and validation rules

## Task Entity

### Description
Represents a todo item with a unique identifier, title, optional description, and completion status.

### Attributes

| Attribute | Type | Required | Constraints | Default |
|-----------|------|----------|-------------|---------|
| id | int | Yes | Unique, auto-generated | N/A (system-assigned) |
| title | str | Yes | 1-200 characters after trimming | N/A (user-provided) |
| description | str | No | No length limit | None (optional) |
| completed | bool | No | True or False | False |

### Python Type Definition

```python
Task = dict[
    'id': int,           # Unique identifier, auto-generated
    'title': str,         # Task title, 1-200 characters
    'description': str,   # Optional description, no limit
    'completed': bool      # Completion status
]
```

### Validation Rules

#### ID Validation
- Must be unique across all tasks
- Must be a positive integer (> 0)
- Generated automatically by system (not user input)
- Strategy: `max([task['id'] for task in tasks], 0) + 1`

#### Title Validation
- Required field (cannot be None or empty after trimming)
- Length: 1-200 characters (after stripping leading/trailing whitespace)
- Whitespace-only input rejected
- Leading/trailing whitespace stripped before validation
- Special characters allowed
- Case-sensitive (preserves user input)

#### Description Validation
- Optional field (can be None or empty string)
- No length limit
- Whitespace-only input accepted as valid empty description
- Leading/trailing whitespace preserved
- Special characters allowed
- Case-sensitive (preserves user input)

#### Completed Validation
- Boolean value (True or False)
- Default: False for new tasks
- Toggled between True/False via operation

### Example Task Instances

```python
# Task 1: Simple task
{
    'id': 1,
    'title': 'Complete assignment',
    'description': None,
    'completed': False
}

# Task 2: Task with description
{
    'id': 2,
    'title': 'Buy groceries',
    'description': 'Milk, bread, eggs, butter',
    'completed': False
}

# Task 3: Completed task
{
    'id': 3,
    'title': 'Call dentist',
    'description': 'Schedule appointment for next week',
    'completed': True
}

# Task 4: Task with long description
{
    'id': 4,
    'title': 'Write documentation',
    'description': 'Document all API endpoints, including request/response formats, error codes, and examples.',
    'completed': False
}
```

## Task Collection

### Description
Global list storing all tasks in memory.

### Type Definition

```python
tasks: list[Task] = []  # Empty list initialized on application start
```

### Invariants

1. **Uniqueness**: No two tasks have the same ID
2. **Order**: Tasks are stored in creation order (first created = first in list)
3. **Volatility**: All tasks lost when application exits (no persistence)

### Operations

#### Add Task
- Validates title (1-200 chars, not empty)
- Generates unique ID using max + 1 strategy
- Creates task dict with default completed=False
- Appends to tasks list

#### View Tasks
- Returns all tasks without modification
- Formats output as table with ID, Title, Description, Status columns
- Displays "No tasks yet." if list empty

#### Update Task
- Validates task ID exists
- Updates title and/or description
- Preserves ID and completed status
- Validates new title if provided (1-200 chars, not empty)

#### Delete Task
- Validates task ID exists
- Removes task from list
- Remaining tasks keep their IDs (no renumbering)

#### Toggle Complete
- Validates task ID exists
- Flips completed flag (True ↔ False)
- Returns confirmation with new status

### State Transitions

```
[New Task]
    ↓ (Add)
[Active] ←completed: False→
    ↓ (Toggle)
[Completed] ←completed: True→
    ↓ (Toggle)
[Active] ←completed: False→
    ↓ (Toggle)
...
    ↓ (Delete)
[Deleted] - removed from collection
```

## Error Scenarios

### Invalid ID Reference
- **Scenario**: User provides task ID that doesn't exist
- **Detection**: Task lookup returns None or raises KeyError
- **Response**: Display "Task not found."

### Empty Title on Add
- **Scenario**: User provides empty string or whitespace-only title
- **Detection**: Title length check after stripping whitespace
- **Response**: Display "Title is required."

### Title Too Long
- **Scenario**: User provides title > 200 characters
- **Detection**: Title length check after stripping whitespace
- **Response**: Display "Title too long (max 200 characters)."

### Non-Numeric ID Input
- **Scenario**: User provides text instead of number for task ID
- **Detection**: ValueError when converting to int
- **Response**: Display "Please enter a valid number."

### Empty Task Collection
- **Scenario**: User views tasks when no tasks exist
- **Detection**: len(tasks) == 0
- **Response**: Display "No tasks yet." (not an error, just informational)

---

## Spec References

- Task entity defined in spec.md: Key Entities section
- Validation rules from spec.md: Functional Requirements FR-004, FR-005, FR-006, FR-013, FR-014
- Task collection structure from spec.md: FR-003, FR-016
- Error handling requirements from spec.md: FR-015
