from AllPair_ShortestPath import *

class Bellman_Ford():

    def __init__(self, G, source):
        self.G = G #input graph
        self.s = source
        self.A = None

    def initialize_2D(self):
        A = [[] for i in range(self.G.m)] # edge budget up to m - 1
        for i in range(self.G.m):
            A[i] = [float('inf') for j in range(self.G.n + 1)]  # vertex  
        # v != s
        for v in range(1,self.G.n + 1):
            A[0][v] = float('inf')
        # v == s
        A[0][self.s] = 0
        self.A = A

    def run(self):
        # edge budget from 1 upto m - 1
        for i in range(1, self.G.m):
            for v in range(1, self.G.n + 1):
            #for v in self.G.thc.keys(): # only those that has incoming edge
            
                #print('tail',v,': ', self.G.thc[v])
                try:
                    incoming_cost = []
                    for w in self.G.thc[v].keys(): # incoming edge of v
                        incoming_cost.append(self.A[i-1][w] + self.G.thc[v][w])
                    self.A[i][v] = min( self.A[i - 1][v], min(incoming_cost))
                    
                except: # no incoming edge
                    self.A[i][v] = self.A[i-1][v]



if __name__ == "__main__":
    g = Graph()
    g.read_text_input('./small_g.txt')

    BF = Bellman_Ford(g, 1)
    BF.initialize_2D()

    print('source: ', BF.s)
    print('init A: ', BF.A)

    BF.run()
    print('After run A: ', BF.A)

