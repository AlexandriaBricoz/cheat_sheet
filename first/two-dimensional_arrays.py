# Инициализация массива -- метод 1
...
x = [[1,2,3,4]] * 3
print(x)
# обращение к элементу
print(x[2][3])

# Инициализация массива -- метод 2
...
y = [[1,2,3,4] for _ in range(3)]

print(y)
'''
    Кажется, что оба подхода обеспечивают один и тот же результат, но есть важное различие. 
Второй метод, как и ожидалось, создаёт массив из трёх элементов, 
каждый из которых является независимым четырехэлементным массивом. 
В первом же методе все члены массива указывают на один и тот же объект.
Это может привести к наиболее вероятному непредвиденному и нежелательному поведению, как показано ниже.
'''