from compound_summaries import find_elements_present
from inputs_outputs import get_compounds_from_file

def check_fissile(compounds):
    elements = find_elements_present(compounds)

    for fissile_element in ("U", "Pu", "Th"):
        if fissile_element in elements:
            return(True)
    else:
        return(False)

def check_poisons(compounds):
    for compound in compounds:
        if compound in ("HCN", "Cl2"):
            return(True)
    else:
        return(False)

def order_approver(path, *checker_functions, authorisation_code=None, **kwargs):
    if kwargs:
        raise ValueError("Unknown keyword arguments provided")

    compounds = get_compounds_from_file(path)

    if authorisation_code == "UUDDLRLRBAS" or authorisation_code == "rosebud":
        print("Authorisation code accepted")
        return(True)
    elif authorisation_code is not None:
        raise ValueError("Invalid authorisation code")

    for checker_function in checker_functions:
        if checker_function(compounds):
            approved = False
            print("One or more checks failed and the order is rejected!")
            break
    else:
        approved = True
        print("All checks passed, the order is approved!")

    print("Order checked")
    return(approved)

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons)

checker_functions = (check_fissile, check_poisons)

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", *checker_functions, authorisation_code="rosebud")

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons, authorisation_code="wrong")

# order_approver("10 Function Arguments\Exercise - Authorisation\\batch.txt", check_fissile, check_poisons, code="rosebud")
