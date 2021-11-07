import matplotlib.pyplot as plt
import random
import time
from quicksort import quickSort
from bubblesort import bubbleSort
from heapsort import heapSort



startTime = time.time()




n = 1000
retries = 1500



fixer = int(n*1/8)

start = int(n*0.5)

end = n+1

arrayLength = [*range(start, end, fixer)]


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

        #return sorted([*range(0, x)],reverse=True)

        return random.sample([*range(0, x)],x)

# QUICKSORT RUNTHORUGH
for x in range(start,end,fixer):
    quicksorttimeValues = []
    for y in range(0,retries):

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



print(worstTime)

plt.plot(arrayLength, worstTime,marker="o")
plt.plot(arrayLength, averageTime,marker="o")
plt.plot(arrayLength, bestTime,marker="o")



plt.title("Number of retries: "+str(retries)+", seconds used: "+str(time.time()-startTime))
plt.xlabel('length of array')
plt.ylabel('time consumption (s)')
plt.legend(["Worst","Average","Best"])


plt.xlim([start, end])


plt.show()


print("Total time consumed: " + str(time.time()-startTime)+", "+str(int(sum(averageTime))))





# GODE BEGREBER AT KUNNE:
# Turing equivalence
# Law of large numbers


