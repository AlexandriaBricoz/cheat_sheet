# не используем range(Len(List)), если нужен индекс то используем enumerate

if __name__ == '__main__':
    array = [e for e in range(10) if e%2==0]
    print(array)
    for index, element in enumerate(array):
        print(f'{index+1} - {element}')

    array = [e for e in range(10)]          # array[3:] указывает на то что итерация начинается с 3
    for index in array[3:]:
        print(index)
            # filter
    values = [123,23,434,5,232,434,3,434,9,34,34,76,76765,0,0,12,5]
    filter_velues = list(filter(lambda x: x>70,values))  # надо писать лист, иначе будет ссылка на объект
    filterr_velues = list(filter(bool,values))
    filterrr_velues = list(filter(None,values))
    print(filter_velues)
    print(filterr_velues)
    print(filterrr_velues)
    string = 'hiuhuhiu78988h7h7h98h9h9ud454d5f3ag87bv5d4s3456'
    filter_str = list(filter(str.isdigit,string))
    print(filter_str)
    dictionary = {
        'Moskow' : 120,
        'Kiev' : 100,
        'Novgorod' : 80,
        'Astrahan' : 65,
    }
    dictionary_filter = list(filter(lambda x: dictionary[x]>75 and dictionary[x]<101,dictionary))
    print(dictionary_filter)

            # map
    def func(velue):
        return (velue**2)%10
    numbers = [1,23,4,3,23,4]
    values = numbers[:]
    numbers = list(map(lambda x: (x**2)%10, numbers))
    values = list(map(func,values))
    print(numbers)
    print(values)
    string = ['mewcmwokcmsk','weffw','we']
    string = list(map(str.upper,string))        # можно истользовать методы объктов
    print(string)