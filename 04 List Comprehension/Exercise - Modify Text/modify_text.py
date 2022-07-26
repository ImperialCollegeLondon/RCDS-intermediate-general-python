def disemvowel(string_in):
    string_list = [char for char in string_in if not char.lower() in ["a", "e", "i", "o", "u"]]

    return("".join(string_list))

