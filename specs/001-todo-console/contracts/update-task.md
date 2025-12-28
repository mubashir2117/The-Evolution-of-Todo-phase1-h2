# Function Contract: Update Task

**Function**: `update_task(tasks: list[dict]) -> None`
**Purpose**: Update task title and/or description by ID
**Spec Reference**: FR-011, FR-013, FR-014

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## User Input Prompts

1. `task_id = input("Enter task ID: ").strip()`
2. `new_title = input("Enter new title (press Enter to keep current): ").strip()`
3. `new_description = input("Enter new description (press Enter to keep current): ").strip()`

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

3. Update title if provided (not empty):
   - If `new_title` is not empty:
     - Validate title length (1-200 characters)
     - If > 200: Display "Title too long (max 200 characters)." and return
     - If empty after stripping: Display "Title is required." and return
     - Update: `task['title'] = new_title`

4. Update description if provided:
   - If `new_description` is not empty:
     - Update: `task['description'] = new_description`
   - Else (empty input): Keep existing description unchanged

5. Display confirmation: `f"Task {task_id} updated."`

## Error Handling

| Error | Condition | Response |
|-------|-----------|----------|
| Invalid ID | Non-numeric input | Display "Please enter a valid number." |
| Task not found | ID not in tasks list | Display "Task not found." |
| Empty title | New title is empty/whitespace-only | Display "Title is required." |
| Title too long | New title > 200 characters | Display "Title too long (max 200 characters)." |

## Side Effects

- Modifies task dict in `tasks` list
- Preserves task ID and completed status
- No return value (in-place modification)

## Examples

### Update Title Only
```python
Input:  task_id="1", new_title="Updated title", new_description=""
Output: Task 1 updated.
Result: task[1]['title'] = "Updated title", description unchanged
```

### Update Description Only
```python
Input:  task_id="1", new_title="", new_description="New description"
Output: Task 1 updated.
Result: task[1]['description'] = "New description", title unchanged
```

### Update Both
```python
Input:  task_id="1", new_title="New title", new_description="New desc"
Output: Task 1 updated.
Result: Both title and description updated
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

- Empty input for title/description means "keep current value"
- Whitespace stripped from inputs before validation
- Task ID and completed status are never modified
- Only updates fields that user provides values for
