# Check the file containing the exercise solution exists
try:
    import factorial_exercise
except ModuleNotFoundError:
    raise ModuleNotFoundError("The file 'factorial_exercise.py' could not be imported. Make sure it exists in this directory and the file name is spelled correctly.")

# Check the function exists in the relevant file
try:
    factorial_exercise.factorial
except AttributeError:
    raise AttributeError("The file factorial_exercise.py doesn't contain a function named 'factorial'. Make sure you've defined the function and it's spelled correctly.")

from types import FunctionType

# Check factorial_exercise.factorial is a function
assert type(factorial_exercise.factorial) == FunctionType, "factorial_exercise.factorial is not a function. Make sure you're using 'def' to define it as a function and have not redefined it later in your script."

# Define a function to check the correct value is returned
def check_factorial_value(input, reference_output):
    try:
        student_output = factorial_exercise.factorial(input)
    except:
        print("When factorial was called with the value '{}', the following exception was raised. Check its contents carefully and amend your code.".format(input))

    assert student_output == reference_output, "When factorial was called with the value '{}', your code returned '{}' when it should have returned '{}'. Check the logic of your code to find out why it produced the wrong answer.".format(input, student_output, reference_output)

# Check the values of the first few factorials
check_factorial_value(0, 1)
check_factorial_value(1, 1)
check_factorial_value(2, 2)
check_factorial_value(3, 6)
check_factorial_value(4, 24)
check_factorial_value(5, 120)
check_factorial_value(6, 720)
check_factorial_value(7, 5040)

# Check if a ValueError is raised when called with a negative value
raised = False
try:
    factorial_exercise.factorial(-1)
except ValueError:
    raised = True
except:
    print("When factorial was called with a value of -1, a ValueError should have been raised. Instead, the following exception was raised. Read it carefully and use it to debug your code.")
    raise

assert raised, "When factorial was called with a value of -1, a ValueError should have been raised, but it wasn't. Check the logic of your code."

# All tests have passed
print("All tests passed. Congratulations!")