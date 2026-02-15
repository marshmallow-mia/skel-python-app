"""Main application entry point."""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.example_module import greet, calculate_sum


def main():
    """
    Main application function.
    
    Returns:
        int: Exit code (0 for success)
    """
    print("Welcome to the Python Application Skeleton!")
    
    # Example usage of module functions
    message = greet("World")
    print(message)
    
    result = calculate_sum(10, 20)
    print(f"Sum of 10 and 20 is: {result}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
