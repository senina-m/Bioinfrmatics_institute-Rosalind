# string = "GATGGAACTTGACTACGTAAATT"

f = open("../count_RNA/rosalind_rna.txt", "r")
string = f.readline()
f.close()

list = []
list[:0] = string


for i in range(0, len(list)):
    if list[i] == "T":
        list[i] = "U"

print("".join(list))
print("GAUGGAACUUGACUACGUAAAUU")
