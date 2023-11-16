class Vertex():
    def __init__ (self, name, destDistanceDict):
        self.name = name
        self.edgeDestDistance = destDistanceDict


class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.lastPointScoreDict = {}

    def _create_graph(self, inputFile):
        with open(inputFile) as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('\t')
                destDistanceDict = {}
                nodeName = line[0]
                for i in range(1, len(line) - 1): # exclude tail and new line char
                    dest, dist = line[i].split(',')
                    destDistanceDict[dest] = dist

                self.vtxDict[nodeName] = Vertex(nodeName, destDistanceDict)

    def dijkstra(self, nodeStart = '1'):

        nNodes = len(self.vtxDict.keys())

        # initialization
        vtxExplored = [nodeStart]
        vtxUnexplored = list(self.vtxDict.keys())
        vtxUnexplored.remove(nodeStart)

        self.lastPointScoreDict[nodeStart]  = 0
        isExhausted = False
        while not isExhausted:
            currMinScore = 9999999
            isExhausted = True # must invalidate this in loop

            for node in vtxExplored:

                for dest in list(self.vtxDict[node].edgeDestDistance.keys()):
                    if dest not in vtxExplored:
                        isExhausted = False
                        # calculate
                        currScore = (self.lastPointScoreDict[node] + int(self.vtxDict[node].edgeDestDistance[dest]))

                        if currScore < currMinScore:
                            currMinScore = currScore
                            currDest = dest
                            #currNode = node
            # get the edge wanted
            if isExhausted:
                break
            self.lastPointScoreDict[currDest]= currMinScore
            vtxExplored.append(currDest)
            vtxUnexplored.remove(currDest) 

        # for those unreachable
        for node in vtxUnexplored:
            self.lastPointScoreDict[node] = 1000000



if __name__ == "__main__":
    G = Graph()
    G._create_graph("./dijkstraData.txt")

    G.dijkstra()

    print(len(G.lastPointScoreDict.keys()))

    Ans = ''
    toAns = [7,37,59,82,99,115,133,165,188,197]
    for id in toAns:
        Ans += (str(G.lastPointScoreDict[str(id)]) +',')
    print('>> Ans: ', Ans)