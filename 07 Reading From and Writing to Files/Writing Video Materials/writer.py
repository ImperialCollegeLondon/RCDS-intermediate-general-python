# Import os so we can use the os.path.join function and os.mkdir function
import os

# Construct a path to the file to be written use os.path.join
# This will use the appropriate path separator for the operating system
path = os.path.join("Squares", "numbers.dat")

# Create the directory Squares if it doesn't already exist
try:
    # Attempt to create the directory using os.mkdir
    # If the directory already exists, a FileExistsError will be raised
    os.mkdir("Squares")
except FileExistsError:
    # If the directory already exists, we don't need to do anything
    # We don't need to do anything if this happens, so we can use pass to do nothing
    pass


# Open the file. The argument "w" means that the file will be ready to write to
# A reference to the file is stored in the variable f
with open(path, "w") as f:
    # Loop through the numbers 1 to 10 and write a line for each
    for i in range(1, 11):
        # For each line write the number and its square separated by a comma
        # Use the format method to convert the numbers to strings
        # The \n character is the newline character, which will start a new line
        f.write("{}, {}\n".format(i, i ** 2))
