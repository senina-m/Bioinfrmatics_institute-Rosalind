def read(filename):
    my_dict = {}
    f = open(filename, "r")
    seq_name = "start"
    fasta = ""
    for line in f:
        arr = list(line)
        if arr[len(arr) - 1] == "\n":
            arr = arr[0:-1]
        if arr[0] == ">":
            my_dict[seq_name] = fasta
            fasta = ""
            seq_name = "".join(arr[1:])
        else:
            fasta = fasta + "".join(arr[0:])
    f.close()
    my_dict[seq_name] = fasta
    my_dict.pop("start")
    return my_dict


# a c g t
def get_atcg(list):
    a = 0
    t = 0
    g = 0
    c = 0
    for letter in list:
        if letter == "A":
            a = 1 + a
        if letter == "T":
            t = 1 + t
        if letter == "C":
            c = 1 + c
        if letter == "G":
            g = 1 + g
    return [a, c, g, t]


dictionary = read("rosalind_cons.txt")
arr_of_lines = []
for line in dictionary.values():
    arr_of_lines.append(list(line))

arr_by_place = []
for i in range(0, len(arr_of_lines[0])):
    arr_by_place.append([])
    for j in range(0, len(arr_of_lines)):
        arr_by_place[i].append(arr_of_lines[j][i])

# a c g t
profile = []
for line in arr_by_place:
    profile.append(get_atcg(line))


for i in range(0, len(profile)):
    maximum = max(profile[i])
    if profile[i][0] == maximum:
        print("A", end="")
    if profile[i][1] == maximum:
        print("C", end="")
    if profile[i][2] == maximum:
        print("G", end="")
    if profile[i][3] == maximum:
        print("T", end="")

arr = ["A", "C", "G", "T"]
for i in range(0, len(profile[0])):
    print("")
    print(arr[i] + ": ", end="")
    for j in range(0, len(profile)):
        print(profile[j][i], end=" ")
