from collections import Counter


def count_and_list_repeated_chars(s):
    counts = Counter(s)

    repeated = sorted([char for char, count in counts.items() if count > 1])

    if repeated:
        print(len(repeated))
        print(" ".join(repeated))
    else:
        print(0)
        print("None")


print("--- 'Hello' ---")
count_and_list_repeated_chars("Hello")

print("\n--- 'Corporation' ---")
count_and_list_repeated_chars("Corporation")

print("\n--- 'Python' ---")
count_and_list_repeated_chars("Python")