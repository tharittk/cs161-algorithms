

class MinHeap():

    def __init__(self):
        # Trick: 0th index to always be the least to
        # so we can use the convention that the index starts at 1
        self.heap = [-99]


    def insert(self, key):
        self.heap.append(key)

        keyIndex = (len(self.heap) -1)

        self.bubble_up(keyIndex)


    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


    def bubble_up(self, keyIndex):

        #if keyIndex % 2 == 0:
        #    parentIndex = (keyIndex // 2)
        #else:
        #    parentIndex = ((keyIndex + 1) // 2)
        parentIndex = keyIndex // 2

        #print(keyIndex, parentIndex)
        # Loop while heap property not satisified

        print('inserting', self.heap[keyIndex], 'parent', self.heap[parentIndex])
        while not (self.heap[parentIndex] <= self.heap[keyIndex]):

            self.swap(keyIndex, parentIndex)

            # next iteration
            keyIndex = parentIndex
            
            parentIndex = parentIndex // 2
           # if parentIndex % 2 == 0:
           #     parentIndex = parentIndex // 2
           # else:
           #     parentIndex = (parentIndex + 1) // 2



def read_input(inputFile):
    stream = []
    with open(inputFile) as f:
        lines = f.readlines()
        for line in lines:
            stream.append(int(line.strip()))

    return stream
def main(inputFile):
    
    stream = read_input(inputFile)

    #print(stream)



if __name__ == "__main__":

    #main('./Median.txt')

    minHeap = MinHeap()

    stream = [11,13,9,12,4,4,9,8,4,3,6,7,3]

    for i in stream:
        minHeap.insert(i)
    
    print(minHeap.heap)