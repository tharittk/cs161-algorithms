

class Heap():

    def __init__(self, isMinHeap = True):
        # Trick: 0th index to always be the least to
        # so we can use the convention that the index starts at 1
        # same logic to max heap
        self.isMinHeap = isMinHeap
        if isMinHeap:
            self.heap = [-99]
        else:
            self.heap = [999999999]
        
        self.medianSum = 0
        self.medianVals = []

    def getHeapSize(self):
        return len(self.heap) - 1

    def getRootValue(self):
        return self.heap[1]

    def insert(self, key):
        self.heap.append(key)

        keyIndex = (len(self.heap) -1)

        self.bubble_up(keyIndex)


    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


    def bubble_up(self, keyIndex):

        parentIndex = keyIndex // 2

        if self.isMinHeap:
            while not (self.heap[parentIndex] <= self.heap[keyIndex]):

                self.swap(keyIndex, parentIndex)

                # next iteration
                keyIndex = parentIndex
                
                parentIndex = parentIndex // 2

        # max heap
        else:
            while not (self.heap[parentIndex] >= self.heap[keyIndex]):

                self.swap(keyIndex, parentIndex)

                # next iteration
                keyIndex = parentIndex
                
                parentIndex = parentIndex // 2

    def bubble_down(self, keyIndex):

        childIndexLeft = 2 * keyIndex
        childIndexRight = 2* keyIndex + 1

        # edge case: leaf node
        lastIndex = len(self.heap) - 1
        if childIndexRight > lastIndex and childIndexLeft >  lastIndex:
            return 0
        elif childIndexRight > lastIndex and childIndexLeft <= lastIndex:
            swapChildIndex = childIndexLeft

        else:
        # swap with smaller child (minHeap) and conversely
            if self.heap[childIndexLeft] <= self.heap[childIndexRight]:
                smallerChildIndex = childIndexLeft
                largerChildIndex = childIndexRight
            else:
                smallerChildIndex = childIndexRight
                largerChildIndex = childIndexLeft

            # swapping index
            if self.isMinHeap:
                swapChildIndex = smallerChildIndex
            else:
                swapChildIndex = largerChildIndex
            
        parentIndex = keyIndex

        if self.isMinHeap:
            while not (self.heap[parentIndex] <= self.heap[swapChildIndex]):

                self.swap(swapChildIndex, parentIndex)

                # next iteration
                parentIndex = swapChildIndex

                childIndexLeft = 2 * parentIndex
                childIndexRight = 2* parentIndex + 1

                # edge case: leaf node
                lastIndex = len(self.heap) - 1
                if childIndexRight > lastIndex and childIndexLeft >  lastIndex:
                    break

                elif childIndexRight > lastIndex and childIndexLeft <= lastIndex:
                    swapChildIndex = childIndexLeft

                # swap with smaller child 
                else:
                    if self.heap[childIndexLeft] <= self.heap[childIndexRight]:
                        swapChildIndex = childIndexLeft
                    else:
                        swapChildIndex = childIndexRight
            # max heap
        else:
            while not (self.heap[parentIndex] >= self.heap[swapChildIndex]):

                self.swap(swapChildIndex, parentIndex)

                # next iteration
                parentIndex = swapChildIndex

                childIndexLeft = 2 * parentIndex
                childIndexRight = 2* parentIndex + 1


                # edge case: leaf node
                lastIndex = len(self.heap) - 1
                if childIndexRight > lastIndex and childIndexLeft >  lastIndex:
                    break

                elif childIndexRight > lastIndex and childIndexLeft <= lastIndex:
                    swapChildIndex = childIndexLeft
                else:
                    # swap with smaller child 
                    if self.heap[childIndexLeft] <= self.heap[childIndexRight]:
                        swapChildIndex = childIndexRight
                    else:
                        swapChildIndex = childIndexLeft

    def extractRoot(self):
        lastIndex = len(self.heap) - 1
        self.swap(lastIndex, 1)
        root = self.heap.pop(-1)
        self.bubble_down(1)

        return root

def read_input(inputFile):
    stream = []
    with open(inputFile) as f:
        lines = f.readlines()
        for line in lines:
            stream.append(int(line.strip()))

    return stream

def MedianMaintenance(stream):
    minHeap = Heap()
    maxHeap = Heap(isMinHeap=False)
    
    maxHeap.insert(stream[0])
    minHeap.medianSum += stream[0]
    minHeap.medianVals.append(stream[0])

    #maxHeap.insert(stream[1])
    #minHeap.medianSum += stream[1]

    for val in stream[1:]:
        # bucketing to max or min heap

        if val <= maxHeap.getRootValue():
            maxHeap.insert(val)
        else:
            #assert val >= minHeap.getRootValue()
            minHeap.insert(val)

        # rebalance
        minHeapSize = minHeap.getHeapSize()
        maxHeapSize = maxHeap.getHeapSize() 
        diff = abs( minHeapSize - maxHeapSize )
        if diff > 1:
            assert diff == 2
            
            if maxHeapSize > minHeapSize:
                root = maxHeap.extractRoot()
                minHeap.insert(root)
            else:
                root = minHeap.extractRoot()
                maxHeap.insert(root)
        # get median
        minHeapSize = minHeap.getHeapSize()
        maxHeapSize = maxHeap.getHeapSize() 
        totalSize = minHeapSize + maxHeapSize


        if totalSize % 2 == 0:
            medianVal = maxHeap.getRootValue()

        elif maxHeapSize == (minHeapSize + 1):
            medianVal = maxHeap.getRootValue()
        
        elif (maxHeapSize + 1) == minHeapSize:
            medianVal = minHeap.getRootValue()
        else:
            # not balancing
            print('Fail to balance Heaps !')
            raise ValueError

        minHeap.medianSum += medianVal
        minHeap.medianVals.append(medianVal)
        #print('maxHeap:minHeap', maxHeap.heap[1:], minHeap.heap[1:], 'median: ', medianVal)

    return minHeap, maxHeap

if __name__ == "__main__":

    #main('./Median.txt')

    #minHeap = Heap()
    #maxHeap = Heap(isMinHeap=False)

    stream = [11,13,9,12,4,4,9,8,4,3,6]

    stream = read_input('./Median.txt')

    minHeap, maxHeap = MedianMaintenance(stream)

    print('>>> ', minHeap.medianSum % 10000)
    assert minHeap.medianSum == sum(minHeap.medianVals)
    assert len(minHeap.medianVals) == len(stream)

    print(minHeap.medianVals[:5])