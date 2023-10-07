def print_in_times(srting: str, n: int = 10):
    for i in range(n):
        print(srting)
def calc(time=[]):          # ОШИБКА нельзя использовать изменяемы типы, значение по умолчнию создётся один раз!!!
    time.append(1)
    print(time)

def calc2(time=None):          # ПРАВИЛЬНЫЙ ВЫРИАНТ!!!
    if time==None:
        time = [2]
    print(time)
def printt(sting):
    print(sting,end='')
if __name__ == '__main__':
    print_in_times('21212',3)
    printt(1)
    printt(1)
    print(1,end='')
    print(1)
    calc()
    calc()
    calc()
    calc2()
    calc2()
    calc2()