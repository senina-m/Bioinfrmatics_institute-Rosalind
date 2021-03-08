f = open("rosalind_hamm.txt", "r")
line1 = list(f.readline())[0: -1]
line2 = list(f.readline())[0: -1]
f.close()
mismatches = 0

for i in range(0, len(line1)):
    if line1[i] != line2[i]:
        mismatches = mismatches + 1
print(mismatches)
print(line1)
