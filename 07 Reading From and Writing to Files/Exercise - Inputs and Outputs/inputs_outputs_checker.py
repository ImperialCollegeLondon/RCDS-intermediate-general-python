from types import FunctionType
import os

try:
    from inputs_outputs import get_compounds_from_file
except ModuleNotFoundError:
    assert False, "inputs_outputs_checker.py tried to import from the file compound_summaries.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "inputs_outputs_checker.py tried to import the function 'get_compounds_from_file' from the file compound_summaries.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check get_compounds_from_file is a function
assert type(get_compounds_from_file) == FunctionType, "get_compounds_from_file is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

sample_directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_orders")
print(sample_directory_path)

assert os.path.isdir(sample_directory_path), "The directory sample_orders does not exist to contain the input files for this exercise"

def check_compounds_from_file(path, reference_dictionary):
    try:
        student_dictionary = get_compounds_from_file(path)
    except FileNotFoundError:
        print("get_compounds_from_file was called to construct a dictionary of compounds from the file {}. However, the following FileNotFoundError was raised, suggesting the file is not present in the relevant directory. Check it's present and try again.".format(path))
        raise
    except:
        print("get_compounds_from_file was called to construct a dictionary of compounds from the file {}. However, the following exception was raised. Check your programs logic.".format(path))
        raise

    assert type(student_dictionary) == dict, "get_compounds_from_file was called to construct a dictionary of compounds from the file {}. However, the value returned was not a dictionary as it should be. Check your code always returns a value and that this is always a dictionary.".format(path)

    assert student_dictionary == reference_dictionary, "get_compounds_from_file was called to construct a dictionary of compounds from the file {}. However, the value returned was {}, not {} as it should be. The order of the entries doesn't matter, but they should match. Values may be either ints or floats. Check the logic of your code when this order is processed.".format(path, student_dictionary, reference_dictionary)

# Check an empty dictionary is returned from an empty input file
check_compounds_from_file(os.path.join(sample_directory_path, "order_empty.txt"), {})

# Check the correct dictionary is returned from order1.txt
check_compounds_from_file(os.path.join(sample_directory_path, "order_1.txt"), {"CO2": 1})

# Check the correct dictionary is returned from order1.txt
check_compounds_from_file(os.path.join(sample_directory_path, "order_2.txt"), {"Ne": 1, "NaCl": 3.5})

#==============================================================================================================================================

try:
    from inputs_outputs import get_atoms_from_file
except ModuleNotFoundError:
    assert False, "inputs_outputs_checker.py tried to import from the file compound_summaries.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "inputs_outputs_checker.py tried to import the function 'get_atoms_from_file' from the file compound_summaries.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check get_atoms_from_file is a function
assert type(get_atoms_from_file) == FunctionType, "get_atoms_from_file is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

# Check get_atoms_from_file in compounds exists
assert "get_atoms_from_file" in locals() or "get_atoms_from_file" in globals(), "There is no variable/function defined named get_atoms_from_file. Make sure you haven't made any spelling mistakes"

# Check get_atoms_from_file is a function
assert type(get_atoms_from_file) == FunctionType, "get_atoms_from_file is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def check_atoms_from_file(path, reference_dictionary):
    try:
        student_dictionary = get_atoms_from_file(path)
    except FileNotFoundError:
        print("get_atoms_from_file was called to construct a dictionary of atoms from the file {}. However, the following FileNotFoundError was raised, suggesting the file is not present in the relevant directory. Check it's present and try again.".format(path))
        raise
    except:
        print("get_atoms_from_file was called to construct a dictionary of atoms from the file {}. However, the following exception was raised. Check your programs logic.".format(path))
        raise

    assert type(student_dictionary) == dict, "get_atoms_from_file was called to construct a dictionary of atoms from the file {}. However, the value returned was not a dictionary as it should be. Check your code always returns a value and that this is always a dictionary.".format(path)

    assert student_dictionary == reference_dictionary, "get_atoms_from_file was called to construct a dictionary of atoms from the file {}. However, the value returned was {}, not {} as it should be. The order of the entries doesn't matter, but they should match. Values may be either ints or floats. Check the logic of your code when this order is processed.".format(path, student_dictionary, reference_dictionary)

# Check an empty dictionary is returned from an empty input file
check_atoms_from_file(os.path.join(sample_directory_path, "order_empty.txt"), {})

# Check the correct dictionary is returned from order1.txt
check_atoms_from_file(os.path.join(sample_directory_path, "order_1.txt"), {"C":1, "O": 2})

# Check the correct dictionary is returned from order1.txt
check_atoms_from_file(os.path.join(sample_directory_path, "order_2.txt"), {"Ne": 1, "Na": 3.5, "Cl": 3.5})

#==============================================================================================================================================

try:
    from inputs_outputs import write_atoms_from_file
except ModuleNotFoundError:
    assert False, "inputs_outputs_checker.py tried to import from the file compound_summaries.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "inputs_outputs_checker.py tried to import the function 'write_atoms_from_file' from the file compound_summaries.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check write_atoms_from_file is a function
assert type(write_atoms_from_file) == FunctionType, "write_atoms_from_file is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def check_atoms_in_file(input_path, output_path, reference_dictionary):
    try:
        write_atoms_from_file(input_path, output_path)
    except FileNotFoundError:
        print("write_atoms_from_file was called to write a file containing the number of atoms in compounds from the file {}. However, the following FileNotFoundError was raised. This might suggest that the input file is not present in the relevant directory, or that the open statement you used to create the output file did not use the appropriate argument to create a file that doesn't exist. Check the input file is present and the logic of your program and try again.".format(input_path))
        raise
    except:
        print("write_atoms_from_file was called to write a file containing the number of atoms in compounds from the file {}. However, the following exception was raised. Check your programs logic.".format(input_path))
        raise

    student_file = open(output_path)

    student_lines = student_file.readlines()

    student_dictionary = {}

    for i_line, line in enumerate(student_lines):
        if line.strip() == "":
            continue
        
        words = line.split()

        format_error = "write_atoms_from_file was called and asked to read the input file {} (which contains the number of moles of different compounds) and calculate the number of moles of different types of atoms present and write the result to {}. Line {} (with the first line being line 1) of the output file {} was '{}' when it should have been a single atomic symbol and a number of atoms separated by a space (e.g. 'Au 1')".format(input_path, output_path, i_line + 1, output_path, line)

        assert len(words) == 2, format_error

        assert not words[0] in student_dictionary, "write_atoms_from_file was called and asked to read the input file {} (which contains the number of moles of different compounds) and calculate the number of moles of different types of atoms present and write the result to {}. This file contained two entries for the atomic symbol {}, when it should only contain one.".format(input_path, output_path, words[0])

        try:
            student_dictionary[words[0]] = float(words[1])
        except ValueError:
            assert False, format_error

    assert student_dictionary == reference_dictionary, "write_atoms_from_file was called and asked to read the input file {} (which contains the number of moles of different compounds) and calculate the number of moles of different types of atoms present and write the result to {}. This file contained the atom numbers {} when it should have contained {}. Order does not matter, but the elemental symbols and the associated number of moles should be the same.".format(input_path, output_path, student_dictionary, reference_dictionary)

# Check an empty file is returned from an empty input file
check_atoms_in_file(os.path.join(sample_directory_path, "order_empty.txt"), os.path.join(sample_directory_path, "order_empty_out.txt"), {})

# Check an empty file is returned from from order1.txt
check_atoms_in_file(os.path.join(sample_directory_path, "order_1.txt"), os.path.join(sample_directory_path, "order_1_out.txt"), {"C": 1, "O": 2})

# Check an empty file is returned from from order2.txt
check_atoms_in_file(os.path.join(sample_directory_path, "order_2.txt"), os.path.join(sample_directory_path, "order_2_out.txt"), {"Ne": 1, "Na": 3.5, "Cl": 3.5})

print("Congratulations - you code passed all the tests.")

