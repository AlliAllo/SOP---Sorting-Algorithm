import matplotlib.pyplot as plt
import random
import os
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort
from mergesort import mergeSort

startTime = time.time()


n = 10000
retries = 20
points = 4
start = 0.5  # DECIMAL VALUE FOR WHERE TO START


start = int(n*start)
points = int((n -start) * 1 / points)
end = n+1
arrayLength = [*range(start, end, points)]



averagequicksorttimeValues = []
averageheapsorttimeValues = []
bubblesorttimeValues = []
averagemergesorttimeValues = []


def data(x):
    #print([*range(1, x + 1)])
    if x == 1:
        return [1]
    else:
        # HER BRUGER JEG RANDOM.SAMPLE I STEDET FOR RANDOM.SHUFFLE
        # DET ER FORDI AT RANDOM.SHUFFLE RETURNER NONE, FORDI DER IKKE ER TILSAT EN VARIABLE
        # DERFOR VIRKER RANDOM.SAMPLE BEDST
        #return [1,3,5,6,2,4,15,12,10,14,13,14,8]
        #print(random.sample([*range(1, x+1)],x))
        return random.sample([*range(1, x+1)],x)

        #return sorted([*range(0, x)])


# RUNTHORUGH
for x in range(start, end, points):
    quicksorttimeValues = []
    heapsorttimeValues = []
    mergesorttimeValues = []

    for y in range(0, retries):

        #QUICKSORT
        quicksortstartTime = time.time()

        quickSort(data(x), 0, x-1)

        quicksorttimeValues.append(time.time() - quicksortstartTime)


        #HEAPSORT
        heapsortstartTime = time.time()

        heapSort(data(x))

        heapsorttimeValues.append(time.time() - heapsortstartTime)

        #MERGESORT
        mergesortstartTime = time.time()

        mergeSort(data(x))

        mergesorttimeValues.append(time.time() - mergesortstartTime)

    # PROGESS "BAR"
    print(str(x)+":"+str(n))


    averagequicksorttimeValues.append(sum(quicksorttimeValues)/len(quicksorttimeValues))
    averageheapsorttimeValues.append(sum(heapsorttimeValues) / len(heapsorttimeValues))
    averagemergesorttimeValues.append(sum(mergesorttimeValues)/len(mergesorttimeValues))



plt.plot(arrayLength, averagequicksorttimeValues,marker="o")
plt.plot(arrayLength, averageheapsorttimeValues,marker="o")
plt.plot(arrayLength, averagemergesorttimeValues,marker="o")


plt.xlabel('length of array')
plt.ylabel('time consumption (s)')
plt.legend(["Quicksort","Heapsort","Mergesort"])
plt.title(f"Number of retries: {retries}")

plt.xlim([start-start/100, end])

plt.show()


print("Total time consumed: " + str(time.time()-startTime))





