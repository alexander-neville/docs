#!/usr/bin/python3

def add_initial(function):

    def local():

        output = function()
        processed = output + " N"
        return processed

    return local


def add_capital(function):

    def local():

        output = function()
        processed = output[0].upper() + output[1:]
        return processed

    return local

@add_initial
@add_capital
def get_name():

    return "alex"

print(get_name())
