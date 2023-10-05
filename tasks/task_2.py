def is_prime(i:int)->bool:
    hhh = list(range(i))
    booling = False
    remainder = i
    for n in hhh[2:]:
        if remainder % n==0:
            print(n)
            remainder = remainder//n
            booling = True
    return booling

if __name__ == '__main__':
    print(is_prime(int(input())))
