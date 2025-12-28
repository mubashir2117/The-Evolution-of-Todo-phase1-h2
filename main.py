#!/usr/bin/env python3
# FR-003: System MUST create tasks with a unique identifier
# FR-004: System MUST store tasks with id, title, description, completed
# FR-016: System MUST NOT persist tasks to disk (in-memory only)

# Global task storage - see FR-003, FR-004, FR-016
# Type: list[dict] where each dict has: 'id' (int), 'title' (str), 'description' (str|None), 'completed' (bool)
tasks: list[dict] = []

# T004: Implement _generate_next_id helper function
# Uses max() + 1 strategy for unique IDs even after deletions (see plan.md ID Generation Algorithm)
def _generate_next_id(tasks_list: list[dict]) -> int:
    """Generate next unique task ID.

    Rationale: Using max() + 1 ensures unique IDs even after deletions.
    Alternative len() + 1 would cause non-unique IDs if tasks are deleted.
    """
    return max((task['id'] for task in tasks_list), default=0) + 1

# T003: Menu handler skeleton - displays menu and gets user input
# See contracts/menu-handler.md for full specification
def _display_menu() -> None:
    """Display the main menu options."""
    print("\n=== Todo Console App ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Toggle Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def _get_menu_choice() -> int | None:
    """Get and validate user's menu choice.

    Returns:
        int: Valid menu choice (0-5)
        None: Invalid input (should display error)
    """
    try:
        choice_str = input("\nEnter choice: ").strip()
        choice = int(choice_str)
        return choice
    except ValueError:
        return None

# T006: Integrate add_task into menu handler (when user selects option 1)
# This will be completed in T017 with full main() function

# T007: Implement view_tasks function
# FR-007: System MUST display task lists in table-like format
# FR-008: System MUST indicate completion status using [✓]/[ ]
# FR-009: System MUST display "No tasks yet." when list is empty
# See contracts/view-tasks.md for full specification
def view_tasks(tasks_list: list[dict]) -> None:
    """Display all tasks in table-like format with status indicators.

    Args:
        tasks_list: Global task collection (read-only)

    Side Effects:
        - Prints formatted table to console
        - No modifications to tasks_list
    """
    # FR-009: Display "No tasks yet." when list is empty
    if len(tasks_list) == 0:
        print("\nNo tasks yet.")
        return

    # Print table header (FR-007)
    print("\nID  Title                   Description         Status")
    print("--- ---------------------- -------------------- ------")

    # Display each task with status icon (FR-008)
    for task in tasks_list:
        # FR-008: [✓] for completed, [ ] for incomplete
        icon = "[✓]" if task['completed'] else "[ ]"
        # Format description (may be None)
        desc = task['description'] if task['description'] else ""

        # Format row with fixed-width columns
        print(f"{task['id']: <4} {task['title']: <22} {desc: <20} {icon}")

# T005: Implement add_task function
# FR-003: System MUST create tasks with a unique identifier
# FR-004: System MUST store tasks with id (int), title (str), description (str|None), completed (bool)
# FR-005: System MUST validate that task titles are between 1 and 200 characters
# FR-006: System MUST reject task creation if title is empty
# FR-014: System MUST strip leading and trailing whitespace from user input
# See contracts/add-task.md for full specification
def add_task(tasks_list: list[dict]) -> None:
    """Create new task with user-provided title and optional description.

    Args:
        tasks_list: Global task collection (modified in-place)

    Side Effects:
        - Appends new task to tasks_list
        - Displays confirmation or error messages
    """
    # Get user input
    # FR-014: Strip leading and trailing whitespace
    title = input("Enter task title: ").strip()
    description_input = input("Enter description (optional, press Enter to skip): ").strip()

    # Validate title is not empty (FR-006)
    if not title:
        print("Title is required.")
        return

    # Validate title length (FR-005)
    if len(title) > 200:
        print("Title too long (max 200 characters).")
        return

    # Generate unique ID using max() + 1 strategy (FR-003)
    new_id = _generate_next_id(tasks_list)

    # Store description as None if empty (optional field)
    description = description_input if description_input else None

    # Create task dict (FR-004)
    new_task = {
        'id': new_id,
        'title': title,
        'description': description,
        'completed': False
    }

    # Append to tasks list (FR-016: in-memory storage only)
    tasks_list.append(new_task)

    # Display confirmation
    print(f"Task '{title}' added with ID {new_id}.")

# Toggle complete implementation
def _find_task_by_id(tasks_list: list[dict], task_id: int) -> dict | None:
    """Find a task by its ID.

    Args:
        tasks_list: Global task collection (read-only)
        task_id: The task ID to search for

    Returns:
        The task dict if found, None otherwise
    """
    for task in tasks_list:
        if task['id'] == task_id:
            return task
    return None

def toggle_complete(tasks_list: list[dict]) -> None:
    """Toggle the completion status of a task.

    Args:
        tasks_list: Global task collection (modified in-place)

    Side Effects:
        - Updates the 'completed' status of the specified task
        - Displays confirmation or error messages
    """
    # Get user input for task ID
    task_id_input = input("Enter task ID to toggle: ").strip()

    # Validate input is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    # Find the task
    task = _find_task_by_id(tasks_list, task_id)
    if not task:
        print(f"Task {task_id} not found.")
        return

    # Toggle completion status
    task['completed'] = not task['completed']
    status = "completed" if task['completed'] else "incomplete"
    print(f"Task {task_id} marked as {status}.")

def update_task(tasks_list: list[dict]) -> None:
    """Update a task's title and/or description.

    Args:
        tasks_list: Global task collection (modified in-place)

    Side Effects:
        - Updates the 'title' and/or 'description' of the specified task
        - Displays confirmation or error messages
    """
    # Get user input for task ID
    task_id_input = input("Enter task ID to update: ").strip()

    # Validate input is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    # Find the task
    task = _find_task_by_id(tasks_list, task_id)
    if not task:
        print(f"Task {task_id} not found.")
        return

    # Display current task
    print(f"\nCurrent task: {task['title']}")
    if task['description']:
        print(f"Description: {task['description']}")

    # Get new title (optional)
    new_title = input("Enter new title (press Enter to keep current): ").strip()
    if new_title:
        # Validate title length
        if len(new_title) > 200:
            print("Title too long (max 200 characters). Update cancelled.")
            return
        task['title'] = new_title

    # Get new description (optional)
    new_desc = input("Enter new description (press Enter to keep current): ").strip()
    if new_desc:
        task['description'] = new_desc
    elif new_desc == "" and input("Clear description? (y/n): ").strip().lower() == 'y':
        task['description'] = None

    print(f"Task {task_id} updated.")

def delete_task(tasks_list: list[dict]) -> None:
    """Delete a task from the list.

    Args:
        tasks_list: Global task collection (modified in-place)

    Side Effects:
        - Removes the specified task from tasks_list
        - Displays confirmation or error messages
    """
    # Get user input for task ID
    task_id_input = input("Enter task ID to delete: ").strip()

    # Validate input is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    # Find the task index
    for i, task in enumerate(tasks_list):
        if task['id'] == task_id:
            # Confirm deletion
            confirm = input(f"Delete task '{task['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                del tasks_list[i]
                print(f"Task {task_id} deleted.")
            else:
                print("Deletion cancelled.")
            return

    # Task not found
    print(f"Task {task_id} not found.")

# T017: Add main() function with while True loop, menu display, choice routing, and exit on 0
# FR-001: System MUST provide numbered menu with options 1-5 + 0 exit
# FR-002: System MUST display menu continuously in a loop until user selects option 0
# FR-015: System MUST display user-friendly error messages (no crashes)
# T016: Input validation for menu choice (numeric 0-5) with "Invalid choice." error message
def main() -> None:
    """Main application loop with menu display and routing.

    Side Effects:
        - Displays menu and processes user input
        - Calls appropriate functions based on user choice
        - Exits when user selects option 0
    """
    while True:
        # Display menu (T003)
        _display_menu()

        # Get and validate menu choice (T003, T016)
        choice = _get_menu_choice()

        # T015: Graceful error handling - ensure no crashes (FR-015)
        if choice is None:
            print("Invalid choice. Please enter 1-6.")
            continue

        # Route to appropriate function based on user choice
        if choice == 1:
            # T006: Add task (User Story 1)
            add_task(tasks)
        elif choice == 2:
            # T008: View tasks (User Story 2)
            view_tasks(tasks)
        elif choice == 3:
            # Toggle complete (User Story 3)
            toggle_complete(tasks)
        elif choice == 4:
            # Update task (User Story 4)
            update_task(tasks)
        elif choice == 5:
            # Delete task (User Story 5)
            delete_task(tasks)
        elif choice == 6:
            # Exit the application (FR-002)
            print("Goodbye!")
            break
        else:
            # T016: Invalid choice (not 1-6)
            print("Invalid choice. Please enter 1-6.")

# T019: Add comments linking to spec.md sections (FR numbers) - done throughout file

# Entry point - call main() when script is executed directly
if __name__ == "__main__":
    main()
