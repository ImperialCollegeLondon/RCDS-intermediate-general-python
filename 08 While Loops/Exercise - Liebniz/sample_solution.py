def liebniz(epsilon):
    denominator = 1
    sign = 1
    result = 0

    while 1 / denominator > epsilon:
        result += sign/ denominator

        denominator += 2
        sign *= -1

    return(result)