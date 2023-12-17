import numpy as np
import matplotlib.pyplot as plt
from itertools import chain, combinations

class TSP():

    def __init__(self):
        self.n_vertices = None
        self.v_x_y = {}
        self.distance_matrix = None
        self.A = None
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
    

    def map_subset_to_array_index (self, subset):

        index = 1

        return index

    def run(self):
        # initialize A matrix
        self.A = np.zeros((2**self.n_vertices, self.n_vertices + 1))

        # A[S, 1] = 0 if S = {1}
        # and + inf o.w.
        #self.A[:, 1] = float('inf')
        #self.A[self.map_subset_to_array_index((1,)), 1] = 0
        
        # cannot, we wil handle this in base-case
        
        
        #print(self.A.shape)
        #print(self.A[0:5, 1])


        vertex_list = [i for i in range(1,self.n_vertices + 1)]
        for m in range(2, self.n_vertices + 1): # size of subset
            subusets = self.generate_subsets_with_size( vertex_list, m)

            for subset in subusets:
                if 1 in subset:

                    # hash function -- key = subset, key 2 =vertex index , values = cost
                    print(subset)
            break

            #print(type(list(subusets)[0]))
            #break


if __name__ == "__main__":

    tsp = TSP()

    tsp.read_text_input('./tsp.txt')
    tsp.calculate_distance_matrix()

    #subsets = tsp.generate_subsets_with_size([1,2,3],1)
    #print(list(subsets))

    tsp.run()
