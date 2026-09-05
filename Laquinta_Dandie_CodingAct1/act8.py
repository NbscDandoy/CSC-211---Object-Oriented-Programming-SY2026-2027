def reverse_words_and_swap_case(s):
    words = s.split(" ")

    transformed_words = [word[::-1].swapcase() for word in words]

    result = " ".join(transformed_words)

    print(f'"{result}"')
    return result


reverse_words_and_swap_case("Hello World")
reverse_words_and_swap_case("Python is Awesome")