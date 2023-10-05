def f(i):
    if i==0 or i==1:
        return 1
    return f(i-1)+f(i-2)

print(f(4))