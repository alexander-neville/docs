class test(object):

    def __init__(self):

        self.name = "test_class"
     
instance = test()
print(dir(instance))
print(test.__mro__)
print(test.mro())
