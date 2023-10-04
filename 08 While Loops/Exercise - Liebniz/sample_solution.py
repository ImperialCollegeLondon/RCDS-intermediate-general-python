# This returns the sum of all the terms of the Liebniz formula which are greater than epsilon.
def liebniz(epsilon):
    # Set initial values for the denominator and sign
    denominator = 1
    sign = 1
    # Start result of at 0, so we can add to it
    result = 0

    # Repeatedly add the nxt term to result
    # Exit the loop when the absolute value of the next term is less than epsilon
    while 1 / denominator > epsilon:
        # The next term is sign / denominator
        # Add it to result
        result += sign / denominator

        # Prepare for the next term by modifying denominator and sign
        # Increase the denominator by 2
        denominator += 2
        # Flip the sign
        sign *= -1

    # Return the result
    return (result)
