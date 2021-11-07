import matplotlib.pyplot as plt
import random
import os
import tracemalloc
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort

import psutil
import tracemalloc
import linecache

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



n = 10000

fixer = int(1/4 * n)
arrayLength = [*range(0, int(n / fixer + 1))]
arrayLength = [element * fixer for element in arrayLength]
print(arrayLength)
quicksorttimeValues = []
quicksortmemoryUsage = []
quicksortcallbacks = []

bubblesorttimeValues = []
bubblesortmemoryUsage = []
bubblesortcallbacks = []

heapsorttimeValues = []
heapsortmemoryUsage = []
heapsortcallbacks = []

def data(x):
    #print([*range(1, x + 1)])
    if x == 1:
        return [1]
    else:
        # HER BRUGER JEG RANDOM.SAMPLE I STEDET FOR RANDOM.SHUFFLE
        # DET ER FORDI AT RANDOM.SHUFFLE RETURNER NONE, FORDI DER IKKE ER TILSAT EN VARIABLE
        # DERFOR VIRKER RANDOM.SAMPLE BEDST
        return random.sample([*range(1, x + 1)],x)

# QUICKSORT RUNTHORUGH
for x in range(1,n+2,fixer):

    quickSort.callbacks = 0
    quicksortstartTime = time.time()
    tracemalloc.start()


    quickSort(data(x), 0, x-1)

    snapshot = tracemalloc.take_snapshot()

    quicksortmemoryUsage.append(display_top(snapshot))

    #quicksortmemoryUsage.append(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    quicksortcallbacks.append(quickSort.callbacks)

    quicksorttimeValues.append(time.time() - quicksortstartTime)

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
for x in range(1,n+2,fixer):

    heapSort.callbacks = 0

    timsortstartTime = time.time()
    tracemalloc.start()


    heapSort(data(x))

    snapshot = tracemalloc.take_snapshot()
    heapsortmemoryUsage.append(display_top(snapshot))
    tracemalloc.stop()

    heapsortcallbacks.append(heapSort.callbacks)
    heapsorttimeValues.append(time.time() - timsortstartTime)


"""
# FUNCTIONS
for x in range(0,len(arrayLength)):
    if x == 0:
        print("Callbacks,  "+ "Length of array")
    else:
        print(quicksortcallbacks[x],arrayLength[x])
"""




figure, axis = plt.subplots(3)

# plotting the points
axis[0].plot(arrayLength, quicksorttimeValues,marker="o")
#plt.plot(bubblesorttimeValues, Operations,marker="o")
axis[0].plot(arrayLength, heapsorttimeValues,marker="o")
#axis[0].plot(arrayLength, bubblesorttimeValues, marker="o")



axis[1].plot(arrayLength, quicksortmemoryUsage, marker="o")
axis[1].plot(arrayLength, heapsortmemoryUsage, marker="o")
#axis[1].plot(arrayLength, bubblesortmemoryUsage, marker="o")



axis[2].plot(arrayLength, quicksortcallbacks, marker="o")
axis[2].plot(arrayLength, heapsortcallbacks, marker="o")
#axis[2].plot(arrayLength, bubblesortcallbacks, marker="o")


plt.setp(axis[0], xlabel='length of array')
plt.setp(axis[0], ylabel='time consumption (s)')
axis[0].legend(["Quicksort","Heapsort","Bubblesort"])

plt.setp(axis[1], xlabel='length of array')
plt.setp(axis[1], ylabel='memory usage (b)')
axis[1].legend(["Quicksort","Heapsort","Bubblesort"])

plt.setp(axis[2], xlabel='length of array')
plt.setp(axis[2], ylabel='number of callbacks')
axis[2].legend(["Quicksort","Heapsort","Bubblesort"])



plt.xlim([0, max(arrayLength) + (max(arrayLength) / 10)])


plt.show()







memory = psutil.virtual_memory().used

#print(str(memory)+" b")
#print(str(memory*10**-6)+" mb")

#Current memory usage is 1.83849MB; Peak was 6.55887MB





# GODE BEGREBER AT KUNNE:
# Turing equivalence


