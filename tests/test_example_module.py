"""Tests for example_module."""

import pytest

from modules.example_module import greet, calculate_sum, process_data


def test_greet_returns_greeting():
    """Test greet function returns proper greeting."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_with_empty_string():
    """Test greet function with empty string."""
    result = greet("")
    assert result == "Hello, !"


def test_calculate_sum_positive_numbers():
    """Test calculate_sum with positive numbers."""
    result = calculate_sum(5, 10)
    assert result == 15


def test_calculate_sum_negative_numbers():
    """Test calculate_sum with negative numbers."""
    result = calculate_sum(-5, -10)
    assert result == -15


def test_calculate_sum_mixed_numbers():
    """Test calculate_sum with mixed positive and negative numbers."""
    result = calculate_sum(10, -5)
    assert result == 5


def test_process_data_with_list():
    """Test process_data with list input."""
    data = [1, 2, 3]
    result = process_data(data)
    assert result["original"] == data
    assert result["type"] == "list"
    assert result["processed"] is True


def test_process_data_with_dict():
    """Test process_data with dictionary input."""
    data = {"key": "value"}
    result = process_data(data)
    assert result["original"] == data
    assert result["type"] == "dict"
    assert result["processed"] is True


def test_process_data_invalid_type():
    """Test process_data raises TypeError for invalid input."""
    with pytest.raises(TypeError, match="Data must be a list or dictionary"):
        process_data("invalid")


def test_process_data_with_number():
    """Test process_data raises TypeError for number input."""
    with pytest.raises(TypeError, match="Data must be a list or dictionary"):
        process_data(42)
