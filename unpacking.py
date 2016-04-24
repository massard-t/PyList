#!/usr/bin/python3.5


a, b, c = 1, 2, 3
print("a, b, c = 1, 2, 3 \na: {} b: {} c: {}\n".format(a, b, c))
a, b, c = [1, 2, 3]
print("a, b, c = [1, 2, 3]\na: {} b: {} c: {}".format(a, b, c))
a, b, c = (2 * i + 1 for i in range(3))
print("""
a, b, c = (2 * i + 1 for i in range(3))\na: {} b: {} c: {}
    """.format(a, b, c))
a, (b, c), d = [1, (2, 3), 4]
print("a, (b, c), d = [1, (2, 3), 4]")
print("a: {} b: {} c: {} d: {}".format(a, b, c, d))
