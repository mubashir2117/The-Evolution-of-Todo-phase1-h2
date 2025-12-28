# Function Contract: Toggle Task

**Function**: `toggle_task(tasks: list[dict]) -> None`
**Purpose**: Flip task completion status (True ↔ False)
**Spec Reference**: FR-010, FR-013

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## User Input Prompts

1. `task_id = input("Enter task ID to toggle: ").strip()`

## Outputs

Returns None (modifies task in-place)

## Behavior

### Validation Steps

1. Validate task ID is numeric:
   - Use try-except with `int(task_id)`
   - If not numeric: Display "Please enter a valid number." and return

2. Find task by ID:
   - `task = next((t for t in tasks if t['id'] == task_id), None)`
   - If not found: Display "Task not found." and return

3. Toggle completion status:
   - `task['completed'] = not task['completed']`

4. Determine status text:
   - `status = "completed" if task['completed'] else "not completed"`

5. Display confirmation: `f"Task '{task['title']}' is now {status}."`

## Error Handling

| Error | Condition | Response |
|-------|-----------|----------|
| Invalid ID | Non-numeric input | Display "Please enter a valid number." |
| Task not found | ID not in tasks list | Display "Task not found." |

## Side Effects

- Modifies task['completed'] in `tasks` list
- No other task attributes changed
- No return value (in-place modification)

## Examples

### Toggle to Completed
```python
tasks = [{'id': 1, 'title': 'Task 1', 'completed': False}]
Input:  task_id="1"
Output: Task 'Task 1' is now completed.
Result: tasks[0]['completed'] = True
```

### Toggle to Not Completed
```python
tasks = [{'id': 1, 'title': 'Task 1', 'completed': True}]
Input:  task_id="1"
Output: Task 'Task 1' is now not completed.
Result: tasks[0]['completed'] = False
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

- Uses `not` operator to flip boolean (True → False, False → True)
- Confirmation message shows new status in plain text
- Task title shown in confirmation for clarity
- No confirmation prompt (immediate toggle)
- Can toggle same task multiple times (flip back and forth)
