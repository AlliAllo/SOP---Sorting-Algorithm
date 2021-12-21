import random
import time
import string

startTime = time.time()


class sortingAlgorithms():
    def __init__(self, array,retries,start,end,space,dumb):
        self.array = array
        self.retries = retries
        self.start = start
        self.end = end

        # DENNE VARAIBLE HANDLER OM HVOR VIGTIGT SPACE ER. I DETTE EKSEMPEL ER DET BARE EN BOOLEAN VÆRDI. TRUE BETYDER AT DET ER VIGTIGT.
        self.space = space

        # DENNE VARIABLE OMHANDLER OM DER SKAL UDVÆLGES EN DÅRLIG ALGORITME(Bubblesort).
        self.dumb = dumb


        # TJEK DATA OG KONKLUDERE HVIKLEN SORTERINGSALGORITME DER ER BEDST.
        if space == True:
            self.algorithm = "Heap"
        if self.dumb == True:
            self.algorithm = "Bubble"
        if not self.space and not self.dumb:
            self.algorithm = "Quick"

        print(f"You are sorting the following array: {self.array}")

        # SORTER VORES ARRAY:
        self.sort()

    # QUICKSORT:
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pindex = self.partition(arr, low, high)

            self.quickSort(arr, low, pindex - 1)
            self.quickSort(arr, pindex + 1, high)


    # HEAPSORT
    def heapify(self,arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self,arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def bubbleSort(self,arr):
        n = len(arr)

        if len(arr) == 1:
            return arr

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # SORTER DATA
    def sort(self):
        for x in range(self.retries):
            self.sortingtimeValues = []

            self.sortingstartTime = time.time()

            if self.algorithm == "Quick":
                self.quickSort(self.array, 0 , self.end-1)

            if self.algorithm == "Heap":
                self.heapSort(self.array)

            self.sortingtimeValues.append(time.time() - self.sortingstartTime)

            print("Progress: "+str(x+1) + "/" + str(self.retries))

        self.averageTime = sum(self.sortingtimeValues) / len(self.sortingtimeValues)

        # ALLE ALGORITMER ER IN-PLACE SÅ VI KAN GODT BARE PRINTE VORES ARRAY:
        print(f"Algorithm used: {self.algorithm}sort")
        print(f"Sorted array: {self.array}")
        print(f"Time consumed: {self.averageTime} seconds")


def randomizer(x):
    # EITHER MAKE A LIST OF INTEGERS OR LIST OF LETTERS
    chance = random.randint(1,3)

    # ONLY INTEGERS
    if chance == 1:
        # print([*range(1, x + 1)])
        if x == 1:
            return [1]
        else:
            # HER BRUGER JEG RANDOM.SAMPLE I STEDET FOR RANDOM.SHUFFLE
            # DET ER FORDI AT RANDOM.SHUFFLE RETURNER NONE, FORDI DER IKKE ER TILSAT EN VARIABLE
            # DERFOR VIRKER RANDOM.SAMPLE BEDST
            # return [1,3,5,6,2,4,15,12,10,14,13,14,8]
            # print(random.sample([*range(1, x+1)],x))
            return random.sample([*range(1, x + 1)], x)
    # LETTERS
    if chance == 2:
        array = []
        for i in range(int(x)):
            # ADD RANDOM LETTER THEN RANDOM NUMBER AFTERWARDS
            array.append(string.ascii_lowercase[random.randint(0,25)])

        return array

    # NEGATIVE AND POSITVE FLOATS:
    if chance == 3:
        array = []
        for i in range(x):
            array.append(random.uniform(-1,1))
        return array




if __name__ == "__main__":
    # UNDGÅ STORE VÆRDIER, > 900, PYTHON HAR NEMLIG EN RECURSION LIMIT.
    n = 500
    retries = 10
    start = 0
    end = n

    sortingAlgorithms(randomizer(n), retries, start, end, random.randint(0, 1),random.randint(0, 1))




# ALL ALGORITHMS WERE TAKEN FROM GEEKFORGEEKS, THANK YOU! <3:
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# https://www.geeksforgeeks.org/merge-sort/?ref=lbp
# https://www.geeksforgeeks.org/heap-sort/?ref=lbp
# https://www.geeksforgeeks.org/bubble-sort/

# SMALL HELP:
#https://www.pythoncentral.io/use-python-multiply-strings/
#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python




