---

description: "Task list for feature implementation"
---

# Tasks: Todo Console App

**Input**: Design documents from `/specs/001-todo-console/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below do NOT include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: main.py at repository root
- Paths shown below follow the single-file structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create main.py file at repository root with Python 3.13+ shebang line

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T002 Initialize global tasks list in main.py: `tasks: list[dict] = []`
- [x] T003 Create menu handler function with display menu and input choice skeleton in main.py
- [x] T004 Implement _generate_next_id helper function for unique ID generation in main.py (uses max() + 1 strategy)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new tasks with title and optional description

**Independent Test**: Can be fully tested by creating main.py, calling add_task() directly with a tasks list, and verifying the task is added with a unique ID and default completed=False

### Implementation for User Story 1

- [x] T005 [US1] Implement add_task function in main.py with title/description prompts, validation (1-200 chars, not empty), and task creation (see spec.md FR-003, FR-004, FR-005, FR-006 and plan.md contracts/add-task.md)
- [x] T006 [US1] Add add_task call to menu handler when user selects option 1 in main.py

**Checkpoint**: At this point, users can add tasks via the menu, but cannot view them yet

---

## Phase 4: User Story 2 - View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to view all tasks in a table-like format with status indicators

**Independent Test**: Can be fully tested by adding multiple tasks, calling view_tasks(), and verifying the output shows ID, title, description, and status in a formatted table

### Implementation for User Story 2

- [x] T007 [US2] Implement view_tasks function in main.py with table format, status icons [✓]/[ ], and "No tasks yet." message (see spec.md FR-007, FR-008, FR-009 and plan.md contracts/view-tasks.md)
- [x] T008 [US2] Add view_tasks call to menu handler when user selects option 2 in main.py

**Checkpoint**: At this point, users can add and view tasks - MVP is functional

---

## Phase 5: User Story 3 - Toggle Complete Status (Priority: P2)

**Goal**: Enable users to flip task completion status between True and False

**Independent Test**: Can be fully tested by creating a task, calling toggle_task() with its ID, and verifying the completed flag changes and confirmation message displays

### Implementation for User Story 3

- [ ] T009 [US3] Implement toggle_task function in main.py with ID validation, task lookup, status flip, and confirmation message (see spec.md FR-010, FR-013 and plan.md contracts/toggle-task.md)
- [ ] T010 [US3] Add toggle_task call to menu handler when user selects option 3 in main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Enable users to update task title and/or description while preserving ID and completed status

**Independent Test**: Can be fully tested by creating a task, calling update_task() with new title/description, and verifying the task is updated without changing ID or completed status

### Implementation for User Story 4

- [ ] T011 [US4] Implement update_task function in main.py with ID validation, title/description prompts, validation (title 1-200 chars if provided), and partial field updates (see spec.md FR-011, FR-013, FR-014 and plan.md contracts/update-task.md)
- [ ] T012 [US4] Add update_task call to menu handler when user selects option 4 in main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Enable users to remove tasks from the collection by ID

**Independent Test**: Can be fully tested by creating multiple tasks, calling delete_task() with an ID, and verifying the task is removed and confirmation message displays

### Implementation for User Story 5

- [ ] T013 [US5] Implement delete_task function in main.py with ID validation, task lookup, removal from list, and confirmation message (see spec.md FR-012, FR-013 and plan.md contracts/delete-task.md)
- [ ] T014 [US5] Add delete_task call to menu handler when user selects option 5 in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, error handling, and validation

- [ ] T015 Complete menu handler with try-except error wrapping for all function calls in main.py (ensure no crashes per spec.md FR-015)
- [ ] T016 Add input validation for menu choice (numeric 0-5) with "Invalid choice." error message in main.py
- [ ] T017 Add main() function with while True loop, menu display, choice routing, and exit on 0 in main.py
- [ ] T018 Add type hints to all functions in main.py (see plan.md contracts/ for signatures and spec.md FR-04 for Task type)
- [ ] T019 Add comments linking to spec.md sections (FR numbers) in main.py
- [ ] T020 Validate app against quickstart.md testing checklist

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001) - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion (T002-T004)
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 - Add Task (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 - View Tasks (P1)**: Can start after Foundational (Phase 2) - Works independently but benefits from US1 to have tasks to view
- **User Story 3 - Toggle Complete (P2)**: Can start after Foundational (Phase 2) - Works independently but requires tasks to exist
- **User Story 4 - Update Task (P2)**: Can start after Foundational (Phase 2) - Works independently but requires tasks to exist
- **User Story 5 - Delete Task (P3)**: Can start after Foundational (Phase 2) - Works independently but requires tasks to exist

### Task Dependencies Within Phases

- **Phase 2 (Foundational)**: T002 and T003 can run in parallel [P], T004 must follow T002
- **Phase 3 (US1)**: T005 must precede T006
- **Phase 4 (US2)**: T007 must precede T008
- **Phase 5 (US3)**: T009 must precede T010
- **Phase 6 (US4)**: T011 must precede T012
- **Phase 7 (US5)**: T013 must precede T014
- **Phase 8 (Polish)**: T015-T019 can mostly run in parallel [P], T020 must be last

---

## Parallel Opportunities

Within constraints of single-file main.py, parallel opportunities are limited but exist:

**Phase 1**: Single task, no parallelization

**Phase 2**:
- T002 and T003 can be started in parallel [P] (tasks list and menu handler skeleton are independent)
- T004 depends on T002 (needs tasks list for ID generation)

**Phase 3-7 (User Stories)**:
- After Phase 2 completes, Phase 3 (US1) and Phase 4 (US2) can proceed in parallel [P]
- Phase 5 (US3), Phase 6 (US4), and Phase 7 (US5) can also proceed in parallel after Phase 2
- Within each user story phase, implementation must precede integration

**Phase 8**:
- T015-T019 can proceed in parallel [P] (error handling, validation, main(), type hints, comments)
- T020 must be last (validation of complete app)

**Parallel Team Strategy** (with multiple developers):
1. Team completes Setup (T001) and Foundational (T002-T004) together
2. Once Foundational is done:
   - Developer A: Phase 3 (Add Task)
   - Developer B: Phase 4 (View Tasks)
   - Developer C: Phase 5 (Toggle Complete)
3. Team merges work and continues:
   - Developer A: Phase 6 (Update Task)
   - Developer B: Phase 7 (Delete Task)
   - Developer C: Polish tasks
4. Team completes final validation together

---

## Implementation Strategy

### MVP First (User Stories 1 and 2 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002-T004) - **CRITICAL**
3. Complete Phase 3: Add Task (T005-T006)
4. Complete Phase 4: View Tasks (T007-T008)
5. **STOP and VALIDATE**: Test User Stories 1 and 2 independently
6. Deploy/demo as MVP (users can add and view tasks)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Add Task) → Test independently → MVP + Add
3. Add User Story 2 (View Tasks) → Test independently → Full MVP!
4. Add User Story 3 (Toggle Complete) → Test independently → Enhanced MVP
5. Add User Story 4 (Update Task) → Test independently → Feature complete
6. Add User Story 5 (Delete Task) → Test independently → Full feature set
7. Complete Polish phase → Production ready

Each story adds value without breaking previous stories.

---

## Format Validation

All tasks follow the required format:
- ✅ Start with `- [ ]` checkbox
- ✅ Sequential Task ID (T001-T020)
- ✅ [P] marker for parallelizable tasks
- ✅ [Story] label for user story phases (US1, US2, US3, US4, US5)
- ✅ Clear description with exact file path (main.py)
- ✅ Links to spec.md (FR numbers) and plan.md contracts/

---

## Notes

- [P] tasks = can run in parallel (different files or no dependencies)
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Single-file structure (main.py) limits some parallelization but user stories remain independent
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, skipping constitution principles, missing error handling
