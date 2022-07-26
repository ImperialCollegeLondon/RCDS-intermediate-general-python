# Check the file containing the exercise solution exists
try:
    import modify_text
except ModuleNotFoundError:
    raise ModuleNotFoundError("The file 'modify_text.py' could not be imported. Make sure it exists in this directory and the file name is spelled correctly.")

# Check disemvowel exists in the relevant file
try:
    modify_text.disemvowel
except AttributeError:
    raise AttributeError("The file modify_text.py doesn't contain a function named 'disemvowel'. Make sure you've created this function and that it's named correctly.")

from types import FunctionType

# Check modify_text.disemvowel is a function
assert type(modify_text.disemvowel) == FunctionType, "disemvowel is not a function. Make sure you defined it as a function and haven't redefined it later in your script."

# Define a function to help check disemvowel behaves as expected
def check_disemvowel(string_in, reference_result):
    try:
        student_result = modify_text.disemvowel(string_in)
    except:
        print("When disemvowel was called with the string '{}' the following exception was raised. Read through it carefully and check the logic of your function.".format(string_in))
        raise

    assert type(student_result) == str, "When disemvowel was called with the string '{}' the returned value was {} which has the type {} when it should be a str. Check the logic of your function to make sure you return a str.".format(string_in, student_result, type(student_result))

    assert student_result == reference_result, "When disemvowel was called with the string '{}' the returned value was '{}' when it should have been '{}'. Check the logic of your function.".format(string_in, student_result, reference_result)

# Check disemvowel behaves as expected
check_disemvowel("thnx", "thnx")
check_disemvowel("fortnight", "frtnght")
check_disemvowel("fun coding", "fn cdng")
check_disemvowel("LATENT HEAT", "LTNT HT")
check_disemvowel("Awesome Programming Skillz", "wsm Prgrmmng Skllz")