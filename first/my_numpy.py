import numpy as np


def printt(x):  # декоратор по приколу
    print('вывод:')
    print(x)  # выводит массив строками


array = np.array([[1, 2, 3], [1, 3, 4]])  # простое создание массива
zeros = np.zeros((3, 5))  # создаёт массив из нулей
ones = np.ones((2, 6))  # создаёт массив из едениц
joke = np.empty((3, 3))  # создаёт массив из непустых ячеек, которые не меняет(просто мусор из оперативы)
num_range = np.arange(2, 10, 2)
printt(array)
printt(zeros)
printt(ones)
printt(joke)
printt(num_range)
printt(np.arange(0, 3000, 1))  # автоматически скрывает центр если массив грамоздкий
# Создаем большой массив для демонстрации
large_array = np.arange(0, 3000, 1)
printt(array.itemsize)  # размер каждого элемента массива в байтах
printt(array.size)  # количество элементов массива
printt(array.dtype)  # объект, описывающий тип элементов массива
printt(array.shape)  # размеры массива, его форма
printt(array.ndim)  # число измерений (чаще их называют "оси") массива
# .date - буфер, содержащий фактические элементы массива
# Получаем доступ к буферу данных массива
data_buffer = array.data

# Преобразуем буфер данных в байты
data_bytes = bytes(data_buffer)

# Теперь data_bytes содержит данные массива в бинарной форме
# Вы можете использовать data_bytes для передачи данных или обработки их
print(data_bytes)

# Устанавливаем параметры вывода для отображения полного массива
np.set_printoptions(threshold=np.inf)

# Выводим массив
print(large_array)
