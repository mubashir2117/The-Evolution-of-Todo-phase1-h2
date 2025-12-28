# Quickstart: Todo Console App

**Feature**: 001-todo-console
**Purpose**: Quick start guide for running and testing the Todo Console App

## Prerequisites

- Python 3.13 or higher installed
- Command-line terminal access
- No external dependencies required

## Installation

1. Clone or download the repository
2. Navigate to the project root directory:
   ```bash
   cd /path/to/todo-phase1
   ```

3. Verify Python version:
   ```bash
   python --version
   # or
   python3 --version
   ```
   Should show: Python 3.13.x or higher

4. No pip install required - uses only Python standard library

## Running the Application

### Start the App

```bash
python main.py
# or
python3 main.py
```

### Using the App

You'll see the main menu:

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

### Common Operations

#### Add a Task
1. Enter `1` and press Enter
2. Enter task title (required): `Complete assignment`
3. Enter description (optional, press Enter to skip): `Due tomorrow`
4. Confirmation: `Task 'Complete assignment' added with ID 1.`

#### View Tasks
1. Enter `2` and press Enter
2. See all tasks in table format:
   ```
   ID  Title                   Description         Status
   --- ---------------------- -------------------- ------
   1   Complete assignment       Due tomorrow        [ ]
   ```

#### Mark Task as Complete
1. Enter `3` and press Enter
2. Enter task ID: `1`
3. Confirmation: `Task 'Complete assignment' is now completed.`

#### Update a Task
1. Enter `4` and press Enter
2. Enter task ID: `1`
3. Enter new title (or press Enter to keep): `Updated title`
4. Enter new description (or press Enter to keep): `New description`
5. Confirmation: `Task 1 updated.`

#### Delete a Task
1. Enter `5` and press Enter
2. Enter task ID: `1`
3. Confirmation: `Task 'Updated title' deleted.`

#### Exit
1. Enter `0` and press Enter
2. Application closes (all tasks lost)

## Example Session

```bash
$ python main.py

=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice: 1
Enter task title: Buy groceries
Enter description (optional, press Enter to skip): Milk, bread, eggs

Task 'Buy groceries' added with ID 1.

=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice: 2

ID  Title          Description         Status
--- -------------- -------------------- ------
1   Buy groceries  Milk, bread, eggs    [ ]

=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice: 3
Enter task ID to toggle: 1

Task 'Buy groceries' is now completed.

=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice: 2

ID  Title          Description         Status
--- -------------- -------------------- ------
1   Buy groceries  Milk, bread, eggs   [✓]

=== Todo Console App ====
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
0. Exit

Enter choice: 0
```

## Error Handling Examples

### Empty Title
```
Enter choice: 1
Enter task title: [press Enter without typing]
Title is required.
```

### Title Too Long
```
Enter choice: 1
Enter task title: [paste 201+ characters]
Title too long (max 200 characters).
```

### Invalid Task ID
```
Enter choice: 3
Enter task ID to toggle: abc
Please enter a valid number.
```

### Task Not Found
```
Enter choice: 3
Enter task ID to toggle: 999
Task not found.
```

### Empty Task List
```
Enter choice: 2
No tasks yet.
```

## Important Notes

- **Data Volatility**: All tasks are lost when you exit the application (no persistence)
- **Case Sensitivity**: Task titles are stored exactly as entered
- **ID Behavior**: Task IDs are NOT renumbered after deletion
- **Input Stripping**: Whitespace is stripped from beginning/end of titles and descriptions
- **Special Characters**: Allowed in titles and descriptions

## File Structure

```
main.py              # Main application file
todo.py (optional)   # Modular functions (if implemented separately)
```

## Testing Checklist

- [ ] Launch app successfully
- [ ] Add a task with title only
- [ ] Add a task with title and description
- [ ] View tasks when list is empty
- [ ] View tasks when list has items
- [ ] Toggle task status (not completed → completed)
- [ ] Toggle task status (completed → not completed)
- [ ] Update task title
- [ ] Update task description
- [ ] Update both title and description
- [ ] Delete a task
- [ ] Exit application
- [ ] Try all error scenarios (empty title, invalid ID, etc.)
