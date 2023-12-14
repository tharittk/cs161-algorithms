from AllPair_ShortestPath import *

class Bellman_Ford():

    def __init__(self, G, source):
        self.G = G #input graph
        self.s = source
        self.A = None
        self.out = None

    def initialize_2D(self):
        A = [[] for i in range(self.G.m + 1)] # edge budget up to m (to check negative cycle)
        for i in range(self.G.m + 1):
            A[i] = [float('inf') for j in range(self.G.n + 1)]  # vertex  
        # v != s
        for v in range(1,self.G.n + 1):
            A[0][v] = float('inf')
        # v == s
        A[0][self.s] = 0
        self.A = A

    def run(self):
        # edge budget from 1 upto m - 1
        for i in range(1, self.G.m + 1):
            if i % 1000 == 0:
                print(i)
            for v in range(1, self.G.n + 1):
                try:
                    min_cost = float('inf')
                    for w in self.G.thc[v].keys(): # incoming edge of v
                        current_cost = self.A[i-1][w] + self.G.thc[v][w]

                        if current_cost < min_cost:
                            min_cost = current_cost


                        #incoming_cost.append(self.A[i-1][w] + self.G.thc[v][w])

                    self.A[i][v] = min( self.A[i - 1][v], min_cost)

                except: # no incoming edge
                    self.A[i][v] = self.A[i-1][v]

            # Stop early
            if self.A[i] == self.A[i - 1]:
                print("Stop Early")

                self.out = self.A[i]
                break        

        if self.A[-1] != self.A[-2]:
            print("Negative-cost Cycle exist")
        else:
            print("No Negtive-cost cycle")
            print('After-run A: ', self.out[-10:])

            for i in self.out[1:]:
                if i == float('inf'):
                    print('incomplete algorithms')


if __name__ == "__main__":
    g = Graph()
    g.read_text_input('./g3.txt')

    #g.read_text_input('./small_g.txt')

    BF = Bellman_Ford(g, 1)
    BF.initialize_2D()
    BF.run()

    print("Graph n: ", g.n, "m: ", g.m)
    #print('After run A final: ', BF.A)
