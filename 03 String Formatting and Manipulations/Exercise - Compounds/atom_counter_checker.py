from types import FunctionType

# Import the function and give feedback if it fails
try:
    from atom_counter import count_atoms
except ModuleNotFoundError:
    assert False, "atom_count_checker.py tried to import from the file atom_counter.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "atom_count_checker.py tried to import the function 'count_atoms' from the file atom_counter.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check count_atoms exists
assert "count_atoms" in locals() or "count_atoms" in globals(), "There is no variable/function defined named count_atoms. Make sure you haven't made any spelling mistakes"

# Check count_atoms is a function
assert type(count_atoms) == FunctionType, "count_atoms is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

# Check 0 is returned when Si is searched for in H2O
Si_H2O = count_atoms("H2O", "Si")
assert Si_H2O == 0, "When looking for the number of atoms of Si in H2, {} was returned instead of 0. Check your logic.".format(Si_H2O)

# Check 1 is returned when Cl is searched for in NaCl
try:
    Cl_NaCl = count_atoms("NaCl", "Cl")
except IndexError:
    assert False, "When looking for the number of atoms of Cl in NaCl, you referenced outside of the bounds of a string, probably formula. Check your logic when the element symbol is at the end of formula."

assert Cl_NaCl == 1, "When looking for the number of atoms of Cl in NaCl, {} was returned instead of 1. Check your logic.".format(Cl_NaCl)

# Check 1 is returned when Ca is searched for in CaCO3
Ca_CaCO3 = count_atoms("CaCO3", "Ca")
assert Ca_CaCO3 == 1, "When looking for the number of atoms of Ca in CaCO3, {} was returned instead of 1. Check your logic.".format(Ca_CaCO3)

# Check 2 is returned when Al is searched for in Al2O3
Al_Al2O3 = count_atoms("Al2O3", "Al")
assert Al_Al2O3 == 2, "When looking for the number of atoms of Al in Al2O3, {} was returned instead of 2. Check your logic.".format(Al_Al2O3)

# Check 1 is returned when Al is searched for in Al2O3
Br_NaBrO3 = count_atoms("NaBrO3", "Br")
assert Br_NaBrO3 == 1, "When looking for the number of atoms of Br in NaBrO3, {} was returned instead of 1. Check your logic.".format(Br_NaBrO3)

# Check 1 is returned when O is searched for in CO
try:
    O_CO = count_atoms("CO", "O")
except IndexError:
    assert False, "When looking for the number of atoms of O in CO, you referenced outside of the bounds of a string, probably formula. Check your logic when the element symbol is at the end of formula."
assert O_CO == 1, "When looking for the number of atoms of O in CO, {} was returned instead of 1. Check your logic.".format(O_CO)

# Check 2 is returned when F is searched for in FeF2
F_FeF2 = count_atoms("FeF2", "F")
assert F_FeF2 == 2, "When looking for the number of atoms of F in FeF2, {} was returned instead of 2. Check your logic.".format(F_FeF2)

# Check 1 is returned when N is searched for in NO2
N_NO2 = count_atoms("NO2", "N")
assert N_NO2 == 1, "When looking for the number of atoms of N in NO2, {} was returned instead of 1. Check your logic.".format(N_NO2)

# Check 0 is returned when S is searched for in SiO2
S_SiO2 = count_atoms("SiO2", "S")
assert S_SiO2 == 0, "When looking for the number of atoms of S in SiO2, {} was returned instead of 0. Check your logic.".format(S_SiO2)

# Check 0 is returned when C is searched for in UO2
C_UO2 = count_atoms("UO2", "C")
assert C_UO2 == 0, "When looking for the number of atoms of C in UO2, {} was returned instead of 0. Check your logic.".format(C_UO2)

# Check 1 is returned when C is searched for in HCN
C_HCN = count_atoms("HCN", "C")
assert C_HCN == 1, "When looking for the number of atoms of C in HCN, {} was returned instead of 1. Check your logic.".format(C_HCN)

print("Congratulations, all the tests passed!")