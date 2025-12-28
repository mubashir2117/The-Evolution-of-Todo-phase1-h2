# Function Contract: Add Task

**Function**: `add_task(tasks: list[dict]) -> None`
**Purpose**: Create new task with user-provided title and optional description
**Spec Reference**: FR-003, FR-004, FR-005, FR-006, FR-014

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## User Input Prompts

1. `title = input("Enter task title: ").strip()`
2. `description = input("Enter description (optional, press Enter to skip): ").strip()` or `None`

## Outputs

Returns None (appends new task to `tasks` list)

## Behavior

### Validation Steps

1. Validate title is not empty after stripping whitespace
   - If empty: Display "Title is required." and return

2. Validate title length (1-200 characters after stripping)
   - If > 200: Display "Title too long (max 200 characters)." and return

3. Generate unique ID: `new_id = max([task['id'] for task in tasks], 0) + 1`
   - Handles empty list (returns 0 + 1 = 1)

4. Create task dict:
   ```python
   new_task = {
       'id': new_id,
       'title': title,
       'description': description if description else None,
       'completed': False
   }
   ```

5. Append to tasks: `tasks.append(new_task)`

6. Display confirmation: `f"Task '{title}' added with ID {new_id}."`

## Error Handling

| Error | Condition | Response |
|-------|-----------|----------|
| Empty title | Title is empty or whitespace-only after stripping | Display "Title is required." |
| Title too long | Title > 200 characters | Display "Title too long (max 200 characters)." |

## Side Effects

- Appends new task to `tasks` list
- Modifies `tasks` in-place (no return value)

## Examples

### Success
```python
Input:  title="Complete assignment", description=""
Output: Task 'Complete assignment' added with ID 1.
Result: tasks = [{'id': 1, 'title': 'Complete assignment', 'description': None, 'completed': False}]
```

### Empty Title
```python
Input:  title="   ", description=None
Output: Title is required.
Result: tasks unchanged
```

### Title Too Long
```python
Input:  title="a" * 201, description=None
Output: Title too long (max 200 characters).
Result: tasks unchanged
```

## Notes

- Description is optional: empty input stored as None
- Title whitespace stripped before validation
- ID generation ensures uniqueness even after deletions
- Task always created with completed=False
