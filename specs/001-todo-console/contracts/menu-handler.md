# Function Contract: Menu Handler

**Function**: `menu_handler(tasks: list[dict]) -> None`
**Purpose**: Display menu, get user input, route to appropriate function
**Spec Reference**: FR-001, FR-002

## Inputs

```python
tasks: list[dict]  # Global task collection
```

## Outputs

Returns None (modifies tasks in-place through called functions)

## Behavior

### Display Loop

1. Clear screen (optional, platform-dependent)
2. Display menu options:

```
=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice:
```

3. Get user input: `choice = input("Enter choice: ").strip()`

4. Validate input is numeric: Use try-except with int() conversion

5. Route to function based on choice:
   - 0: Exit loop (return)
   - 1: call `add_task(tasks)`
   - 2: call `view_tasks(tasks)`
   - 3: call `toggle_task(tasks)`
   - 4: call `update_task(tasks)`
   - 5: call `delete_task(tasks)`
   - Other: Display "Invalid choice. Please enter 0-5."

6. Loop back to step 1

## Error Handling

| Error | Condition | Response |
|-------|-----------|----------|
| Invalid choice | Non-numeric or not 0-5 | Display "Invalid choice. Please enter 0-5." |
| Unexpected | Any exception in called functions | Display "An error occurred." and continue loop |

## Side Effects

- Calls functions that modify `tasks` list
- No return value (all operations in-place)

## Notes

- Infinite loop until user selects 0
- Routes to appropriate function based on user choice
- All functions receive `tasks` as parameter
- No modifications to tasks in menu handler itself
