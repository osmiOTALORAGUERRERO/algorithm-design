import time

def getMinMax(arr: list, n: int):
    max = 0
    min = 0
    # If there is only one element then return it as min and max both
    if n == 1:
        max = arr[0]
        min = arr[0]
        return minmax

    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]

    for i in range(2, n):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]

    return (min, max)

def getMinMax2(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:

        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax2(low, mid, arr)
        arr_max2, arr_min2 = getMinMax2(mid + 1, high, arr)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
start_time = time.time()
arr_max, arr_min = getMinMax(arr, len(arr))
elapsed_time = time.time() - start_time
print("Elapsed time: %0.10f seconds of function bsRecursive()." % elapsed_time)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

# start_time = time.time()
# arr_max, arr_min = getMinMax2(low, high, arr)
# elapsed_time = time.time() - start_time
# print("Elapsed time: %0.10f seconds of function bsRecursive()." % elapsed_time)
# print('Minimum element is ', arr_min)
# print('nMaximum element is ', arr_max)
