import datetime

a = 'Hello'
b = 'Word'
result = 121
result2 = 200
pi = 3.141592
long = 1413241224242
array = [25, 4, 46, 8]
today = datetime.datetime.now()

# ГЛАВНОЕ ИСПОЛЬЗОВАТЬ ФОРМАТ f'{}'

if __name__ == '__main__':
    print(f'{a}, {b}')
    print(f'{result}')
    print(f'{result=}')
    print(f'{result:b}')
    print(f'{result:x}')
    print(f'{pi:.2f}')  # .2 значит два знака после точки, f значит что с плавающей точкой
    print(f'{pi:.3f}')
    print(f'{result:6}')  # :6 значит сколько что нужно в начало довить пробелов для того чтобы вывелось 6 символов
    print(f'{result:06}')  # :06 вместо пробелов заполнит нулями
    print(f'{result:^12}')  # ^12  поставит result в середину
    print(f'{result:>12}')
    print(f'{result:<12}')  # <, > анологичны
    print(f'{result:0<12}')  # заполнит нулями
    print(f'{result:=^12}')  # заполнит =
    print(f'{long:,}')  # , разделить на тысячи
    print(f'{min(array)}')  # работа с функциями
    print(range(4))
    print(today)
    print(f'{today:%d-%m-%Y %H:%M}')  # маски с datetime
    print(f'{result / result2:.2f}%')  # пример стчёта процентов
    l = f'{result} кон'
    print(f'{l}ь')
