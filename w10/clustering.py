import numpy as np


class UnionFind():

    def __init__(self, n):
        self.num_nodes = n
        self.parents = np.arange(n) + 1
        self.ranks = np.zeros(n)


    def get_parent_of_node(self, i):
        return self.parents[i - 1]
    
    def get_rank_of_node(self, i):
        return self.ranks[i - 1]

    def increase_rank_of_node(self, i):
        self.ranks[i - 1] += 1

    def change_parent_of_node(self, i, parent_node):

        self.parents[i - 1] = parent_node

    
    def union(self, i, j):
        rank_parent_i = self.get_rank_of_node( self.find(i) )
        rank_parent_j = self.get_rank_of_node( self.find(j) )

        #rank_parent_i = self.get_rank_of_node( self.get_parent_of_node(i) )
        #rank_parent_j = self.get_rank_of_node( self.get_parent_of_node(j) )

        if rank_parent_i == rank_parent_j:
            self.change_parent_of_node(self.get_parent_of_node(j), self.get_parent_of_node(i)) # arbitary
            self.increase_rank_of_node(self.get_parent_of_node(i))

        elif rank_parent_i > rank_parent_j:
            self.change_parent_of_node(self.get_parent_of_node(j), self.get_parent_of_node(i))

        else:
            self.change_parent_of_node(self.get_parent_of_node(i), self.get_parent_of_node(j))


    # helper function to check number of clusters
    def find(self, i):
        # itself is a root
        if self.get_parent_of_node(i) == i:
            return i
        else:
            parent = self.find( self.get_parent_of_node(i) )
            self.change_parent_of_node(i, parent)

            return parent

    def exhaust_find(self):
        for i in range(1, self.num_nodes + 1):
            self.find(i)

class Graph():

    def __init__(self):
        self.num_nodes = None

        self.e1 = []
        self.e2 = []
        self.cost = []

    def read_text_input(self, file_name):
    
        with open(file_name) as f:

            self.num_nodes = int(f.readline().strip())

            for line in f.readlines():
                line = line.strip().split(" ")
                self.e1.append(int(line[0]))
                self.e2.append(int(line[1]))
                self.cost.append(int(line[2]))

    def create_sorted_edges(self):
        tmp = np.array(list(zip(self.e1, self.e2, self.cost)), dtype=[('e1', 'int'), ('e2', 'int'), ('cost', 'int')])
        sort_order = np.argsort(tmp, order = ['cost'])

        data_structure = tmp[sort_order]
        self.e1e2cost_sorted = data_structure


def main():
    return 0

    # while cluster size != k i.e. len(self.leader) != k
    #self.leaders.pop(self.leaders.index(absorbedVertex))

if __name__ == "__main__":
    uf = UnionFind(11)

    '''
    print('parents before union:', uf.parents)
    #print('rank before union:', uf.ranks)

    uf.union(1,2)
    uf.union(2,3)
    uf.union(3,4)
    uf.union(5,6)
    uf.union(6,7)
    uf.union(8,9)
    uf.union(10,11)
    #uf.union(8,2)
    #uf.union(10,8)
    #uf.union(7,2)

    print('parents after union :', uf.parents)

    uf.exhaust_find()

    print('parents after exhaust find :', uf.parents)
    '''

    #print(uf.find(2) == uf.find(3))
    #print(uf.find(11) == uf.find(8))




    # initialize data structure


    g = Graph()
    g.read_text_input('./cluster_small.txt')
    g.create_sorted_edges()

    n_edges = len(g.cost)
    uf = UnionFind(g.num_nodes)

    n_cluster = g.num_nodes

    k = 3

    for i in range(n_edges):

        e1 = g.e1e2cost_sorted['e1'][i]
        e2 = g.e1e2cost_sorted['e2'][i]
        cost = g.e1e2cost_sorted['cost'][i]

        # if has no cycle
        if uf.find(e1) != uf.find(e2):
            
            uf.union(e1, e2)

            # for sure not creating a cycle, reduce number of cluster by 1
            n_cluster = n_cluster - 1
        
        # stop early
        if n_cluster <= k:
            break

    print('before exhaust find', np.unique(uf.parents))
    uf.exhaust_find()

    print('after exhaust find', np.unique(uf.parents))
