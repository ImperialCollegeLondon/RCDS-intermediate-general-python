def factorial(n):
    if n < 0:
        raise ValueError("'n' shouldn't be negative")
    result = 1

    for i in range(2, n + 1):
        result *= i

    return (result)
