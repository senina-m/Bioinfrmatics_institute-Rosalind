n = 22
m = 88
sequence = list()
for i in range(n):
    if i < 2:
        total = 1
        sequence.append(total)
    elif (i < m) or (m == 0):
        total = sequence[i - 1] + sequence[i - 2]
        sequence.append(total)
    elif i == m:
        total = sequence[i - 1] + sequence[i - 2] - 1
        sequence.append(total)
    else:
        total = sequence[i - 1] + sequence[i - 2] - sequence[i - (m + 1)]
        sequence.append(total)
print(total)
