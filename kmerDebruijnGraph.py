import sys
import re
import json
import glob
import linecache

def kmerDebruijnGraph(kmers):
    print("start kmerDebruijnGraph")
    dict ={}

    for kmer in kmers:
        if kmer[0:len(kmer) - 1] not in dict:
            dict[kmer[0:len(kmer) - 1]] = []
        dict[kmer[0:len(kmer) - 1]].append(kmer[1:])
        dict[kmer[0:len(kmer) - 1]].sort()

    #print(dict)

    res = ""

    keys = dict.keys()
    keys.sort()

    for key in keys:
        res = res + key + " -> "
        for value in range(len(dict[key])):
            if value == 0:
                res = res + dict[key][value]
            else:
                res = res + "," + dict[key][value]
        res = res +"\n"

    res = res[:-1]
    
    #print("res",res)
    return res


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(kmerDebruijnGraph(text))
