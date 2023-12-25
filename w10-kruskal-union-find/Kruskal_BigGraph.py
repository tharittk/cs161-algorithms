from Kruskal_UnionFind import UnionFind

class HammingEdges():

    def __init__(self):
        self.n_nodes = None
        self.n_bits = None

        self.node_bits_int = []

        self.dist_node = {}

    def read_hamming_input(self, file_name):
    
        with open(file_name) as f:

            tmp =  f.readline().strip().split(" ")
            self.n_nodes = int(tmp[0])
            self.n_bits =  int(tmp[1])

            i = 1
            dup = 0
            for line in f.readlines():
                bin_str = ''.join(line.strip().split(" "))
                bin_int = (int(bin_str, 2))
                self.node_bits_int.append(bin_int)

                if bin_int in self.dist_node.keys():
                    self.dist_node[bin_int].append(i)
                    dup += 1
                else:
                    self.dist_node[bin_int] = [i]

                i += 1
        #print(len(self.dist_node.keys()))

    def search_for_neighbors_with_cost(self, current_node, cost):
        e2 = []
        node_idx = current_node - 1
        current_bit = self.node_bits_int[node_idx]

        if cost == 0:
            exact_neighbors = self.dist_node[current_bit]
            for j in exact_neighbors:
                if j != current_node:
                    e2.append(j)

            #self.dist_node[current_bit] = [] # test of double counting

        # if wants it to be more general, 
        # generate the tuple size (n_bits ^ n_cost - 24 x 24 for all permutation)
        
        elif cost == 1:
        # cost is 1
            for shift in range(self.n_bits):
                new_code  = current_bit ^ (1 << shift)
                #if new_code in self.dist_node.keys():
                try:
                    neighbors = self.dist_node[new_code]
                    for j in neighbors:
                        e2.append(j)
                except:
                    pass
        
        # cost is 2
    
        elif cost == 2:
            for shift_1 in range(self.n_bits):
                for shift_2 in range(self.n_bits):
                    new_code  = current_bit ^ (1 << shift_1) ^ (1 << shift_2) 
                    
                    #if new_code in self.dist_node.keys():
                    try: 
                        neighbors = self.dist_node[new_code]
                        for j in neighbors:
                            e2.append(j)
                    except:
                        pass

        return e2
    
class Graph():

    def __init__(self, n):
        self.n_nodes = n

        self.e1 = []
        self.e2 = []
        self.cost = []

    def appoint_e1_e2_cost(self, e1_node, e2_node_list, cost):

        for i in range(len(e2_node_list)):
            self.e1.append(e1_node)
            self.e2.append(e2_node_list[i])
            self.cost.append(cost)


if __name__ == "__main__":

    h = HammingEdges()
    h.read_hamming_input('./cluster_big.txt')
    g = Graph(h.n_nodes)
    max_cost = 2
    for cost in range(0,max_cost + 1):

        for node in range(1, h.n_nodes + 1):

            e2_list= h.search_for_neighbors_with_cost(node, cost)

            if e2_list != []:

                g.appoint_e1_e2_cost(node, e2_list,cost)

    print(len(g.e1))
    print(len(g.e2))
    print(len(g.cost))

    print(g.e1[:10])
    print(g.e2[:10])
    print(g.cost[:10])

  
    n_edges = len(g.cost)
    uf = UnionFind(g.n_nodes)
    n_cluster = g.n_nodes

    for i in range(n_edges):

        e1 = g.e1[i]
        e2 = g.e2[i]
        cost = g.cost[i]

        # if has no cycle
        if uf.find(e1) != uf.find(e2):
            
            uf.union(e1, e2)

            #if n_cluster <= k:
            #    print(e1,e2, cost)

            # for sure not creating a cycle, reduce number of cluster by 1

            n_cluster = n_cluster - 1
    print("start n_cluster:" , g.n_nodes)
    print("Final n_cluster:" , n_cluster)