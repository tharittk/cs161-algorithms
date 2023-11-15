

class Vertex():
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.isExplored = False
        self.finishingTime = None

class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.currentLeader = None
        self.currentSource = None
        self.finishingTimeCounter = None
        #self.vtxList = []

    def _create_graph_old(self, inputFile, reverse= False):
        with open(inputFile) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n').split(' ')
                if not reverse:
                    tail = line[0]
                    head = line[1]
                else:
                    head = line[0]
                    tail = line[1]

                if tail not in self.vtxList:
                    self.vtxList.append(tail)
                if head not in self.vtxList:
                    self.vtxList.append(head)

                if tail not in self.vtxDict.keys():
                    self.vtxDict[tail] = Vertex(tail, [head])
                else:
                    self.vtxDict[tail].edges.append(head)

        # append vtx that does not have outgoing edge
        for vtx in self.vtxList:
            if vtx not in self.vtxDict.keys():
                self.vtxDict[vtx] = Vertex(vtx, [])
                 

    def _create_graph(self, inputFile, reverse= False):

        edges = np.loadtxt(inputFile, dtype='str')
        if not reverse:
            tailIdx = 0
            headIdx = 1
        else:
            tailIdx = 1
            headIdx = 0

        for row in range(edges.shape[0]):

            tail = edges[row, ][tailIdx]
            head = edges[row, ][headIdx]

            # TOO SLOW to implement
            #if tail not in self.vtxList:
            #        self.vtxList.append(tail)
            #if head not in self.vtxList:
            #        self.vtxList.append(head)

            if tail not in self.vtxDict.keys():
                self.vtxDict[tail] = Vertex(tail, [head])
            else:
                self.vtxDict[tail].edges.append(head)

            if row % 100000 == 0:
                print(row)

        # append vtx that does not have outgoing edge
        #for vtx in self.vtxList:
        #    if vtx not in self.vtxDict.keys():
        #        self.vtxDict[vtx] = Vertex(vtx, [])

    def dfs(self, currentNode):
        # mark explored
        self.vtxDict[currentNode].isExplored = True
        # set leader node
        self.currentLeader = self.currentSource
        for head in self.vtxDict[currentNode].edges:

            if not self.vtxDict[head].isExplored:
                self.dfs(head)
        
        self.finishingTimeCounter += 1
        self.vtxDict[currentNode].finishingTime = self.finishingTimeCounter

        print(">> Node ", currentNode, 'f(t): ', self.finishingTimeCounter)
    
    def dfs_loop(self):
        keysList = list(self.vtxDict.keys())
        n_vtx = len(self.vtxList)

        self.finishingTimeCounter = 0
        self.currentSource = None

        for i in range(n_vtx, 0, -1):
            key = str(i)
            if not self.vtxDict[key].isExplored:
                self.currentSource = str(key)
                self.dfs(str(key))

        #for key in keysList:
        #    if not self.vtxDict[key].isExplored:
        #        self.currentSource = key
        #        self.dfs(key)



if __name__ == "__main__":
    import sys, threading, numpy as np
    sys.setrecursionlimit(800000)
    threading.stack_size(67108864)
    def main():

        G = Graph()
        G._create_graph("./scc_small.txt")
        Grev = Graph()
        Grev._create_graph("./scc.txt", reverse=True)

        #for key in G.vtxDict.keys():
        #    print(key, G.vtxDict[key].edges)
        
        #for key in Grev.vtxDict.keys():
        #    print(key, Grev.vtxDict[key].edges)

        #Grev.dfs_loop()

        print('>>>', len(Grev.vtxDict.keys()))

        #for i in range(10):
        #    print(str(arr[i,0]), str(arr[i,1]))

    thread = threading.Thread(target=main)
    thread.start()
