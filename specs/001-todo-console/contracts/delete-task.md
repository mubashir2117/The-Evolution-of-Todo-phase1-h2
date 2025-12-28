# Function Contract: Delete Task

**Function**: `delete_task(tasks: list[dict]) -> None`
**Purpose**: Remove task from collection by ID
**Spec Reference**: FR-012, FR-013

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## User Input Prompts

1. `task_id = input("Enter task ID to delete: ").strip()`

## Outputs

Returns None (removes task from `tasks` list)

## Behavior

### Validation Steps

1. Validate task ID is numeric:
   - Use try-except with `int(task_id)`
   - If not numeric: Display "Please enter a valid number." and return

2. Find task by ID:
   - `task_index = next((i for i, t in enumerate(tasks) if t['id'] == task_id), None)`
   - If not found (None): Display "Task not found." and return

3. Remove task from list:
   - `deleted_task = tasks.pop(task_index)`

4. Display confirmation: `f"Task '{deleted_task['title']}' deleted."`

## Error Handling

| Error | Condition | Response |
|-------|-----------|----------|
| Invalid ID | Non-numeric input | Display "Please enter a valid number." |
| Task not found | ID not in tasks list | Display "Task not found." |

## Side Effects

- Removes task from `tasks` list
- Remaining tasks shift to fill gap (no renumbering)
- No return value (in-place modification)

## Examples

### Successful Delete
```python
tasks = [
    {'id': 1, 'title': 'Task 1', ...},
    {'id': 2, 'title': 'Task 2', ...},
    {'id': 3, 'title': 'Task 3', ...}
]
Input:  task_id="2"
Output: Task 'Task 2' deleted.
Result: tasks = [
    {'id': 1, 'title': 'Task 1', ...},
    {'id': 3, 'title': 'Task 3', ...}
]
```

### Invalid ID
```python
Input:  task_id="abc"
Output: Please enter a valid number.
Result: No changes
```

### Task Not Found
```python
Input:  task_id="999"
Output: Task not found.
Result: No changes
```

## Notes

- Task IDs are NOT renumbered after deletion
- Remaining tasks keep their original IDs
- List order is preserved (removed item's gap closed)
- Deleted task title used in confirmation message
- No confirmation prompt (immediate deletion)
