# Implementation Plan: Todo Console App

**Branch**: `001-todo-console` | **Date**: 2025-12-29 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-console/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a console-based Todo application using Python 3.13+ with in-memory storage. The app provides a menu-driven interface for task management operations (add, view, update, delete, toggle complete). All operations use Python's standard library with no external dependencies. The application follows a simple architecture: main.py contains the menu loop and routes to modular functions in todo.py, with a global list[dict] for task storage. This approach maximizes simplicity and modularity while meeting all constitutional requirements.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory list[dict] structure (volatile, no persistence)
**Testing**: pytest (for unit tests if specified in tasks)
**Target Platform**: Command-line interface (CLI) on any platform with Python 3.13+
**Project Type**: Single console application
**Performance Goals**: Menu operations complete in under 1 second, view operations display 100+ tasks in under 2 seconds
**Constraints**: No external dependencies, no file/database persistence, must handle all errors gracefully without crashing
**Scale/Scope**: Single-user, single-session, up to thousands of tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|--------|
| I. Spec-Driven Only | ✅ PASS | Implementation will be generated from this plan and tasks.md via `/sp.implement` |
| II. Simplicity | ✅ PASS | Using only Python stdlib, single-file or minimal modular structure, straightforward architecture |
| III. Modularity | ✅ PASS | Each operation (Add, View, Update, Delete, Toggle) will be a separate function with clear interfaces |
| IV. User-Friendly | ✅ PASS | Clear text menus, descriptive error messages, graceful error handling, visual status indicators |
| V. Clean Code | ✅ PASS | PEP 8 compliance, type hints on all functions, comments linking to spec.md sections |
| VI. In-Memory Storage | ✅ PASS | Global list[dict] structure, no persistence, volatile data |
| VII. No Extras | ✅ PASS | Only the 5 specified features implemented, no additional functionality |

**Gate Result (Initial)**: ✅ PASS - All constitutional principles satisfied. No violations detected.

**Gate Result (Post-Phase 1 Design)**: ✅ PASS - Design maintains compliance with all constitutional principles. No violations introduced.

---

## Design Verification

### Constitutional Compliance Review

| Principle | Design Compliance | Evidence |
|-----------|-------------------|----------|
| I. Spec-Driven Only | ✅ COMPLIANT | Implementation will be generated from this plan via `/sp.implement` |
| II. Simplicity | ✅ COMPLIANT | Python stdlib only, single-file structure, straightforward algorithms |
| III. Modularity | ✅ COMPLIANT | Separate functions for each operation (add, view, update, delete, toggle) |
| IV. User-Friendly | ✅ COMPLIANT | Clear numbered menu, descriptive error messages, status icons |
| V. Clean Code | ✅ COMPLIANT | Type hints in contracts, PEP 8 specified, comment references planned |
| VI. In-Memory Storage | ✅ COMPLIANT | Global list[dict] structure, no persistence |
| VII. No Extras | ✅ COMPLIANT | Only 5 specified features implemented |

### Technical Decisions Alignment

| Decision | Constitution Principle | Alignment |
|----------|----------------------|------------|
| Python 3.13+ stdlib only | Simplicity, Clean Code | ✅ Uses only stdlib, follows PEP 8 |
| list[dict] storage | In-Memory Storage | ✅ Exactly as mandated |
| Separate functions | Modularity | ✅ Each operation is separate function |
| Menu-driven CLI | User-Friendly | ✅ Clear text menu, intuitive options |
| Input validation | User-Friendly | ✅ Graceful error handling, no crashes |
| Type hints | Clean Code | ✅ Specified in all function contracts |
| No external libs | Simplicity, No Extras | ✅ Only stdlib features used |

### Design Completeness

✅ All technical decisions documented in research.md
✅ Data model fully specified in data-model.md
✅ All function contracts defined in contracts/ directory
✅ Architecture decisions documented with rationale
✅ Quickstart guide provides complete usage instructions
✅ No NEEDS_CLARIFICATION markers remain
✅ Agent context updated with project-specific information

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
└── contracts/           # Phase 1 output (/sp.plan command - CLI function contracts)
```

### Source Code (repository root)

```text
main.py                # Main entry point: menu loop, input handling, routing
todo.py                 # (Optional) Modular functions: add, view, update, delete, toggle
```

**Structure Decision**: Single-file or minimal two-file structure. main.py contains the menu loop, global tasks list, and function routing. todo.py (optional) separates the CRUD operations into individual functions for better modularity. This structure balances simplicity (constitution principle II) with modularity (constitution principle III). The flat structure is appropriate for a console application with no need for deeper directory hierarchies.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | No violations | All constitutional principles satisfied |

---

## Phase 1: Design & Contracts

### Data Model Documentation

See `data-model.md` for complete Task entity specification including:
- Task attributes with types and validation rules
- Task collection invariants and operations
- State transitions and error scenarios
- Example task instances

### Function Contracts

The following function contracts are defined in the `contracts/` directory:

1. **menu-handler.md** - Main menu loop, input routing, error handling
2. **add-task.md** - Create new task with title/description, validate input
3. **view-tasks.md** - Display tasks in table format with status icons
4. **update-task.md** - Update title/description by ID, preserve other fields
5. **delete-task.md** - Remove task from collection by ID
6. **toggle-task.md** - Flip completed status (True ↔ False)

Each contract includes:
- Function signature with type hints
- Input/output specifications
- Step-by-step behavior description
- Error handling scenarios
- Side effects and examples

### Quickstart Guide

See `quickstart.md` for complete usage guide including:
- Installation and prerequisites
- Running the application
- Common operations with examples
- Full example session
- Error handling examples
- Testing checklist

### Architecture Decisions

#### File Structure

**Single-file approach** (recommended for simplicity):
```
main.py
├── tasks: list[dict] = []           # Global task collection
├── add_task(tasks: list[dict])        # Create new task
├── view_tasks(tasks: list[dict])       # Display all tasks
├── update_task(tasks: list[dict])      # Update task by ID
├── delete_task(tasks: list[dict])      # Remove task by ID
├── toggle_task(tasks: list[dict])      # Toggle completion status
└── main()                             # Menu loop and routing
```

**Two-file approach** (alternative for modularity):
```
main.py
├── tasks: list[dict] = []           # Global task collection
└── main()                             # Menu loop and routing

todo.py
├── add_task(tasks: list[dict])        # Create new task
├── view_tasks(tasks: list[dict])       # Display all tasks
├── update_task(tasks: list[dict])      # Update task by ID
├── delete_task(tasks: list[dict])      # Remove task by ID
└── toggle_task(tasks: list[dict])      # Toggle completion status
```

#### Menu Flow

```
Initialize tasks = []
    ↓
[Display Menu]
    ↓
Get User Choice (0-5)
    ↓
┌───┼──────────────────┼───────────────┐
│   │                  │               │
0   1                  2              3-5
│   │                  │               │
│   ↓                  ↓               ↓
Exit              Add Task          View/Update/
Return            ↓                 Delete/Toggle
               ↓
            Validate
            Input
               ↓
          [Create/Modify]
          tasks list
               ↓
            [Back to Menu]
```

#### Data Flow

- **Add Task**: User input → validation → create dict → append to tasks list
- **View Tasks**: Read tasks list → format table → print to console
- **Update Task**: User input → find by ID → validate → update fields → confirm
- **Delete Task**: User input → find by ID → remove from list → confirm
- **Toggle Task**: User input → find by ID → flip completed → confirm

#### ID Generation Algorithm

```python
def _generate_next_id(tasks: list[dict]) -> int:
    """Generate next unique task ID."""
    return max((task['id'] for task in tasks), default=0) + 1
```

**Rationale**: Using max() + 1 ensures unique IDs even after deletions, unlike len() + 1 which would cause collisions.

#### Output Formatting Strategy

Use `str.format()` or f-strings with fixed-width columns:

```python
print(f"{task['id']: <4} {task['title']: <22} {desc: <20} {icon}")
```

Column specifications:
- ID: 4 chars, left-aligned
- Title: 22 chars, left-aligned (may truncate long titles)
- Description: 20 chars, left-aligned (may truncate long descriptions)
- Status: 6 chars (icon: [✓] or [ ])

---

## Phase 0: Research & Decisions

### Research Summary

**Decision**: Use Python 3.13+ with standard library only

**Rationale**:
- Constitution principle II mandates no external dependencies
- Python stdlib provides all required functionality (input/output, string manipulation, list/dict operations)
- Simplicity reduces complexity and eliminates dependency management
- Ensures broad compatibility and rapid iteration for hackathon

**Alternatives Considered**:
- Python with external libraries (rich/click): Rejected due to constitution violation
- Other languages (JavaScript, Ruby): Rejected due to user's Python specification

---

**Decision**: In-memory storage using list[dict]

**Rationale**:
- Constitution principle VI mandates in-memory list[dict] structure
- Volatile storage eliminates complexity of file I/O and schema management
- Aligns with hackathon Phase I goals focusing on core functionality
- Data persistence is out of scope per spec assumptions

**Alternatives Considered**:
- JSON file persistence: Rejected per constitution principle VI
- SQLite database: Rejected per constitution principle VI (no external storage)

---

**Decision**: Single-file or minimal two-file architecture

**Rationale**:
- Constitution principle II emphasizes simplicity
- Constitution principle III requires modularity (separate functions)
- Main file: menu loop and routing
- Optional secondary file: modular CRUD functions
- Balances simplicity with testability and maintainability

**Alternatives Considered**:
- Single monolithic file with all functions: Less modular, harder to test
- Complex package structure: Violates simplicity principle for this scope

---

**Decision**: ID generation using max(task['id']) + 1

**Rationale**:
- Ensures unique, sequential IDs even after deletions
- Simple to implement: next_id = max([t['id'] for t in tasks], 0) + 1
- Handles empty list gracefully
- Alternative len(tasks) + 1 would cause ID collision if tasks are deleted

**Alternatives Considered**:
- len(tasks) + 1: Rejected because it causes non-unique IDs after deletions
- UUID: Rejected as over-engineering for simple console app

---

**Decision**: Console interface with numbered menu and input() for user interaction

**Rationale**:
- Constitution principle IV requires user-friendly text menu
- Simple, universal CLI pattern users understand
- input() for all user input (strings for titles/descriptions, integers for IDs/menu choices)
- print() for all output including error messages and formatted task lists

**Alternatives Considered**:
- Argument-based CLI (e.g., python main.py --add "Task"): Rejected as less interactive
- GUI framework: Rejected per constitution principle II (no external dependencies)
