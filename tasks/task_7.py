"""
У вас есть массив чисел, составьте из них максимальное число
"""
def func(list):
    list = sort(list)
    string = ''
    for value in list:
        string = string + str(value)
    return int(string)


def sort(list):
    if any([isinstance(e,str) for e in list]): # type(e) == str
        raise ValueError('Введена строка')
    if not all([isinstance(e,int) for e in list]):
        raise ValueError('Введены не целые числа')
    array = []
    for namber in range(9,0,-1):
        k = 0
        primer = []
        n = 0
        for i, value in enumerate(list):
            if value >= namber*(10**(n-1)):
                if int(str(list[i])[n]) == namber:
                    primer.append(value)
                    k += 1
        if primer:
            n += 1
            primer = [e for e in primer if e]
            for i, value in enumerate(primer):
                for i2, value2 in enumerate(primer[i+1:]):
                    if primer[i2+i+1]>namber*(10**(n-1)) and primer[i]>namber*(10**(n-1)):
                        if int(str(primer[i2+i+1])[n]) > int(str(primer[i])[n]):
                            time = primer[i]
                            primer[i] = primer[i2+i+1]
                            primer[i2+i+1] = time
                    elif primer[i2+i+1]<=namber*(10**(n-1)):
                        time = primer[i]
                        primer[i] = primer[i2 + i + 1]
                        primer[i2 + i + 1] = time
        for i in primer:
            array.append(i)

    return array



if __name__ == '__main__':
    print(func([22,1,54,98,92,9,999,67,5656466,94,35,43,534,5,34,5325,23,45,2345,324,5,3425,342,534,5,34,523,45324,52,36,435,7]))
    print(func([12,23,342,90,9,99,967,30]))
    assert (func([1,111,11,2,12,10]))=='21211111110'
    assert func([1,22,94,54,9])==99454221, 'плохо чел'
    assert func([1,22,9,54,94])==99454221, 'плохо чел'