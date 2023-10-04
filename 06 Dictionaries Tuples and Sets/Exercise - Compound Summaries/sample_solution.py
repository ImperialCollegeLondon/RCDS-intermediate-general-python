# Import the count_atoms function you wrote before
from atom_counter import count_atoms
# Import the element_symbols tuple which contains the symbols of all the elements
from elements import element_symbols


def count_atoms_in_compounds(compound_moles):
    # Receives a dictionary of compound formulas and the number of moles of these compounds
    # The key is the formula and the value is the number of moles

    # Create a dictionary to store the total number of atoms of each element
    atom_totals = {}

    # Loop over the compound formulas
    # This will take the keys from the dictionary compound_moles, i.e. the compound formulas
    for compound_formula in compound_moles:
        # Loop over all elements in the supplied tuple
        for element in element_symbols:
            # Find the number of atoms of the current element in the current compound
            n_atoms = count_atoms(compound_formula, element)
            # Use the truthiness of this value to determine if there are any atoms of this element in the compound
            # If n_atoms is 0, this is falsy and the if-block will not be executed
            if n_atoms:
                # If n_atoms is non-zero (truthy), add the number of atoms to the total for this element
                # The number of moles of this element is equal to the number of moles of the compound multiplied by the number of atoms of this element in the compound
                # atom_totals[element] may already exist from a previous compound
                # We can use the try-except block to handle this, which is more Pythonic that checking in advance
                try:
                    # Try to add the number of moles to the existing total for this element
                    atom_totals[element] += n_atoms * compound_moles[compound_formula]
                except KeyError:
                    # If the element is not already in the dictionary, a KeyError will have been raised
                    # Add te current element and the number of moles to the dictionary
                    atom_totals[element] = n_atoms * compound_moles[compound_formula]
    # When we have looped over all compounds, return the dictionary of total atoms
    return (atom_totals)


def find_elements_present(compound_moles):
    # Receives a dictionary of compound formulas and the number of moles of these compounds
    # The key is the formula and the value is the number of moles

    # We only want to know which elements are present in the compounds
    # We don't care how many atoms of each element there are so we can use a set
    # Create an empty set to store the elements present
    elements_present = set()

    # Loop over the compound formulas from the keys of compound_moles
    for compound_formula in compound_moles:
        # Loop over all elements in the supplied tuple
        for element in element_symbols:
            # Find the number of atoms of the current element in the current compound
            n_atoms = count_atoms(compound_formula, element)
            # Use the truthiness of this value to determine if there are any atoms of this element in the compound
            if n_atoms:
                # If n_atoms is non-zero (truthy), add the element to the set
                # If the element is not already in the set, it will be added
                # If the element is already in the set, it will not be added again
                elements_present.add(element)
            # If the element is not present in the compound, the if-block will not be executed
            # The code will continue to the next element in the for-loop

    # When we have looped over all compounds, return the set of elements present
    return (elements_present)
