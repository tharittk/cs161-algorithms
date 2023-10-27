import random

class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.vtxStatus = {}
    
    def total_alive_vertices(self):
        return sum (self.vtxStatus.values())

    def mergeVertex(self, srcName, destName):

        #print('in src: ', srcName, 'in dest: ', destName)

        srcNameFinal = srcName
        destNameFinal = destName

        if G.vtxStatus[src] == False:
            #isChildSrc = True
            while G.vtxStatus[srcNameFinal] == False:
                srcNameFinal = G.vtxDict[srcNameFinal].pointsToVertexName

        if G.vtxStatus[dest] == False:
            #isChildDest = True
            while G.vtxStatus[destNameFinal] == False:
                destNameFinal = G.vtxDict[destNameFinal].pointsToVertexName


        # for future randomization
        srcVtx = self.vtxDict[srcName]
        srcVtx.remainingEdges.remove(destName)
        destVtx = self.vtxDict[destName]
        destVtx.remainingEdges.remove(srcName)



        if srcNameFinal != destNameFinal:

            # set inactive
            self.vtxStatus[destNameFinal] = False 
            #print(destNameFinal, 'becomes inactive')
            #print('in srcFinal: ', srcNameFinal, 'in destFinal: ', destNameFinal)

            # consolidate edge to the parent
            srcVtxFinal = self.vtxDict[srcNameFinal]
            destVtxFinal = self.vtxDict[destNameFinal]


            # remove original name

            srcVtxFinal.edges.remove(destName)
            destVtxFinal.edges.remove(srcName)


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

    # inactive vertex
    #randVtxNameOrig= randVtxName # save original

    #while G.vtxStatus[randVtxName] == False:
    #    randVtxName = G.vtxDict[randVtxName].pointsToVertexName
    #    isChildSrc = True

    idxEdge = random.randint(0, len(G.vtxDict[randVtxName].remainingEdges) -1 )
    randEdgeName = G.vtxDict[randVtxName].remainingEdges[idxEdge]

    return randVtxName, randEdgeName


def printVtxEdgeList(G):
    for key in G.vtxDict.keys():
        print(key, G.vtxDict[key].edges, 'child: ',  G.vtxDict[key].childVertexName)

if __name__ == "__main__":
    random.seed(11)

    G = Graph()
    #with open('pa4.txt') as f:
    with open('kargerMincut.txt') as f:
    #with open('graph.txt') as f:

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
            print(key, 'edge len', len(G.vtxDict[key].edges))

    #printVtxEdgeList(G)



