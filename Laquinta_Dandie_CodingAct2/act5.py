def problem_5(lst):
    deduplicated = []
    for item in lst:
        if item not in deduplicated:
            deduplicated.append(item)
    print(deduplicated)

# Test Cases
problem_5([1, 1, 2, 3, 4, 4])
problem_5(["a", "a", "b", "a"])
problem_5([1, 2, 3])
problem_5([])