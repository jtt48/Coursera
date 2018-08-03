import sys
import re
import json
import glob
import linecache
import random
import copy

def eulerianCycles(text):
    
    case = formatToCycleDict(text)
    edges = case[0]
    start = case[1]
    end = case[2]
    #return ""
    keys = edges.keys()    
    
    print("start eulerianCycles")
    
    #randomly select starting node
    toggle = 0
    currentTry = edges
    position = start
    path = [position]
    while toggle == 0:
        #print("New try")
        #print ("path", path)
        #print(currentTry)
        res = position
        while areThereEdges(currentTry[position]):
            #print("==========")
            #print("position", position)
            #randomly select edge and move
            selection = random.randint(0,len(currentTry[position])- 1) 
            while currentTry[position][selection] == "V":
                selection = random.randint(0,len(currentTry[position])- 1) 
            #print("selected array entry", selection)
            movingTo = currentTry[position][selection]
            currentTry[position][selection] = "V"
            position = movingTo
            path.append(movingTo)
            #print("moving to", movingTo)
            #print("path",path)
            res = res + "->" + movingTo
            #print("position",position)
            if position not in currentTry:
                break

        #if there are no more edges check if all have been traversed
        toggle = 1
        for key in keys:
            if areThereEdges(currentTry[key]) == True:
                #if not scroll back till we find a node with edges still
                #make that our new starting point, update path to show this
                #then continue.
                toggle = 0
          #      print("path", path)
                for entry in path:
           #         print("for Entry in path", entry)
                    if areThereEdges(currentTry[entry]) == True:
         #               print("position in path with edges", entry)
                        position = entry
                        break
                #if we had a cycle then 0, and x will be the same
                #so we delete the first entry to prevent the path being
                #something like 5,5.
        #        print("path", path)
                path.pop(len(path) - 1)
       #         print("path pop", path)
                while path[0] != position:
       #             print("path[0]", path[0], " pos", position)
                    path.append(path.pop(0))
      #              print("path Rotation:", path)
     #               print("")
                path.append(position)
                break

    #print("p0", path[0], "pe", path[len(path) - 1])
    #print("start", start, " end", end)
    if path[0] != start or path[len(path) - 1] != end:
      # print("popping")
       path.pop(len(path) - 1)
    while path[0] != start or path[len(path) - 1] != end:
        #print("path[0]", path[0], " pos", position)
        path.append(path.pop(0))
        #print("path Rotation:", path)
    #    print("")
    #print("path", path)

    res = path[0]
    for e in range(1,len(path)):
        res = res + "->" + path[e]
    return res


def areThereEdges(array):
    for edge in array:
        if edge != "V":
            return True
    return False


def formatToCycleDict(badFormat):
    dict = {}
    for line in badFormat:
        nw = line.split()
        #print(nw)
        dict[nw[0]] = []
        nc = nw[2].split(",")
        for node in nc:
            dict[nw[0]].append(node)
    #print(dict)
    
    n1 = ""
    p1 = ""
    tally = {}
    keys = dict.keys()
    
    for key in keys:
        if key not in dict:
            dict[key] = []
       # print("node lord", key)
        if key not in tally:
            tally[key] = 0
        for edge in dict[key]:
            if edge not in dict:
                dict[edge] = []
        #    print("edge lord", edge)
            if edge not in tally:
                tally[edge] = 0
            tally[edge] = tally[edge] - 1
            tally[key] = tally[key] + 1

    for node in tally:
        if tally[node] > 0:
            p1 = node
        if tally[node] < 0:
            n1 = node
    print("tally", tally) 
    print("n1", n1, " p1", p1)
    dict[n1].append(p1)
    print("DICT WE PASS",dict)
    return [dict, p1, n1]


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(eulerianCycles(text))
