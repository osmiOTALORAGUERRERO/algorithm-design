class search:
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
