filename = "rosalind_subs (1).txt"
f = open(filename, "r")
s = list(f.readline())[0:-1]
t = list(f.readline())
print(s)
print(t)
f.close()

substrings_start = []
for i in range(0, len(s)):
    k = s[i:(i + len(t))]
    if k == t:
        substrings_start.append(i+1)

for i in substrings_start:
    print(i,  end=" ")
