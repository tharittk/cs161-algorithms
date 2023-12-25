import numpy as np
import matplotlib.pyplot as plt


class TSP():

    def __init__(self):
        self.n_vertices = None
        self.v_x_y = {}
        self.distance_matrix = None
        self.visited = [1]


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


    def _check_symmetric(self, rtol=1e-05, atol=1e-08):
        return np.allclose(self.distance_matrix, self.distance_matrix.T, rtol=rtol, atol=atol)
    

    def find_left_city (self, current_v):
        if current_v == 1:
            return float('inf'), current_v

        nearest_dist = float('inf')
        nearest_dest = None     
        for dest in range(current_v - 1, 0, -1):
            if dest not in self.visited:
                # check delta x, if exceed current min, stop iteration
                if abs(self.v_x_y[current_v]['x'] - self.v_x_y[dest]['x']) > nearest_dist:
                    return nearest_dist, nearest_dest
                else:
                    current_dist = np.sqrt(((self.v_x_y[current_v]['x'] - self.v_x_y[dest]['x'])**2) + ((self.v_x_y[current_v]['y'] - self.v_x_y[dest]['y'])**2) )
                    if current_dist < nearest_dist:
                            nearest_dist = current_dist
                            nearest_dest = dest
        
        return nearest_dist, nearest_dest

    def find_right_city (self, current_v):
        if current_v == self.n_vertices:
            return float('inf'), current_v

        nearest_dist = float('inf')
        nearest_dest = None              
        for dest in range(current_v + 1, self.n_vertices + 1):
             if dest not in self.visited:

                # check delta x, if exceed current min, stop iteration
                if abs(self.v_x_y[current_v]['x'] - self.v_x_y[dest]['x']) > nearest_dist:
                    return nearest_dist, nearest_dest
                else:
                    current_dist = np.sqrt(((self.v_x_y[current_v]['x'] - self.v_x_y[dest]['x'])**2) + ((self.v_x_y[current_v]['y'] - self.v_x_y[dest]['y'])**2) )
                    if current_dist < nearest_dist:
                            nearest_dist = current_dist
                            nearest_dest = dest

            
        return nearest_dist, nearest_dest

    def run(self):

        #vertex_list = [i for i in range(1,self.n_vertices + 1)
        total_dist = 0
        current_v = 1

        while len(self.visited) != self.n_vertices:

            dist_left, v_left = self.find_left_city(current_v)
            dist_right, v_right = self.find_right_city(current_v)


            if dist_left < dist_right:
                total_dist += dist_left
                self.visited.append(v_left)
                current_v = v_left

            else:
                total_dist += dist_right
                self.visited.append(v_right)
                current_v = v_right


            if len(self.visited) % 500 == 0:
                print('Visit {count}/{total}'.format(count = len(self.visited), total = self.n_vertices))
                #print('Visting: ', current_v)

        # go back to 1
                
        dest = 1
        total_dist += np.sqrt(((self.v_x_y[current_v]['x'] - self.v_x_y[dest]['x'])**2) + ((self.v_x_y[current_v]['y'] - self.v_x_y[dest]['y'])**2) )

        return total_dist



if __name__ == "__main__":

    tsp = TSP()

    tsp.read_text_input('./nn.txt')
    #tsp.calculate_distance_matrix()
    #print(">> Input:", tsp.n_vertices, 'finish calculate distance matrix')

    total_dist = tsp.run()

    print(">> min cost:", total_dist)
