from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv

# OrderedDict значит упорядоченный словарь
# OrderedDict используется только когда важен порядок или его нужно изменить
# OrderedDict занимает в два раза больше памяти
first = {1:1,2:2,3:3}
second = {2:2,1:1,3:3}
third = {4:4,5:5}

order1 = OrderedDict(first)
order2 = OrderedDict(second)
order3 = OrderedDict(third)

print(first==second)
print(order1 == order2)         # Имеет значение ПОРЯДОК в словаре

print(order1.popitem(last=False))       # last=False значит с начала, так умеет только OrderedDict
order2.move_to_end(1)                   # Метод, который сдвигает в конец по ключу
print(order2)
order2.move_to_end(3,last=False)        # двигает в конец
print(order2)

# ChainMap нужен для логического объединения словарей для поиска, но меняется первый словарь
# не рекомендуется менять словари через ChainMap, правильно менять словари
# ChainMap хранит ссылки на словари, а не копирует их
chain = ChainMap(first,second,third)
print(chain)
chain[1] = 200
print(chain)
print(1 in chain)

# считает количество элементов
# работает с хешированными типами данных(числа, строки, словари)
counter = Counter('vetrverve')
print(counter)
counter.update('scscsxc')
print(counter)
print(counter.most_common(3))   # выводит 3 самые частые буквы или что то другое семое частое, если задать больше чем есть, то выведет всё

# defaultdict нежен для создания словаря со значением по умолчанию, Значение представляется несуществующему ключу
a_dect = defaultdict(int)       # дефолтное значение int() или 0(одно и тоже)
print(int())
a_dect[1] += 1                  # в дефолтном словаре можно обращаться и в них уже будет дефолтное значение
print(a_dect[1])
b_dect = defaultdict(list)      # можно делать так
for i in 'hello':
    b_dect[i].append(i)
print(b_dect)
print('fdgvsdbsdbd' in b_dect)  # изначально ключа нет, но его значение изменить можно

# deque быстро работает с двумя концами(по сути лист наа максималках)
# deque потокобезопасна
# deque занимает меньше памяти чем list
a_deque = deque()
a_deque.append(1)
print(a_deque)
a_deque.appendleft(2)       # daque добавляет слева
print(a_deque)
b_deque = deque([1,2,3],maxlen=3)   # задаётся максимальная длинна, если добавить элемент, с противоположного конца элемент удалиться
print(b_deque)
b_deque.appendleft(4)
print(b_deque)

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом
# namedtuple работает даже быстрей классов
# namedtuple неизменяемый, позволяет обращаться по имени атрибута и по индексам
Cat = namedtuple('Cat','name age color')
tom = Cat('Tom',4,'yellow')
print(tom)
print(tom[0])
print(tom.name)
# tom[1] = 100 изменять нельзя так как это кортеж

Point = namedtuple('Point','x y')
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)