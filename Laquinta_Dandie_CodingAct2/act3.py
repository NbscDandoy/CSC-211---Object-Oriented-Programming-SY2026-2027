def problem_3(lst, elem_to_remove):
    if not lst:
        print('"Empty List"')
    elif elem_to_remove not in lst:
        print('"Not Found"')
    else:
        new_list = [x for x in lst if x != elem_to_remove]
        print(new_list)

problem_3([1, 2, 3, 4], 2)
problem_3([3, 3, 2, 1], 3)
problem_3(["a", "b", "c", "b"], "b")
problem_3([3, 4, 5, 6], 7)
problem_3([], 0)