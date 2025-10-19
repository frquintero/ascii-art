<!-- Sync Impact Report:
Version change: new → 1.0.0
List of modified principles: All principles added (5 new)
Added sections: Core Principles, Additional Constraints, Development Workflow, Governance
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md (update Constitution Check gates to reflect new principles)
Follow-up TODOs: Update plan template with specific constitution compliance checks
-->

# Amp Test Constitution

## Core Principles

### I. Clear and Modern Coding
Code must be written using modern language features, clear and descriptive naming, and established best practices. Avoid deprecated patterns and ensure code is readable and maintainable by following current standards and conventions.

### II. No Patching Solutions
All code changes must address root causes rather than applying temporary patches or workarounds. Sustainable, long-term solutions are required, with proper testing to prevent regressions.

### III. Test-Driven Development
Write tests before implementing features. Tests should cover functionality, edge cases, and prevent regressions.

### IV. Code Review
All code changes require review by at least one other developer to ensure quality and adherence to principles.

### V. Documentation
Maintain up-to-date documentation for all code, APIs, and processes.

## Additional Constraints

Technology stack: Use modern, supported versions of languages and frameworks.
Security: Implement secure coding practices and regular security reviews.
Performance: Code should be optimized for performance within reasonable bounds.

## Development Workflow

Use git for version control with feature branches.
Follow commit message conventions.
Regular code reviews and automated testing.

## Governance
Constitution supersedes all other practices. Amendments require proposal, review, and approval. Version follows semantic versioning. Compliance must be verified in all PRs.

**Version**: 1.0.0 | **Ratified**: 2025-10-18 | **Last Amended**: 2025-10-18
