def replace_char_occurrences(s, curr_char, new_char):
    
    result = s.replace(curr_char, new_char)
    print(f'"{result}"')
    return result


# Test Cases
replace_char_occurrences("Hello", "l", "s")
replace_char_occurrences("World", "W", "A")
replace_char_occurrences("Python", "P", "x")
replace_char_occurrences("Python", "p", "a")