def remove_char_at_index(s, n):
    if 0 <= n < len(s):
        result = s[:n] + s[n + 1 :]
    else:
        result = s

    print(f'"{result}"')
    return result


remove_char_at_index("Hello", 1)
remove_char_at_index("World", 3)
remove_char_at_index("Dog", 15)
remove_char_at_index("", 2)