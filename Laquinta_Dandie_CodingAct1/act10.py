def sort_chars_in_words(s):
    words = s.lower().split(" ")

    
    sorted_words = ["".join(sorted(word)) for word in words]

    result = " ".join(sorted_words)

    print(f'"{result}"')
    return result


sort_chars_in_words("Hello World")
sort_chars_in_words("Wonderful World")