class Graph():

    def __init__(self):
        self.n = None
        self.m = None
        self.thc= {} # tail-head-cost

        #self.head = []
        #self.cost = []

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

                if tail not in self.thc.keys():
                    self.thc[tail] = {}
                    self.thc[tail][head] = cost
                else:
                    self.thc[tail][head] = cost

        print(self.thc)

        #for i in range(1, self.n + 1):
        #    if i not in self.head:
        #        print(i)



if __name__ == "__main__":
    
    g = Graph()
    g.read_text_input('./g1.txt')
    #print(len(g.tail))


#for i in range(1,4):
#    file_name = './g' + str(i) + '.txt'
#    g.read_text_input(file_name)
