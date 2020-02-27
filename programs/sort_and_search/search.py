from ..efficiency.functionTime import count_elapsed_time

@count_elapsed_time
def linearsearch(list, target):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
    return None

@count_elapsed_time
def BinarySearch(Array, x):
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

def BinarySearch_Recursive(Array, x, lB, uB):
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

def interpolationSearch(array, x):
    inter = ((len(array)-1)/(array[len(array)-1]-array[0])*x)-array[0]
    if x > array[len(array)-1] :
        return -1
    elif len(array) == 1 and array[0] != x :
        return -1
    elif x > array[int(inter)] :
        interpolationSearch(array[int(inter):],x)
    elif x < array[int(inter)] :
        interpolationSearch(array[:int(inter)],x)
    else :
        return int(inter)
