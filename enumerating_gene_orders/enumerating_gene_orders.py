import math
import itertools

n = 5
print(math.factorial(n))
arr = []
for i in range(1, n + 1):
    arr.append(i)
permutations = list(itertools.permutations(arr))
for line in permutations:
    print("")
    for j in range(0, n):
        print(line[j], end=" ")
