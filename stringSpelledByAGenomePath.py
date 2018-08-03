import sys
import re
import json
import glob
import linecache

def stringSpelledByAGenomePath (text):
    
    #compare results and next, if they dont match we slice offf
    # a letter and compare the slices, doing this till we have
    # a match we can merge on.

    print("starting stringSpelledByGenomePath")
    results = ""
    for i in range(len(text)):
        if results == "":
            results = text[i].strip()
        else:
            next = text[i].strip()
            window = results[(len(results) - len(text[i])):len(results)]
            print("Window:" , window)
            print("Next:", next)
            for letter in range(len(window)):
                print("Trying-  Window:", window[letter:], "Next:",next[0:len(next) - letter])
                if window[letter:] == next[0:len(next) - letter]:
                    print("adding to results: ", next[len(next) - letter:])
                    results = results + next[len(next) - letter:]
                    break
            print("Results current state: ", results)
    return str(results)

if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
        
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(stringSpelledByAGenomePath(text))
