import sys, threading, numpy as np

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

        self.clusters = []
        self.currentClusterMembers = []

        self.n_vars = None

    def create_graph(self, edges, reverse= False):

        x1_idx = 0 # tail
        x2_idx = 1 # head

        if not reverse:
            for row in range(edges.shape[0]):

                x1 = edges[row, x1_idx]
                x2 = edges[row, x2_idx]

                # not x1 -> x2
                if -x1 not in self.vtxDict.keys():
                    self.vtxDict[-x1] = Vertex(-x1, [x2])
                else:
                    self.vtxDict[-x1].edges.append(x2)

                # not x2 -> x1
                if -x2 not in self.vtxDict.keys():
                    self.vtxDict[-x2] = Vertex(-x2, [x1])
                else:
                    self.vtxDict[-x2].edges.append(x1)
    
        # reverse graph
        else:
            for row in range(edges.shape[0]):

                x1 = edges[row, x1_idx]
                x2 = edges[row, x2_idx]

                # x2 -> not x1
                if x2 not in self.vtxDict.keys():
                    self.vtxDict[x2] = Vertex(x2, [-x1])
                else:
                    self.vtxDict[x2].edges.append(-x1)

                # x1 -> not x2
                if x1 not in self.vtxDict.keys():
                    self.vtxDict[x1] = Vertex(x1, [-x2])
                else:
                    self.vtxDict[x1].edges.append(-x2)
    
    def append_sink_vertex(self):
        # append vtx that does not have outgoing edge
        keysList = self.vtxDict.keys()
        for vtx in range(-self.n_vars, 0, 1):
            if vtx not in keysList:
                self.vtxDict[vtx] = Vertex(vtx, [])
                #print(vtx, 'has no outgoing')

        for vtx in range(1, self.n_vars + 1):
            if vtx not in keysList:
                self.vtxDict[vtx] = Vertex(vtx, [])
                #print(vtx, 'has no outgoing')
                

    def dfs(self, currentNode):
        #print('explored, ', currentNode)
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
        self.currentClusterMembers.append(currentNode)
        #print("cluster size: ", self.currentClusterSize)
        #print(">> Node ", currentNode, 'f(t): ', self.finishingTimeCounter)
    
    def dfs_loop(self):

        self.finishingTimeCounter = 0
        self.currentSource = None


        for key in range( self.n_vars, -self.n_vars - 1, -1):
            if key != 0:
        
        #for key in self.vtxDict.keys:
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
            #if self.currentClusterSize != 0 :
            if self.currentClusterSize > 1:

                self.clusterSizeList.append(self.currentClusterSize)
                self.clusters.append(self.currentClusterMembers)
            # reset the cluster size
            self.currentClusterSize =  0
            self.currentClusterMembers = [] #reset



if __name__ == "__main__":
    import sys, threading, numpy as np
    sys.setrecursionlimit(800000)
    threading.stack_size(67108864)
    def main():

        #big = 2,3,5

        #1 = 1
        #2 = 0
        #3 = 1
        #4 = 1
        #5 = 0
        #6 = 0

        i = 6
        edges = np.loadtxt('./2sat{i}.txt'.format(i=i), dtype=int, skiprows=1 )
        n_clauses = edges.shape[0]
        #n_vtx = 5 # test cases
        n_vtx = n_clauses # PSET config

        G = Graph()
        G.create_graph(edges)
        #print('>>> Done Create: ', len(G.vtxDict.keys()))
        
        Grev = Graph()
        Grev.create_graph(edges, reverse = True)
        
        #print('>>> Done Create reverse: ', len(Grev.vtxDict.keys()))

        G.n_vars = n_vtx
        Grev.n_vars = n_vtx

        Grev.append_sink_vertex()
        G.append_sink_vertex()
        #print('>>> Done append Sink: ', len(Grev.vtxDict.keys()))

        Grev.dfs_loop()
        #print('>>> Finishing DFS on REV')
        G.finishingTimeRank = Grev.finishingTimeRank
        #print("time rank reverse", G.finishingTimeRank[::-1])

        G.dfs_second_pass()
        
        #print('>>> Finishing DFS second pass on Normal')

        ans = G.clusterSizeList
        members = G.clusters
        print('Cluster members', members)
        print('Cluster size list', ans)
        print('Number of SCC: ', len(ans))

        # CHECK inside cluster

        for cluster in members:
            for member in cluster:
                for member2 in cluster:
                    if (member + member2) == 0:
                        print('impossible', member, member2,'in',cluster) 

    thread = threading.Thread(target=main)
    thread.start()

