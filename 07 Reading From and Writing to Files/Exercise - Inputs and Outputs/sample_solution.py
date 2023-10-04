# Import count_atoms_in_compounds from the compound_summaries module
# We'll use this to count the number of atoms of each element in each compound
from compound_summaries import count_atoms_in_compounds


# This function will read in a file containing a specification of the number of moles of different compounds
# It will return a dictionary containing the compounds and the corresponding number of moles
def get_compounds_from_file(path):
    # Receive a path to the file to be read as an input

    with open(path) as f:
        # The file is opened and stored in the variable f for the duration of the with block
        # The with block ensures that the file is closed after the block is executed
        # The readlines method reads the file line by line and returns a list of strings
        # This is stored in lines
        lines = f.readlines()
    # The files is closed when the with block ends

    # Create a dictionary to store the compounds and the corresponding number of moles using a dictionary comprehension
    # line will represent each line from the file in turn
    # line.split will return a list of strings in the line
    # line[0] will be the name of the compound
    # line[1] will be the number of moles of the compound
    # Use the name for the key and the number of moles converted to a float for the value
    compounds = {line.split()[0]: float(line.split()[1]) for line in lines}

    # Once we've constructed the dictionary, return it
    return (compounds)


# This function will read in a file containing a specification of the number of moles of different compounds
# It will return a dictionary containing the elements and the corresponding number of moles of atoms
def get_atoms_from_file(path):
    # Receive a path to the file to be read as an input

    # Use the get_compounds_from_file function to read in the compounds and the corresponding number of moles
    compounds = get_compounds_from_file(path)

    # Use the count_atoms_in_compounds function to count the number of number of each atom in the compounds represented in the file
    # Provide compounds as an input to the function
    atom_totals = count_atoms_in_compounds(compounds)

    # Return the dictionary of elements and the corresponding number of moles of atoms
    return (atom_totals)


# This function will read a file containing a specification of the number of moles of different compounds
# It will write a file containing a specification of the number of moles of atoms of different elements
def write_atoms_from_file(input_path, output_path):
    # Input path is the path to the file to be read
    # Output path is the path to the file to be written

    # Get the dictionary of elements and the corresponding number of moles of atoms
    # Use get_atoms_from_file which uses get_compounds_from_file and count_atoms_in_compounds
    atom_totals = get_atoms_from_file(input_path)

    with open(output_path, "w") as f:
        # Open the file to be written
        # The with block ensures that the file is closed after the block is executed
        # The "w" argument specifies that the file should be opened for writing

        # Loop over each atom in the dictionary and write a line for each
        for atom in atom_totals:
            # Use f.write() for each line
            # Use the format method to format the string
            # The line will be of the form "atom number_of_atoms"
            # The "\n" creates a line break
            f.write("{} {}\n".format(atom, atom_totals[atom]))
