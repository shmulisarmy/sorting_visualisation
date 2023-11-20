def sort(nums_list):
    less_than, more_than = [], []
    pivit = nums_list[len(nums_list)//2]
    for i in range(len(nums_list)):
        if i == len(nums_list)//2:
            continue
        if nums_list[i] < pivit:
            less_than.append(nums_list[i])
        else:
            more_than.append(nums_list[i])

    rt =  ''.join((sort(less_than) if len(less_than) > 1 else str(less_than[0]) if len(less_than) == 1 else '', str(pivit), sort(more_than) if len(more_than) > 1 else str(more_than[0]) if len(more_than) == 1 else ''))
    return rt

numbers = [1, 5, 7, 3, 9, 6, 5, 9, 2]

print(sort(numbers))