#!/usr/bin/python3

class Tree:

    def __init__(self):

        self._value = None
        self._left = None
        self._right = None

    def insert(self, value):

        if not self._value:

            self._value = value

        else:

            if value < self._value:

                if self._left:

                    self._left.insert(value)

                else:

                    self._left = Tree()
                    self._left.insert(value)

            elif value >= self._value:

                if self._right:

                    self._right.insert(value)

                else:

                    self._right = Tree()
                    self._right.insert(value)

    def hasdata(self):

        if self._value:

            return True

        else:

            return False

    def __str__(self):

        if self._left:

            self._left.__str__()

        print(self._value)

        if self._right:

            self._right.__str__()


def main():

    root = Tree()
    print(root)

if __name__ == "__main__":

    main()
