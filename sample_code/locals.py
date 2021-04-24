#!/usr/bin/python3

one = "one"

two = "two"

def outer():
    
    three = "three"
    def inner():

        print(one, two, three)

    inner()

outer()

def test():

    one = "tricked"
    print(one, two)
    print(one)

test()

print(one)
