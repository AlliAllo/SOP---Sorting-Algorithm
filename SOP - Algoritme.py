import matplotlib.pyplot as plt
import random
import os
import tracemalloc
import time
from quicksort import quickSort
from bubblesort import bubbleSort
import psutil
import tracemalloc


n = 100000

fixer = int(1/4 * n)

arrayLength = [*range(0, int(n / fixer + 1))]
arrayLength = [element * 1000 for element in arrayLength]

quicksorttimeValues = []
quicksortmemoryUsage = []

bubblesorttimeValues = []
bubblesortmemoryUsage = []

timsorttimeValues = []
timsortmemoryUsage = []



# QUICKSORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)


    quicksortstartTime = time.time()
    tracemalloc.start()


    quickSort(data,0,x-1)


    quicksortmemoryUsage.append(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    quicksorttimeValues.append(time.time() - quicksortstartTime)

""""
# BUBBLESORT RUNTHORUGH
for x in range(1,n+1,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)
    bubblesortstartTime = time.time()

    bubbleSort(data)

    bubblesorttimeValues.append(time.time() - bubblesortstartTime)
"""

# TIMSORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)

    timsortstartTime = time.time()
    tracemalloc.start()

    data.sort()

    timsortmemoryUsage.append(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    timsorttimeValues.append(time.time() - timsortstartTime)



# FUNCTIONS




figure, axis = plt.subplots(2)

# plotting the points
plt.plot(arrayLength, quicksorttimeValues, marker="o")
#plt.plot(bubblesorttimeValues, Operations,marker="o")
plt.plot(arrayLength, timsorttimeValues, marker="o")



axis[0].plot(arrayLength, quicksortmemoryUsage, marker="o")
axis[0].plot(arrayLength, timsortmemoryUsage, marker="o")

axis[0].legend(["Quicksort","Timsort"])

plt.setp(axis[0], xlabel='length of array')
plt.setp(axis[0], ylabel='memory usage (b)')






plt.legend(["Quicksort","Timsort"])

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

print(timsortmemoryUsage)
print(quicksortmemoryUsage)



memory = psutil.virtual_memory().used
#print(str(memory)+" b")
#print(str(memory*10**-6)+" mb")

#Current memory usage is 1.83849MB; Peak was 6.55887MB





# GODE BEGREBER AT KUNNE:
# Turing equivalence


