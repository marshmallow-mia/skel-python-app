# AI Agent Coding Instructions

This document provides detailed coding rules and guidelines for AI agents working on this repository.

## Code Style and Standards

### Import Organization

Organize imports in three distinct groups with blank lines between them:

1. Standard library imports
2. Third-party imports  
3. Local application imports

Example:
```python
import os
import sys
from typing import Dict, List

import pytest
import requests

from modules.example_module import greet
from app.main import main
```

### Naming Conventions

- **Functions and variables**: `snake_case`
  - Examples: `calculate_sum`, `user_name`, `process_data`
  
- **Classes**: `PascalCase`
  - Examples: `UserManager`, `DataProcessor`, `ConfigParser`
  
- **Constants**: `UPPER_SNAKE_CASE`
  - Examples: `MAX_RETRIES`, `DEFAULT_TIMEOUT`, `API_BASE_URL`

- **Private methods/attributes**: Prefix with single underscore `_`
  - Examples: `_internal_method`, `_cache`

### Error Handling

**Always use specific exception types:**
```python
# Good
try:
    with open(file_path, 'r') as f:
        data = f.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
except PermissionError:
    print(f"Permission denied: {file_path}")

# Avoid bare except
# Bad
try:
    risky_operation()
except:
    pass
```

**Use try/except for I/O operations:**
- File operations
- Network requests
- Database queries
- External API calls

**Provide meaningful error messages:**
```python
if not isinstance(data, dict):
    raise TypeError(f"Expected dict, got {type(data).__name__}")
```

### Documentation

**Write simple docstrings with Args and Returns sections:**

```python
def process_data(data, options=None):
    """
    Process the input data with optional configuration.
    
    Args:
        data: Input data to process (dict or list)
        options: Optional configuration dictionary
        
    Returns:
        dict: Processed data with metadata
    """
    if options is None:
        options = {}
    # Processing logic here
    return result
```

**Module docstrings:**
```python
"""
Module for data processing utilities.

This module provides functions for processing and transforming data.
"""
```

### Type Hints

**Type hints are not required** but can be used if they improve clarity:
```python
# Optional - use when beneficial
def calculate_sum(a: int, b: int) -> int:
    return a + b

# Also acceptable
def calculate_sum(a, b):
    return a + b
```

## Testing Requirements

### Test Every New Feature

All new code must include corresponding tests:

```python
def test_greet_returns_greeting():
    """Test greet function returns proper greeting."""
    result = greet("Alice")
    assert result == "Hello, Alice!"
```

### Test Framework

- Use **pytest** (not unittest)
- Follow pytest naming conventions: `test_*.py` and `test_*` functions
- Use pytest fixtures when appropriate
- Use pytest's built-in assertions

### Test Coverage

Aim to test:
- Happy path (expected usage)
- Edge cases (empty inputs, boundary values)
- Error cases (invalid inputs, exceptions)

Example:
```python
def test_process_data_with_list():
    """Test process_data with list input."""
    result = process_data([1, 2, 3])
    assert result["type"] == "list"

def test_process_data_invalid_type():
    """Test process_data raises TypeError for invalid input."""
    with pytest.raises(TypeError):
        process_data("invalid")
```

## Code Formatting

### Line Length
- Keep lines under 88 characters when reasonable
- Break long lines logically

### Whitespace
- Two blank lines between top-level functions and classes
- One blank line between methods in a class
- Use blank lines sparingly within functions

### Strings
- Use double quotes `"` for strings by default
- Use single quotes `'` for string literals that contain double quotes
- Use f-strings for string formatting: `f"Hello, {name}!"`

## Project Structure

```
skel-python-app/
├── app/                    # Main application code
├── modules/               # Reusable modules
├── tests/                 # Test suite
├── .github/workflows/     # CI/CD configuration
└── [configuration files]
```

### Adding New Modules

When adding new modules:
1. Create the module file in `modules/`
2. Add corresponding test file in `tests/`
3. Update imports in `app/main.py` if needed
4. Document the module with docstrings

## What AI Agents CANNOT Do

### Protected Files and Directories

**Cannot modify without explicit permission:**
- `.github/workflows/` - CI/CD workflows
- Security configurations
- `.gitignore` critical entries

### Prohibited Actions

**Never do the following:**
- Remove existing tests (unless replacing with better tests)
- Commit sensitive data (API keys, passwords, secrets)
- Use `eval()` or `exec()` with user input
- Suppress errors without logging
- Modify security-critical code without review
- Ignore error handling for file I/O, network, or database operations
- Create security vulnerabilities

### Testing Restrictions

**Must not:**
- Delete tests without replacement
- Skip test writing for new features
- Mark tests as `@pytest.mark.skip` without justification
- Reduce test coverage

## Security Requirements

### Input Validation
```python
def process_user_input(user_data):
    if not isinstance(user_data, dict):
        raise TypeError("Expected dictionary input")
    
    # Validate required fields
    required = ['name', 'email']
    for field in required:
        if field not in user_data:
            raise ValueError(f"Missing required field: {field}")
```

### Avoid Security Anti-Patterns
- No `eval()` or `exec()` with user input
- No shell injection vulnerabilities
- No hardcoded credentials
- Validate all external inputs
- Use parameterized queries for databases

### File Operations
```python
# Good - with proper error handling
try:
    with open(file_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    # Handle missing file
    pass
except PermissionError:
    # Handle permission issues
    pass
```

## Git and Version Control

### Commit Messages (AI Agents Only)

AI agents **must** use Conventional Commits v1.0.0 format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes (formatting)
- `chore`: Maintenance tasks

Examples:
```
feat(modules): add data validation function
fix(main): correct error handling in main loop
docs(readme): update installation instructions
test(example_module): add edge case tests
```

### Branch Naming

Not strictly enforced, but prefer:
- `feature/description`
- `fix/description`
- `docs/description`

## Python Version Compatibility

- Support Python 3.8+
- Avoid features only available in Python 3.9+
- Test on multiple Python versions via CI

## Dependencies

### Adding Dependencies

1. Add to `requirements.txt`
2. Use pinned versions for stability
3. Document why the dependency is needed
4. Ensure compatibility with Python 3.8+

### Example
```
pytest==8.0.0
requests>=2.31.0,<3.0.0
```

## Best Practices Summary

✅ **Do:**
- Write clear, focused functions
- Include comprehensive tests
- Handle errors explicitly
- Document public APIs
- Follow naming conventions
- Organize imports properly
- Validate inputs

❌ **Don't:**
- Use bare `except:` clauses
- Ignore error cases
- Skip tests
- Commit secrets
- Use dangerous functions (`eval`, `exec`)
- Remove existing tests
- Break existing functionality

## Questions or Clarifications?

When in doubt:
1. Follow existing code patterns
2. Prioritize safety and clarity
3. Add tests
4. Document your changes
5. Ask for review if uncertain
