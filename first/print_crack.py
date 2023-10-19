_print = print


def print(*args, **kwargs):
    kwargs['end'] = ''
    _print(*args, **kwargs)


print(1, end='')
print(1)
print(1)
