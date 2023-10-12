# - имена привязываются (bind) покально, они доступнытвне контекста match, для использования внешних констант нужно использовать точку, применяются правила распаковки
# - для OR случаев должны быть привязаны одинаковые имена
# - AS позволит привязать имя даже внутри паттерна
# - проверять типы можно даже внутри паттерна и при привязке имени
# HEЛЬЗЯ:：
# 1） писать：**_ для маппингов(dict)
# 2) вызывать свои функции или обращаться к какой-то коллекции по индексу (a_list[×]) в блоке case
# 3) привязывать разные имена при использовании OR (|)

from collections import namedtuple
consts = namedtuple('magnitude','value measurement')
PI = consts(3.14,'Пи')
g = consts(9.8,'джи')
null = 0
def out_pass(value):
    match value:
        case [name, age]:
            return f'Имя: {name}, возраст: {age}'
        case {'name': name,'age' : age}:
            return f'Имя: {name}, возраст: {age}'
        case str(x) if len(x.split())==2:
            name, age=x.split()
            return f'Имя: {name}, возраст: {age}'
        case _:
            raise ValueError(f'неизвестное значение {value}')

def check(value: tuple):
    match value:
        case (name,salary) if name in ('John','Ana'):
            return salary
        case ('Helen',age, _):
            return age
        case (_,_,_,_,str (something)):
            return f'Strange! {something}'
        case (*_,something) if len(value) == 6:
            return f'{something}'
        case tuple():
            return f'Unknown content {value}'
        case _:
            raise ValueError(f'Expected a turple')
def examination_magnitude(value):
    match value:
        case float(value) if value==PI.value:
            return f'Число равно {PI.measurement}'
        case float(value) if value == g.value:
            return f'Число равно {g.measurement}'
        case str(x) if x==PI.measurement:
            return f'Число равно {PI.value}'
        case str(x) if x == g.measurement:
            return f'Число равно {g.value}'
        case int(x) if x == null:           # пример с переменной в условии
            return f'Это нуль'


if __name__ == '__main__':
    print(out_pass('Лёня 19'))
    print(examination_magnitude(3.14))
    print(examination_magnitude(9.8))
    print(examination_magnitude('Пи'))
    print(check(('Helen',12,23)))
    assert (examination_magnitude('джи')) =='Число равно 9.8'
    print(examination_magnitude(0))

