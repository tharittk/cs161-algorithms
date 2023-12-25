import numpy as np
import matplotlib.pyplot as plt
from itertools import chain, combinations

class TSP():

    def __init__(self):
        self.n_vertices = None
        self.v_x_y = {}
        self.distance_matrix = None
        self.A = {}
    def read_text_input(self, input_file):

        with open(input_file) as f:
            
            self.n_vertices = int(f.readline())

            lines = f.readlines()

            i = 1
            for line in lines:
                line = line.split(" ")
                x = float(line[0])
                y = float(line[1])

                self.v_x_y[i] = {}
                self.v_x_y[i]['x'] = x
                self.v_x_y[i]['y'] = y

                i += 1
        #print(self.v_x_y)

    def calculate_distance_matrix(self):
        self.distance_matrix = np.zeros((self.n_vertices + 1, self.n_vertices + 1))

        for i in range(1, self.n_vertices + 1):
            for j in range(1, self.n_vertices + 1):

                dist = np.sqrt(((self.v_x_y[i]['x'] - self.v_x_y[j]['x'])**2) + ((self.v_x_y[i]['y'] - self.v_x_y[j]['y'])**2) )
                
                self.distance_matrix[i][j] = dist

        #plt.imshow(self.distance_matrix)
        #plt.show()

        assert self._check_symmetric()

    def _check_symmetric(self, rtol=1e-05, atol=1e-08):
        return np.allclose(self.distance_matrix, self.distance_matrix.T, rtol=rtol, atol=atol)
    
    def generate_subsets_with_size(self, list_members, size):
        return combinations(list_members, size)
    
    def find_min(self,S, j):
        global_min = float('inf')
        #print('S: ',S, 'j: ', j)
        S_minus_j = tuple(sorted(set(S) - {j}))
        #print('S minus j', S_minus_j)
        for k in S:
            if k != j:
                current_min = self.A[S_minus_j][k] + self.distance_matrix[k][j]
                if current_min < global_min:
                    global_min = current_min
        return global_min



    def run(self):

        vertex_list = [i for i in range(1,self.n_vertices + 1)]
        self.A[(1,)] = np.empty(self.n_vertices + 1)
        self.A[(1,)][1] = 0

        for m in range(2, self.n_vertices + 1): # size of subset
            print('m = ', m)
            subusets = self.generate_subsets_with_size( vertex_list, m)
            for subset in subusets: #all subsuet size m
                if 1 in subset:
                    self.A[subset] = np.zeros(self.n_vertices + 1)
                    self.A[subset][1] = float('inf') # A[S, 1] = inf if S != {1}

                    for j in subset: # j in S and j != 1
                        if j != 1:
                            self.A[subset][j] = self.find_min(subset, j) # find min


        #    break
        #print(self.A)
        tuple_vertex_list = tuple(sorted(vertex_list))
        global_min = float('inf')
        #min_index = None
        for j in range(2, self.n_vertices + 1):

            current_min = self.A[tuple_vertex_list][j] + self.distance_matrix[j][1]
            if current_min < global_min:
                global_min = current_min
        
        return global_min

if __name__ == "__main__":

    tsp = TSP()

    tsp.read_text_input('./tsp.txt')
    tsp.calculate_distance_matrix()

    #subsets = tsp.generate_subsets_with_size([1,2,3],1)
    #print(list(subsets))

    min_cost = tsp.run()

    print(">> min cost:", min_cost)
