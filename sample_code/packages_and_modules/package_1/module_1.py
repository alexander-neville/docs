def function_1():

    print("This is a function from module_1")

class class_1():

    def __init__(self, name, number):

        self._name = name
        self.__number = number

    def print_name(self):

        return self._name
