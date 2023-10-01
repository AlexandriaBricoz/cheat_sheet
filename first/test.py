def foo(a: str, b: list[int] = []) -> list[int]:
    b.append(a)
    return b

a_list = [1,4]
foo('jku')
foo('nuion')
foo('mkk')
print(a_list)
