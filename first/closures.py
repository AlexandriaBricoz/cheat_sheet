# Closures замыкания
# это внутренняя функция, которая возвращается из внешней и использует переменные из внешнего скоупа
# каждое замыкание хранит свое состояние, они не пересекаются
# хранит состяние(данные), предоставляет интерфейс для работы с ними,"скрывает" данные, помогает избегать global

def new():
    array = []

    def inner(x: int) -> list:
        array.append(x)
        return array

    return inner


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def pow_(degree: int) -> int:
    def inner(velue: int) -> int:
        return velue ** degree

    return inner


def average(degree):
    return lambda value: value ** degree


if __name__ == '__main__':
    boys = new()
    girls = new()
    print(boys(1))  # не паресекаются, как отдельные объекты
    print(boys(2))
    print(boys(3))
    print(girls(4))
    print(girls(5))
    print(girls(6))
    count = counter()
    print(count())
    print(count())
    power = pow_(3)
    print(power(10))
    aver = average(3)
    print(aver(3))
