#!/usr/bin/python
import json
import sys


def main():
    try:
        input_str = sys.stdin.read()
        print(json.dumps(json.loads(input_str), sort_keys=True, indent=2))
    except ValueError, e:
        print "error %snError: %s"%(input_str, str(e))


if __name__ == '__main__':
        main()
