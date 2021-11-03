import matplotlib.pyplot as plt
import random
import os
import tracemalloc
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from mergesort import timSort

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



n = 5000

fixer = int(1/4 * n)

arrayLength = [*range(0, int(n / fixer + 1))]
arrayLength = [element * 1000 for element in arrayLength]

quicksorttimeValues = []
quicksortmemoryUsage = []
quicksortcallbacks = []

bubblesorttimeValues = []
bubblesortmemoryUsage = []
bubblesortcallbacks = []

timsorttimeValues = []
timsortmemoryUsage = []
timsortcallbacks = []

# QUICKSORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)

    quickSort.callbacks = 0
    quicksortstartTime = time.time()
    tracemalloc.start()

    quickSort(data, 0, x - 1)

    snapshot = tracemalloc.take_snapshot()
    quicksortmemoryUsage.append(display_top(snapshot))

    #quicksortmemoryUsage.append(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    quicksortcallbacks.append(quickSort.callbacks)
    print(quicksortcallbacks)

    quicksorttimeValues.append(time.time() - quicksortstartTime)


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


# TIMSORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)
    timSort.callbacks = 0

    timsortstartTime = time.time()
    tracemalloc.start()

    timSort(data)

    snapshot = tracemalloc.take_snapshot()
    timsortmemoryUsage.append(display_top(snapshot))
    tracemalloc.stop()

    timsortcallbacks.append(timSort.callbacks)
    timsorttimeValues.append(time.time() - timsortstartTime)



# FUNCTIONS




figure, axis = plt.subplots(3)

# plotting the points
plt.plot(arrayLength, quicksorttimeValues, marker="o")
#plt.plot(bubblesorttimeValues, Operations,marker="o")
plt.plot(arrayLength, timsorttimeValues, marker="o")
plt.plot(arrayLength, bubblesorttimeValues, marker="o")



axis[0].plot(arrayLength, quicksortmemoryUsage, marker="o")
axis[0].plot(arrayLength, timsortmemoryUsage, marker="o")
axis[0].plot(arrayLength, bubblesortmemoryUsage, marker="o")

axis[0].legend(["Quicksort","Timsort","Bubblesort"])

print(quicksortcallbacks)
print(timsortcallbacks)
print(bubblesortcallbacks)

axis[1].plot(arrayLength, quicksortcallbacks, marker="o")
axis[1].plot(arrayLength, timsortcallbacks, marker="o")
axis[1].plot(arrayLength, bubblesortcallbacks, marker="o")


axis[1].legend(["Quicksort","Timsort","Bubblesort"])



plt.setp(axis[0], xlabel='length of array')
plt.setp(axis[0], ylabel='memory usage (b)')

plt.setp(axis[1], xlabel='length of array')
plt.setp(axis[1], ylabel='number of callbacks')





plt.legend(["Quicksort","Timsort","Bubblesort"])

#plt.legend(["Quicksort", "Bubblesort","Timsort"])


# naming the x axis
plt.xlabel("length of array")
# naming the y axis
plt.ylabel('time consumption (s)')



# giving a title to my graph
plt.title("sonoffabish")

# function to show the plot

plt.xlim([0, max(arrayLength) + (max(arrayLength) / 10)])

plt.ylim([0, max(quicksorttimeValues)+max(quicksorttimeValues)/10])

plt.show()






memory = psutil.virtual_memory().used
#print(str(memory)+" b")
#print(str(memory*10**-6)+" mb")

#Current memory usage is 1.83849MB; Peak was 6.55887MB





# GODE BEGREBER AT KUNNE:
# Turing equivalence


