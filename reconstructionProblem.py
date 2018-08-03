import sys
import re
import json
import glob
import linecache
import random
import copy
from eulerianPath import eulerianPath
from kmerDebruijnGraph import kmerDebruijnGraph

#AKA out first assembler! *squeeeeeeee*

def reconstructionProblem(text):
   graph = kmerDebruijnGraph(text).splitlines()
   #print("Graph:", graph)
   kmers = eulerianPath(graph).split("->")
   res = ""
   for kmer in kmers:
       if res == "":
           res = kmer
       else:
           res = res + kmer[-1:]
   return res


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            k = param[0]
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(reconstructionProblem(text))
