from compound_summaries import count_atoms_in_compounds

def get_compounds_from_file(path):
    with open(path) as f:
        lines = f.readlines()

    compounds = {line.split()[0]: float(line.split()[1]) for line in lines}

    return(compounds)

def get_atoms_from_file(path):
    compounds = get_compounds_from_file(path)

    atom_totals = count_atoms_in_compounds(compounds)

    return(atom_totals)

def write_atoms_from_file(input_path, output_path):
    atom_totals = get_atoms_from_file(input_path)

    with open(output_path, "w") as f:
        for atom in atom_totals:
            f.write("{} {}\n".format(atom, atom_totals[atom]))
