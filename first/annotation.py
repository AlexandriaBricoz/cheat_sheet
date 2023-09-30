def summ(a:int, b:int)->int:
    return a+b

def summ_list(a_list:list[str])->[int]:   #сумма квадратов от строк
    return sum([int(e)*int(e) for e in a_list])

if __name__ == '__main__':
    print(summ(1,61))
    print(summ_list(['10','5','6']))