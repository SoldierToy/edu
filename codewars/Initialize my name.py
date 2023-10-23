def initialize_names(name):
    new_str = ''
    lst = name.split(' ')
    new_str += lst[0] + " "

    for i in lst[1: -1]:
        new_str += i[0] + ". "

    if len(lst) > 1:
        new_str += lst[-1]

    print(new_str)
    return new_str.rstrip(' ')


initialize_names('Alice Betty Catherine Davis')
