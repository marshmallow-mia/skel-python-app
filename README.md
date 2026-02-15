# skel-python-app

![Python CI](https://github.com/marshmallow-mia/skel-python-app/workflows/Python%20CI/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

Python Application Skeleton Template - A minimal starting point for new Python projects.

## Description

This is a generic Python application skeleton template designed to provide a clean, well-structured starting point for new Python projects. It includes:

- Clean application structure with separation of concerns
- Example modules demonstrating best practices
- Comprehensive test suite using pytest
- CI/CD workflow with automated testing
- Security checks integrated into the CI pipeline
- Documentation and contribution guidelines
- AI agent coding rules and instructions

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/marshmallow-mia/skel-python-app.git
cd skel-python-app
```

2. Create and activate a virtual environment:
```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the environment variables template:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

Run the main application:
```bash
python app/main.py
```

Run tests:
```bash
pytest tests/ -v
```

## Project Structure

```
skel-python-app/
├── app/                    # Main application package
│   ├── __init__.py
│   └── main.py            # Application entry point
├── modules/               # Application modules
│   ├── __init__.py
│   └── example_module.py  # Example module
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── test_main.py
│   └── test_example_module.py
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD workflow
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── CONTRIBUTING.md      # Contribution guidelines
├── AGENTS.md           # AI agent overview
├── INSTRUCTIONS.md     # AI agent coding rules
└── github-instructions.md  # GitHub-specific agent instructions
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## AI Agents

This repository supports AI agents for automated development tasks. See [INSTRUCTIONS.md](INSTRUCTIONS.md) for detailed AI agent coding guidelines and [AGENTS.md](AGENTS.md) for an overview of AI agent capabilities.

## License

This is a template project - choose an appropriate license for your specific use case.

## Support

For issues, questions, or contributions, please open an issue on GitHub.