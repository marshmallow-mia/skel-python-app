# AI Agents in skel-python-app

## Overview

This repository supports AI agents for automated development tasks. AI agents can assist with:

- Code implementation
- Bug fixes
- Test creation
- Documentation updates
- Refactoring
- Code reviews

## Agent Capabilities

AI agents working on this repository have access to:

- Code reading and modification
- Test execution
- Git operations (via specialized tools)
- CI/CD workflow monitoring
- Security scanning

## Working with AI Agents

### For Repository Maintainers

AI agents follow strict coding guidelines defined in [INSTRUCTIONS.md](INSTRUCTIONS.md). These guidelines ensure:

- Consistent code style
- Proper error handling
- Comprehensive testing
- Security best practices
- Documentation standards

### Conventional Commits Requirement

**AI agents MUST use Conventional Commits v1.0.0 format** for all commit messages. This ensures:

- Automated changelog generation
- Clear commit history
- Semantic versioning compatibility
- Better traceability

**Note:** Human contributors are encouraged to write informative commit messages but are not required to follow the strict Conventional Commits format.

## Detailed Guidelines

For comprehensive AI agent coding rules and restrictions, see:
- [INSTRUCTIONS.md](INSTRUCTIONS.md) - Detailed coding rules and standards
- [github-instructions.md](github-instructions.md) - GitHub-specific instructions

## Repository-Specific Information

### Structure

This is a Python application skeleton template designed for:
- Python 3.8+ projects
- Generic Python applications (not framework-specific)
- Projects requiring clear structure and best practices

### Testing

- Framework: pytest
- All new code must include tests
- Tests must pass before merging

### CI/CD

- Automated testing on multiple Python versions (3.8-3.12)
- Security checks with Bandit and Safety
- All checks must pass before merging

## Security

AI agents are configured to:
- Never commit sensitive data
- Follow security best practices
- Use Bandit for security scanning
- Implement proper error handling

## Limitations

AI agents cannot:
- Modify `.github/workflows/` without explicit permission
- Remove existing tests without justification
- Ignore error handling for critical operations
- Use `eval()` or `exec()` with user input
- Modify security configurations without review

## Questions or Issues?

If you have questions about AI agent behavior or need to report issues, please open a GitHub issue.
