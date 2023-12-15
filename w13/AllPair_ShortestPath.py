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


def reweighting_and_create_graph(file_name, weigths):
    
    g = Graph()
    with open(file_name) as f:
        line = f.readline().strip().split(" ")
        g.n = int(line[0])
        g.m = int(line[1])

        for line in f.readlines():
            line = line.strip().split(" ")
            tail = int(line[0])
            head = int(line[1])
            cost = int(line[2])

            # for Bellman-Ford
            cost = cost + weights[head] - weights[tail]
            if tail not in g.thc.keys():
                g.thc[tail] = {}
                g.thc[tail][head] = cost
            else:
                g.thc[tail][head] = cost

                # for Dijkstra
            if head not in g.htc.keys():
                g.htc[head] = {}
                g.htc[head][tail] = cost
            else:
                g.htc[head][tail] = cost   

    return g
    
def get_true_score(weights, raw_score, source_vertex):
    true_score = {}
    for dest in raw_score.keys():
        true_score[dest] = raw_score[dest] - weights[source_vertex] + weights[dest]
    
    return true_score



if __name__ == "__main__":
    
    g = Graph()
    #g.read_text_input('./g3.txt')
    #g.read_text_input('./small_g.txt')
    g.read_text_input('./johnson_g.txt')
    
    g.append_external_source_vertex(g.n + 1)
    #print('tail <- head', g.thc)
    #print('head -> tail', g.htc)

    BF = Bellman_Ford(g)
    BF.initialize_2D(g.n)
    weights = BF.run()[:-1] # exclude the last psuedo-source vertex
    #print(weights)

    g_rewighted = reweighting_and_create_graph('./johnson_g.txt', weights)
    print(">> Creating reweight graph")
    #g_rewighted = reweighting_and_create_graph('./g3.txt', weights)

    #print('After reweight (head -> tail)', g_rewighted.htc)
    #print('After reweight (tail <- head)', g_rewighted.thc)

    #print("Graph n: ", g.n, "m: ", g.m)
    # all node as source

    min_from_all_source = []
    for s in range(1, g_rewighted.n + 1):
        if s % 20 == 0:
            print(">> Running Dijkstra: ", s)

        source_vertex = s
        raw_score = dijkstra(g_rewighted, source_vertex)
        true_score = get_true_score(weights, raw_score, source_vertex)

        min_score = min(true_score.values())

        min_from_all_source.append(min_score)
    #print('After Dijsktra (True score all):', min_from_all_source)

    print('After Dijsktra (True score min):', min(min_from_all_source))
