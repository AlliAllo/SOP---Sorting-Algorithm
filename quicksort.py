def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    quickSort.callbacks += 1

    for j in range(low, high):

        if arr[j] <= pivot:
            quickSort.callbacks += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    quickSort.callbacks += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        quickSort.callbacks += 3

        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

