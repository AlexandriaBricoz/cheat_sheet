# ВСЕГДА ПИСАТЬ ЧТО-ТО EXCEPT В, НЕ ОСТАВЛЯТЬ PASS

integers = [1,2,3,-11]
try:
    int('a')
except ValueError as e:
    print(e)
    print('Error')