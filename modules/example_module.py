"""Example module demonstrating proper structure."""


def greet(name):
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


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


def process_data(data):
    """
    Process input data.
    
    Args:
        data: Data to process (list or dict)
        
    Returns:
        dict: Processed data with metadata
    """
    if not isinstance(data, (list, dict)):
        raise TypeError("Data must be a list or dictionary")
    
    result = {
        "original": data,
        "type": type(data).__name__,
        "processed": True
    }
    
    return result
