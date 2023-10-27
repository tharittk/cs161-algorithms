# Quick Sort

def QuickSort (array, l = 0, r = None):

    # first run case
    if r == None:
        r = len(array) - 1

    # size one array
    if (l >= r):
        return array, 0
        
    p = ChoosePivot(array,l ,r, 'median')
    
    # swap pivot to the first position
    array = swap(array, p, l)

    array, pivot_index = Partition(array, l, r)

    total_count = r - l

    # lhs part
    array, comp_l = QuickSort(array, l, pivot_index - 1)
    # rhs part
    array, comp_r = QuickSort(array, pivot_index + 1, r)

    total_count += comp_l
    total_count += comp_r

    return array, total_count

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
        n = r - l + 1
        if n % 2 == 0:
            mid_index = l + n//2 - 1
        else:
            mid_index = l + n//2
        first = array[l]
        last = array[r]
        mid = array[mid_index]
        median = first + mid + last - max(first, mid, last) - min(first, mid, last)
        if median == mid:
            return mid_index
        elif median == first:
            return l
        elif median == last:
            return r
        else:
            raise ValueError
            
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
        result, count = QuickSort(arrayInput)

    print('is sorted:', all(result[i] <= result[i+1] for i in range(len(result) - 1)))
    print('total count:', count)
    #print(result)