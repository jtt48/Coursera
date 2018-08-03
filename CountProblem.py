import sys
import re
import json
import glob
import linecache

with open(sys.argv[1], "r+") as input:
    with open("CountOutput.txt", "w+") as output:
        
        f = input.read().splitlines()
        count = 0
        #value = input.read().split('/n')[0]
        
        #value = linecache.getline(sys.argv[1],3)

        #inp = linecache.getline(sys.argv[1],2) 
        
        value = f[1]

        inp = f[0]

        for i in range(len(inp) - 1):
            #print((len(value)))
            if inp[i:(i + len(value))] == value:
                print(i + len(value))
                print(inp[i:(i + len(value))])
                count = count + 1

        output.write(value)
        output.write(str(count))
 

