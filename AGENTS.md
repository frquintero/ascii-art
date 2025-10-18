# AGENTS.md - Project Guidance for AI Agents

## Purpose
This document provides project-specific guidance, conventions, and context to AI coding assistants working in this repository. It serves as the single source of truth for project standards and agent behavior.

## Core Principles
- **Understand the problem space**: Before proposing solutions, ensure a deep understanding of the problem domain
- **Collaborate with users**: Engage with team members and users to gather insights and validate assumptions
- **Always explain changes**: Provide clear reasoning for code changes, including trade-offs considered
- **Preserve existing functionality**: Assume all existing code serves a purpose
- **Minimal changes**: Make the smallest effective change to achieve goals
- **Progressive enhancement**: Prefer incremental improvements over rewrites
- **Documentation parity**: Keep documentation updated with code changes
- **Safety first**: Never break existing functionality without explicit approval

## Project Conventions

### Code Style & Standards
- Follow existing patterns and style in the codebase
- Use [Language/Framework]-specific linters and formatters (e.g., ESLint, Black, Prettier)
- Write self-documenting code with clear variable/function names
- Include meaningful comments for complex logic only

### Testing Requirements
- Maintain or improve current test coverage
- Write tests for new features and bug fixes
- Run existing tests before submitting changes
- Prefer unit tests over integration tests where appropriate

### Documentation Standards
- Update README.md for significant architectural changes
- Document API changes in OpenAPI/Swagger format if applicable
- Include code examples for new libraries or complex features
- Keep CHANGELOG.md updated with meaningful entries

### Git & Version Control
- Write clear, conventional commit messages
- Create focused PRs with descriptive titles and detailed descriptions
- Reference relevant issues in commit messages and PRs
- Keep commits atomic and logically grouped

## AI Agent Behavior Guidance

### Context Awareness
- **Automatically use Context7 MCP tools** when you need:
    - Code generation, setup, or configuration steps
    - Library/API documentation lookup
    - Framework-specific guidance
    - Dependency resolution
- Analyze the entire codebase context before making significant changes
- Respect existing architectural decisions unless explicitly asked to change them

### Change Management
- **Always ask for clarification** on ambiguous requirements
- **Propose changes before implementing** when dealing with:
    - Breaking changes to APIs
    - Database schema modifications
    - Security-related changes
    - Performance-critical code
- **Provide multiple solution options** with pros/cons for complex problems

### Safety & Validation
- **Never commit API keys, secrets, or sensitive data**
- Validate inputs and handle edge cases in new code
- Consider security implications of all changes
- Check for potential performance regressions

## Project-Specific Guidelines

### Technology Stack
[Customize this section for your project]
- **Frontend**: [Framework, version, key libraries]
- **Backend**: [Framework, version, key libraries]
- **Database**: [Type, version, ORM/ODM]
- **Testing**: [Testing framework, mocking libraries]
- **Build Tools**: [Bundler, package manager, CI/CD]

### Architecture Patterns
[Customize this section for your project]
- Follow [MVC/MVVM/Hexagonal/etc.] architecture
- Use [specific design patterns] for common problems
- Follow [framework]-specific best practices

### Development Workflow
1. Analyze existing code and requirements
2. Propose solution approach
3. Implement with tests
4. Verify against existing functionality
5. Document changes

## Communication Protocol

### When to Ask for Help
- Requirements are unclear or contradictory
- You identify potential security vulnerabilities
- Proposed changes would break existing functionality
- You discover technical debt that should be addressed separately

### Output Formatting
- Use clear, professional language
- Structure code explanations with examples
- Include relevant code snippets in responses
- Highlight potential risks and tradeoffs

## Quality Gates

### Pre-Submission Checklist
- [ ] Code follows project conventions
- [ ] Tests pass and coverage is maintained
- [ ] Documentation is updated
- [ ] No sensitive data exposed
- [ ] Changes are minimal and focused
- [ ] Performance implications considered

## Commands
- `/init-copilot` — Initialize .github/copilot-instructions.md with repository defaults
- `/review-standards` — Review and validate against project standards
- `/test-scope` — Analyze testing requirements for current changes

---

*This document should evolve with the project. Update it when establishing new patterns or changing technologies.*
