import numpy as np


class UnionFind():

    def __init__(self, n):
        self.num_nodes = n
        self.parents = np.arange(n) + 1
        self.ranks = np.zeros(n)
        self.leaders = [i for i in range(1, n+1)]


    def get_parent_of_node(self, i):
        return self.parents[i - 1]
    
    def get_rank_of_node(self, i):
        return self.ranks[i - 1]

    def increase_rank_of_node(self, i):
        self.ranks[i - 1] += 1

    def change_parent_of_node(self, i, parent_node):
        self.parents[i - 1] = parent_node
    
    def union(self, i, j):
        #rank_parent_i = self.get_rank_of_node( self.find(i) )
        #rank_parent_j = self.get_rank_of_node( self.find(j) )

        rank_parent_i = self.get_rank_of_node( self.get_parent_of_node(i) )
        rank_parent_j = self.get_rank_of_node( self.get_parent_of_node(j) )

        if rank_parent_i == rank_parent_j:
            self.change_parent_of_node(self.get_parent_of_node(j), self.get_parent_of_node(i)) # arbitary
            self.increase_rank_of_node(self.get_parent_of_node(i))

        elif rank_parent_i > rank_parent_j:
            self.change_parent_of_node(j, self.get_parent_of_node(i))
        else:
            self.change_parent_of_node(i, self.get_parent_of_node(j))

    def find(self, i):
        # itself is a root
        if self.get_parent_of_node(i) == i:
            return i
        else:
            parent = self.find( self.get_parent_of_node(i) )
            self.change_parent_of_node(i, parent)

            return parent


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

def main():
    return 0

    # while cluster size != k i.e. len(self.leader) != k
    #self.VNotInTree.pop(self.VNotInTree.index(absorbedVertex))

if __name__ == "__main__":
    uf = UnionFind(11)

    
    print('parents before union:', uf.parents)

    uf.union(1,2)
    uf.union(2,3)
    uf.union(3,4)
    uf.union(5,6)
    uf.union(6,7)
    uf.union(8,9)
    uf.union(10,11)

    print('parents after union:', uf.parents)
    print('ranks: ', uf.ranks)
    uf.union(8,2)
    uf.union(10,1)

    print('parents after union tie:', uf.parents)
    print('ranks: ', uf.ranks)
    print(uf.find(11))
    print(uf.parents)
    

    #g = Graph()
    #g.read_text_input('./cluster_small.txt')
    #print(len(g.e1))
