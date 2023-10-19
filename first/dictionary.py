# list не может быть ключом

if __name__ == '__main__':
    dictionary = dict(fol=4, gol=1, moskva=100)  # key:value
    print(dictionary)
    a_list = [['moskva', 7], ['london', 4], ['novgorod', 1]]
    dictionary = dict(a_list)
    print(dictionary)
    dictionary = dict.fromkeys(['a', 'b', 'c'])  # создаёт только ключи
    print(dictionary)
    dictionary = dict.fromkeys(['a', 'b', 'c'], 100)  # создаёт ключи и по умолчанию присваивает 100 всем значениям
    print(dictionary)
    dictionary = {}  # пустой словарь
    print(dictionary)
    a_list = [[('москва', 2), 4], ['новосибирск', 656], ['кострома', [1, 5, 'волгоград']]]
    dictionary = dict(a_list)
    print(dictionary['новосибирск'])
    dictionary[4] = 'njn'
    print(dictionary)
    example = 'Alexandr Skvortsov 19 Dema 5 4 5 4 5'
    example = example.split()
    print(example)
    person = {}
    person['first_name'] = example[0]
    person['last_name'] = example[1]
    person['age'] = example[2]
    person['adress'] = example[3]
    person['estimates'] = []
    for i in example[4:]:
        person['estimates'].append(int(i))
    print(person)
    del person['estimates']  # можно удалять только существующие элементы, иначе будет ошибка
    print(person)
    print(len(person))  # длинна словаря
    print('age' in person)  # есловие нахождения ключа в словаре
    print('age' in person, 'ggg' in person, 'kkkk' not in person)  # комбо
    for element in person:  # вывод ключей
        print(element)
    for element in person:  # вывод ключей
        print(person[element])  # вывод значений
    for element in person.values():  # вывод значений
        print(element)
    for pair in person.items():
        print(pair)
    for key, value in person.items():
        print(key, value)
    print(
        person.get('age', 'No such key'))  # выводит значение по ключу, если ключ не найден возращает заданное значение
    print(dictionary.pop('кострома'))  # возращает значение п ключу и и удаляет ключ и его значение
    print(dictionary)
    print(dictionary.popitem())  # возвращает случейный ключ и его значение, после удаляет их
    print(dictionary)
    print(dictionary.keys())  # выводит ключи
    print(dictionary.values())  # выводит значения
