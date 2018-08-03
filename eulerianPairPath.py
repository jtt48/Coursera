import sys
import re
import json
import glob
import linecache
import random
import copy

def eulerianPairPath(graph):
    
    case = formatToCycle(graph)
    edges = case[0]
    start = case[1]
    end = case[2]
    keys = edges.keys()    
    if start == "":
        start = keys[0]
    print("start eulerianPath")
    
    #randomly select starting node
    toggle = 0
    position = start
    path = [position]
    while toggle == 0:
        print("New try")
        res = position
        while areThereEdges(edges[position]):
            #randomly select edge and move
            selection = random.randint(0,len(edges[position])- 1) 
            while edges[position][selection] == "V":
                selection = random.randint(0,len(edges[position])- 1) 
            
            #cant use lists as keys in python so must convert list into string to use as key
            movingTo = edges[position][selection][0] + "|" + edges[position][selection][1]
            edges[position][selection] = "V"
            path.append(movingTo)
            res = res + "->" + movingTo
            position = movingTo
            print("Path: ", path)
            
            #cant remember why this is here.
            if position not in edges:
                break

        #if there are no more edges check if all have been traversed
        toggle = 1
        for key in keys:
            if areThereEdges(edges[key]) == True:
                #if not scroll back till we find a node with edges still
                #make that our new starting point, update path to show this
                #then continue.
                toggle = 0
           
                for entry in path:
                    if areThereEdges(edges[entry]) == True:
                        position = entry
                        break
                #if we had a cycle then path[0] and path[len(path) -1] will be the same
                #so we delete the first entry to prevent the path being
                #something like 5,5 where 5 does not point to iself.
                path.pop(len(path) - 1)
                while path[0] != position:
                    path.append(path.pop(0))
                path.append(position)
                break

    print("start", start, " end", end)
    # if start and end dont match what we expect then rotate path till it matches.
    if end != "":
        count = len(path) + 1
        if path[0] != start or path[len(path) - 1] != end:
            # print("popping")
            path.pop(len(path) - 1)
            while path[0] != start or path[len(path) - 1] != end:
                path.append(path.pop(0))
                count = count - 1
                if count < 0:
                    print("failed to find matching path with expected start and end..")
                    print("start:",start,"end",end)
                    print("path",path)
                    return ""
    
    # return string of path. Start at path[0] then add each node + ->
    res = path[0]
    for e in range(1,len(path)):
        res = res + "->" + path[e]
    return res


def areThereEdges(array):
    for edge in array:
        if edge != "V":
            return True
    return False


def formatToCycle(dict):
    
    n1 = ""
    p1 = ""
    tally = {}
    keys = dict.keys()
    
    for key in keys:
        if key not in tally:
            tally[key] = 0
        
        for edge in dict[key]:
            # becuase lists cant be keys in python
            # we are forced to transform the list into a string to use as the key
            tmpKey = edge[0] + "|" + edge[1]
            if tmpKey not in dict:
                dict[tmpKey] = []
            
            if tmpKey not in tally:
                tally[tmpKey] = 0
            tally[tmpKey] = tally[tmpKey] - 1
            tally[key] = tally[key] + 1

    for node in tally:
        if tally[node] > 0:
            p1 = node
        if tally[node] < 0:
            n1 = node
    print("tally", tally) 
    
    for thing in tally:
        if tally[thing] != 0:
            print(thing)
            print(tally[thing])
    print("n1", n1, " p1", p1, "  Length:", len(dict))
    if p1 != "" and n1 !="":
        print("APPENDED")
        dict[n1].append(p1)
        print("Format to cycle results", dict)
    return [dict, p1, n1]


if __name__ == "__main__":
    with open(sys.argv[1], "r+") as input:
        with open("output.txt", "w+") as output:
        
            param = input.read().splitlines()
            text = param[0:]
            #print(makeProfile(["AGC", "AAA", "AGG", "CAC"]))
            output.write(eulerianiPairPath(text))
