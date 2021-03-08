import re


def read():
    my_dict = {}
    f = open("mDNA_to_protein.txt", "r")
    for line in f:
        arr = re.split("\s+", line)
        my_dict[arr[0]] = arr[1]
        my_dict[arr[2]] = arr[3]
        my_dict[arr[4]] = arr[5]
        my_dict[arr[6]] = arr[7]
    f.close()
    return my_dict


filename = "../rosalind_prot.txt"
f = open(filename, "r")
line = list(f.readline())
f.close()
my_dict = read()

num_list = [i * 3 for i in range(0, int((len(line)/3)))]
protein = ""
for i in num_list:
    mdna = line[i] + line[i + 1] + line[i + 2]
    if my_dict[mdna] == "Stop":
        break
    protein = protein + my_dict[mdna]
print(protein)

