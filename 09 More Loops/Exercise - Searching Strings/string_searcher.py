def string_comparer(string_1, string_2):
    result = set()

    string_1 = string_1.lower()
    string_2 = string_2.lower()

    for char_1, char_2 in zip(string_1, string_2):
        if char_1 == char_2:
            result.add(char_1)

    return(result)

def character_finder(string, character):
    result = []

    string = string.lower()
    character = character.lower()

    for index_in_string, character_in_string in enumerate(string):
        if character == character_in_string:
            result.append(index_in_string)

    return(result)