from types import FunctionType

try:
    from results_processor import process
except ModuleNotFoundError:
    assert False, "results_processor_checker.py tried to import from the file results_processor.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "results_processor_checker.py tried to import the function 'process' from the file results_processor.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check process is a function
assert type(process) == FunctionType, "process is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."


def check_process(raw_data, reference_output):
    try:
        student_output = process(raw_data)
    except Exception:
        print("When 'process' was called with the input {} the following exception was raised. Read the exception carefully and check the syntax and logic of your function".format(raw_data))

    assert type(student_output) == list, "When 'process' was called with the input {} the returned value had the type {} when it should have been a list".format(raw_data, type(student_output))

    assert student_output == reference_output, "When 'process' was called with the input {} the returned value had the value {} when it should have been {}".format(raw_data, student_output, reference_output)


# Check various values
check_process([1, 2, 4], [0.454, 0.908, 1.816])
check_process([1, 0, 4], [0.454, 0, 1.816])
check_process([-1, 2, 4], [0.908, 1.816])
check_process([1, 2, -4], [0.454, 0.908])
check_process([1, -2, 4], [0.454, 1.816])
check_process([1, -2, -4], [0.454])

print("Congratulations, your function passed all the tests.")