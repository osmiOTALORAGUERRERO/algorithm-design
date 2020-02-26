from ..efficiency.functionTime import count_elapsed_time

@count_elapsed_time
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
	return arr

@count_elapsed_time
def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0 :
            if arr[j-1] > arr[j] :
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
            else:
                break
    return arr

@count_elapsed_time
def select_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

@count_elapsed_time
def Quick_Sort(arr):
    less_subArr = []
    greather_subArr = []
    result = []
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<pivot:
                less_subArr.append(arr[i])
            else:
                greather_subArr.append(arr[i])

        result.extend(Quick_Sort(less_subArr))
        result.append(pivot)
        result.extend(Quick_Sort(greather_subArr))
        return result
