# global может создать переменную, nonlocal так делать не может
# нужно быть мегеаккуратно с global и nonlocal
# global и nonlocal использовать только для изменения значений

counter = 20
value = 1
value2 = 8
i = 'привет'
number = 100


def counter_n(namber):
    return namber + 1  # лучше делать так для наглядности и вообще топ


def func():
    print(i)
    value = 4
    global counter
    counter += 1  # нельзя изменять глобальное значение если не написано global counter
    print(counter)
    value2 = 32

    def inner():
        global value
        print(value)  # печатает значение из глобального скоупа
        nonlocal value2  # ищет значение не в локальном скоупе, а во внешний, но не в глобальном
        print(value2)
        global counter  # ещё раз следует писать во внутреннем скоупе
        counter += 1

    inner()
    print(counter)


if __name__ == '__main__':
    number = counter_n(number)  # лучше сделать так, потому что так потом проще разобраться
    print(number)
    func()
