# лямда может использоваться только для замены функций, где есть return
# лямда не работает с цыклами
def f(x):
    return x % 10


print((lambda a, b: a * b)(17, 14))
print((lambda a, b: a if a > b else b)(12, 23))
example = lambda x: x * x
string = lambda: 'Hello'
print(example(7))
print(string())
numbers = [21, 24, 34, 5, 3, 9, 0]
numbers.sort(key=f)  # пример сортировки по кретерию
velues = [2, 4, 353, 43, 32, 4, 5]
velues.sort(key=lambda x: (x * x % 10))
print(numbers)
print(velues)
