class CallCount:

    def __init__(self, function):

        self._function = function
        self._count = 0

    def __call__(self, name):

        self._count += 1
        return self._function(name)



@CallCount
def sayhello(name):

    return (f"hello {name}")

@CallCount
def sayhi(name):

    return(f"hi {name}")


print(sayhello('alex'))
print(sayhello('benjy'))
print(sayhello._count)

print(sayhi('alex'))
print(sayhi('benjy'))
print(sayhi('Richard'))
print(sayhi._count)

print(sayhello._count)
