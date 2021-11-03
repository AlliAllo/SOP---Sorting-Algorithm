def bubbleSort(arr):
    n = len(arr)

    if len(arr) == 1:
        return arr

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                bubbleSort.callbacks += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


