
class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.vtxStatus = {}
    
    def total_alive_vertices(self):
        return sum (self.vtxStatus.values())

    
    def mergeVertex(self, srcName, destName):

        srcVtx = self.vtxDict[srcName]
        srcVtx.edges.remove(destName)

        # Trace back to the active
        while G.vtxStatus[destName] == False:
            destName = G.vtxDict[destName].pointsToVertexName
        destVtx = self.vtxDict[destName]
        destVtx.edges.remove(srcName)
        
        # inactivate the vertex
        self.vtxStatus[destName] = False 

        # consolidate edge to the parent
        srcVtx.edges += destVtx.edges
        destVtx.pointsToVertexName = srcVtx.name
        destVtx.edges = []

        # consolidate the child to the parent
        srcVtx.childVertexName += (destVtx.childVertexName + [destVtx.name])

        # Clear self-loop
        for childName in srcVtx.childVertexName:

            if childName in srcVtx.edges:
                #print('dropping ', childName)
                #print(srcVtx.name, 'has child ', srcVtx.childVertexName, 'edge list', srcVtx.edges)
                srcVtx.edges.remove(childName)



class Vertex():
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.pointsToVertexName = None
        self.childVertexName = []


def radomlySelectEdge(G):
    # manual testing
    src = '1'
    dest = '3'

    return src, dest

def printVtxEdgeList(G):
    for key in G.vtxDict.keys():
        print(key, G.vtxDict[key].edges, 'child: ',  G.vtxDict[key].childVertexName)

if __name__ == "__main__":

    G = Graph()
    #with open('kargerMincut.txt') as f:
    with open('graph.txt') as f:

        lines = f.readlines()
        for line in lines:
            ve = line.strip().split('\t')
            vtxName = ve[0]
            edges = ve[1:]
            
            vertex = Vertex(vtxName, edges)
            G.vtxDict[vertex.name] = vertex
            G.vtxStatus[vertex.name] = True

        printVtxEdgeList(G)

    while ( G.total_alive_vertices() > 2 ):
        print("---merge")
        G.mergeVertex('1','2')
        printVtxEdgeList(G)

        print("---merge")

        src, dest = radomlySelectEdge(G)

        G.mergeVertex(src, dest)
        printVtxEdgeList(G)

        break



