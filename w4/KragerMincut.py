import random

class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.vtxStatus = {}
    
    def total_alive_vertices(self):
        return sum (self.vtxStatus.values())

    def mergeVertex(self, srcName, destName):

        srcNameFinal = srcName
        destNameFinal = destName

        if G.vtxStatus[src] == False:
            while G.vtxStatus[srcNameFinal] == False:
                srcNameFinal = G.vtxDict[srcNameFinal].pointsToVertexName

        if G.vtxStatus[dest] == False:
            while G.vtxStatus[destNameFinal] == False:
                destNameFinal = G.vtxDict[destNameFinal].pointsToVertexName


        # for future randomization
        srcVtx = self.vtxDict[srcName]
        srcVtx.remainingEdges.remove(destName)
        destVtx = self.vtxDict[destName]
        destVtx.remainingEdges.remove(srcName)

        # to prevent case of edge within the merge group
        if srcNameFinal != destNameFinal:

            # set inactive
            self.vtxStatus[destNameFinal] = False 

            # consolidate edge to the parent
            srcVtxFinal = self.vtxDict[srcNameFinal]
            destVtxFinal = self.vtxDict[destNameFinal]

            # remove original name
            srcVtxFinal.edges.remove(destName)
            destVtxFinal.edges.remove(srcName)

            # consolidate edge
            srcVtxFinal.edges += destVtxFinal.edges
            destVtxFinal.pointsToVertexName = srcVtxFinal.name
            destVtxFinal.edges = []

            # consolidate the child to the parent
            srcVtxFinal.childVertexName += (destVtxFinal.childVertexName + [destVtxFinal.name])

            # clear self-loop
            for childName in srcVtxFinal.childVertexName:

                while childName in srcVtxFinal.edges:
                    srcVtxFinal.edges.remove(childName)

            while srcVtxFinal.name in srcVtxFinal.edges:
                srcVtxFinal.edges.remove(srcVtxFinal.name)


class Vertex():
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.pointsToVertexName = None
        self.childVertexName = []
        self.remainingEdges = edges[:] # to keep track


def radomlySelectEdge(G):
    idxVtx = random.randint(0, len(G.vtxDict) - 1)
    randVtxName = list(G.vtxDict.keys())[idxVtx]

    # Random sampling until not empty node
    while G.vtxDict[randVtxName].remainingEdges == []:
        idxVtx = random.randint(0, len(G.vtxDict) - 1)
        randVtxName = list(G.vtxDict.keys())[idxVtx]

    idxEdge = random.randint(0, len(G.vtxDict[randVtxName].remainingEdges) -1 )
    randEdgeName = G.vtxDict[randVtxName].remainingEdges[idxEdge]

    return randVtxName, randEdgeName


def printVtxEdgeList(G):
    for key in G.vtxDict.keys():
        print(key, G.vtxDict[key].edges, 'child: ',  G.vtxDict[key].childVertexName)

if __name__ == "__main__":
    results = []
    for i in range(1):
        random.seed(i)

        G = Graph()
        #with open('pa4.txt') as f:
        with open('kargerMincut.txt') as f:
            lines = f.readlines()
            for line in lines:
                ve = line.strip().split('\t')
                vtxName = ve[0]
                edges = ve[1:]
                
                vertex = Vertex(vtxName, edges)
                G.vtxDict[vertex.name] = vertex
                G.vtxStatus[vertex.name] = True

        while ( G.total_alive_vertices() > 2 ):

            src, dest = radomlySelectEdge(G)

            G.mergeVertex(src, dest)

        for key in G.vtxDict.keys():
            if G.vtxStatus[key] == True:
                #print(key, 'edge len: ', len(G.vtxDict[key].edges))
                result = len(G.vtxDict[key].edges)

        results.append(result)
    print(results)
    print(min(results))

    #printVtxEdgeList(G)



