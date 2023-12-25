

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
        self.finishingTimeCounter = 0
        self.finishingTimeRank = []
        self.currentClusterSize = -1
        self.clusterSizeList = []

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


            if tail not in self.vtxDict.keys():
                self.vtxDict[tail] = Vertex(tail, [head])
            else:
                self.vtxDict[tail].edges.append(head)

    def _append_sink_vertex(self, nvtx):
        # append vtx that does not have outgoing edge
        keysList = self.vtxDict.keys()
        for i in range(1, nvtx + 1):
            vtx = str(i)
            if vtx not in keysList:
                self.vtxDict[vtx] = Vertex(vtx, [])

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
        
        # record the ranking from first to last
        self.finishingTimeRank.append(currentNode)
        
        # for second pass
        self.currentClusterSize += 1
        #print(">> Node ", currentNode, 'f(t): ', self.finishingTimeCounter)
    
    def dfs_loop(self):
        keysList = list(self.vtxDict.keys())
        n_vtx = len(keysList)

        self.finishingTimeCounter = 0
        self.currentSource = None

        for i in range(n_vtx, 0, -1):
            key = str(i)
            if not self.vtxDict[key].isExplored:
                self.currentSource = key
                self.dfs(key)

    def dfs_second_pass(self):
        self.currentClusterSize =  0
        # reverse order, finish last comes first
        for node in self.finishingTimeRank[::-1]:
            
            if not self.vtxDict[node].isExplored:
                self.dfs(node)
            # finish one dfs node
            if self.currentClusterSize != 0:
                self.clusterSizeList.append(self.currentClusterSize)
            # reset the cluster size
            self.currentClusterSize =  0


if __name__ == "__main__":
    import sys, threading, numpy as np
    sys.setrecursionlimit(800000)
    threading.stack_size(67108864)
    def main():

        G = Graph()
        G._create_graph("./scc.txt")
        Grev = Graph()
        Grev._create_graph("./scc.txt", reverse=True)
        print('>>> Done Create: ', len(Grev.vtxDict.keys()))

        nvtx = 875714
        #nvtx = 9
        Grev._append_sink_vertex(nvtx)
        G._append_sink_vertex(nvtx)
        print('>>> Done append Sink: ', len(Grev.vtxDict.keys()))

        Grev.dfs_loop()
        print('>>> Finishing DFS first pass')

        #print(Grev.finishingTimeRank)

        G.finishingTimeRank = Grev.finishingTimeRank

        G.dfs_second_pass()
        
        print('>>> Finishing DFS second pass')
        ans = sorted(G.clusterSizeList, reverse=True)[:10]
        print('Cluster size list Top 5', ans)

    thread = threading.Thread(target=main)
    thread.start()
