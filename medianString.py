import sys
import re
import json
import glob
import linecache
import copy
from hammingDistance import hammingDistance

# create list of every kmer and try them all vs each given string
# score each kmer
#return single kmer that has the best cumultive score amongst all strings.

def medianString(k, dna):
    
    print("starting frequentWordsMismatch")
    # print("text: ", text)
    count = 0
    highCount = 0
    rstring = ""


    k = int(k)
    # print("K: ",k)
    dict = {}
    kmers = allKmers(k)
    for i in range(len(kmers)):
        dict[kmers[i]] = k
    dictArray = []

    keys = list(dict.keys())

# for every dna
    for entry in dna:
# make a copy of dict
        dictCopy = copy.copy(dict)
# move window over whole dna
        for w in range(len(entry)):
            if(w == (len(entry) - k - 1)):
                break
            window = entry[w:w+k]
            #print("window ", window, " : ", k)

# hamminging distance window with every key
            for key in keys:
                # stort value in dict copy
                ham = hammingDistance(window, key)
                #print("Ham: ", ham, dictCopy[key])
                if int(ham) < dictCopy[key]:
                    dictCopy[key] = int(ham)
                #print(key, " window: ", window, " HD: ", dictCopy[key])
            # append dictcopy to dict Array
        dictArray.append(dictCopy)
        #print(dictCopy)

    # compare keys and return one with least distance.
    dictCopy = copy.copy(dict)
    for key in keys:
        count = 0
        #print("dictArrayLen: ",len(dictArray))
        for entry in dictArray:
            #print("key: ", key," count: ", count, " val: ", int(entry[key]))
            count = count + int(entry[key])
        dictCopy[key] = count
    #print(dictCopy) 
    res = ""
    #this is lazy and will break with big enough input
    finalCount = 99999
    for key in keys:
        if dictCopy[key] < finalCount:
            res = key
            finalCount = dictCopy[key]
    return res


def allKmers(k):
    if k == 1:
        return ["G","C","A","T"]
    re = reBuild("G",allKmers(k - 1))
    re.extend(reBuild("C",allKmers(k-1)))
    re.extend(reBuild("A",allKmers(k-1)))
    re.extend(reBuild("T",allKmers(k-1)))
    return re
 
def reBuild(letter,array):
    for i in range(len(array)):
        array[i] = letter + array[i]
    return array



with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        dna = []
        
        for line in range(len(param)):
            if line == 0:
                k = param[0]
            else:
                dna.append(param[line])
        
        output.write(medianString(k,dna))


