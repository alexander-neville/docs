import abc

class Animal(abc.ABC):

    @abc.abstractmethod
    def go_swimming(self):
        pass

    @abc.abstractmethod
    def go_flying(self):
        pass

    @abc.abstractmethod
    def make_noise(self):
        pass

class Bird(Animal):

    def go_swimming(self):
        
        print("usually birds dont't go swimming")

    def go_flying(self):

        print("I am a bird so I can go flying")

    def make_noise(self):

        print(f"I am a bird and my name is {self._name}.")

class Duck(Bird):

    def __init__(self, name):

        self._name = name

    def go_swimming(self):

        Bird.go_swimming(self)
        print("But I am a duck and I can go swimming")

class Penguin(Bird):

    def __init__(self, name):

        self._name = name


    def go_flying(self):

        Bird.go_flying(self)
        print("Because I am a penguin I cannot fly.")

def test_noise(animal):
    
    animal.make_noise()

def test_swimming(animal):

    animal.go_swimming()

def test_flying(animal):

    animal.go_flying()

def main():

    penguin_1 = Penguin("john")
    duck_1 = Duck("alexander")

    test_noise(penguin_1)
    test_noise(duck_1)


    test_flying(penguin_1)

    print("\n")
    test_swimming(penguin_1)
    print("\n")
    test_swimming(duck_1)
    print("\n")
    test_flying(penguin_1)
    print("\n")
    test_flying(duck_1)
    print("\n")

if __name__ == "__main__":

    main()
