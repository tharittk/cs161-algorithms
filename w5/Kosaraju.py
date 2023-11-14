

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

    def _create_graph(self, inputFile, reverse= False):
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

                if tail not in self.vtxDict.keys():
                    self.vtxDict[tail] = Vertex(tail, [head])
                else:
                    self.vtxDict[tail].edges.append(head)   

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
        n_vtx = len(keysList)

        self.finishingTimeCounter = 0
        self.currentSource = None

        for i in range(n_vtx, 0, -1):
            #key = keysList[i - 1]
            #print('dfs loop i:', key)
            key = str(i)
            if not self.vtxDict[key].isExplored:
                self.currentSource = str(key)
                self.dfs(str(key))









if __name__ == "__main__":
    G = Graph()
    G._create_graph("./scc_small.txt")
    Grev = Graph()
    Grev._create_graph("./scc_small.txt", reverse=True)

    #for key in G.vtxDict.keys():
    #    print(key, G.vtxDict[key].edges)
    
    #for key in Grev.vtxDict.keys():
    #    print(key, Grev.vtxDict[key].edges)

    Grev.dfs_loop()