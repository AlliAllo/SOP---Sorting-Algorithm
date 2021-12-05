import math



def calc(number):
    print("Base  e: "+ str(math.log(number)))
    print("Base  2: "+ str(math.log2(number)))
    print("Base 10: "+ str(math.log10(number)))








n = 10000000000**100000
calc(int(n))