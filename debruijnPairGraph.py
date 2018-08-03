import sys
import re
import json
import glob
import linecache

#gen graph
#ex: {"AGCT|CCTC]:[AGAT,CTCT],[]],
#     []         : [[]]}
def debruijnPairGraph(kmers):
    print("start debruijnPairGraph")
    print("kmers:", kmers)
    dict ={}

    for kmer in kmers:
        splitmer = kmer.split("|")
        key = splitmer[0][0:-1] + "|" + splitmer[1][0:-1]
        if key not in dict:
            dict[key] = []
        dict[key].append([splitmer[0][1:],splitmer[1][1:]])

    print(dict)
    return dict

if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(debruijnPairGraph(text))
