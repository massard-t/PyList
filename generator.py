#!/usr/bin/python3.5
from random import random


def get_an_integer():
    while True:
        my_random = random()
        yield my_random


def print_an_integer(n=None):
    if n is None:
        n = 3
    for i in range(n):
        print("A random number ({}): {}".format(i, next(get_an_integer())))


if __name__ == '__main__':
    print_an_integer(10)
