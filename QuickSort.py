# Quick Sort
'''
    # edge case - size two array
    if (l+1) == r:
        # swap
        

        return array, r
    
        # not swap

        return array, l
'''

def QuickSort (array, l = 0, r = None):

    # first run case
    if r == None:
        r = len(array) - 1

    # size one array
    if (l >= r):
        return array
        
    p = ChoosePivot(array,l ,r, 'first')
    
    # swap pivot to the first position
    array = swap(array, p, l)

    array, pivotIndex = Partition(array, l, r)
    # lhs part
    array = QuickSort(array, l, pivotIndex - 1)
    # rhs part
    array = QuickSort(array, pivotIndex + 1, r)
    
    return array

# Partitioning: pivot has to be at 0
def Partition(array, l = 0, r = -1):


    # partition boundary i i.e. array[i] is ready to be swapped
    i = l + 1
    for j in range(l + 1, r + 1):
        if array[j] < array[l]:
            array = swap(array, i, j)
            i += 1

    # swap pivot with latest element to lhs
    array = swap(array, i - 1, l)
    return array, i-1


# return index of the pivot
def ChoosePivot(array, l, r, method = 'first'):
    if method == 'first':
        return l
    if method == 'last':
        return r
    if method == 'median':
        n = len(array)
        if n % 2 == 0:
            return n //2 - 1
        else:
            return n//2
            
def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp
    return array


if __name__ == "__main__":

    #test = [3, 0, -1 ,8, 2, 5, 1, 4, 7, 6]
    #test = [3, 0, -1 ,8, 2, 5, 1, 4]
    #test = [0,-1]

    #print("test,", test)
    #result = QuickSort(test)
    #print(result)
    #print('is sorted:', all(result[i] <= result[i+1] for i in range(len(result) - 1)))

    with open("QuickSort.txt") as f:
        arrayInput = [int(line.rstrip('\n')) for line in f]
        result = QuickSort(arrayInput)

    print('is sorted:', all(result[i] <= result[i+1] for i in range(len(result) - 1)))
    #print(result)