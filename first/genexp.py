# Generator expressions = geneR
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс недоступны извне
# читается слева направо
# для словаря обязательно указать КЛЮЧ: ЗНАЧЕНИЕ
# генератор вернет объект, а не коллекцию
# генератор ленивый, не выполняет действий и не занимает память пока не потребуется
# генератор проверяет источник при создании!!!
# генератор одноразовый, если исчерпан то бросает StopIteration
# цикл for перехватывает StopIteration
# используйте генэксп вместо компс, кроме случаев когда нужна длина Len или индексы

from time import sleep


def source():
    print('!!!')
    sleep(2)
    return [1, 2, 3]


def kv(x):
    sleep(2)
    return x * x


def array():
    print('!!!')
    sleep(2)
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


gen = (kv(e) for e in range(100_000_000_000_000))
print(next(gen))
print(next(gen))
gen = (kv(e) for e in array())
print(next(gen))
print(next(gen))
gen = [kv(e) for e in range(100_000_000_000_000)]  # присходит очень медленно
print(next(gen))
print(next(gen))
