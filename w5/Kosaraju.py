
class Graph():
    def __init__ (self):
        self.vtxDict = {}

    def _create_graph(self, inputFile):
        with open(inputFile) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n').split(' ')
                tail = line[0]
                head = line[1]
                if tail not in self.vtxDict.keys():
                    self.vtxDict[tail] = Vertex(tail, [head])
                else:
                    self.vtxDict[tail].edges.append(head)
    
    def _create_reverseGraph(self, inputFile):
        with open(inputFile) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n').split(' ')
                head = line[0]
                tail = line[1]
                if tail not in self.vtxDict.keys():
                    self.vtxDict[tail] = Vertex(tail, [head])
                else:
                    self.vtxDict[tail].edges.append(head)
    

class Vertex():
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.isExplored = False


if __name__ == "__main__":
    G = Graph()
    G._create_graph("./scc_small.txt")
    Grev = Graph()
    Grev._create_reverseGraph("./scc_small.txt")

    #for key in G.vtxDict.keys():
    #    print(key, G.vtxDict[key].edges)
    
    for key in Grev.vtxDict.keys():
        print(key, Grev.vtxDict[key].edges)