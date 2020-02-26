from ..efficiency.functionTime import count_elapsed_time

@count_elapsed_time
def linearsearch(self, list, target):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
    return None

@count_elapsed_time
def BinarySearch(self, Array, x):
    lowerBound = 0
    upperBound = len(Array)-1
    index = -1

    while lowerBound < upperBound:
        middlePoint = int((lowerBound+upperBound)/2)
        if x==Array[middlePoint]:
            index = middlePoint
            break
        else:
            if x < Array[middlePoint]:
                upperBound = middlePoint-1
            else:
                lowerBound = middlePoint+1
    if lowerBound == upperBound and Array[lowerBound]==x:
        index = lowerBound
    return index

@count_elapsed_time
def BinarySearch_Recursive(self, Array, x, lB, uB):
    middlePoint = int((lB+uB)/2)

    if lB == uB:
        if x==Array[middlePoint]:
            return middlePoint
        else:
            return -1
    else:
        if x==Array[middlePoint]:
            return middlePoint
        else:
            if x < Array[middlePoint]:
                return BinarySearch_Recursive(Array, x , lB, middlePoint)
            else:
                return BinarySearch_Recursive(Array, x, middlePoint+1, uB)

@count_elapsed_time
def interpolationSearch(key, array, left, right):
    if right< left:
        return - 1 # Not found
    midpoint = left + (int) ((key - array[left]) / (array[right] - array[left]) * (right - left))
    if key == array[midpoint]:
        return midpoint # Found at position
    if key > array[midpoint]:
        return interpolationSearch(key, array, midpoint + 1, right) # Take the upper section
    else:
        return interpolationSearch(key, array, left, midpoint - 1) # Take the lower section
