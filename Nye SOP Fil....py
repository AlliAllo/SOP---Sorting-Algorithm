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



n = 100
retries = 10000

start = int(n*0)

end = n+1

arrayLength = [*range(start, end)]

worstTime = []
averageTime = []
bestTime = []

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
for x in range(start,end):
    quicksorttimeValues = []
    for y in range(1,retries):

        quicksortstartTime = time.time()

        quickSort(data(x), 0, x-1)

        quicksorttimeValues.append(time.time() - quicksortstartTime)

    # PROGESS CHECKER
    print(str(x)+":"+str(n))

    bestTime.append(min(quicksorttimeValues))
    averageTime.append(sum(quicksorttimeValues)/len(quicksorttimeValues))
    worstTime.append(max(quicksorttimeValues))



"""
# FUNCTIONS
for x in range(0,len(arrayLength)):
    if x == 0:
        print("Callbacks,  "+ "Length of array")
    else:
        print(quicksortcallbacks[x],arrayLength[x])
"""





plt.plot(arrayLength, worstTime)
plt.plot(arrayLength, averageTime)
plt.plot(arrayLength, bestTime)



plt.title("Number of retries: "+str(retries))
plt.xlabel('length of array (s)')
plt.ylabel('time consumption (s)')
plt.legend(["Worst","Average","Best"])


plt.xlim([start, end])


plt.show()


print("Total time consumed: " + str(time.time()-startTime))





# GODE BEGREBER AT KUNNE:
# Turing equivalence
# Law of large numbers


