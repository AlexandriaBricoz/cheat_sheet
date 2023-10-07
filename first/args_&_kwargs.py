# позиционные аргументы всегда идут в начале
# / - все что слева - только позиционные аргументы
# *, = все, что справа - только keyword аргументы
# *args собирает все позиционные аргументы в кортеж
# **kwargs собирает все keyword аргументы в словарь

def exemple2(a,b,/,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
def exemple(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

def my_print(*args,**kwargs):
    print(f'keywords:{kwargs}')
    for arg in args:
        print(str(arg), **kwargs)    # пример распаковки

if __name__ == '__main__':
    print([1,2,3])
    print(*[1,2,3])     # пример распаковки
    print(1,2,**{'sep':":",'end':'-'})   # ещё пример распаковки    sep зарденяет объекты в выводе
    print()
    print(1,2,sep=':',end='-')
    exemple('cdc','ddfc',c = 'True',d='dc')
    print()
    exemple2('cdc','ddfc',c = 'True',d='dc')
    print(*'dwcwewcwecewc') # пример распаковки со строкой