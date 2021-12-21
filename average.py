import random
start = 1
end = 5

retries = 1000000

sum = 0
for x in range(start,end+1):
    sum += x

average = sum/(end+1-start)


Sum = 0
for x in range(retries):
    Sum += random.randint(start,end)
Average = Sum / retries


print(Average)
print(average)


