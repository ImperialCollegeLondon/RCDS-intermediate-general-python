from atom_counter import count_atoms
from elements import element_symbols


def count_atoms_in_compounds(compound_moles):
    atom_totals = {}
    for compound_formula in compound_moles:
        for element in element_symbols:
            n_atoms = count_atoms(compound_formula, element)
            if (n_atoms):
                try:
                    atom_totals[element] += n_atoms * compound_moles[compound_formula]
                except KeyError:
                    atom_totals[element] = n_atoms * compound_moles[compound_formula]
    return(atom_totals)

def find_elements_present(compound_moles):
    elements_present = set()

    for compound_formula in compound_moles:
        for element in element_symbols:
            n_atoms = count_atoms(compound_formula, element)
            if (n_atoms):
                elements_present.add(element)
    return(elements_present)
