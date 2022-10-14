from types import FunctionType

# Import string_comparer
try:
    from string_searcher import string_comparer
except ModuleNotFoundError:
    assert False, "string_searcher_checker.py tried to import from the file string_searcher.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "string_searcher_checker.py tried to import the function 'string_comparer' from the file string_searcher.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check string_comparer is a function
assert type(string_comparer) == FunctionType, "string_comparer is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def string_comparer_checker(string1, string2, reference_answer):
    try:
        student_answer = string_comparer(string1, string2)
    except:
        print("When string_comparer was called to compare the strings '{}' and '{}', the following exception was raised. Read it carefully and check the logic of your function".format(string1, string2))
        raise

    assert type(student_answer) == set, "When string_comparer was called to compare the strings '{}' and '{}', the value returned had the type of {} when it should have been a set. Check the logic of your function.".format(string1, string2, type(student_answer))

    assert student_answer == reference_answer, "When string_comparer was called to compare the strings '{}' and '{}', the value returned was {} when it should have been {}. Check the logic of your function.".format(string1, string2, student_answer, reference_answer)

# Perform some checks
string_comparer_checker("", "", set())
string_comparer_checker("abcd", "abcd", {"a", "b", "c", "d"})
string_comparer_checker("abcd", "dcba", set())
string_comparer_checker("abcd", "aaaa", {"a"})
string_comparer_checker("aaaa", "aaaa", {"a"})
string_comparer_checker("ABCD", "abcd", {"a", "b", "c", "d"})

print("Congratulations - your function string_comparer passed all the tests.")

# Import character_finder
try:
    from string_searcher import character_finder
except ModuleNotFoundError:
    assert False, "string_searcher_checker.py tried to import from the file string_searcher.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "string_searcher_checker.py tried to import the function 'character_finder' from the file string_searcher.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check character_finder is a function
assert type(character_finder) == FunctionType, "character_finder is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def character_finder_checker(string, character, reference_answer):
    try:
        student_answer = character_finder(string, character)
    except:
        print("When character_finder was called to find the indices of the character '{}' in the string '{}', the following exception was raised. Read it carefully and check the logic of your function".format(character, string))
        raise

    assert type(student_answer) == list, "When string_comparer was called to find the indices of the character '{}' in the string '{}', the value returned had the type of {} when it should have been a list. Check the logic of your function.".format(character, string, type(student_answer))

    assert student_answer == reference_answer, "When string_comparer was called to find the indices of the character '{}' in the string '{}', the value returned was {} when it should have been {}. Check the logic of your function.".format(character, string, student_answer, reference_answer)

character_finder_checker("", "", [])
character_finder_checker("a", "a", [0])
character_finder_checker("aaaa", "a", [0,1,2,3])
character_finder_checker("abab", "a", [0,2])
character_finder_checker("abab", "b", [1,3])
character_finder_checker("abab", "c", [])
character_finder_checker("abab", "A", [0,2])
character_finder_checker("abab", "B", [1,3])
character_finder_checker("abab", "C", [])
character_finder_checker("ABAB", "a", [0,2])
character_finder_checker("ABAB", "b", [1,3])
character_finder_checker("ABAB", "c", [])

print("Congratulations, both your functions passed all the tests.")