from types import FunctionType
import multiprocessing.pool
import functools

try:
    from liebniz_calculator import liebniz
except ModuleNotFoundError:
    assert False, "liebniz_calculator_checker.py tried to import from the file liebniz_calculator.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "liebniz_calculator_checker.py tried to import the function 'liebniz' from the file liebniz_calculator.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check liebniz is a function
assert type(liebniz) == FunctionType, "liebniz is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."


# This code defines a decorator which will case a TimeoutError if a function takes too long to run
def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


@timeout(5)
def liebniz_wrapper(epsilon):
    return (liebniz(epsilon))


def check_liebniz(epsilon, reference_value, tolerance):
    try:
        student_value = liebniz_wrapper(epsilon)
    except multiprocessing.context.TimeoutError as ex:
        raise TimeoutError("When the function 'liebniz' was called with a value of {} for epsilon, your code executed for more than 5s. This may indicate your code contains an infinite loop. Check the logic of your code. The TimeOurError raised is displayed below".format(epsilon)) from ex
    except Exception:
        print("When the function 'liebniz' was called with a value of {} for epsilon, the following exception was raised. Check the logic of your code.".format(epsilon))
        raise

    assert type(student_value) == float or type(student_value) == int, "When the function 'liebniz' was called with a value of {} for epsilon, the value returned had a type of {} instead of float or int. Check the logic of your code.".format(epsilon, type(student_value))

    assert abs(student_value - reference_value) < tolerance, "When the function 'liebniz' was called with a value of {} for epsilon, the resulting answer should have been {}, but it was {}. Check your logic. In particular, make sure you're not including any terms with an absolute value lower than epsilon.".format(epsilon, reference_value, student_value)


check_liebniz(1e-3, 0.7848981638974463, 1e-4)

check_liebniz(1e-6, 0.785397663397423, 1e-7)

check_liebniz(10, 0, 1e-3)

print("Congratulations - you code passed all the tests.")