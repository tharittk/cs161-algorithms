
import numpy as np
def read_input(input_file):
    with open(input_file) as f:
        line = f.readline().split(" ")

        W = int(line[0])
        n = int (line[1])

        value = [float('-inf')]
        weight = [float('inf')]
        
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")

            value.append(int(line[0]))
            weight.append(int(line[1]))

    return W, n, value, weight


class Knapsack():

    def __init__(self, W, n, values, weights):
        self.W = W
        self.n = n
        self.values = values
        self.weights = weights

    def initialize_2D(self):
        A = [[] for i in range(self.n + 1)]
        A[0] = [0 for i in range(self.W + 1)]

        for i in range(1, self.n + 1):
            A[i] = [None for i in range(self.W + 1)]
        
        self.A = A

    def naive_run(self, minimal = True):
        self.initialize_2D()

        if minimal:
            self.find_optimal(self.n, self.W)

        else:

            for i in range(1, self.n + 1):
                for x in range(self.W + 1):
                
                    self.find_optimal(i, x)

    def find_optimal(self,i, x):
        
        # end of item          
        if i == 0:
            return self.A[i][x]

      # caching
        if self.A[i][x] != None:
            return self.A[i][x]    

        else:
            wi = self.weights[i]
            vi = self.values[i]

            if x - wi < 0:
                self.A[i][x] = self.find_optimal(i -1, x)
            else:
                self.A[i][x] = max( self.find_optimal(i -1, x), \
                                self.find_optimal(i-1, x - wi) + vi )
                
            return self.A[i][x]




if __name__ == "__main__":

    W, n, values, weights = read_input('./ks_small.txt')

    # lecture case
    #W = 6
    #n = 4
    #values = [float('-inf'), 3,2,4,4]
    #weights = [float('inf'),4,3,2,3]

    ks = Knapsack(W, n, values, weights)

    ks.naive_run(minimal=False)

    print("Maximum value: ", ks.A[ks.n][ks.W])