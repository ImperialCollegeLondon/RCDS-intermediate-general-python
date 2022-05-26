# Check the file containing the exercise solution exists
try:
    import modify_text
except ModuleNotFoundError:
    raise ModuleNotFoundError("The file 'modify_text.py' could not be imported. Make sure it exists in this directory and the file name is spelled correctly.")

# Check the list_to_string still function exists in the relevant file
try:
    modify_text.list_to_string
except AttributeError:
    raise AttributeError("The file modify_text.py doesn't contain a function named 'list_to_string'. make sure you haven't deleted or renamed this function.")

from types import FunctionType

# Check modify_text.list_to_string is still a function
assert type(modify_text.list_to_string) == FunctionType, "modify_text.list_to_string is not a function. Make sure you haven't redefined it later in your script."

# Check modify_text.list_to_string behaves as expected
hello_string = modify_text.list_to_string(["H", "e", "l", "l", "o"])
assert hello_string == "Hello", "modify_text.list_to_string was given the list ['H', 'e', 'l', 'l', 'o'], but returned '{}' instead of 'Hello'. Make sure you havn't edited this function and changed its behaviour.". format(hello_string)

a1_string = modify_text.list_to_string(["a", "1"])
assert a1_string == "a1", "modify_text.list_to_string was given the list ['a', '1], but returned '{}' instead of 'a1'. Make sure you havn't edited this function and changed its behaviour.". format(a1_string)