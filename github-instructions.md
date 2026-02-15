# GitHub-Specific Instructions for AI Agents

This document provides GitHub-specific guidelines for AI agents working with this repository.

## Repository Context

- **Organization**: EchoTools ecosystem
- **Template Purpose**: Python application skeleton for new projects
- **Security Level**: 2-admin approval required for releases
- **Deadline**: 2026-04-07

## Branch Management

### Branch Naming Conventions

Use descriptive branch names following these patterns:

- `feature/<description>` - For new features
- `fix/<description>` - For bug fixes
- `docs/<description>` - For documentation updates
- `refactor/<description>` - For code refactoring
- `test/<description>` - For test additions/updates

Examples:
```
feature/add-user-authentication
fix/resolve-import-error
docs/update-api-documentation
refactor/simplify-error-handling
test/add-edge-case-coverage
```

### Branch Protection

- `main` branch is protected
- Pull requests required for merging
- CI checks must pass before merge
- Code review may be required

## Commit Message Format

### Conventional Commits v1.0.0

**AI agents MUST follow this format strictly.**

Format:
```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

### Commit Types

- `feat`: New feature or enhancement
- `fix`: Bug fix
- `docs`: Documentation changes only
- `style`: Code style/formatting (no logic change)
- `refactor`: Code restructuring (no behavior change)
- `test`: Adding or updating tests
- `perf`: Performance improvements
- `chore`: Maintenance, dependencies, tooling
- `ci`: CI/CD configuration changes
- `build`: Build system changes

### Scope (Optional)

The scope should indicate what area of the codebase is affected:

- `app`: Changes to app/ directory
- `modules`: Changes to modules/ directory
- `tests`: Changes to tests/ directory
- `ci`: Changes to CI workflow
- `docs`: Documentation files
- `deps`: Dependencies

### Examples

**Good commit messages:**
```
feat(modules): add data validation function

Add validate_email() and validate_phone() functions to example_module
with comprehensive input checking and error messages.

Closes #123
```

```
fix(app): correct error handling in main loop

The main() function now properly catches and logs FileNotFoundError
when configuration files are missing.
```

```
docs(readme): update installation instructions

Add virtual environment setup steps and troubleshooting section
for common installation issues.
```

```
test(example_module): add edge case tests for greet()

Add tests for empty string, None, and numeric inputs to ensure
robust error handling.
```

```
chore(deps): update pytest to 8.0.0

Update pytest version for security patch and new features.
```

### Breaking Changes

If a commit introduces breaking changes, add `BREAKING CHANGE:` in the footer:

```
feat(modules): change greet() return type

BREAKING CHANGE: greet() now returns a dict instead of string
to include timestamp and metadata.
```

### Human Contributors Note

Human contributors are **not required** to use Conventional Commits format, but they should write clear, informative commit messages that explain what changed and why.

## Pull Request Guidelines

### PR Title

- Use clear, descriptive titles
- For AI agents: Follow Conventional Commits format
- For humans: Use natural language

Examples:
```
feat: Add user authentication module
fix: Resolve import error in main.py
docs: Update contributing guidelines
```

### PR Description

Include the following sections:

**Summary:**
- What changes were made
- Why the changes were needed

**Testing:**
- How the changes were tested
- Test results

**Checklist:**
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests pass
- [ ] No security vulnerabilities introduced

### PR Size

- Keep PRs focused and reasonably sized
- Large changes should be broken into multiple PRs
- Each PR should address a single concern

## CI/CD Integration

### Automated Checks

The CI pipeline runs:
1. Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12
2. Security scanning with Bandit
3. Dependency vulnerability checks with Safety

### Required Status Checks

All of the following must pass:
- ✅ All test suites pass
- ✅ Security checks pass
- ✅ No critical vulnerabilities

### Handling CI Failures

If CI fails:
1. Review the failure logs
2. Fix the issue locally
3. Run tests locally before pushing
4. Push fixes and wait for CI to rerun

## Security Requirements

### Code Scanning

- Bandit scans all Python code
- Safety checks all dependencies
- No critical or high severity issues allowed

### Sensitive Data

**Never commit:**
- API keys
- Passwords
- Tokens
- Private keys
- Database credentials
- Personal information

**Use instead:**
- Environment variables
- Secret management systems
- `.env` files (not committed)

### Security Checklist

Before submitting PR:
- [ ] No secrets in code
- [ ] No `eval()` or `exec()` with user input
- [ ] Input validation implemented
- [ ] Error handling doesn't expose sensitive info
- [ ] Dependencies checked for vulnerabilities

## Role-Based Access Control

- **Maintainers**: Full access, can approve PRs
- **Contributors**: Can create PRs, limited access
- **Bots/AI Agents**: Automated access with restrictions

## Release Process

### Versioning

Follow Semantic Versioning (SemVer):
- MAJOR version: Breaking changes
- MINOR version: New features (backward compatible)
- PATCH version: Bug fixes (backward compatible)

### Release Requirements

- 2-admin approval required
- All CI checks passed
- Documentation updated
- Changelog generated (from Conventional Commits)

## Working with Issues

### Issue Templates

When creating issues, include:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Environment details (Python version, OS)

### Linking Issues

Link commits and PRs to issues:
```
fix(app): resolve configuration error

Fixes #42
```

Use keywords:
- `Fixes #123` - Closes the issue when merged
- `Relates to #123` - References without closing
- `Closes #123` - Explicitly closes the issue

## Best Practices

### Before Creating PR

1. Run tests locally: `pytest tests/ -v`
2. Check code style
3. Update documentation
4. Review your own changes
5. Write clear commit messages

### During Review

- Respond to feedback promptly
- Make requested changes
- Keep discussion professional
- Re-run CI after changes

### After Merge

- Delete feature branch (if applicable)
- Verify deployment (if applicable)
- Monitor for issues

## Questions or Issues?

If you encounter problems or need clarification:
1. Check existing documentation
2. Search existing issues
3. Create a new issue with details
4. Tag relevant maintainers

## Emergency Procedures

### Reverting Changes

If a merged PR causes critical issues:
1. Create revert PR immediately
2. Tag as `priority: critical`
3. Get expedited review
4. Document what went wrong

### Security Vulnerabilities

If you discover a security vulnerability:
1. **Do NOT** create a public issue
2. Contact maintainers privately
3. Follow responsible disclosure
4. Wait for patch before announcing

## Compliance

This repository follows:
- GitHub Terms of Service
- Open source best practices
- Security disclosure policies
- Data privacy regulations

---

**Remember**: These guidelines exist to maintain code quality, security, and collaboration efficiency. When in doubt, prioritize safety and clarity.
