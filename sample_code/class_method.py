class Person:
    
    number = 0 

    @classmethod
    def issue_id(cls):

        cls.number += 1
        return cls.number

    @classmethod
    def return_population(cls):

        return cls.number

    def __init__(self, name):

        self._name = name
        self._id = Person.issue_id()

def main():

    print(f"Current population: {Person.return_population()}")
    person_1 = Person("Alex")
    person_2 = Person("John")
    print(f"person_1 id: {person_1._id}")
    print(f"person_2 id: {person_2._id}")
    print(f"Current population: {Person.return_population()}")

if __name__ == "__main__":

    main()
