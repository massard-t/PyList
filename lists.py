#!/usr/bin/python3.5


stuff = [10] * 10
print("Stuff: {}".format(stuff))
print("Some stuff: {}".format(stuff[::2]))
stuff[2:7] = [0] * 6
print("Assigned 0 to [2:7]: {}".format(stuff))
