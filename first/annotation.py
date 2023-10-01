def summ(a:[int,float], b:[int,float])->[int,float]:
    return a+b
def summ2(a:[int,float], b:[int,float])->int:
    return a+b

def summ_list(a_list:list[str])->int:               #сумма квадратов от строк
    return sum([int(e)*int(e) for e in a_list])

if __name__ == '__main__':
    print(summ(1.4,61))
    print(summ2(1.4, 61))
    print(summ_list(['10','5','6']))