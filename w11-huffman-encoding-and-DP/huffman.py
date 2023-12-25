class Heap():

    def __init__(self, isMinHeap = True):
        # Trick: 0th index to always be the least to
        # so we can use the convention that the index starts at 1
        # same logic to max heap
        self.isMinHeap = isMinHeap
        if isMinHeap:
            self.heap = [-float('inf')]
        else:
            self.heap = [float('inf')]
        

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
        n_symbol = int(f.readline())

        lines = f.readlines()
        for line in lines:
            stream.append(int(line.strip()))

    return n_symbol, stream


class TwoNodesTree():

    def __init__(self):
        self.symbol_childern = {}
        self.symbol_freq = {}
        self.symbol_active = {}
        self.symbol_code = {}


    def insert_symbol_children(self, top, l_child, r_child):
        if top not in two_nodes_tree.symbol_childern.keys():
            #print("ERROR Duplicate symbol in children")
            self.symbol_childern[top] =  [[l_child, r_child]]
        else:
            print("ERROR Duplicate symbol in children")

            self.symbol_childern[top].append([l_child, r_child])

    def get_key_l_r_child(self, key_value):
        lr = self.symbol_childern[key_value].pop()
        l = lr[0]
        r = lr[1]

        #print('l,r key', l, r)
        return l,r


    def expand_tree(self, top_key, current_code):


        l_child, r_child = self.get_key_l_r_child(top_key)
        #r_child = self.get_key_r_child(top_key)

        if l_child == None and r_child == None:
            self.symbol_code[top_key] = current_code

        else:
            self.expand_tree(l_child, current_code + '0')
            self.expand_tree(r_child, current_code + '1')




if __name__ == "__main__":

    #n_symbol, freqs = read_input('./symbol_freq.txt')
    n_symbol, freqs = read_input('./sym.txt')

    #print(n_symbol, freqs[:10])

    min_heap = Heap()
    two_nodes_tree = TwoNodesTree()

    i = 1
    for freq in freqs:
        min_heap.insert(freq)
        two_nodes_tree.symbol_freq[str(i)] = freq
        two_nodes_tree.symbol_active[str(i)] = True
        two_nodes_tree.insert_symbol_children(str(i), None, None)
        # for later expansion
        two_nodes_tree.symbol_code[str(i)] = ''

        i += 1

    #print(len(two_nodes_tree.key_childern.keys()))

    # run #(n-1) merge
    for j in range(n_symbol-1):
        min_key_1st = min_heap.extractRoot()
        min_key_2nd = min_heap.extractRoot()

        merge_min_key  = min_key_1st + min_key_2nd

        #symbol_min_1 = list(two_nodes_tree.symbol_freq.keys())[list(two_nodes_tree.symbol_freq.values()).index(min_key_1st)] 
        #symbol_min_2 = list(two_nodes_tree.symbol_freq.keys())[list(two_nodes_tree.symbol_freq.values()).index(min_key_2nd)] 

        for k in range(len(list(two_nodes_tree.symbol_freq.keys()))):
            key = list(two_nodes_tree.symbol_freq.keys())[k]
            if two_nodes_tree.symbol_freq[key] == min_key_1st and two_nodes_tree.symbol_active[key] == True:

                two_nodes_tree.symbol_active[key] = False

                symbol_min_1 = key
                break
        #print(two_nodes_tree.symbol_active)
        for m in range(len(list(two_nodes_tree.symbol_freq.keys()))):
            key = list(two_nodes_tree.symbol_freq.keys())[m]
            #print(min_key_2nd, two_nodes_tree.symbol_freq[key])
            if two_nodes_tree.symbol_freq[key] == min_key_2nd and two_nodes_tree.symbol_active[key] == True:

                two_nodes_tree.symbol_active[key] = False

                symbol_min_2 = key
                break
            

        #new_symbol = symbol_min_1 + symbol_min_2
        new_symbol = i
        i += 1
        if new_symbol in two_nodes_tree.symbol_freq.keys():
            print("ERROR Duplicate symbol")
        two_nodes_tree.symbol_freq[new_symbol] = merge_min_key
        two_nodes_tree.symbol_active[new_symbol] = True

        # record two-nodes tree

        two_nodes_tree.insert_symbol_children(new_symbol, symbol_min_1, symbol_min_2)

        # re-insert
        min_heap.insert(merge_min_key)



    #print(min_heap.heap)
    #print(sum(freqs))
    #print(two_nodes_tree.symbol_freq)
    #print(two_nodes_tree.symbol_childern)
    
    top_key = list(two_nodes_tree.symbol_freq.keys())[-1]

    two_nodes_tree.expand_tree(top_key, current_code='')

    #print(len(two_nodes_tree.key_code.values()))

    print(two_nodes_tree.symbol_code)

    lengths = []
    for code in two_nodes_tree.symbol_code.values():
        lengths.append(len(code))
    print('min code length: ', min(lengths))
    print('max code length: ', max(lengths))
# 