# Import the functions find_elements_present and get_compounds_from_file that you've already written
from compound_summaries import find_elements_present
from inputs_outputs import get_compounds_from_file


# This function checks if the order contains any fissile elements
def check_fissile(compounds):
    # Compounds is a dictioanry with the compounds in the order as keys and the corresponding number of moles as values

    # Get the elements present in the order as a set
    elements = find_elements_present(compounds)

    # Loop through the fissile elements
    for fissile_element in ("U", "Pu", "Th"):
        # Check if the current fissile element is present in the set of elements present in the order
        if fissile_element in elements:
            # If the fissile element is present, return True
            return (True)
        # If the fissile element is not present, move on to the next one
    else:
        # The else statement will be triggered if the loop isn't exited through a return statement
        # In this case, none of the fissile elements are present, so return False
        return (False)


# This function checks if the order contains any poisons
def check_poisons(compounds):
    # Compounds is a dictioanry with the compounds in the order as keys and the corresponding number of moles as values

    # We already have the compounds in the order, so we can examine them directly
    for compound in compounds:
        # compound will take its values from the keys of the dictionary compounds
        # This will give us the names of the compounds present in turn
        if compound in ("HCN", "Cl2"):
            # If the current compound is a poison, return True
            return (True)
        # If the current compound is not a poison, move on to the next one
    else:
        # The else statement will be triggered if the loop isn't exited through a return statement
        # In this case, none of the compounds are poisons, so return False
        return (False)


# This function checks if the order violates the conditions of any of the checker functions
def order_approver(path, checker_functions):
    # path is the path to the file containing the order
    # checker_functions is a list of the checker functions to be used

    # Get a dictionary of the compounds in the order and the number of moles of each
    compounds = get_compounds_from_file(path)

    # Loop over each checker function and apply it to the order
    for checker_function in checker_functions:
        # checker_function will take its values from the elements of the list checker_functions
        # This will be a reference to each checker function in turn
        if checker_function(compounds):
            # If the check returns True, its terms were violated, so we shouldn't approve the order
            # Set approved to False and, print an error message and break out of the loop
            approved = False
            print("One or more checks failed and the order is rejected!")
            break
    else:
        # The else statement will be triggered if the loop isn't exited through a break statement
        # In this case, no checks failed, so the order is approved
        # Set approved to True and print a success message
        approved = True
        print("All checks passed, the order is approved!")

    # Print a message that the check has finished
    print("Order checked")
    # Return the value of approved
    return (approved)
