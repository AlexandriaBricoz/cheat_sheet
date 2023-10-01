
    # list не может быть ключом

if __name__ == '__main__':
    dictionary = dict(fol=4,gol=1,moskva=100)   # key:value
    print(dictionary)
    a_list = [['moskva',7],['london',4],['novgorod',1]]
    dictionary = dict(a_list)
    print(dictionary)
    dictionary = dict.fromkeys(['a','b','c'])   # создаёт только ключи
    print(dictionary)
    dictionary = dict.fromkeys(['a', 'b', 'c'],100)  # создаёт ключи и по умолчанию присваивает 100 всем значениям
    print(dictionary)
    dictionary = {}                             # пустой словарь
    print(dictionary)
    a_list = [[('москва',2),4],['новосибирск',656],['кострома',[1,5,'волгоград']]]
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
        person['estimates'].append(i)
    print(person)
