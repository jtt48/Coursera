import sys
import re
import json
import glob
import linecache
#find most probable Kmer in dna givne dna, k, neuclotide matrix
def profileMostProbableKmer(dna,k,a,c,g,t):
    k = int(k)
    bGuest = ""
    bProb = 0
    #move window of size k through dna
    for w in range(len(dna)):
        if w == (len(dna) - k + 1):
            break
        window = dna[w:w+k]
        count = 1;
        #print(w,"-",w+k)
        #print("k:",k)
        #calculate probabilit
        for i in range(k):
            letter = window[i]
            if letter == "A":
                count = count * float(a[i])
                #print("countA",count)
            if letter == "C":
                count = count * float(c[i])
                #print("countiC",count)
            if letter == "G":
                count = count * float(g[i])
                #print("countG",count)
            if letter == "T":
                count = count * float(t[i])
                #print("countT",count)
        #print("window / Count",window,count)
        #print("a,g,c,t:",a[i],c[i],g[i],t[i])
        #print("countEnd",count)
        if window == "CCTCACTGAACT":
            print("window", window, " count", count)
        if count > bProb:
            bProb = count
            bGuest = window
    #print("bguest",bGuest)
    if bGuest == '':
        bGuest =  dna[0:0+k]
    return bGuest


   #if probobility is better than current, replace
   #return most probable.
    return "yolo" 
   
if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()

            dna = param[0]
            k = param[1]
            a = param[2].split(" ")
            c = param[3].split(" ")
            g = param[4].split(" ")
            t = param[5].split(" ")
        
            output.write(profileMostProbableKmer(dna,k,a,c,g,t))


