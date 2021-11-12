import matplotlib.pyplot as plt
import random
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort
import pickle as pkl
import math
import linecache


startTime = time.time()




n = 10000
retries = 100


# VARIABLE FOR INTERVAL, ALSO NUMBER OF POINTS.
points = int(n * 1 / 12)

start = int(n*0.5)

end = n+1

arrayLength = [*range(start, end, points)]


averageTime = []
averageCallbacks = []

def data(x):
    #print([*range(1, x + 1)])
    if x == 1:
        return [1]
    else:
        # HER BRUGER JEG RANDOM.SAMPLE I STEDET FOR RANDOM.SHUFFLE
        # DET ER FORDI AT RANDOM.SHUFFLE RETURNER NONE, FORDI DER IKKE ER TILSAT EN VARIABLE
        # DERFOR VIRKER RANDOM.SAMPLE BEDST

        #return sorted([*range(0, x)],reverse=True)

        return random.sample([*range(0, x)],x)

# QUICKSORT RUNTHORUGH
for x in range(start, end, points):
    quicksorttimeValues = []
    quicksortcallbacks = []

    for y in range(0,retries):

        quickSort.callbacks = 0

        quicksortstartTime = time.time()

        #heapSort(data(x))
        quickSort(data(x), 0, x-1)

        quicksorttimeValues.append(time.time() - quicksortstartTime)
        quicksortcallbacks.append(quickSort.callbacks)

    # PROGESS CHECKER
    print(str(x)+":"+str(n))

    averageTime.append(sum(quicksorttimeValues)/len(quicksorttimeValues))
    averageCallbacks.append(sum(quicksortcallbacks)/len(quicksortcallbacks))



"""
# FUNCTIONS
for x in range(0,len(arrayLength)):
    if x == 0:
        print("Callbacks,  "+ "Length of array")
    else:
        print(quicksortcallbacks[x],arrayLength[x])
"""

theory = []
for x in arrayLength:
    if x == 0:
        theory.append(0)
    else:
        theory.append(x*math.log2(x))


#plt.plot(arrayLength, averageTime,marker="o")
print(averageCallbacks)
plt.plot(arrayLength, averageCallbacks,marker="o")

plt.plot(arrayLength, theory,marker="o")


plt.title("Number of retries: "+str(retries)+", seconds used: "+str(time.time()-startTime))
plt.xlabel('length of array')
plt.ylabel('operations')
plt.legend(["Average","Theory"])

#støt shabab

plt.xlim([start, end])


plt.show()

pkl.dump(plt.show(),  open("FigureObject.pickle",  'wb'))


print("Total time consumed: " + str(time.time()-startTime)+", "+str(int(sum(averageTime))))





# GODE BEGREBER AT KUNNE:
# Turing equivalence
# Law of large numbers


