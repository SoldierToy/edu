def filter_homogenous(arrays):
    new_arr = []

    for arr in arrays:
        if arr:
            type_arr = type(arr[0])
        else:
            continue

        for j in arr:
            flag = True
            if not isinstance(j, type_arr):
                flag = False
                break

        if flag:
            new_arr.append(arr)

    return new_arr


filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])
