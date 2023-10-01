# не используем range(Len(List)), если нужен индекс то используем enumerate



array = [e for e in range(10)]
print(array)
for index, element in enumerate(array):
    print(f'{index+1} - {element}')

array = [e for e in range(10)]          # array[3:] указывает на то что итерация начинается с 3
for index in array[3:]:
    print(index)