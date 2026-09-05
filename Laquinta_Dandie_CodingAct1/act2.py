def filter_even_indices(s):
    result = s[1::2] if len(s) > 1 else s
    print(f'"{result}"')
    return result


filter_even_indices("Coding")
filter_even_indices("Pizza")
filter_even_indices("Python")
filter_even_indices("A")
filter_even_indices("")