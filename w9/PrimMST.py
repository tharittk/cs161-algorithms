# Implementation of Prim's MST using Heap

import sys

sys.path.insert(0,'/Users/TharitT/dev-proj-local/cs161-algorithms')

# Heap class API
from w7.MedianMaintenance import *

import heapq


# Graph class API - undirected 

class Graph():
    def __init__ (self):
        self.graph = {}
        self.VinTree = []
        self.VNotInTree = []

    def create_graph(self, inputFile):
        with open(inputFile) as f:
           header = f.readline().strip().split(' ')
           n_nodes = int(header[0])
           n_edges = int(header[1])

           mem = []

           for i in range(n_edges):
                line = f.readline().strip().split(" ")

                src = int(line[0])
                dest = int(line[1])
                cost = int(line[2])

                #print(src, dest, cost)

                # src side
                if src not in self.graph.keys():
                    self.graph[src] = {dest : cost}
                else:
                    #if dest not in self.graph[src].keys():
                    #    self.graph[src] =  {dest : [cost]}
                    #else:
                    #    self.graph[src][dest].append(cost)
                    self.graph[src][dest] = cost

                # dest side
                if dest not in self.graph.keys():
                    self.graph[dest] = {src : cost}
                else:
                    #if src not in self.graph[dest].keys():
                    #    self.graph[dest] =  {src : [cost]}
                    #else:
                    #    self.graph[dest][src].append(cost)
                    self.graph[dest][src] = cost

                if (src, dest) in mem or (dest, src) in mem:
                    print("error")
                else:
                    mem.append((src, dest))
                
    def initialize(self):
        
        # initialize vertex
        self.VinTree.append(list(self.graph.keys())[0])
        self.VNotInTree = list(self.graph.keys())[1:]

        # initialize heap of yet-to-be-included

        #print(self.graph[1])

        # O (mn) run-time

        allVertices = sorted(list(self.graph.keys()))

        sumEdgeWeight = 0

        while sorted(self.VinTree) != allVertices:


            globalMin = float('inf')
            absorbedVertex = None

            for w in self.VNotInTree:
                #print('current w >> ', w)
                currentDestInTree, currentMinCost = self.computeCheapestEdgeToCurrentTree(w)
                if currentDestInTree != None:
                    if currentMinCost < globalMin:
                        globalMin = currentMinCost
                        absorbedVertex = w
            
            # absorbed vertex
            sumEdgeWeight += globalMin

            self.VinTree.append(absorbedVertex)

            self.VNotInTree.pop(self.VNotInTree.index(absorbedVertex))

        print('finish, vtx in tree', len(self.VinTree))
        print('total weight, ', sumEdgeWeight)





    
    def computeCheapestEdgeToCurrentTree(self, srcNotInTree):

        currentMinCost= float('inf')
        currentDestInTree = None

        reachableVertices = self.get_reachable_vertices(srcNotInTree)
        #print(reachableVertices)
        for dest  in reachableVertices:
            if dest in self.VinTree:
                currentCost = self.get_cost(srcNotInTree, dest)
                if currentCost < currentMinCost:
                    currentMinCost = currentCost
                    currentDestInTree = dest

        return currentDestInTree, currentMinCost
    
    def maintainCheapestEdgeInvariant(self, absorbedVertex):

        reachableVertices = self.get_reachable_vertices(absorbedVertex)
        consideredVertices = []

        for w in reachableVertices:

            if w in self.VNotInTree:
                # delete w from heap

                # recompute key[w] = min {w->abosorbedVertices, currentKey[w]}

                # reinsert into heap

                pass
        return 0

    def get_reachable_vertices(self, src):

        return list(self.graph[src].keys())
    
    def get_cost(self, src, dest):

        return self.graph[src][dest]

    def prim(self):
        return 0
    


if __name__ == "__main__":

    print('>>')

    graph = Graph()
    graph.create_graph('./edges.txt')
    graph.initialize()

