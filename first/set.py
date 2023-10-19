if __name__ == '__main__':
    box = {1, 2, 3, 4, 4, 3, 5}
    box = set([1, 4, 5, 3, 5, 6, 4])
    print(box)
    alphabet = set('wrfwnnwpoidwieojcrui][poiuytrewqasdfghjkl;/.,mnbvcxznvepics,wp[')  # парсит по символам
    print(alphabet)
    words = set(('df dfdffe vr rvrev').split())  # парсит по словам
    print(words)
    rangee = set(range(20))
    print(rangee)
    tuples = set([(1, 2, 3), (3, 2, 1,), (5, 6, 7), (1, 2, 3)])  # использует только неизменяемые типы
    print(tuples)
    a_list = [1, 2, 4, 2, 5, 4]
    a_tuples = {e for e in a_list}  # только так вроде
    print(a_tuples)
    a_list = [set(a_list)]  # cпособ из list убрать повторы
    print(a_list)
    a_tuples.add(9)  # добвление в set
    a_tuples.add(4)
    a_tuples.update([3, 4, 3, 56, 7, 8])
    a_tuples.update({45, 34})
    a_tuples.update(range(34, 39))
    print(a_tuples)
    a_tuples.discard(1)
    a_tuples.discard(1)  # не вызывает ошибку
    a_tuples.remove(2)  # вызывает ошибку
    print(a_tuples)
    print(a_tuples.pop())  # удалит и вернёт случайное
    print(a_tuples)
    print(len(a_tuples))
    print(4 in a_tuples, 3 in a_tuples, 1 not in a_tuples)
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6, 9, 10}
    c = {9, 10, 11}
    print(a & b)
    print(a | b)
    print(a - b)
    print(a ^ b)
    print(a == b)
    print(a > b)  # значит b входит в a
    print(a >= b)
    b -= a
    a &= b
    print(a.intersection(b))
    print(a & c)
    c.intersection_update(b)
    print(c)
    print(a)
    for velue in a_tuples:  # обращаться к индесам нельзя, только к значения
        print(velue)
