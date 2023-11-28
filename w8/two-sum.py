# use python dict as a hash table

import numpy as np

class TwoSum():
    def __init__(self):
        self.arr = None
        self.memoryOfSum = []
        self.hashTable = {}
        self.counter = 0
    def read_input(self, fileName):
        files = np.loadtxt(fileName, dtype=int)

        #print(files.shape)
        self.arr = files
    
    # use built-in dictionary
    def hashing(self):
        count = 0
        memKey = ''
        for i in self.inputArray:
            #self.hashTable[self.inputArray[i]] = self.inputArray[i]

            # duplicate 
            if str(i) in self.hashTable.keys():
                #print(self.inputArray[i])
                count +=1
                self.hashTable[i].append(i)

                #memKey = str(i)
                #print(self.hashTable[memKey])
            else:
                self.hashTable[i] = [i]

        print(count)
        print(len(self.hashTable.keys()))
        print(self.hashTable[-21123414637])

#    def search(self, targetSum, firstValue):
#        secondValue = targetSum - firstValue
#
#        if not (self.hashTable.get(str(secondValue)) is None):#
#
#            self.counter += len(self.hashTable[str(secondValue)])

    def main(self, minBound, maxBound):

        nArr = self.arr.shape[0]

        self.arr = np.sort(self.arr)

        '''
        for targetSum in range(minBound, maxBound + 1):
            if targetSum % 1000 == 0:
                print(targetSum)

            targetSumArray = np.ones(nArr) * targetSum
            secondValueArray = targetSumArray - self.inputArray
            for i in range(nArr):
                if self.hashTable.get(secondValueArray[i]) != None:
                    if secondValueArray[i] != self.inputArray[i]:
                        self.counter += 1
                        break
        print('done')
        '''

        i = 0
        j = nArr - 1

        while (i < j):
            sum = self.arr[i] + self.arr[j] 
            if sum > maxBound:
                j = j - 1

            elif sum < minBound:
                i = i + 1
            
            else:
                k = j
                sum2 = self.arr[i] + self.arr[k]
                # sweep
                while not (sum2 < minBound):
                    if (self.arr[i] !=  self.arr[k]) and not (sum2 in self.memoryOfSum):
                        self.memoryOfSum.append(sum2)
                        self.counter +=1

                   
                    k = k - 1
                    sum2 = self.arr[i] + self.arr[k]

                i = i + 1



if __name__ == "__main__":

    twoSum = TwoSum()
    twoSum.read_input('two-sum.txt')
    #twoSum.hashing()

    minBound = -10000
    maxBound = 10000

    #twoSum.inputArray = np.sort(twoSum.inputArray)

    #print(twoSum.inputArray[:10])

    twoSum.main(minBound, maxBound)


    print(twoSum.counter)
