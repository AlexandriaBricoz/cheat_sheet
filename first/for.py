# не используем range(Len(List)), если нужен индекс то используем enumerate



array = [e for e in range(10)]
print(array)
for index, element in enumerate(array):
    print(f'{index+1} - {element}')