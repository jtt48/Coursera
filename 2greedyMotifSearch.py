import sys
import re
import json
import glob
import linecache
from profileMostProbableKmer import profileMostProbableKmer

def greedyMotifSearch (dna, k):
    
    print("starting greedyMotifSearch")
    print("dna:",dna)

    resArr = []
    k = int(k)
    for i in range(len(dna[0])):
        if i == len(dna[0]) - k + 1:
            break
        kmer = dna[0][i:i+k]
        print("kmer",kmer)
        tmpArr = []
        #tmpArr.append(kmer)
        #print("tmpArr:", tmpArr)
        for j in range(len(dna)):
            if j == 0:
                tmpArr.append(kmer)
            else:
                pro = makeProfile2(tmpArr)
                print("pro:",pro)
                print("dna[j]:",dna[j])
                pmp = profileMostProbableKmer(dna[j],k,pro[0],pro[1],pro[2],pro[3])
                print("PMP:", pmp)
                tmpArr.append(pmp)
                print ("current tmpArr:", tmpArr)
        return dna

//
def makeProfile1(arrays):
    print("---------------")

def makeProfile(arr):
    # make profile matrix from all elements in arr.
    print("------------------")
    print("arr:",arr)
    size = len(arr[0])
    length = len(arr)
    reArr = []
    
    print("size:",size)
    print("length:",length)
    #print("test:", arr[0][0])
    #print("test:", arr[0][1])
    for i in range(length):
        for j in range(size):
            tmpDict = {
                "A":0.0,
                "C":0.0,
                "G":0.0,
                "T":0.0,
                }
            #print(arr[j][i], tmpDict[arr[j][i]])
            #print("size",size)
            #print("i",i)
            #print("length",length)
            #print("j:",j)
            #print("query:", tmpDict[arr[i][j]] + (float(1) / length))
            tmpDict[arr[i][j]] = tmpDict[arr[i][j]] + (float(1) / length)
            reArr.append(tmpDict)
        #print("")
        #print("reArr", reArr)
        #print("")
    res = []
    arrA = []
    arrC = []
    arrG = []
    arrT = []
    
    arrA2 = []
    arrC2 = []
    arrG2 = []
    arrT2 = []

    print("reArr:",reArr)
    for arr2 in reArr:
        if len(arrA) == 0:
            arrA.append(arr2['A'])
            print ("arrA: ", arrA)
            arrC.append(arr2["C"])
            arrG.append(arr2["G"])
            arrT.append(arr2["T"])
        else:
            addArrays(arrA, arr2['A'])
            addArrays(arrC, arr2['C'])
            addArrays(arrG, arr2['G'])
            addArrays(arrT, arr2['T'])
    res.append(arrA)
    res.append(arrC)
    res.append(arrG)
    res.append(arrT)
    #print("pro res")
    return res

# take 2 arrays and add a[1] and b[1], a[2] and b[2], etc
# return array with merged values
def addArrays(arr1, arr2):
    for cell in range(len(arr1)):
        arr1[cell] = arr1[cell] + arr2[cell]
    return arr1



with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        k = param[0]
        dna = param[1:]
        #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
        output.write(greedyMotifSearch(dna,k))
