from compound_summaries import find_elements_present
from inputs_outputs import get_compounds_from_file


# This function is the same as it was in Section 9
def check_fissile(compounds):
    elements = find_elements_present(compounds)

    for fissile_element in ("U", "Pu", "Th"):
        if fissile_element in elements:
            return (True)
    else:
        return (False)


# This function is the same as it was in Section 9
def check_poisons(compounds):
    for compound in compounds:
        if compound in ("HCN", "Cl2"):
            return (True)
    else:
        return (False)


# This function receives a path to a file containing a list of compounds and their amounts
# It receives a number of checker functions and, potentially an authorisation code
# Based on these it decides if the order should be approved or not
def order_approver(path, *checker_functions, authorisation_code=None, **kwargs):
    # path is the path to the file containing the list of compounds and their amounts
    # checker_functions is a tuple of functions that check the compounds for specific properties. It will receive any positional arguments (after the path) passed to the function
    # authorisation_code is the authorisation code that may override the results of the checks. By default, it is None to indicated one has not been provided
    # kwargs is a dictionary of keyword arguments passed to the function. It will receive any keyword arguments passed to the function that do not match the names of named parameters in the function definition

    # We don't expect this function to receive any keyword arguments that don't go into named parameters, so raise an error if any are provided
    if kwargs:
        raise ValueError("Unknown keyword arguments provided")

    # Get the compounds from the file
    # We could do this after checking the authorisation code, but doing it first means we check the validity of the order even if the authorisation code is valid
    compounds = get_compounds_from_file(path)

    # Check the authorisation code
    if authorisation_code == "UUDDLRLRBAS" or authorisation_code == "rosebud":
        # If it's one of the correct codes, print an acceptance message and return True - the order is approved
        print("Authorisation code accepted")
        return (True)
    elif authorisation_code is not None:
        # If an invalid code is provided, print a rejection message and return False - the order is rejected
        raise ValueError("Invalid authorisation code")
    # If no authorisation code is provided, continue with the checks

    # Perform the checks
    for checker_function in checker_functions:
        # checker_function will be each checker function in turn
        if checker_function(compounds):
            # If the checker function returns True, print a rejection message and return False - the order is rejected
            approved = False
            print("One or more checks failed and the order is rejected!")
            # We don't need to check any more functions, so break out of the loop
            break
    else:
        # The else block is executed if no checks fail and the loop completes without breaking - the order is approved
        approved = True
        print("All checks passed, the order is approved!")

    # Print a message to indicate the order has been checked and return whether it was approved or not
    print("Order checked")
    return (approved)


# Below are some sample calls to the function to demonstrate how it works

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons)

checker_functions = (check_fissile, check_poisons)

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", *checker_functions, authorisation_code="rosebud")

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons, authorisation_code="wrong")

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons, code="rosebud")
