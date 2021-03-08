import re


def read():
    my_dict = {}
    f = open("protein_mass.txt", "r")
    for line in f:
        arr = re.split("\s+", line)
        my_dict[arr[0]] = float(arr[1])
    f.close()
    return my_dict


filename = "rosalind_prtm.txt"
f = open(filename, "r")
line = list(f.readline())
f.close()
my_dict = read()

mass = 0
for letter in line:
    mass = mass + my_dict[letter]
print(mass)
