"""Tests for main application."""

import sys
from unittest.mock import patch

from app.main import main


def test_main_returns_success():
    """Test that main function returns 0 on success."""
    assert main() == 0


def test_main_prints_welcome(capsys):
    """Test that main function prints welcome message."""
    main()
    captured = capsys.readouterr()
    assert "Welcome to the Python Application Skeleton!" in captured.out


def test_main_uses_greet_function(capsys):
    """Test that main function uses greet from example_module."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out


def test_main_uses_calculate_sum(capsys):
    """Test that main function uses calculate_sum from example_module."""
    main()
    captured = capsys.readouterr()
    assert "Sum of 10 and 20 is: 30" in captured.out
