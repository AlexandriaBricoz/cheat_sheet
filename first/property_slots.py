# Используем сет/гет, а также property только при наличии логики в получении или установки атрибута
# Возможность установки/получения атрибутов с логикой
# запретить менять атрибут или добавлять новые атрибуты
# __dict__ - это атрибут объектов в питоне, который хранит состояние
# __setattr__ - вызывается при попытке установить атрибут
# __slots__ - создан для уменьшения, занимаемой объектами(при использовании нельзя добавлять атрибуты)

from pympler import asizeof     # для измерения размера в байтах(по умолчанию) просто топ


class Cat:
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property       # это декораторы GETTER
    def name(self):
        return self._name

    @name.setter    # SETTER
    def name(self, value):
        self._name = value

    @property       # GETTER
    def age(self):
        return self._age

    @age.setter    # SETTER
    def age(self, value):
        self._age = value


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):      # тип сетеры для всех аргументов
        self.__dict__[key] = value


if __name__ == '__main__':
    tom = Cat('Tom', 12)
    tom.name = 'Pusy'
    print(tom.name)
    print(asizeof.asizeof(tom))
    tuzik = Dog('Tuzik', 12)
    tom.name = 'Rex'
    print(tom.name)
    print(asizeof.asizeof(tuzik))