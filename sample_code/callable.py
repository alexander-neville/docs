#!/usr/bin/python3
import socket

class Resolver:

    def __init__(self):

        self._cache = {}

    def __call__(self, host):

        if host not in self._cache:

            self._cache[host] = socket.gethostbyname(host)

        return self._cache[host]


def main():

    resolve = Resolver()
    resolve("bbc.co.uk")
    resolve("google.com")

    print(resolve._cache)
    resolve("archlinux.org")
    print(resolve._cache)


if __name__ == "__main__":

    main()
