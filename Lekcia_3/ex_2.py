def sum_str(*args):
    res = ' '
    for i in args:
        res += i
    return res

print(sum_str('q', 'e'))
print(sum_str('q', 'e', 'd'))
print(sum_str('1', '2'))