# LEGB -rule
# L-Local
# E-enclosed
# G-global
# B-builtins
scope = 'global'
max = 10


def outer():
    scope = 'enclosed'

    def inner():
        scope = "local"
        print(scope)  # питон ищет переменную или функцию изнутри
        # print(max([1,2,3]))     # здесь будет ошибка из-за того что max переназначен

    inner()


if __name__ == '__main__':
    outer()
