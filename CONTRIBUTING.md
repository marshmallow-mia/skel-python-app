# Contributing to skel-python-app

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the repository.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

1. Ensure you have Python 3.8+ installed
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Code Style

### Python Coding Standards

- Follow PEP 8 guidelines
- Use snake_case for function and variable names
- Use PascalCase for class names
- Use UPPER_SNAKE_CASE for constants
- Keep functions focused and single-purpose
- Write descriptive docstrings for all public functions and classes

### Import Organization

Organize imports in three groups with blank lines between them:
1. Standard library imports
2. Third-party imports
3. Local application imports

Example:
```python
import os
import sys

import pytest

from modules.example_module import greet
```

### Documentation

- Write docstrings for all functions, classes, and modules
- Use simple docstring format with Args and Returns sections
- Keep documentation clear and concise

Example:
```python
def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b
```

## Testing

- All new code must include tests
- Use pytest for testing
- Follow existing test patterns
- Ensure all tests pass before submitting PR:
  ```bash
  pytest tests/ -v
  ```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update the README.md if needed
5. Submit your pull request with a clear description

### Commit Messages

**For Human Contributors:**
- Write clear, informative commit messages
- Explain what changed and why
- No strict format required, but be descriptive

**For AI Agents:**
- Must follow Conventional Commits v1.0.0 format
- See [github-instructions.md](github-instructions.md) for details

### Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Reference any related issues
- Provide a clear description of changes
- Ensure CI checks pass

## Error Handling

- Use specific exception types
- Include try/except blocks for I/O operations and external calls
- Provide meaningful error messages
- Don't suppress errors silently

## Security

- Never commit sensitive data (API keys, passwords, etc.)
- Follow security best practices
- Report security vulnerabilities privately

## Questions?

If you have questions, please open an issue for discussion.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on what is best for the project
- Show empathy towards other community members

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
