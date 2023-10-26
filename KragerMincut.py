
class Graph():
    def __init__ (self):
        self.vtxDict = {}
        self.vtxStatus = {}
    
    def total_alive_vertices(self):
        return sum (self.vtxStatus.values())

    def mergeVertex(self, vtxName1, vtxName2):
        
        vtx1 = self.vtxDict[vtxName1]
        vtx2 = self.vtxDict[vtxName2]

        vtx1.edges.remove(vtxName2)
        vtx2.edges.remove(vtxName1)

        self.vtxStatus[vtxName2] = False

        vtx1.edges += vtx2.edges
        vtx2.pointsToVertexName = vtx1.name
        vtx2.edges = []

        # Clear self-loop

# pick '2' of vertex 3
class Vertex():
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.pointsToVertexName = None



def radomlySelectEdge(G):


    dest = '2'
    # only active vertex
    if G.vtxStatus[dest] == False:
        dest = G.vtxDict[dest].pointsToVertexName



    return dest

def printVtxEdgeList(G):
    for key in G.vtxDict.keys():
        print(key, G.vtxDict[key].edges)

if __name__ == "__main__":

    # read input
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


    while ( G.total_alive_vertices() > 2):
        print("---merge")
        G.mergeVertex('1','2')
        printVtxEdgeList(G)

        print("---merge")

        dest = radomlySelectEdge(G)
        G.mergeVertex(dest,'3')
        printVtxEdgeList(G)

        break



