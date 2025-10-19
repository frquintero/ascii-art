# Tasks: ASCII Art Converter CLI

**Input**: Design documents from `/specs/001-specify-scripts-bash/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python project with Click and Pillow dependencies
- [X] T003 [P] Configure pytest testing framework
- [X] T004 [P] Setup basic directory structure (src/, tests/)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Setup basic CLI framework with Click in src/cli.py
- [X] T006 Create converter module skeleton in src/converter.py
- [X] T007 Create utils module for file handling in src/utils.py
- [X] T008 Setup basic error handling and validation framework

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Convert Image to ASCII Art (Priority: P1) 🎯 MVP

**Goal**: Enable conversion of image files to ASCII art output

**Independent Test**: Can be fully tested by running the CLI with an image file and verifying ASCII art is produced that resembles the image

### Tests for User Story 1 ⚠️

**NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for image conversion function in tests/unit/test_converter.py
- [X] T010 [US1] Integration test for CLI image conversion in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T011 [US1] Implement image loading and grayscale conversion in src/converter.py
- [X] T012 [US1] Implement ASCII character mapping algorithm in src/converter.py
- [X] T013 [US1] Add image validation in src/utils.py
- [X] T014 [US1] Update CLI to accept image file paths in src/cli.py
- [X] T015 [US1] Integrate image conversion into CLI workflow
- [X] T016 [US1] Add error handling for invalid image files

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Convert Text to ASCII Art (Priority: P1)

**Goal**: Enable conversion of text strings to ASCII art output

**Independent Test**: Can be tested by providing text string and verifying ASCII art text output

### Tests for User Story 2 ⚠️

- [X] T017 [P] [US2] Unit test for text conversion function in tests/unit/test_converter.py
- [X] T018 [US2] Integration test for CLI text conversion in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T019 [US2] Implement text to ASCII art conversion algorithm in src/converter.py
- [X] T020 [US2] Add text input validation in src/utils.py
- [X] T021 [US2] Update CLI to accept text strings as input in src/cli.py
- [X] T022 [US2] Integrate text conversion into CLI workflow
- [X] T023 [US2] Add error handling for invalid text inputs

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Customize Character Set (Priority: P2)

**Goal**: Allow users to specify custom character sets for ASCII art generation

**Independent Test**: Can be tested by providing custom character string and verifying output uses only those characters

### Tests for User Story 3 ⚠️

- [ ] T024 [P] [US3] Unit test for custom character mapping in tests/unit/test_converter.py
- [ ] T025 [US3] Integration test for CLI character option in tests/integration/test_cli.py

### Implementation for User Story 3

- [ ] T026 [US3] Add character set configuration to converter functions in src/converter.py
- [ ] T027 [US3] Add --chars CLI option in src/cli.py
- [ ] T028 [US3] Add character set validation in src/utils.py
- [ ] T029 [US3] Update both image and text conversion to use custom characters

**Checkpoint**: At this point, User Story 3 should work independently

---

## Phase 6: User Story 4 - Adjust Output Density (Priority: P3)

**Goal**: Allow users to control the density/resolution of ASCII art

**Independent Test**: Can be tested by specifying density value and verifying output dimensions match

### Tests for User Story 4 ⚠️

- [ ] T030 [P] [US4] Unit test for density adjustment in tests/unit/test_converter.py
- [ ] T031 [US4] Integration test for CLI width option in tests/integration/test_cli.py

### Implementation for User Story 4

- [ ] T032 [US4] Add density/width configuration to converter functions in src/converter.py
- [ ] T033 [US4] Add --width CLI option in src/cli.py
- [ ] T034 [US4] Add width validation in src/utils.py
- [ ] T035 [US4] Update both image and text conversion to handle width adjustments

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T036 [P] Documentation updates in README.md
- [ ] T037 Code cleanup and refactoring across all modules
- [ ] T038 Performance optimization for large images
- [ ] T039 [P] Additional unit tests for edge cases in tests/unit/
- [ ] T040 Security review and input sanitization
- [ ] T041 Run quickstart.md validation and update examples

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Core conversion logic before CLI integration
- Validation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for image conversion function in tests/unit/test_converter.py"
Task: "Integration test for CLI image conversion in tests/integration/test_cli.py"

# Launch core implementation tasks:
Task: "Implement image loading and grayscale conversion in src/converter.py"
Task: "Implement ASCII character mapping algorithm in src/converter.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3 & 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

</content>
</xai:function_call"> 

<xai:function_call name="todo_write">
<parameter name="todos">[{"content": "Generate tasks.md for ASCII Art Converter CLI feature based on design documents", "status": "completed", "priority": "high", "id": "generate_tasks_md"}]
