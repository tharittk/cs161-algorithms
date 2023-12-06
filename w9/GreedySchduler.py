
# Template

import numpy as  np

class GreedyScheduler():

    def __init__(self):
        self.numJobs = None
        self.weight = []
        self.length = []
        self.cost = []
        self.dataStructure = None
        self.sumWeightedCompletionTime = 0
    
    def readInputFile(self, inputFile):
        with open(inputFile) as f:

            self.numJobs = int(f.readline().strip())

            for i in range(self.numJobs):
                line = f.readline().strip().split(" ")
                self.weight.append(int(line[0]))
                self.length.append(int(line[1]))

    def computeCost(self, option = 'diff'):

        if option == 'diff':
            for i in range(self.numJobs):
                self.cost.append( self.weight[i] - self.length[i])
        elif option =='ratio':
            for i in range(self.numJobs):
                self.cost.append( self.weight[i] / self.length[i])

    def createSortedData(self):
        tmp = np.array(list(zip(self.weight, self.length, self.cost)), dtype=[('weight', 'float'), ('length', 'float'), ('cost', 'float')])
        sortOrder = np.argsort(tmp, order = ['cost', 'weight'])

        dataStructure = tmp[sortOrder]
        self.dataStructure = dataStructure
        #print((dataStructure['cost']))
        #print((dataStructure['weight']))


    def computeCompletionTime(self):
        cumSumTime = 0
        for i in range(self.numJobs - 1, -1, -1):
            cumSumTime += self.dataStructure['length'][i]
            self.sumWeightedCompletionTime += self.dataStructure['weight'][i] * (cumSumTime)

        print(self.sumWeightedCompletionTime)
    
        
if __name__ == "__main__":
    scheduler = GreedyScheduler()

    scheduler.readInputFile('./jobs.txt')
    scheduler.computeCost(option = 'diff')
    scheduler.createSortedData()
    scheduler.computeCompletionTime()