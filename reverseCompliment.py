import sys
import re
import json
import glob
import linecache

def reverseCompliment(dna):
    
    rstring = ""
    
    for i in reversed(dna):
        if i == "A":
            rstring = rstring + "T"
        elif i == "T":
            rstring = rstring + "A"
        elif i == "G":
            rstring = rstring + "C"
        elif i == "C":
            rstring = rstring + "G"
        else:
            return "Character was not recognized"

    return rstring


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:

            output.write(reverseCompliment(input.read().splitlines()[0]))


