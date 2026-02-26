def add_numbers(a, b):
    """Add two numbers together.

    This function will be tested.
    """
    return a + b


def power_numbers(a, b):
    """Raise `a` to the power of `b`.

    This function is intentionally small and side-effect free so it is easy to test.

    Args:
        a: The base number.
        b: The exponent.

    Returns:
        a ** b
    """
    return a ** b


def multiply_numbers(a, b):
    """Multiply two numbers together.

    This function will be tested.
    """
    if a == 0 or b == 0:
        return 0
    return a * b


def divide_numbers(a, b):
    """Divide two numbers.

    This function will NOT be tested.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
