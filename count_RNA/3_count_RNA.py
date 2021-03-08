string = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"

# f = open("rosalind_dna.txt", "r")
# string = f.readline()
# f.close()

list = []
list[:0] = string

a = 0
t = 0
g = 0
c = 0

for i in range(0, len(list)):
    if list[i] == "A":
        a = 1 + a
    if list[i] == "T":
        t = 1 + t
    if list[i] == "C":
        c = 1 + c
    if list[i] == "G":
        g = 1 + g
print("A: " + str(a) + ", C: " + str(c) + ", G: " + str(g) + ", T: " + str(t))
print(str(a) + " " + str(c) + " " + str(g) + " " + str(t))
