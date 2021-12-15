def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    print(arr)
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr

    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        #print("seocnd:"+str(pivot))
        quickSort(arr, pivot + 1, high)


