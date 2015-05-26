#!/usr/bin/python
import sys

class Reducer:
        def __call__(self):
                curr_word = None
                curr_count = None
                for line in sys.stdin:
                        word, count = line.split()
                        if curr_word == None:
                                curr_word = word
                                curr_count = int(count)
                        elif curr_word == word:
                                curr_count += int(count)
                        else:
                                print curr_word, curr_count
                                curr_word = word
                                curr_count = int(count)
                if curr_word != None:
                        print curr_word, curr_count

if __name__ == "__main__":
        r = Reducer()
        r()
