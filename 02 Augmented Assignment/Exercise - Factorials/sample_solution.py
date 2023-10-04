def factorial(n):
    # Receive the value "n" we want to find the factorial of

    # Check if n is negative first, so we don't proceed any further if the factorial is invalid
    if n < 0:
        # If n is negative, raise a ValueError with a descriptive message
        raise ValueError("'n' shouldn't be negative")

    # Start result with a value of 1
    result = 1

    # Multiply result by every number from 2 to n
    for i in range(2, n + 1):
        result *= i

    # Return the result
    return (result)
