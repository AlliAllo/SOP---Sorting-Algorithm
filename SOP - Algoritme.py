import matplotlib.pyplot as plt
import random
import os
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort
import math
import tracemalloc
import linecache

startTime = time.time()


def display_top(snapshot, key_type='lineno', limit=None):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])

        line = linecache.getline(frame.filename, frame.lineno).strip()


    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
    total = sum(stat.size for stat in top_stats)

    return (total / 1024)


n = 40
retries = 1
points = 1
start = 0


start = int(n*start)

points = int((n -start) * 1 / points)

end = n+1

arrayLength = [*range(start, end, points)]


averagequicksortcallbacks = []
averagequicksortmemoryusage = []
averagequicksorttimeValues = []

averageheapsortcallbacks = []
averageheapsortmemoryusage = []
averageheapsorttimeValues = []

bubblesorttimeValues = []
bubblesortmemoryUsage = []
bubblesortcallbacks = []



def data(x):
    #print([*range(1, x + 1)])
    if x == 1:
        return [1]
    else:
        # HER BRUGER JEG RANDOM.SAMPLE I STEDET FOR RANDOM.SHUFFLE
        # DET ER FORDI AT RANDOM.SHUFFLE RETURNER NONE, FORDI DER IKKE ER TILSAT EN VARIABLE
        # DERFOR VIRKER RANDOM.SAMPLE BEDST
        return random.sample([*range(0, x )],x)

        #return sorted([*range(0, x)])


# QUICKSORT RUNTHORUGH
for x in range(start, end, points):
    quicksorttimeValues = []
    quicksortmemoryUsage = []
    quicksortcallbacks = []

    for y in range(0, retries):
        quickSort.callbacks = 0

        quicksortstartTime = time.time()
        tracemalloc.start()

        # heapSort(data(x))
        quickSort(data(x), 0, x - 1)

        snapshot = tracemalloc.take_snapshot()

        quicksortmemoryUsage.append(display_top(tracemalloc.take_snapshot()))
        tracemalloc.stop()

        quicksorttimeValues.append(time.time() - quicksortstartTime)
        quicksortcallbacks.append(quickSort.callbacks)

    print(str(x)+":"+str(n))

    averagequicksorttimeValues.append(sum(quicksorttimeValues)/len(quicksorttimeValues))
    averagequicksortcallbacks.append(sum(quicksortcallbacks)/len(quicksortcallbacks))
    averagequicksortmemoryusage.append(sum(quicksortmemoryUsage)/len(quicksortmemoryUsage))
print(quicksortcallbacks)



"""""
# BUBBLESORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)
    bubbleSort.callbacks = 0

    bubblesortstartTime = time.time()
    tracemalloc.start()

    bubbleSort(data)

    snapshot = tracemalloc.take_snapshot()
    bubblesortmemoryUsage.append(display_top(snapshot))
    tracemalloc.stop()

    bubblesortcallbacks.append(bubbleSort.callbacks)
    bubblesorttimeValues.append(time.time() - bubblesortstartTime)
"""

# HEAPSORT RUNTHORUGH
for x in range(start, end, points):

    heapsorttimeValues = []
    heapsortmemoryUsage = []
    heapsortcallbacks = []

    for y in range(0, retries):
        heapSort.callbacks = 0

        heapsortstartTime = time.time()
        tracemalloc.start()

        # heapSort(data(x))
        heapSort(data(x))

        snapshot = tracemalloc.take_snapshot()

        heapsortmemoryUsage.append(display_top(tracemalloc.take_snapshot()))
        tracemalloc.stop()
        heapsorttimeValues.append(time.time() - heapsortstartTime)
        heapsortcallbacks.append(heapSort.callbacks)

    print(str(x)+":"+str(n))

    averageheapsorttimeValues.append(sum(heapsorttimeValues) / len(heapsorttimeValues))
    averageheapsortcallbacks.append(sum(heapsortcallbacks) / len(heapsortcallbacks))
    averageheapsortmemoryusage.append(sum(heapsortmemoryUsage) / len(heapsortmemoryUsage))

"""
# FUNCTIONS
for x in range(0,len(arrayLength)):
    if x == 0:
        print("Callbacks,  "+ "Length of array")
    else:
        print(quicksortcallbacks[x],arrayLength[x])
"""

print(averagequicksortcallbacks)
print(averageheapsortcallbacks)

theory = []

for x in arrayLength:
    if x == 0:
        theory.append(0)
    else:
        theory.append(x*math.log2(x))

figure, axis = plt.subplots(3)

# plotting the points
axis[0].plot(arrayLength, averagequicksorttimeValues,marker="o")
#plt.plot(bubblesorttimeValues, Operations,marker="o")
axis[0].plot(arrayLength, averageheapsorttimeValues,marker="o")
#axis[0].plot(arrayLength, bubblesorttimeValues, marker="o")



axis[1].plot(arrayLength, averagequicksortmemoryusage, marker="o")
axis[1].plot(arrayLength, averageheapsortmemoryusage, marker="o")
#axis[1].plot(arrayLength, bubblesortmemoryUsage, marker="o")



axis[2].plot(arrayLength, averagequicksortcallbacks, marker="o")
axis[2].plot(arrayLength, averageheapsortcallbacks, marker="o")
axis[2].plot(arrayLength, theory, marker="o")

#axis[2].plot(arrayLength, bubblesortcallbacks, marker="o")


plt.setp(axis[0], xlabel='length of array')
plt.setp(axis[0], ylabel='time consumption (s)')
axis[0].legend(["Quicksort","Heapsort","Bubblesort"])

plt.setp(axis[1], xlabel='length of array')
plt.setp(axis[1], ylabel='memory usage (b)')
axis[1].legend(["Quicksort","Heapsort","Bubblesort"])

plt.setp(axis[2], xlabel='length of array')
plt.setp(axis[2], ylabel='number of callbacks')
axis[2].legend(["Quicksort","Heapsort","Theory"])



plt.xlim([start, end])

plt.show()


print("Total time consumed: " + str(time.time()-startTime))





