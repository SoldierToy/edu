def pattern(n: int):
    str_ = ''
    for i in range(1, n + 1):
        cnt = '*' * (i - 1)
        if i == 1:
            str_ += '1\n'
        if i > 1:
            str_ += f'1{cnt}{i}\n'
    return str_.rstrip('\n')


print(pattern(3))
