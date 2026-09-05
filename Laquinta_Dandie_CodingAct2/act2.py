def problem_2(lst):
    count = sum(1 for x in lst if x > 3)
    print(count)

problem_2([1, -1, 0, 2, 2, 3])
problem_2([1, 2, 3, 4])
problem_2([7, 8, 9, 10])
problem_2([])