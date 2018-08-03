import sys
import re
import json
import glob
import linecache
from profileMostProbableKmer import profileMostProbableKmer

def greedyMotifSearch (dna, k):
    
    print("starting greedyMotifSearch")
    #print("dna:",dna)

    results = []
    k = int(k)
    for i in range(len(dna[0])):
        if i == len(dna[0]) - k + 1:
            break
        kmer = dna[0][i:i+k]
        #print("kmer",kmer)
        tmpArr = []
        #tmpArr.append(kmer)
        #print("tmpArr:", tmpArr)
        for j in range(len(dna)):
            if j == 0:
                tmpArr.append(kmer)
            else:
                pro = makeProfile(tmpArr)
                #print("pro:",pro)
                #print("dna[j]:",dna[j])
                pmp = profileMostProbableKmer(dna[j],k,pro[0],pro[1],pro[2],pro[3])
                #print("PMP:", pmp)
                tmpArr.append(pmp)
                #print ("current tmpArr:", tmpArr)
        results.append([tmpArr,scoreProfile(tmpArr)])
        #print("Score:",scoreProfile(tmpArr))
    #print(results)
    lowCell = 0
    lowValue = results[0][1]
    for r in range(len(results)):
        if results[r][1] < lowValue:
            lowValue = results[r][1]
            lowCell = r
    
    restring = ""
    for f in results[lowCell][0]:
        restring = restring + f +"\n"
    return restring


def makeProfile(arr):
    # make profile matrix from all elements in arr.
    # ex: Arr= ["GCG, "ACA"]
    #print("------------------")
    #print("profile kmers:",arr)
    size = len(arr[0])
    length = len(arr)
    reArr = []
    
    #print("size:",size)
    #print("length:",length)
    #print("test:", arr[0][0])
    #print("test:", arr[0][1])
    #for every letter in the kmers in arrr
    for i in range(length):
        #an array to hold the whole values for the kmer
        # [[A][C][G][T]]
            kmerArray = []
            for k in range(4):
                kmerArray.append([])
            for j in range(size): 
                #print(arr[j][i], tmpDict[arr[j][i]])
                #print("size",size)
                #print("i",i)
                #print("length",length)
                #print("j:",j)
                #print("query:", tmpDict[arr[i][j]] + (float(1) / length))
                #print("i:j:",i, j)
                letter = arr[i][j]
                if letter == "A":
                    kmerArray[0].append(float(1) / length)
                else:
                    kmerArray[0].append(0.0)
                if letter == "C":
                    kmerArray[1].append(float(1) / length)
                else:
                    kmerArray[1].append(0.0)
                if letter == "G":
                    kmerArray[2].append(float(1) / length)
                else:
                    kmerArray[2].append(0.0)
                if letter == "T":
                    kmerArray[3].append(float(1) / length)
                else:
                    kmerArray[3].append(0.0)
    #Ex: arr[0] = "GCG" -> kmerArray[[0,0,0][0,.5,0][.5,0,.5][0,0,0]]
            
            

            reArr.append(kmerArray)
            #print("")
            #print("reArr", reArr)
            #print("")
    
    
    #multiple all values by length. Add 1, then divide by length + 1
            
    if len(reArr) > 1:
        for s in range(1,len(reArr)):
            addArrays(reArr[0],reArr[s])
    #print("Profile:", reArr[0])
    #apply psuedocounts
    #check for any 0 value. If one is found...
    for t in range(len(reArr)):
        for l in range(len(reArr[t])):
            for w in range(len(reArr[t][l])):
                if reArr[t][l][w] == 0:
                    for t2 in range(len(reArr)):
                        for l2 in range(len(reArr[t2])):
                            for w2 in range(len(reArr[t2][l2])):
                                #print("length: ", length)
                                num = reArr[t2][l2][w2]
                                num = num * length
                                num = num + 1
                                num = num / (length + 4)
                                reArr[t2][l2][w2] = num
    #print("reArr2", reArr)
    return reArr[0]


# take 2 arrays and add a[1] and b[1], a[2] and b[2], etc
# return array with merged values
def addArrays(arr1, arr2):
    for cell in range(len(arr1)):
        for genotype in range(len(arr1[cell])):
            arr1[cell][genotype] = arr1[cell][genotype] + arr2[cell][genotype]
    return arr1



#give score to a profile.
#profile should be an array of kmers.
def scoreProfile(profile):
    length = len(profile[0])
    score = 0
    for letter in range(length):
        nucel = [0,0,0,0]
        for kmer in range(len(profile)):
            if profile[kmer][letter] == "A":
                nucel[0] = nucel[0] + 1
            if profile[kmer][letter] == "C":
                nucel[1] = nucel[1] + 1
            if profile[kmer][letter] == "G":
                nucel[2] = nucel[2] + 1
            if profile[kmer][letter] == "T":
                nucel[3] = nucel[3] + 1
        #figure out which nucleotide is the largets
        # ignore that one and all the rest to score
        largestCell = -1
        largestVal = -1
        for h in range(4):
            if nucel[h] > largestVal:
                largestVal = nucel[h]
                largestCall = h

        nucel[largestCall] = 0
        for v in range(4):
            score = score + nucel[v]

    return score



with open(sys.argv[1], "r+") as input:
    with open("output.txt", "w+") as output:
        
        param = input.read().splitlines()
        
        k = param[0]
        dna = param[1:]
        #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
        output.write(greedyMotifSearch(dna,k))
