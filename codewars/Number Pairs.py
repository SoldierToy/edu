def get_larger_numbers(a, b):
    new_arr = []

    for i in range(len(a)):
        if a[i] >=  b[i]:
            new_arr.append(a[i])
        elif a[i] < b[i]:
            new_arr.append(b[i])

    return new_arr


print(get_larger_numbers(a=[13, 64, 15, 17, 88], b=[23, 14, 53, 17, 80]))