def partition(arr, low, high):
    i = (low - 1)                                 #c1 = 1
    pivot = arr[high]                                 #c2 = 1

    for j in range(low, high):                         #c3 = n+1
        if arr[j] <= pivot:                            #c4 = n
            i = i + 1                                  #c5 = n
            arr[i], arr[j] = arr[j], arr[i]            #c5 = n

    arr[i + 1], arr[high] = arr[high], arr[i + 1]      #c6 = 1
    return (i + 1)                                     #c7 = 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    #print(arr)
    if low < high:

        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

