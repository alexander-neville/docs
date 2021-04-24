class Base_class_1:

    def message_1(self):

        return "this message is from base class 1"

class Base_class_2:

    def message_2(self):

        return "this message is from base class 2"

class Multi_derived_class(Base_class_1, Base_class_2):

    pass

def main():

    instance = Multi_derived_class()

    print(instance.message_1())
    print(instance.message_2())

if __name__ == "__main__":

    main()
