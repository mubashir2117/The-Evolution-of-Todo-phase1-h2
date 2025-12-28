# Function Contract: View Tasks

**Function**: `view_tasks(tasks: list[dict]) -> None`
**Purpose**: Display all tasks in table-like format with ID, title, description, and status
**Spec Reference**: FR-007, FR-008, FR-009

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## Outputs

Returns None (prints to console)

## Behavior

### Empty List Check

1. If `len(tasks) == 0`:
   - Display "No tasks yet."
   - Return

### Format and Display

2. Print table header:
   ```
   ID  Title                   Description         Status
   --- ---------------------- -------------------- ------
   ```

3. For each task in `tasks`:
   - Determine status icon:
     - `icon = "[✓]" if task['completed'] else "[ ]"`
   - Format description:
     - `desc = task['description'] if task['description'] else ""`
   - Print row using `str.format()`:
     ```python
     print(f"{task['id']: <4} {task['title']: <22} {desc: <20} {icon}")
     ```

### Column Widths

- ID: 4 characters (right-aligned or left-aligned)
- Title: 22 characters (left-aligned, truncated if needed)
- Description: 20 characters (left-aligned, truncated if needed)
- Status: 6 characters (icon width)

## Error Handling

None (read-only operation, no errors possible)

## Side Effects

- No modifications to `tasks` list
- Pure display function

## Examples

### Empty List
```python
tasks = []
Output:
No tasks yet.
```

### Single Task
```python
tasks = [{'id': 1, 'title': 'Complete assignment', 'description': None, 'completed': False}]
Output:
ID  Title                   Description         Status
--- ---------------------- -------------------- ------
1   Complete assignment                         [ ]
```

### Multiple Tasks
```python
tasks = [
    {'id': 1, 'title': 'Complete assignment', 'description': 'Due tomorrow', 'completed': True},
    {'id': 2, 'title': 'Buy groceries', 'description': None, 'completed': False}
]
Output:
ID  Title                   Description         Status
--- ---------------------- -------------------- ------
1   Complete assignment       Due tomorrow        [✓]
2   Buy groceries                                [ ]
```

## Notes

- Empty list displays message, not error
- Status icons: [✓] for completed, [ ] for incomplete
- Description may be None, displayed as empty string
- Table format uses fixed-width columns with left alignment
- Long titles/descriptions may be truncated to fit column width
