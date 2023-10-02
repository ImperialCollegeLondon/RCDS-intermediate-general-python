def count_atoms(formula, element):
    if len(element) == 2:
        i_element = formula.find(element)
        if i_element < 0:
            return (0)
        elif i_element + 2 == len(formula):
            return (1)
        elif formula[i_element + 2].isalpha():
            return (1)
        else:
            return (int(formula[i_element + 2]))
    elif len(element) == 1:
        for i_char in range(len(formula)):
            if formula[i_char] == element:
                if i_char == len(formula) - 1:
                    return (1)
                try:
                    return (int(formula[i_char + 1]))
                except ValueError:
                    if formula[i_char + 1].isupper():
                        return (1)
        return (0)
