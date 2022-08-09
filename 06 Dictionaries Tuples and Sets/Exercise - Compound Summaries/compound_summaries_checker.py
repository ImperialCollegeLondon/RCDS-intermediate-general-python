from types import FunctionType

try:
    from compound_summaries import count_atoms_in_compounds
except ModuleNotFoundError:
    assert False, "compound_summaries_checker.py tried to import from the file compound_summaries.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "compound_summaries_checker.py tried to import the function 'count_atoms_in_compounds' from the file compound_summaries.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check count_atoms_in_compounds is a function
assert type(count_atoms_in_compounds) == FunctionType, "count_atoms_in_compounds is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def get_compound_list_string_summary(compound_moles):
    if len(compound_moles) == 0:
        return("an empty dictionary containing no compounds ")
    result = ""
    for i, formula in enumerate(compound_moles):
        result += "{} mole".format(compound_moles[formula])
        if compound_moles[formula] != 1:
            result += "s"
        result += " of {}".format(formula)
        if i == len(compound_moles) - 2:
            result += " and "
        elif i < len(compound_moles) - 2:
            result += ", "
        else:
            result += " "
    return(result)


def check_atoms_counts_match(compound_moles, reference_dictionary):
    student_dictionary = count_atoms_in_compounds(compound_moles)
    if type(student_dictionary) != dict:
        raise AssertionError("When count_atoms_in_compounds was asked to count the moles of elements in {}the returned value was {}, not a dictionary. Check you're creating and returning a dictionary in all cases.".format(get_compound_list_string_summary(compound_moles), type(student_dictionary)))

    if student_dictionary != reference_dictionary:
        raise AssertionError("When count_atoms_in_compounds was asked to count the moles of elements in {}the returned value was {}, not {}. Ordering does not matter, but the keys/values aren't the same. Check you logic.".format(get_compound_list_string_summary(compound_moles), student_dictionary, reference_dictionary))

# Check an empty compound_moles results in an empty dictionary returned from count_atoms_in_compounds
check_atoms_counts_match({}, {})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 1 mole of Ar
check_atoms_counts_match({"Ar": 1}, {"Ar": 1})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 1 mole of H2
check_atoms_counts_match({"H2": 1}, {"H": 2})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of Ne
check_atoms_counts_match({"Ne": 2}, {"Ne": 2})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of O2
check_atoms_counts_match({"O2": 2}, {"O": 4})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of O2
check_atoms_counts_match({"CO2": 1}, {"C": 1, "O": 2})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of O2
check_atoms_counts_match({"He": 1, "N2": 1}, {"He": 1, "N": 2})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of O2
check_atoms_counts_match({"CO2": 2, "CaCO3": 3}, {"Ca": 3, "C": 5, "O": 13})

# Check count_atoms_in_compounds correctly predicts the number of moles of elements in 2 moles of O2
check_atoms_counts_match({"UO2": 1, "HNO3": 1, "H2O": 10}, {"U": 1, "O": 15, "H": 21, "N": 1})

#===============================================================================================================================================================

try:
    from compound_summaries import find_elements_present
except ModuleNotFoundError:
    assert False, "compound_summaries_checker.py tried to import from the file compound_summaries.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "compound_summaries_checker.py tried to import the function 'find_elements_present' from the file compound_summaries.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check find_elements_present is a function
assert type(find_elements_present) == FunctionType, "find_elements_present is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def check_element_sets_match(compound_moles, reference_set):
    student_set = find_elements_present(compound_moles)
    if type(student_set) != set:
        raise AssertionError("When find_elements_present was asked to construct a set containng the elements present in {}the returned value was {}, not a set. Check you're creating and returning a set in all cases.".format(get_compound_list_string_summary(compound_moles), type(student_set)))

    if len(student_set) == 0:
        student_set_description = "an empty set"
    else:
        student_set_description = str(student_set)

    if len(reference_set) == 0:
        reference_set_description = "an empty set"
    else:
        reference_set_description = str(reference_set)

    if student_set != reference_set:
        error_text = "When find_elements_present was asked to construct a set containng the elements present in {}the returned value was {}, not {}.".format(get_compound_list_string_summary(compound_moles), student_set_description, reference_set_description)
        if len(student_set) > 0 and len(reference_set) > 0:
            error_text += " Ordering does not matter, but the values aren't the same. Check you logic."
        raise AssertionError(error_text)

# Check an empty compound_moles results in an empty set returned from find_elements_present
check_element_sets_match({}, set())

# Check find_elements_present correctly predicts the number of moles of elements in 1 mole of Ar
check_element_sets_match({"Ar": 1}, {"Ar"})

# Check find_elements_present correctly predicts the number of moles of elements in 1 mole of H2
check_element_sets_match({"H2": 1}, {"H"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of Ne
check_element_sets_match({"Ne": 2}, {"Ne"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of O2
check_element_sets_match({"O2": 2}, {"O"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of O2
check_element_sets_match({"CO2": 1}, {"C", "O"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of O2
check_element_sets_match({"He": 1, "N2": 1}, {"He", "N"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of O2
check_element_sets_match({"CO2": 2, "CaCO3": 3}, {"Ca", "C", "O"})

# Check find_elements_present correctly predicts the number of moles of elements in 2 moles of O2
check_element_sets_match({"UO2": 1, "HNO3": 1, "H2O": 10}, {"U", "O", "H", "N"})

print("Congratulations! Your code passed all the tests!")