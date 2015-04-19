class Foo:

    def __init__(self, param):
        self.__myprivateattribute = param

    def __str__(self):
        return str(self.__myprivateattribute)


p = Foo(10)
print(str(p)) # 10
p._Foo__myprivateattribute = 1
print(str(p)) # 1
