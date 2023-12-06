import numpy as np


class UnionFind():

    def __init__(self, n):
        self.num_nodes = n
        self.parents = np.arange(n) + 1
        self.ranks = np.ones(n)


    def get_parent_of_node(self, i):
        return self.parents[i - 1]
    
    def get_rank_of_node(self, i):
        return self.ranks[i - 1]

    def increase_rank_of_node(self, i):
        self.ranks[i - 1] += 1

    def change_parent_of_node(self, i, parent_node):
        self.parents[i - 1] = parent_node
    
    def union(self, i, j):

        rank_i = self.get_rank_of_node(i)
        rank_j = self.get_rank_of_node(j)

        if rank_i >= rank_j:
            self.change_parent_of_node[j, i]
            self.increase_rank_of_node[i]
        else:
            self.change_parent_of_node[i, j]
            self.increase_rank_of_node[j]

    def find(self, i):
        # itself is a root
        if self.get_parent_of_node(i) == i:
            return i
        else:
            parent = self.find( self.get_parent_of_node(i) )
            self.change_parent_of_node(i, parent)

            return parent




if __name__ == "__main__":
    uf = UnionFind(4)

    print(uf.parents)
    print(uf.get_parent_of_node(1))

    uf.change_parent_of_node(1,2)
    uf.change_parent_of_node(2,3)
    uf.change_parent_of_node(3,4)

    print(uf.parents)

    print(uf.find(2))
    print(uf.parents)
