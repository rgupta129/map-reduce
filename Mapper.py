#!/usr/bin/python
import sys

class Mapper:
        def __call__(self):
                for line in sys.stdin:
                        words = line.split()
                        for word in words:
                                print word + "\t" + "1"

if __name__ == "__main__":
        m = Mapper()
        m()
