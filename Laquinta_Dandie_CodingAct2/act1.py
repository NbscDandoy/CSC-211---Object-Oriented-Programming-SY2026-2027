def problem_1(set1, set2):
    intersection = set1 & set2
    print(intersection)

problem_1({1, 2, 3}, {4, 5, 6})
problem_1({1, 2, 3}, {3, 4, 5})
problem_1({1, 2, 3, 4}, {3, 4, 5, 6})
problem_1({1, 2, 3, 4}, {1, 2, 3, 4})