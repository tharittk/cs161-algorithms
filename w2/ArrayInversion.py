
import numpy as np

def ArrayInversion(arraysIn):
    n = len(arraysIn)
    # odd case
    if n == 1:
        return arraysIn, 0
    else:
        lhs = arraysIn[ : n//2 ]
        rhs = arraysIn[ n//2 : ]
    # base-case
    if len(rhs) == 1 and len(lhs) == 1:
        # merge
        if lhs[0] <= rhs[0]:
            return np.asarray([lhs, rhs]).flatten(), 0
        else:
            return np.asarray([rhs, lhs]).flatten(), 1
    else:
        lhs_out, countLhs = ArrayInversion(lhs)
        rhs_out, countRhs = ArrayInversion(rhs)


        totalCount = countLhs + countRhs
        n_out = len(lhs_out) + len(rhs_out)
        sortedArray = np.zeros(n_out)
        # merge sorted array & counting count = countRhs
        i = 0
        j = 0
        for k in range(n_out):
            if lhs_out[i] <= rhs_out[j]:
                sortedArray[k] = lhs_out[i]
                i += 1
            else: # right is smaller
                sortedArray[k] = rhs_out[j]
                j += 1
                totalCount += (len(lhs_out) - i)

            if i == len(lhs_out):
                sortedArray[k+1:]= rhs_out[j:]
                break

            if j == len(rhs_out):
                sortedArray[k+1:]= lhs_out[i:]
                break
        return sortedArray.flatten(), totalCount

if __name__ == "__main__":
    with open("IntegerArray.txt") as f:
        lines = [line.rstrip('\n') for line in f]
    n = len(lines)
    arraysIn = np.zeros(n)
    for i in range(n):
        arraysIn[i] = int(lines[i])


    _sortedArray, count = ArrayInversion(arraysIn)

    print("Output: ", count)
