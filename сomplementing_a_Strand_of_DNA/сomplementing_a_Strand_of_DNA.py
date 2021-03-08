# string = "AAAACCCGGT"

f = open("rosalind_revc.txt", "r")
string = f.readline()
f.close()

string = string[::-1]
arr = list(string)

myDict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for i in range(0, len(arr)):
    if arr[i] in myDict:
        arr[i] = myDict.get(arr[i])

print("".join(arr))
