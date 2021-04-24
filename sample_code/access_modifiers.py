class Test_class:

    def __init__(self, name, age, number):

        self.name = name
        self._age = age
        self.__number = number

    def return_age(self):

        return self._age

    def return_number(self):

        return self.__number

    def set_number(self, number):

        self.__number = number

def test_func(test, test2):

    pass

if __name__ == "__main__":
