# Магические методы = dunder методы, методы которые начинаются и заканчиваются __
# init по умолчанию не ждёт аргументов
# repr - для программистов, возвращает строку, по которой видно (и можно воссоздать) состояние объекта
# str - для людей, возвращает строку
# если не реализованы репе и стр, то будет возвращен адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# если методы сравнения не реализованы то падает ошибка
# contains для реализации проверки IN
# bool для самодельных объектов всегда вернет True, для изменения поведения нужно написать __bool__
# len вернет ошибку если не переопределить метод __len__
# чтобы объект стал вызываемым (callable) нужно реализовать __call__, иначе ошибка
# __iter__ возвращает объект итератор, тот кто реализует итер - Итерабл
# __next__ должен вернуть следующий объект из контейнера, ктоего реализует = Итератор
# __getitem__ нужен для функционала [] (аналог списка и словаря), __setitem__ для присвоения через [], если не реализовать =ошибка
# если в объекте не реализован __iter__ то для цикла фор будет использован __getitem__ там ожидается падение InderError
class Banknote:
    def __init__(self,value):               # инициализация
        self.value = value

    def __repr__(self):                     # вывод для программистов
        return f'Banknot({self.value})'

    def __str__(self):                      # вывод для пользователей
        return f'Банкнота размером {self.value}'

    def __lt__(self, other):                # меньше
        if isinstance(other,Banknote):
            return self.value<other.value

    def __le__(self, other):                # меньше или равно
        if isinstance(other,Banknote):
            return self.value<=other.value

    def __gt__(self, other):                # больше
        if isinstance(other,Banknote):
            return self.value>other.value

    def __ge__(self, other):                # больше или равно
        if isinstance(other,Banknote):
            return self.value>=other.value

    def __eq__(self, other):                # равно
        if isinstance(other,Banknote):
            return self.value==other.value
class Iterator:
    def __init__(self, items):
        self.index = 0
        self.items = items

    def __next__(self):
        if 0 <= self.index < len(self.items):
            value = self.items[self.index]
            self.index += 1
            return value
        self.index = 0
        raise StopIteration


class Wallet():
    def __init__(self, *item: Banknote):     # инициализация
        self.items = []
        self.items.extend(item)
        self.index = 0

    def __repr__(self):                     # вывод для программистов
        return f'Wallet({self.items})'

    def __contains__(self, item):           # проверка на наличие в листе
        return item in self.items

    def append(self, item):                 # добавление купюры
        if isinstance(item, Banknote):      # проверка на нужный тип
            self.items.append(item)
        else:
            raise ValueError('Type is not suitable')

    def __bool__(self):                     # для проверки, что не пустой объект (if self:)
        return len(self.items)>0

    def __len__(self):                      # для вычисления длины
        return len(self.items)

    def __call__(self, *args, **kwargs):    # для вызова суммы (self())
        return sum(e.value for e in self.items)

    def __getitem__(self, item):            # вывод по индексу
        if item < 0 or item > len(self.items):
            raise IndexError
        return self.items[item]

    def __setitem__(self, key, value):      # редактирование по индексу
        if key<0 or key>len(self.items):
            raise IndexError
        self.items[key] = value

    def __iter__(self):
        return Iterator(self.items)

if __name__ == '__main__':
    banknote = Banknote(10)
    hundred = Banknote(100)
    print(repr(banknote))
    print(banknote == hundred)
    print(banknote.value > hundred.value)
    print(banknote > hundred)
    wallet = Wallet(hundred,banknote)
    wallet.append(banknote)
    print(wallet)
    wallet[1]= Banknote(80)
    print(len(wallet))
    print(hundred in wallet)
    print(wallet[1])
    if wallet:
        print(12)
    print(wallet())
    for money in wallet:
        print(money)
    for money in wallet:
        print(money)
