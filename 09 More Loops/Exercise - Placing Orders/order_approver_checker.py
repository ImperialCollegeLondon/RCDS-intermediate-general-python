from types import FunctionType
import os

# Import check_fissile
try:
    from order_approver import check_fissile
except ModuleNotFoundError:
    assert False, "order_approver_checker.py tried to import from the file order_approver.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "order_approver_checker.py tried to import the function 'check_fissile' from the file order_approver.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check check_fissile is a function
assert type(check_fissile) == FunctionType, "check_fissile is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

# Check check_fissile returns False with an empty list
fissile_present = check_fissile({})
assert type(fissile_present) == bool, "check_fissile was passed an empty dictionary and so should have returned False to indicate no fissile elements were present. However, the returned value was not a bool."
assert not fissile_present, "check_fissile was passed an empty dictionary and so should have returned False to indicate no fissile elements were present. However, {} was returned instead".format(fissile_present)

# Check check_fissile_returns False with a list of non-fissile elements
input_dictionary = {"CO2": 1, "Cu2O": 5}
fissile_present = check_fissile(input_dictionary)
assert type(fissile_present) == bool, "check_fissile was passed the dictionary {} and so should have returned False to indicate no fissile elements were present. However, the returned value was not a bool.".format(input_dictionary)
assert not fissile_present, "check_fissile was passed the dictionary {} and so should have returned False to indicate no fissile elements were present. However, {} was returned instead".format(input_dictionary, fissile_present)


def check_check_fissile_true(input_dictionary):
    fissile_present = check_fissile(input_dictionary)
    assert type(fissile_present) == bool, "check_fissile was passed the dictionary {} and so should have returned True to indicate fissile elements were present. However, the returned value was not a bool.".format(input_dictionary)
    assert fissile_present, "check_fissile was passed the dictionary {} and so should have returned True to indicate fissile elements were present. However, {} was returned instead".format(input_dictionary, fissile_present)


# Check check_fissile_returns True with various dictionaries containing fissile elements
check_check_fissile_true({"H2O": 1, "UO2": 0.1})
check_check_fissile_true({"PuF6": 3})
check_check_fissile_true({"H2O": 0.1, "ThB6": 1, "O2": 3})
check_check_fissile_true({"UF6": 1, "PuO2": 3})

print("Congratulations - your check_fissile function passed all the tests")

# ===================================================================================================

# Import check_poisons
try:
    from order_approver import check_poisons
except ModuleNotFoundError:
    assert False, "order_approver_checker.py tried to import from the file order_approver.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "order_approver_checker.py tried to import the function 'check_poisons' from the file order_approver.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check check_poisons is a function
assert type(check_poisons) == FunctionType, "check_poisons is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

# Check check_poisons_returns False with an empty list
poison_present = check_poisons({})
assert type(poison_present) == bool, "check_poisons was passed an empty dictionary and so should have returned False to indicate no poison compounds were present. However, the returned value was not a bool."
assert not poison_present, "check_poisons was passed an empty dictionary and so should have returned False to indicate no poison compounds were present. However, {} was returned instead".format(poison_present)

# Check check_poisons_returns False with a list of non-poison compounds
input_dictionary = {"CO2": 1, "Cu2O": 5, "BeCl2": 1}
poison_present = check_poisons(input_dictionary)
assert type(poison_present) == bool, "check_poisons was passed the dictionary {} and so should have returned False to indicate no poison compounds were present. However, the returned value was not a bool.".format(input_dictionary)
assert not poison_present, "check_poisons was passed the dictionary {} and so should have returned False to indicate no poison compounds were present. However, {} was returned instead".format(input_dictionary, poison_present)


def check_check_poisons_true(input_dictionary):
    poison_present = check_poisons(input_dictionary)
    assert type(poison_present) == bool, "check_poisons was passed the dictionary {} and so should have returned True to indicate poison compounds were present. However, the returned value was not a bool.".format(input_dictionary)
    assert poison_present, "check_poisons was passed the dictionary {} and so should have returned True to indicate poisons were present. However, {} was returned instead".format(input_dictionary, poison_present)


# Check check_poisons_returns True with various dictionaries containing poison compounds
check_check_poisons_true({"H2O": 1, "HCN": 0.1})
check_check_poisons_true({"Cl2": 3})
check_check_poisons_true({"HCN": 0.1, "Cl2": 1, "O2": 3})

print("Congratulations - your check_poisons function passed all the tests")

# ===================================================================================================

# Import order_approver
try:
    from order_approver import order_approver
except ModuleNotFoundError:
    assert False, "order_approver_checker.py tried to import from the file order_approver.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "order_approver_checker.py tried to import the function 'corder_approver' from the file order_approver.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."
# Check order_approver exists

# Check order_approver is a function
assert type(order_approver) == FunctionType, "order_approver is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."


def check_order_approver(path, reference_outcome, reason=""):
    try:
        order_approver_result = order_approver(path, [check_fissile, check_poisons])
    except FileNotFoundError:
        print("order_approver was asked to check the contents of an order found at '{}' but the following FileNotFoundError was raised. Check the file is in the correct location in your computer.".format(path))
        raise
    except Exception:
        print("order_approver was asked to check the contents of an order found at '{}' but the following exception was raised. Check the logic of your program.".format(path))
        raise

    assert type(order_approver_result) == bool, "order_approver was asked to check the contents of an order found at '{}' but the returned value was of type {} instead of bool. Check your logic.".format(path, type(order_approver_result))

    if reference_outcome:
        error_message = "order_approver was asked to check the contents of an order found at '{}' but the returned value was {} instead of {} as it should be as the file contains no fissile elements or poison compounds. Check your logic.".format(path, order_approver_result, reference_outcome)
    else:
        error_message = "order_approver was asked to check the contents of an order found at '{}' but the returned value was {} instead of {} as it should be because {}. Check your logic.".format(path, order_approver_result, reference_outcome, reason)

    assert order_approver_result == reference_outcome, error_message


# Find the absolute path of the sample_orders directory
sample_directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_orders")

# Check order_approver returns True for an empty file
print("==============Check three orders which should be approved==================")
check_order_approver(os.path.join(sample_directory_path, "order_empty.txt"), True)

# Check a couple of orders which don't violate any checks cause order_approver to return True
check_order_approver(os.path.join(sample_directory_path, "order_1.txt"), True)
check_order_approver(os.path.join(sample_directory_path, "order_2.txt"), True)

# Check a couple of orders which violate one or more checks cause order_approver to return False
print("==============Check three orders which should be rejected================")
check_order_approver(os.path.join(sample_directory_path, "order_3.txt"), False, "the file contains the fissile element Th")
check_order_approver(os.path.join(sample_directory_path, "order_4.txt"), False, "the file contains the poison compound Cl2")
check_order_approver(os.path.join(sample_directory_path, "order_5.txt"), False, "the file contains the fissile element U and the poison compound HCN")

print("Congratulations - your order_approver function passed all the tests.")
print("Congratulations - all test for all functions passed.")