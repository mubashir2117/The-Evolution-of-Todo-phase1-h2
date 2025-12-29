# The Evolution of Todo - Hackathon2 Phase 1

A console-based todo application with in-memory storage for basic task management. This is Phase 1 of a planned evolution series, focusing on core CRUD operations through a simple command-line interface.

## Features

- **Add Task**: Create new tasks with unique auto-generated IDs
- **View Tasks**: Display all tasks in a formatted table with status indicators
- **Toggle Complete**: Mark tasks as complete or incomplete
- **Update Task**: Modify task titles and descriptions
- **Delete Task**: Remove tasks from the list

## Installation

### Requirements
- Python 3.9 or higher


2. No additional dependencies required - uses Python standard library only

## Usage

### Running the Application
```bash
python main.py
```

### Menu Options
```
=== Todo Console App ===
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit
```

### Example Workflow
```
$ python main.py

=== Todo Console App ===
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit

Enter choice: 1
Enter task title: Learn Python
Enter description (optional, press Enter to skip): Master the basics
Task 'Learn Python' added with ID 1.

Enter choice: 2

ID  Title                   Description         Status
--- ---------------------- -------------------- ------
1   Learn Python            Master the basics    [ ]

Enter choice: 3
Enter task ID to toggle: 1
Task 1 marked as completed.

Enter choice: 6
Goodbye!
```

## Testing

Run the test suite to verify functionality:

```bash
# Run all tests
python -m pytest test_main.py test_mvp.py -v

# Run specific test file
python test_main.py
python test_mvp.py
```

## Task Data Model

Each task contains:
- **ID**: Unique integer identifier (auto-generated)
- **Title**: Required string (1-200 characters)
- **Description**: Optional string (no length limit)
- **Completed**: Boolean status (defaults to False)

## Spec-Driven Development

This project follows Spec-Driven Development (SDD) methodology:

- **Specification**: `specs/001-todo-console/spec.md` - Feature requirements
- **Plan**: `specs/001-todo-console/plan.md` - Architecture decisions
- **Tasks**: `specs/001-todo-console/tasks.md` - Implementation tasks with test cases
- **Contracts**: Detailed API contracts for each operation

## Current Status

**Phase 1**: Console-based MVP with in-memory storage - COMPLETE

**Future Phases**: Planned evolution to include:
- Persistent storage (file/database)
- Enhanced UI options (GUI, web)
- Multi-user support
- Advanced task management features

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! This is an evolving project designed to demonstrate progressive feature development and architectural decisions.

---

**Branch**: `001-todo-console` | **Status**: Phase 1 Complete
