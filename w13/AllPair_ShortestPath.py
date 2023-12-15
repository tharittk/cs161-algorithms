from BellmanFord import *
from Dijkstra import * 

class Graph():

    def __init__(self):
        self.n = None
        self.m = None
        self.thc= {} # tail-head-cost
        self.htc = {} # head-tail-cost (for Dijkstra)

    def read_text_input(self, file_name):
    
        with open(file_name) as f:
            line = f.readline().strip().split(" ")
            self.n = int(line[0])
            self.m = int(line[1])

            for line in f.readlines():
                line = line.strip().split(" ")
                tail = int(line[0])
                head = int(line[1])
                cost = int(line[2])

                # for Bellman-Ford
                if tail not in self.thc.keys():
                    self.thc[tail] = {}
                    self.thc[tail][head] = cost
                else:
                    self.thc[tail][head] = cost

                # for Dijkstra
                if head not in self.htc.keys():
                    self.htc[head] = {}
                    self.htc[head][tail] = cost
                else:
                    self.htc[head][tail] = cost     

    def read_legacy_dijkstra(self, input_file):
        with open(input_file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('\t')
                head = int(line[0])
                for i in range(1, len(line) - 1): # exclude tail and new line char
                    tail, cost = line[i].split(',')

                    tail = int(tail)
                    cost = int(cost)

                    # for Bellman-Ford
                    if tail not in self.thc.keys():
                        self.thc[tail] = {}
                        self.thc[tail][head] = cost
                    else:
                        self.thc[tail][head] = cost

                    # for Dijkstra
                    if head not in self.htc.keys():
                        self.htc[head] = {}
                        self.htc[head][tail] = cost
                    else:
                        self.htc[head][tail] = cost     

    def append_external_source_vertex(self, external_source):
        
        new_s = external_source
        self.htc[new_s] = {}

        # add edge cost 0 to every other vertex
        for i in range(1, self.n + 1):
            self.htc[new_s][i] = 0
            
            if i not in self.thc.keys():
                self.thc[i] = {}

            self.thc[i][new_s] = 0

            self.m += 1
            
        self.n = self.n + 1

    def reweighting(self):
        pass

if __name__ == "__main__":
    
    g = Graph()
    #g.read_text_input('./g3.txt')
    #g.read_text_input('./small_g.txt')
    g.read_text_input('./johnson_g.txt')
    
    g.append_external_source_vertex(g.n + 1)

    print('tail <- head', g.thc)
    print('head -> tail', g.htc)

    BF = Bellman_Ford(g)

    BF.initialize_2D(g.n)

    BF.run()
    #print(BF.A)

    print("Graph n: ", g.n, "m: ", g.m)

    #print(BF.A)