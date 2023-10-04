def count_atoms(formula, element):
    # Find how many atoms of element are in formula

    # We will take two different paths of logic, dependent on whether the element is 1 or 2 characters long
    if len(element) == 2:
        # If the element is two characters long, we can use the find method to find the index of the first character of it in the formula
        # This is guaranteed to not return any false positives
        i_element = formula.find(element)
        if i_element < 0:
            # If i_element is negative, the element was not found in the formula
            # This means there are no atoms of the element in the formula so return 0
            return (0)
        elif i_element + 2 == len(formula):
            # Next check if the element is at the end of the formula
            # If it is, there is only one atom of it in the formula, so return 1
            # We needed to check this before checking the next character to avoid an IndexError being raised
            return (1)
        # We now know that the element is not at the end of the formula, so we can check the next character
        elif formula[i_element + 2].isalpha():
            # If the next character is a letter, it is the start of another element
            # This means there is only one atom of the element in the formula, so return 1            
            return (1)
        else:
            # If the next character is not a letter, it must be a number
            # Convert it to an integer and return it
            return (int(formula[i_element + 2]))
    elif len(element) == 1:
        # If len is 1, find won't work reliably
        # For instance, if we are looking for "C" in CuCO3, find will return 0, even though this is actually the first character of Cu
        # Instead, loop over the formula and check each character to see if it matches the element
        for i_char in range(len(formula)):
            if formula[i_char] == element:
                # We should first check if the character is the last in the formula
                # This is because we will be checking the next character in the formula, so we need to make sure it exists
                if i_char == len(formula) - 1:
                    # If it is the last character, there is only one atom of the element in the formula, so return 1
                    return (1)
                try:
                    # Using a try-except block, we can check if the next character is a number
                    # If it is, convert it to an integer and return it
                    return (int(formula[i_char + 1]))
                except ValueError:
                    # If a ValueError is raised, the next character is not a number and must be a letter
                    if formula[i_char + 1].isupper():
                        # If the following character is uppercase, it is the start of another element
                        # This means there is only one atom of the element we're looking for in the formula, so return 1
                        return (1)
                    # If the following character is lowercase, it means the character we found is actually the start of an element with two characters
                    # For instance, we might have being looking for "N" and found the "N" in "Na"
                    # In this case, don't return anything and allow the loop to move on to the next character
        # If we reach this point, the loop has finished and the element was not found in the formula, so return 0
        return (0)
