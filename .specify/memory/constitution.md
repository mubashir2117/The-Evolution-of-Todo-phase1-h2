<!--
  Sync Impact Report:
  - Version change: [N/A → 1.0.0] (Initial ratification)
  - Modified principles: N/A (Initial creation)
  - Added sections: All principles, constraints, and governance sections
  - Removed sections: N/A (Initial creation)
  - Templates requiring updates:
    - ✅ plan-template.md (Constitution Check section aligns with principles)
    - ✅ spec-template.md (Scope/requirements alignment)
    - ✅ tasks-template.md (Task categorization reflects modularity and simplicity principles)
  - Follow-up TODOs: None
-->

# Todo Console App Constitution

## Core Principles

### I. Spec-Driven Only

All implementation MUST be performed by Claude Code from feature specifications. No manual coding is permitted. Development proceeds through the hierarchy: Constitution → Specify → Plan → Tasks → Implementation. This ensures traceability from business intent to code and prevents uncoordinated changes.

**Rationale**: Automating implementation from specs guarantees that all code is aligned with documented requirements and that changes can be traced back to their source. This reduces technical debt and ensures consistency across the codebase.

### II. Simplicity

The application MUST use only the Python standard library. No external dependencies, frameworks, or third-party packages are permitted. The implementation should be straightforward and avoid over-engineering.

**Rationale**: For a hackathon Phase I project, simplicity enables rapid iteration and eliminates dependency management overhead. Python's stdlib provides all necessary functionality for in-memory data structures, text I/O, and user interaction.

### III. Modularity

Each operation (Add, View, Update, Delete, Toggle Complete) MUST be implemented as a separate, well-defined function. Functions should have a single responsibility and clear interfaces.

**Rationale**: Modular code is easier to test, understand, and maintain. Separating concerns enables parallel development of features and simplifies debugging when issues arise.

### IV. User-Friendly

The console interface MUST provide clear text menus with intuitive navigation. Error messages MUST be descriptive and help users understand what went wrong and how to proceed. The application MUST handle all edge cases gracefully without crashing.

**Rationale**: A good user experience is critical for engagement, even in console applications. Clear feedback prevents user frustration and reduces the need for support.

### V. Clean Code

All code MUST follow PEP 8 style guidelines. Type hints MUST be used for function signatures. Comments MUST link to the relevant specification sections (spec.md references where applicable).

**Rationale**: Consistent code style improves readability and maintainability. Type hints catch errors early and serve as documentation. Linking comments to specifications ensures traceability from code to requirements.

### VI. In-Memory Storage

Task data MUST be stored in memory using Python's list[dict] structure. No file persistence, database, or external storage is permitted. Data is volatile and lost when the application terminates.

**Rationale**: For Hackathon II Phase I, in-memory storage eliminates complexity related to data persistence, file I/O, and schema migrations. This focus on core functionality aligns with sprint goals.

### VII. No Extras

Only the five specified features are permitted: Add, View, Update, Delete, Toggle Complete. No additional features, optimizations, or enhancements may be implemented without explicit specification updates.

**Rationale**: Feature creep dilutes focus and extends development time. This principle enforces scope boundaries and ensures delivery of the MVP within the hackathon timeline.

## Constraints

- **Python Version**: 3.13 or higher
- **Storage**: Volatile list[dict] in memory only
- **Core Features**: Add task, View tasks, Update task, Delete task, Toggle complete status
- **User Interface**: Text-based menu loop with numeric options
- **Error Handling**: All errors must be caught and handled gracefully; application must never crash
- **Artifact Hierarchy**: Constitution > Specify > Plan > Tasks > Implementation (strictly enforced)

## Development Workflow

### Specification Process

1. Feature requirements are documented in `specs/<feature>/spec.md`
2. Implementation plan is created in `specs/<feature>/plan.md`
3. Testable tasks are defined in `specs/<feature>/tasks.md`
4. Claude Code executes tasks via `/sp.implement` command
5. No manual edits to implementation code

### Code Review and Compliance

- All code must be generated from specifications
- Code must pass PEP 8 linting
- Type hints must be complete
- Comments must reference spec sections
- Error handling must be comprehensive
- Each function must have a single responsibility

## Governance

This constitution is the authoritative source for all development decisions. Amendments require:

1. Explicit justification for the change
2. Impact analysis on existing specifications and code
3. Migration plan if the change affects in-progress work
4. Version bump according to semantic versioning:
   - **MAJOR**: Backward-incompatible changes (e.g., removing a principle)
   - **MINOR**: Adding new principles or sections
   - **PATCH**: Clarifications or wording refinements

All feature specifications, implementation plans, and tasks must verify compliance with this constitution. Complex solutions that violate simplicity or modularity principles must be justified in the plan's complexity tracking table.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
