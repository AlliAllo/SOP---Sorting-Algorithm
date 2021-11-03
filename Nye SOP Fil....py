import matplotlib.pyplot as plt
import random
import math
from quicksort import quickSort
from bubblesort import bubbleSort
from mergesort import mergeSort


n = 4000

fixer = int(1/4 * n)

arrayLength = [*range(0, int(n / fixer + 1))]
arrayLength = [element * fixer for element in arrayLength]


quicksortcallbacks = []

bubblesortcallbacks = []

mergesortcallbacks = []

# QUICKSORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)

    quickSort.callbacks = 0

    quickSort(data, 0, x - 1)


    quicksortcallbacks.append(quickSort.callbacks)



# BUBBLESORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)
    bubbleSort.callbacks = 0

    bubbleSort(data)

    bubblesortcallbacks.append(bubbleSort.callbacks)


# MERGESORT RUNTHORUGH
for x in range(1,n+2,fixer):
    data = [*range(1,x+1)]
    random.shuffle(data)
    mergeSort.callbacks = 0

    mergeSort(data,0,x-1)

    mergesortcallbacks.append(mergeSort.callbacks)


quicksortaverageCase = []
mergesortaverageCase = []
bubblesortaverageCase = []

print(arrayLength)
for number in arrayLength:
    if number == 0:
        quicksortaverageCase.append(0)
        mergesortaverageCase.append(0)
        bubblesortaverageCase.append(0)
    else:
        quicksortaverageCase.append(number*math.log10(number))
        mergesortaverageCase.append(number)
        bubblesortaverageCase.append(number**2)

print(quicksortaverageCase)
print(mergesortaverageCase)
print(bubblesortaverageCase)

# plotting the results
plt.plot(arrayLength, quicksortcallbacks, marker="o")
plt.plot(arrayLength, mergesortcallbacks, marker="o")
plt.plot(arrayLength, bubblesortcallbacks, marker="o")

#plotting the theorietical answer
plt.plot(arrayLength, quicksortaverageCase, marker=".")
plt.plot(arrayLength, bubblesortaverageCase, marker=".",label="n*log(n)",color="b")


plt.legend(["Quicksort","Mergesort","Bubblesort,", "Quicksort2 + Mergesort","Bubblesort2"])


# naming the x axis
plt.xlabel("length of array")
# naming the y axis
plt.ylabel("callbacks")



# giving a title to my graph
plt.title("sonoffabish")


plt.xlim([0, max(arrayLength)])

plt.ylim([0, max(quicksortcallbacks) + max(quicksortcallbacks) / 20])

plt.show()











# GODE BEGREBER AT KUNNE:
# Turing equivalence


